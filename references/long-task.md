# Long-running complex project guardrails

Use this reference for multi-step, iterative, cross-repository, release, deployment, or repeatedly failing tasks. It distills the recurring failure modes of long AI-assisted development into operating rules that remain compatible with framework, testing, design, deployment, and document Skills.

## 1. Keep implementation and knowledge aligned

- Reuse the project's components, utilities, tokens, contracts, modules, and existing workflows before creating a parallel version.
- Keep configurable values in configuration or typed constants with one owner. Do not scatter fixed values through views, services, scripts, and tests.
- Search callers and references before replacing an implementation. After a confirmed fix, remove superseded attempts, temporary routes, stale copy, dead comments, and unused trial artifacts.
- Treat the active technical and business handbooks as navigation. Archive superseded rules with effective periods instead of leaving contradictory active copies.
- When a plan, prototype, or old deployment record conflicts with code or current user decisions, label the conflict and resolve it before implementation.

## 2. Confirm the solution before execution

For changes with meaningful scope, produce a compact plan that a reviewer can understand without reading the whole repository. It must state:

- observable behavior and affected users
- reusable implementation points and the smallest intended change surface
- special cases, failure handling, data or compatibility impact
- acceptance evidence, including what requires human interaction
- release, rollback, and authorization boundaries

Use cross-review for plans and risky changes. A reviewer checks assumptions, boundaries, maintainability, reuse, and business truth. The user or responsible owner confirms the chosen behavior before irreversible implementation or release.

## 3. Separate execution and review

Keep requirement decomposition, implementation, review, and acceptance distinct even when one agent performs them. Review the resulting diff and affected callers after implementation. Convert findings into bounded repair tasks rather than allowing an unstructured loop of edits.

## 4. Test in batches and by layer

- Group related paths and untested functions on the same page or workflow into one pass. Do not reopen a page only to repeat an already verified action.
- Use the current mainline goal to choose coverage. Track tested and untested capabilities explicitly.
- Assign deterministic logic, contract, regression, and performance checks to automation. Reserve human checks for visual layout, interaction quality, platform behavior, permissions, and real-world flows.
- Run focused checks after a local change, then run the relevant end-to-end chain and a bounded regression pass after the feature is complete.
- Turn stable repeated checks into scripts, fixtures, commands, or reusable browser flows. Keep test data and environment boundaries explicit.
- A passing build or unit test is evidence of that layer only. Do not report it as business acceptance or real deployment validation.

## 5. Stop repeated failure and change the approach

After repeated failures with the same diagnosis, stop adding retries. Re-check the premise, obtain an independent review or alternate implementation approach, and decide whether to simplify, replace, or defer the feature. Record the failed approach and the reason so later agents do not repeat it.

## 6. Release with recovery paths

Before release, verify branch and revision, changed configuration, migrations, artifact identity, target environment, health checks, and rollback materials. Keep the last known-good code, configuration, static assets, database backup or migration reversal, queue state, and service topology available according to the project rules. Record upload, review, publish, deployment, and user acceptance as separate events.

When a client or service becomes unusable, provide the documented recovery entry first. A safe mode may show a recovery message and the supported update path while preserving enough diagnostics to investigate. Do not conceal a failed release as a successful test.

## 7. End every long task with a handoff

The final handoff lists changed files, current behavior, evidence by test layer, untested areas, unresolved conflicts, release status, and rollback location. It also states whether any commit, push, upload, deployment, data change, or external message occurred.
