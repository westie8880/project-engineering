"""Bounded, dependency-free lookup and validation for project handbooks."""

import argparse
import json
import sys
from pathlib import Path

SUPPORTED_SCHEMA = 1
REQUIRED_FIELDS = ("status", "effective_from", "confidence", "last_verified")
CONFIDENCE = {"confirmed", "inferred", "unknown"}
HIDDEN_FIELDS = {"body", "content", "text", "details"}


def _index_path(root):
    for candidate in (root / "index.json", root / "indexes" / "index.json"):
        if candidate.is_file():
            return candidate
    raise ValueError("missing index.json (expected root/index.json or indexes/index.json)")


def _records(document, label):
    if isinstance(document, list):
        return document
    if not isinstance(document, dict):
        raise ValueError(f"{label} must be a JSON object or array")
    version = document.get("schema_version", SUPPORTED_SCHEMA)
    if version != SUPPORTED_SCHEMA:
        raise ValueError(f"unsupported schema_version: {version}")
    records = document.get("entries", document.get("records"))
    if records is None:
        raise ValueError(f"{label} has no entries or records")
    if isinstance(records, dict):
        records = [dict(value, id=key) if isinstance(value, dict) and "id" not in value else value
                   for key, value in records.items()]
    if not isinstance(records, list):
        raise ValueError(f"{label}.entries must be a list or object")
    return records


def _load(root, include_history=False):
    root = Path(root).resolve()
    current_path = _index_path(root)
    current = _records(json.loads(current_path.read_text(encoding="utf-8")), str(current_path))
    history = []
    if include_history:
        for candidate in (root / "history" / "index.json", root / "history" / "snapshots" / "index.json"):
            if candidate.is_file():
                history = _records(json.loads(candidate.read_text(encoding="utf-8")), str(candidate))
                break
    return root, current + history


def _source_paths(record):
    refs = record.get("source_refs", []) or []
    if isinstance(refs, str):
        refs = [refs]
    refs = list(refs)
    for source in record.get("sources", []) or []:
        refs.append(source.get("path") if isinstance(source, dict) else source)
    return [ref for ref in refs if isinstance(ref, str)]


def _validate_records(root, records):
    errors = []
    known = {record.get("id") for record in records if isinstance(record, dict)}
    seen = set()
    for number, record in enumerate(records):
        if not isinstance(record, dict):
            errors.append(f"record {number} is not an object")
            continue
        record_id = record.get("id")
        if not isinstance(record_id, str) or not record_id.strip():
            errors.append(f"record {number} missing id")
            continue
        if record_id in seen:
            errors.append(f"duplicate id: {record_id}")
        seen.add(record_id)
        for field in REQUIRED_FIELDS:
            if field not in record:
                errors.append(f"{record_id} missing {field}")
        confidence = record.get("confidence")
        if confidence not in CONFIDENCE:
            errors.append(f"{record_id} invalid confidence: {confidence}")
        if confidence == "confirmed" and not _source_paths(record):
            errors.append(f"{record_id} confirmed without source evidence")
        for reference in _source_paths(record):
            path = (root / reference).resolve()
            try:
                path.relative_to(root)
            except ValueError:
                errors.append(f"{record_id} path outside handbook: {reference}")
                continue
            if not path.is_file():
                errors.append(f"{record_id} missing source: {reference}")
        for related in record.get("related", []) or []:
            related_id = related.get("id") if isinstance(related, dict) else related
            if related_id not in known:
                errors.append(f"{record_id} missing related: {related_id}")
    return errors


def check(root, include_history=False):
    try:
        handbook_root, records = _load(root, include_history)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        return [str(error)]
    return _validate_records(handbook_root, records)


def _metadata(record):
    return {key: value for key, value in record.items() if key not in HIDDEN_FIELDS}


def _matching(records, query):
    needle = query.casefold()
    exact = [record for record in records if str(record.get("id", "")).casefold() == needle]
    if exact:
        return exact

    def score(record):
        fields = [record.get("id", ""), record.get("summary", ""), record.get("title", ""), record.get("path", "")]
        fields += record.get("aliases", []) or []
        values = [str(value).casefold() for value in fields]
        if any(value == needle for value in values):
            return 3
        if any(needle in value for value in values):
            return 2
        return 0

    return sorted((record for record in records if score(record)), key=score, reverse=True)


def lookup(root, query, include_history=False):
    if not query.strip():
        raise ValueError("query must not be empty")
    handbook_root, records = _load(root, include_history)
    candidates = _matching(records, query)
    by_id = {record.get("id"): record for record in records if isinstance(record, dict)}
    expanded = []
    seen = set()
    for record in candidates:
        record_id = record.get("id")
        if record_id not in seen:
            expanded.append(record)
            seen.add(record_id)
        for related in record.get("related", []) or []:
            related_id = related.get("id") if isinstance(related, dict) else related
            related_record = by_id.get(related_id)
            if related_record and related_id not in seen:
                expanded.append(related_record)
                seen.add(related_id)
    matches = expanded[:10]
    return {
        "query": query,
        "history_included": bool(include_history),
        "matches": [_metadata(record) for record in matches],
        "truncated": len(expanded) > len(matches),
        "remaining": max(0, len(expanded) - len(matches)),
        "handbook_root": str(handbook_root),
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    check_parser = subparsers.add_parser("check")
    check_parser.add_argument("root")
    check_parser.add_argument("--history", action="store_true", dest="include_history")
    lookup_parser = subparsers.add_parser("lookup")
    lookup_parser.add_argument("root")
    lookup_parser.add_argument("query")
    lookup_parser.add_argument("--history", action="store_true", dest="include_history")
    args = parser.parse_args(argv)
    try:
        if args.command == "check":
            errors = check(args.root, args.include_history)
            print(json.dumps({"ok": not errors, "errors": errors}, ensure_ascii=False))
            return 0 if not errors else 1
        print(json.dumps(lookup(args.root, args.query, args.include_history), ensure_ascii=False))
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False))
        return 2


if __name__ == "__main__":
    sys.exit(main())
