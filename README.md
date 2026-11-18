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

## What it handles / 处理范围

- **Project onboarding / 项目接入**. Resolves the project root, reads applicable `AGENTS.md` files, discovers the existing documentation root, and avoids scanning unrelated dependencies, backups, generated output, or other projects. / 解析项目根目录，读取适用的 `AGENTS.md`，发现现有文档根目录，避免扫描无关依赖、备份、生成物和其他项目。
- **Bounded context retrieval / 有界上下文检索**. Uses a project handbook with stable business and technical IDs, current entries, evidence links, and opt-in historical snapshots. A new conversation can continue from the recorded baseline without rereading the whole repository. / 通过稳定的业务和技术 ID、当前条目、证据链接及按需历史快照读取项目手册，让新对话从已记录基线继续，不必重新读取整个仓库。
- **Cross-stack development / 跨技术栈开发**. Routes Java, Go, Vue, React, Python, mobile, H5, and other stacks through the repository’s own architecture rules. It does not assume a language, framework, package layout, or deployment platform. / 按仓库自身架构规则处理 Java、Go、Vue、React、Python、移动端、H5 和其他技术栈，不把语言、框架、包结构或部署平台固化为前提。
- **Architecture and compatibility / 架构与兼容性**. Checks module ownership, public interfaces, data boundaries, existing callers, migrations, and old behavior before changing code. It keeps new business persistence in the owning module and preserves compatibility contracts unless the request changes them. / 修改前检查模块归属、公开接口、数据边界、现有调用方、迁移和旧行为。新业务持久化归属正确模块，除非需求明确改变，否则保留兼容契约。
- **Batch-oriented testing / 批量化测试**. Groups related untested actions on the same page or workflow, separates automated checks from human acceptance, and records what each layer proves. It avoids reopening a flow merely to repeat an already verified action. / 合并同一页面或业务链路中尚未验证的相关动作，区分自动化检查和人工验收，并记录各层验证范围，避免为了重复已验证动作重新走完整流程。
- **Long-task control / 长任务控制**. Confirms meaningful plans before execution, separates implementation from review, removes superseded attempts after a confirmed fix, stops repeated failures from turning into unbounded retries, and changes approach when the premise is wrong. / 执行前确认有实际意义的计划，分离实现与审查，修复确认后删除被替代的错误尝试，阻止重复失败变成无限重试，并在前提错误时调整方案。
- **Release and deployment knowledge / 发布与部署知识**. Maintains a technical deployment index for branches, revisions, artifacts, services, hosts, ports, domains, configuration sources, migrations, health checks, backups, rollback, and unresolved gaps. Upload, review, publish, deployment, and acceptance remain separate events. / 维护分支、版本、制品、服务、主机、端口、域名、配置来源、迁移、健康检查、备份、回滚和未解决问题的部署索引，并分开记录上传、审查、发布、部署和验收事件。
- **Business and technical handbooks / 业务与技术手册**. Keeps a business iteration view and a technical iteration view linked by stable IDs. Current rules stay easy to retrieve. Superseded rules move to history with effective periods and reasons. / 通过稳定 ID 关联业务迭代视图和技术迭代视图，让当前规则易于检索，被替代规则按生效期间和原因归档到历史记录。
- **New-agent handoff / 新智能体交接**. A new agent reads the project README, index, adapter, relevant active entries, and deployment records before asking for project basics. It reports the resolved scope and next authorized action, then continues from the evidence already recorded. / 新智能体先读取项目 README、索引、适配器、相关当前条目和部署记录，再询问基础信息，并报告已解析范围和下一步授权动作，依据已有证据继续工作。

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
