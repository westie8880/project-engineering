---
name: project-engineering
description: Route sustained repository work from onboarding through implementation, review, testing, release, deployment, and knowledge handoff. It loads project rules and bounded handbook evidence, coordinates compatible specialized Skills, enforces batch-oriented verification, removes superseded attempts after confirmed fixes, and keeps technical and business knowledge aligned across technology stacks. Use for project and repository tasks; ordinary prose and standalone artifacts do not require it.
metadata:
  short-description: Portable project engineering and knowledge workflow
---

# Project engineering

Use this skill as the default project workflow whenever the task touches a repository, project code, configuration, tests, deployment, release, or technical/business handbook, even when the user does not mention the skill. Skip it only for ordinary non-project prose or standalone artifacts. It is independent of Java, Go, Vue, React, Python, or any one build system. Load only the module references needed for the current task.

## First response to a task

1. Bound the task to the requested project and identify its mode. An umbrella workspace is not necessarily a Git repository. Use root instructions and shallow repository discovery before searching source.
2. Follow applicable repository instructions; locate an existing handbook/adapter using explicit paths or the project's documentation index. Do not recursively scan the whole disk/workspace, dependencies, backups, release copies, generated assets or unrelated projects to find them. If an instruction file contains a dated decision log, read its opening rules and current index first; search historical blocks by topic or stable ID only when the task needs them.
3. With a handbook, read README and task-relevant index records, then only their current bodies. See [retrieval and compatibility](references/project-adapter.md). Without one, use [bootstrap and maintenance](references/handbook-maintenance.md); a request to generate a baseline requires actual files, not just a proposed directory tree. A read-only request remains read-only. Bootstrap may inspect named roots, top-level manifests, explicit indexes, tests, deployment files and targeted source paths; it must report gaps instead of recursively reading every document.
4. Before editing, check the affected repository's revision and dirty paths; compare them with the handbook's verification baseline. Read changed task-relevant source; avoid repeated whole-project rediscovery.
5. Use installed skill discovery (including find-skills) when useful; discovery does not require installation or network search for every task. Read only specialized skills relevant to the chosen work.

## New conversation and agent handoff

When this Skill is invoked in a new conversation, by a new agent, or after context compression, follow [new thread and agent handoff](references/agent-handoff.md). Read the project's handbook and adapter before asking for project basics. Use the active indexes and evidence links to continue the documented work, and ask the user only about a material conflict, missing authorization, or unresolved fact.

## Long-task guardrails

For multi-step, iterative, cross-repository, release, deployment, or repeatedly failing work, also read [long-running complex project guardrails](references/long-task.md). Apply its plan confirmation, reuse and cleanup, separate review, batch testing, stop-loss, and release-recovery rules without replacing specialized Skills.

## Handbook placement and write policy

For a project documentation task, write the two handbooks inside the project’s existing documentation root. Prefer `<project-root>/docs/project-handbook/`; if the project already has a documented shared docs root, preserve that root and record the resolved path in its README and adapter. Do not create the handbooks in the Skill directory or an unrelated workspace folder. Generating or updating a handbook is a local working-tree change. Do not commit, push, deploy, upload or publish it unless the user separately requests that action. Show the exact path and dirty-file impact in the delivery report. Deployment credentials may be registered in a user-approved private manifest outside the project documentation root. Record only that manifest path and field names in the handbooks, never credential values.

## Modes and routing

- `bootstrap`: reverse-engineer a new or unfamiliar repository into a baseline. Mark conclusions as `confirmed`, `inferred`, or `unknown`; never present inference as fact.
- `develop`: read [development](references/development.md) plus [frontend](references/frontend.md) or [backend](references/backend.md) as applicable. Full-stack tasks use both. Preserve existing work and follow repository architecture.
- `test`: read `references/batch-testing.md`. Build coverage around the current mainline goal and track what has already been covered.
- `review`: compare code, configuration, tests, and active handbook entries; report conflicts instead of guessing.
- `handbook`: read `references/handbook-maintenance.md`. Update an existing module or capability entry when possible; do not append duplicate rules.
- `release`: read project release instructions and record code, configuration, artifact, environment, and verification evidence.
- `migrate`: produce a compact context package containing the skill, project adapter, active indexes, current snapshots, and evidence manifest.

When multiple modes apply, combine them. Mode names are workflow labels, not shell commands or permission grants. Never invent a priority over system/developer/user instructions. Follow the host's instruction hierarchy and applicable repository constraints.

## Compatibility with other skills

This skill does not replace specialized skills. The specialized skill performs tool-specific work; this skill supplies project context, coverage tracking, cleanup rules, and handbook updates. If unavailable, use a valid generic alternative and state material limits. Do not fabricate tool calls or claim reading a skill executed it. See the compatibility contract in project-adapter.md.

Do not assume a package name, language, framework, database, or deployment platform. Read those from the project adapter and current repository evidence.

## Finalization rule

After the user confirms the final implementation of an iterative fix, trace and remove that task's superseded attempts: obsolete code paths, temporary routes, switches, stale copy, dead comments and unused trial artifacts. Scan callers and configuration references, then run affected checks. Preserve useful regression tests, live compatibility contracts, migrations, audit evidence and other people's work. Confirmation is not blanket authorization to delete data or deploy. Archive material prior decisions before replacing them; Git history only preserves committed changes.

## Context discipline

Use retrieval in this order: project summary and adapter; active indexes; the capability, module, interface, data, and test entries relevant to the task; historical snapshots only for historical behavior, regression, migration, or conflict investigation. Keep context bounded with stable IDs and source references instead of loading an entire repository or all history.

## Deliverable expectations

State what changed, why, how it was verified, and any unresolved evidence gap. Distinguish code checks, build checks, simulated checks, real integration checks, and browser/device checks. Do not claim business validation from a successful build alone.

Read references only when the mode requires them:

- `references/development.md`
- `references/frontend.md` 
- `references/backend.md` 
- `references/batch-testing.md`
- `references/handbook-maintenance.md`
- `references/project-adapter.md`



