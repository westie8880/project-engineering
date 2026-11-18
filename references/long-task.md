# Long-running complex project guardrails

Use this reference for multi-step, iterative, cross-repository, release, deployment, or repeatedly failing tasks. It distills the recurring failure modes of long AI-assisted development into operating rules that remain compatible with framework, testing, design, deployment, and document Skills.

## 1. Prevent implementation drift

Long-running AI development commonly accumulates several forms of drift:

- each new screen or module develops its own style, interaction pattern, and component variant;
- values are embedded in views, services, scripts, and tests instead of having one configuration owner;
- equivalent logic is copied because the agent no longer recognizes an existing utility or component;
- replaced implementations remain in the repository as dead branches, temporary routes, stale comments, or unused assets;
- an old prototype, plan, or deployment note continues to influence implementation after the business decision has changed.

- Reuse the project's components, utilities, tokens, contracts, modules, and existing workflows before creating a parallel version.
- Keep configurable values in configuration or typed constants with one owner. Do not scatter fixed values through views, services, scripts, and tests.
- Search callers and references before replacing an implementation. After a confirmed fix, remove superseded attempts, temporary routes, stale copy, dead comments, and unused trial artifacts.
- Treat the active technical and business handbooks as navigation. Archive superseded rules with effective periods instead of leaving contradictory active copies.
- When a plan, prototype, or old deployment record conflicts with code or current user decisions, label the conflict and resolve it before implementation.

## 2. Confirm a readable solution before execution

For changes with meaningful scope, produce a compact plan that a responsible reviewer can understand without reading the whole repository. A valid plan must answer:

- observable behavior and affected users
- reusable implementation points and the smallest intended change surface
- special cases, failure handling, data or compatibility impact
- acceptance evidence, including what requires human interaction
- release, rollback, authorization boundaries, and the person or system that must confirm them

Use cross-review for plans and risky changes. A reviewer checks assumptions, boundaries, maintainability, reuse, and business truth. The user or responsible owner confirms the chosen behavior before irreversible implementation or release.

## 3. Separate implementation, review, and acceptance

Keep requirement decomposition, implementation, review, and acceptance distinct even when one agent performs them. Review the resulting diff, affected callers, data changes, and user-visible behavior after implementation. Reviewers must check business truth, maintainability, reuse of existing capabilities, and whether the test evidence has real value. Convert findings into bounded repair tasks rather than allowing an unstructured loop of edits.

## 4. Develop in parallel and test in batches and layers

- Group related paths and untested functions on the same page or workflow into one pass. Do not reopen a page only to repeat an already verified action.
- Use the current mainline goal to choose coverage. Track tested and untested capabilities explicitly.
- Assign deterministic logic, contract, regression, and performance checks to automation. Reserve human checks for visual layout, interaction quality, platform behavior, permissions, and real-world flows.
- Run focused checks after a local change, then run the relevant end-to-end chain and a bounded regression pass after the feature is complete.
- Turn stable repeated checks into scripts, fixtures, commands, or reusable browser flows. Keep test data and environment boundaries explicit.
- A passing build or unit test is evidence of that layer only. Do not report it as business acceptance or real deployment validation.
- Independent work may proceed in separate branches or directories. Merge conflicts, shared data, and shared service state must be reconciled before acceptance.
- Human acceptance covers visual layout, interaction quality, platform behavior, permission prompts, and real-world flows that automation cannot establish.

## 5. Convert recurring failure into project rules

When the same class of issue appears repeatedly, record the rule at the correct level instead of relying on a reminder in the current conversation. Examples include interaction conventions, component reuse, configuration ownership, branch and environment selection, evidence requirements, and cleanup obligations. Rules belong in the project handbook or the relevant module reference. They must identify the active rule and archive the superseded version so documentation does not become a second source of contradiction.

## 6. Stop repeated failure and change the approach

After repeated failures with the same diagnosis, stop adding retries. Re-check the premise, obtain an independent review or alternate implementation approach, and decide whether to simplify, replace, or defer the feature. Record the failed approach and the reason so later agents do not repeat it.

## 7. Release with recovery paths and safe mode

Before release, verify branch and revision, changed configuration, migrations, artifact identity, target environment, health checks, and rollback materials. Keep the last known-good code, configuration, static assets, database backup or migration reversal, queue state, and service topology available according to the project rules. Record upload, review, publish, deployment, and user acceptance as separate events.

When a client or service becomes unusable, provide the documented recovery entry first. A safe mode may show a recovery message and the supported update path while preserving enough diagnostics to investigate. Do not conceal a failed release as a successful test.

## 8. End every long task with a handoff

The final handoff lists changed files, current behavior, evidence by test layer, untested areas, unresolved conflicts, release status, and rollback location. It also states whether any commit, push, upload, deployment, data change, or external message occurred.
