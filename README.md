# Project Engineering

`project-engineering` is a portable Codex Skill for sustained software-project work. It gives an agent a bounded way to understand an unfamiliar repository, preserve project decisions, coordinate specialized Skills, test related paths in batches, and leave an evidence-backed handoff.

## 中文说明

`project-engineering` 是一个可移植的 Codex 项目工程 Skill，面向持续迭代的软件项目。它帮助智能体在接手陌生仓库时限定检索范围，读取项目规则和当前有效的业务、技术手册，复用既有架构和接口，按批次验证相关功能，并留下可追溯的交接证据。

它覆盖项目接入、功能开发、调试、代码审查、测试、配置、发布、部署、迁移和知识交接。它兼容 Java、Go、Vue、React、Python、移动端、H5 以及其他技术栈，不把某个语言、框架、包名或部署拓扑固化成通用规则。它还要求在确认修复后删除被替代的错误尝试，避免旧代码、旧文档和过期方案继续干扰后续工作。

Skill 通过项目内的业务迭代手册、技术迭代手册和部署索引保存长期知识。当前规则直接进入上下文，历史快照按稳定 ID 和问题范围按需检索。新对话或新智能体先读取项目根规则、手册入口、当前记录和部署记录，再继续任务，减少重复扫描仓库和重复询问基础信息。

测试采用批量思路。同一页面或业务链路上尚未验证的相关动作合并覆盖，区分自动化检查、真实联调、浏览器或设备验证与人工验收，不为了验证两个按钮而重复走两遍完全相同的前置流程。发布、部署、验收和回滚证据分别记录，凭据只保存在用户批准的仓库外私密配置中。

## English summary

`project-engineering` is a portable Codex Skill for sustained software-project work. It bounds repository discovery, loads current project rules and handbook evidence, preserves architecture and compatibility contracts, coordinates specialized Skills, tests related paths in batches, removes superseded attempts after confirmed fixes, and leaves an evidence-backed handoff.

It covers onboarding, implementation, debugging, review, testing, configuration, release, deployment, migration, documentation, and knowledge transfer. It works across Java, Go, Vue, React, Python, mobile, H5, and other stacks without hard-coding one language, framework, package layout, or deployment topology. Current business and technical rules remain easy to retrieve, while historical snapshots are available by stable ID when an investigation requires them.

Testing is organized around representative workflows and untested related actions. Automated checks, integration, browser or device verification, and human acceptance are recorded separately. Release, deployment, acceptance, rollback, and credential handling remain auditable and independently controlled.

## What it handles

- **Project onboarding**. Resolves the project root, reads applicable `AGENTS.md` files, discovers the existing documentation root, and avoids scanning unrelated dependencies, backups, generated output, or other projects.
- **Bounded context retrieval**. Uses a project handbook with stable business and technical IDs, current entries, evidence links, and opt-in historical snapshots. A new conversation can continue from the recorded baseline without rereading the whole repository.
- **Cross-stack development**. Routes Java, Go, Vue, React, Python, mobile, H5, and other stacks through the repository’s own architecture rules. It does not assume a language, framework, package layout, or deployment platform.
- **Architecture and compatibility**. Checks module ownership, public interfaces, data boundaries, existing callers, migrations, and old behavior before changing code. It keeps new business persistence in the owning module and preserves compatibility contracts unless the request changes them.
- **Batch-oriented testing**. Groups related untested actions on the same page or workflow, separates automated checks from human acceptance, and records what each layer proves. It avoids reopening a flow merely to repeat an already verified action.
- **Long-task control**. Confirms meaningful plans before execution, separates implementation from review, removes superseded attempts after a confirmed fix, stops repeated failures from turning into unbounded retries, and changes approach when the premise is wrong.
- **Release and deployment knowledge**. Maintains a technical deployment index for branches, revisions, artifacts, services, hosts, ports, domains, configuration sources, migrations, health checks, backups, rollback, and unresolved gaps. Upload, review, publish, deployment, and acceptance remain separate events.
- **Business and technical handbooks**. Keeps a business iteration view and a technical iteration view linked by stable IDs. Current rules stay easy to retrieve. Superseded rules move to history with effective periods and reasons.
- **New-agent handoff**. A new agent reads the project README, index, adapter, relevant active entries, and deployment records before asking for project basics. It reports the resolved scope and next authorized action, then continues from the evidence already recorded.

## When to use it

Use it for repository or project tasks such as onboarding, feature work, debugging, code review, testing, configuration, release, deployment, migration, documentation, and handoff. It is intentionally not a general writing or standalone-artifact Skill.

## How it works

The entry point is [`SKILL.md`](SKILL.md). It routes only the references needed for the current task.

| Reference | Purpose |
|---|---|
| [`agent-handoff.md`](references/agent-handoff.md) | Startup contract for a new conversation, new agent, or compressed context |
| [`long-task.md`](references/long-task.md) | Plan confirmation, reuse and cleanup, cross-review, batch testing, stop-loss, and recovery |
| [`development.md`](references/development.md) | General implementation and repository boundaries |
| [`frontend.md`](references/frontend.md) | Frontend-specific review and verification |
| [`backend.md`](references/backend.md) | Backend-specific architecture and data rules |
| [`batch-testing.md`](references/batch-testing.md) | Coverage planning and test evidence |
| [`handbook-maintenance.md`](references/handbook-maintenance.md) | Two-handbook structure, stable IDs, history, and deployment index |
| [`project-adapter.md`](references/project-adapter.md) | Compatibility contract with existing projects and other Skills |

The dependency-free [`scripts/handbook.py`](scripts/handbook.py) helper supports bounded index lookup and structural validation. It does not claim that code or business behavior is correct by itself.

## Handbook placement

The two handbooks belong inside the project’s existing documentation root. The preferred layout is:

```text
<project-root>/docs/project-handbook/
├── README.md
├── index.json
├── active/
│   ├── business/业务迭代手册.md
│   └── technical/技术迭代手册.md
├── history/
└── evidence/
```

If a project already has a shared documentation root, the Skill preserves it and records the resolved path in that project’s README and adapter. Handbook generation is local by default. It does not commit, push, upload, publish, or deploy generated documents unless the user separately authorizes that action.

Deployment credentials may be kept in a user-approved private manifest outside the repository. Handbooks record only the manifest path and field names. Passwords, keys, tokens, cookies, and private connection material must not enter this repository.

## Installation

Copy this directory to the Codex skills directory, then invoke it explicitly with `$project-engineering` or let normal Skill discovery select it for a project task.

```text
<CODEX_HOME>/skills/project-engineering/
```

The Skill keeps automatic invocation enabled. It remains compatible with specialized Skills such as framework, testing, browser, document, and frontend design workflows. Specialized Skills perform tool-specific work. This Skill supplies project scope, evidence retrieval, coverage tracking, cleanup, and handoff.

## Validation

Run the structural validator from the Skill Creator package when available, then inspect the actual references and run any changed helper scripts. The handbook helper can be checked with:

```text
python scripts/handbook.py check <path-to-project-handbook> --history
python scripts/handbook.py lookup <path-to-project-handbook> T.DEPLOY
```

These checks validate structure and navigation. They do not replace builds, integration tests, browser or device acceptance, deployment probes, or human confirmation.

## Design principles

The Skill is intentionally stack-neutral, evidence-oriented, and progressively disclosed. It favors small, reversible changes, current active knowledge, explicit uncertainty, and concrete recovery paths. It does not turn one project’s package names, one failed attempt, or one deployment topology into a universal rule.
