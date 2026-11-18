# Project handbook maintenance

Maintain two linked knowledge views: a technical iteration handbook and a business iteration handbook. Use stable IDs shared by both.

## Retrieval-oriented layout

```text
docs/project-handbook/
├── README.md
├── project-summary.md
├── project-adapter.yaml
├── indexes/
│   ├── module-index.yaml
│   ├── capability-index.yaml
│   ├── traceability-map.yaml
│   └── snapshot-manifest.yaml
├── active/
│   ├── technical/
│   │   └── 部署索引.md
│   └── business/
├── history/
│   └── snapshots/
└── evidence/
```

The startup path reads the summary, adapter, active indexes, and relevant active entries. Historical snapshots are opt-in for regression, migration, historical behavior, or conflict investigation.

The technical handbook must contain a stable deployment index entry, normally `T.DEPLOY`. It is an index, not a secret store or a replacement for deployment evidence. Group each deployable surface and dependency by environment, repository/branch/revision, artifact, host or service, port/domain, configuration source, migration or data change, health check, rollback evidence and unresolved gap. Link the index to dated deployment records and verification artifacts. When an operator hands over a different deployment step, add or update the relevant row and evidence link instead of burying it in a chronological log.

## Entry contract

Every active capability, module, interface, important data rule, and test contract has a stable ID and records `status`, `effective_from`, `source_refs`, `confidence`, and `last_verified`. Use `confirmed`, `inferred`, or `unknown` confidence. Link business entries to technical modules, interfaces, data or configuration, and test evidence.

## Update gate

Update the handbook only for changes to business behavior, interface contracts, data semantics, state, permissions, quotas, architecture boundaries, deployment or environment, or test contracts. Do not add an entry for a typo, variable rename, one-off diagnosis, or behavior-neutral refactor.

When a rule changes, update the current entry in place and move the former version to history with `superseded` or `deprecated`, its effective period, reason, and `superseded_by`. Never append contradictory copies to the active handbook. Do not put passwords, keys, or tokens in the handbook; reference private configuration locations.

## Generation and validation

For a new project, scan repository structure, manifests, build files, configuration, tests, deployment files, and runtime evidence to generate an initial baseline. Mark uncertain conclusions instead of guessing. Validate duplicate IDs, orphan modules, broken references, stale active snapshots, incomplete business-to-code mappings, and claims without evidence. Generate a concise migration package containing the skill, adapter, active indexes, current snapshots, and evidence manifest.

Handbook generation is a project-local working-tree operation. Resolve the project documentation root before writing. Do not commit or publish generated handbooks by default. Record the path, dirty files and any intentionally uncommitted state in the README or evidence manifest.
