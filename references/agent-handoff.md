# New thread and agent handoff

Use this sequence whenever the Skill is invoked in a new conversation, by a new agent, or after context compression.

## Startup contract

1. Resolve the project root and read its applicable `AGENTS.md` files.
2. Read the project handbook `README.md`, then `index.json` and the project adapter if present. Do not load every handbook chapter or historical snapshot.
3. Search the current index by task name, aliases, and stable IDs. Read the matched active business and technical entries plus the minimum one-hop related entries.
4. If the task involves deployment, release, environment, server, port, domain, branch, credentials, or rollback, read `T.DEPLOY` and its linked dated records. Resolve credentials from the private manifest path recorded by the handbook. Never ask the user to repeat a credential location already recorded there.
5. Check the affected repositories' current branch, revision, and dirty paths. Preserve existing work and other people's changes.
6. Select the task mode (`bootstrap`, `develop`, `test`, `review`, `handbook`, `release`, or `migrate`) and load only the relevant reference modules and specialized Skills.
7. For multi-step, iterative, cross-repository, release, deployment, or repeatedly failing work, also read `references/long-task.md`.
8. Continue from the active handbook and current evidence. Do not ask the user to restate project basics already documented. Ask only when a material conflict, missing authorization, or unresolved environment fact blocks the requested action.

## First progress message

Before implementation, report briefly:

- resolved project and handbook paths
- matched business and technical IDs
- repositories, branches, revisions, and dirty paths that affect the task
- environment and deployment boundary when relevant
- the next authorized action and evidence to collect

This message is a bounded checkpoint. Do not paste passwords, keys, tokens, full logs, or the entire handbook into the conversation.

## Continuation rules

- Treat active handbook entries as current navigation and dated records as deployment evidence.
- Treat `confirmed`, `inferred`, and `unknown` confidence explicitly. Do not turn an inference into a fact.
- Preserve user decisions, current code, migrations, queues, and historical evidence. When a confirmed iterative fix supersedes an attempt, remove the obsolete implementation and record the superseded rule in history.
- Finish with changed paths, verification type, evidence paths, unresolved gaps, and whether anything was committed, pushed, uploaded, or deployed.
