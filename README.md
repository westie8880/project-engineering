# Project Engineering

## 中文说明

### 这是什么

`project-engineering` 是一个面向长期软件项目的 Codex Skill。它帮助智能体接手陌生项目、理解现有约束、实施代码变更、组织测试、处理发布部署，并把已经确认的业务和技术知识留下来，方便后续对话或其他智能体继续工作。

它不绑定 Java、Go、Vue 或某一种工程结构。项目使用什么语言、框架、数据库和部署方式，以项目自身的规则和证据为准。

### 适用关键词

项目工程 Skill、代码开发、仓库接手、代码审查、问题修复、重构、批量测试、集成测试、版本发布、部署、回滚、数据库迁移、技术迭代手册、业务迭代手册、项目交接、智能体工作流、跨技术栈开发。

### 处理范围

- **项目接入**：定位项目根目录，读取适用的 `AGENTS.md` 和项目手册入口，识别当前任务涉及的模块。不会扫描无关项目、备份目录、依赖目录或生成文件。
- **上下文检索**：优先读取当前有效的业务规则、技术规则和部署记录。历史版本使用稳定 ID 按问题查询，避免每次新对话都把整套历史资料重新放进上下文。
- **跨技术栈开发**：根据项目已有的架构、模块边界和代码约定工作，不预设包名、框架、目录结构或服务器拓扑。
- **架构与兼容性**：修改前检查数据归属、公开接口、现有调用方、迁移方式和旧行为。新业务数据放在正确的业务模块中，已有接口和调用方在需求未改变时继续可用。
- **业务约束落地**：把资格、身份、资源配额、状态、幂等、时间窗口、权限、数据归属和撤销规则等业务约束写成可检索规则，并映射到代码、配置、数据库和测试。业务约束不能只存在于某次聊天或某个人的理解里。
- **最小业务模型**：只为已确认的业务规则增加字段、状态、台账、接口和流程。不得因为“以后可能用到”就堆加没有实际读写路径、验收标准或数据来源的字段，不得用过度设计替代需求确认。
- **编码规范与质量边界**：遵循项目已有的命名、分层、异常、事务、日志、注释、迁移、接口和文件规模规则。规范用于保证后续修改可读、可审查、可回滚，不以机械格式化代替设计判断。
- **DDD 领域模型**：在 AI 辅助开发时代，代码生成速度提高后，单体项目最容易失控的地方变成模块边界和业务归属。分布式架构的一部分价值来自多人协同和团队隔离，而在由少量人员和智能体持续维护的单体项目中，模块化本身更直接地承担隔离职责。修改前确认限界上下文、聚合、实体、值对象、领域服务、仓储和模块边界，防止 AI 把不同业务塞进共享层或跨模块直接写数据。
- **设计模式与复用**：AI 倾向于把新需求继续写进当前文件，直到控制器、服务或组件承担过多职责。设计模式提供可识别的结构约束，让变化点进入策略、工厂、适配器、模板、状态或领域服务等明确位置。先识别项目已有模式，再决定复用、扩展或新增，避免单文件膨胀，也避免为了形式增加没有变化点支撑的抽象层。
- **批量测试**：这是为了解决 AI 测试只会一个点一个点测，以及由此产生的过量防御性测试。到达一个页面后，先以当前主线为范围，扫一遍这个页面所有尚未测过的功能、状态、按钮、异常提示、权限差异和数据展示，不为了验证两个按钮重复登录和导航。已经测过且证据仍有效的前置流程直接复用；只有代码、配置、角色、环境、状态或证据失效时才复测受影响部分。共享状态下先做读取和展示检查，再做写操作，最后做取消、删除和清理。
- **长任务管理**：针对长期迭代中最容易失控的完整链路建立约束。防止页面和组件各自实现导致样式、交互和能力漂移，防止固定值散落在多个文件，防止同一逻辑重复编写，防止旧实现、临时路由、过期注释和废弃方案继续留在项目中。执行前形成可供负责人审阅的方案，明确复用点、变更边界、异常处理、验收证据、发布授权和回滚路径。实施、复查和人工验收分开，反复失败时重新检查前提而不是无限重试，稳定的重复问题沉淀为项目规则，发布时保留可恢复的安全入口。
- **发布与部署**：维护分支、版本、制品、服务、主机、端口、域名、配置来源、迁移、健康检查、备份、回滚和待解决问题的部署索引。上传、代码审查、发布、部署和验收分别记录。
- **知识索引与跨对话交接**：这是同一套核心机制。项目不是把所有资料堆在 README 里，而是用入口 README、稳定 ID 索引、当前业务手册、当前技术手册、部署索引、证据目录和历史快照组成分层结构。代码人员、产品人员和用户对同一业务场景的描述出现冲突时，按 ID 关联原型、决策、代码、配置、测试和发布证据，明确当前规则、历史规则、事实和待确认项。对话过长发生上下文压缩，或切换到新的对话和智能体时，先读取索引和当前快照，再按任务加载证据，避免改动无法完整迁移、旧规则被误用或已经修复的问题重新出现。

### 适用场景

适用于项目接手、功能开发、问题修复、代码审查、测试、配置调整、数据库迁移、版本发布、部署、回滚、文档维护和智能体交接。普通问答、独立文案和与项目无关的单次文件处理不需要使用这个 Skill。

### 工作方式

入口文件是 [`SKILL.md`](SKILL.md)。它会根据任务类型加载所需的参考规则，而不是每次读取所有资料。

项目手册建议放在项目已有的文档根目录下：

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

索引不是目录清单，而是检索入口。每条记录使用稳定 ID，记录当前状态、适用范围、来源证据、关联代码或配置、验证版本和历史关系。日常只读取活动区和任务相关证据，历史区仅在冲突排查、回归分析或版本追溯时读取。

手册默认只在本地生成和维护。除非用户单独授权，否则不会自动提交、推送、上传、发布或部署。部署密码、密钥、令牌和连接信息只放在仓库外的私密配置中，手册只记录私密配置的位置和字段名称。

### 参考文件

| 文件 | 用途 |
|---|---|
| [`agent-handoff.md`](references/agent-handoff.md) | 新对话、新智能体和上下文压缩后的启动流程 |
| [`long-task.md`](references/long-task.md) | 长任务计划、复查、失败止损、恢复和交接 |
| [`development.md`](references/development.md) | 通用开发边界和仓库操作规则 |
| [`frontend.md`](references/frontend.md) | 前端开发、兼容性和界面验证 |
| [`backend.md`](references/backend.md) | 后端架构、数据边界和接口规则 |
| [`batch-testing.md`](references/batch-testing.md) | 批量测试范围和测试证据 |
| [`design-rationale.md`](references/design-rationale.md) | 各项规则要解决的痛点、设计原因和预期结果 |
| [`origin-pain-points.md`](references/origin-pain-points.md) | 从长期协作问题整理出的完整设计依据 |
| [`handbook-maintenance.md`](references/handbook-maintenance.md) | 双手册、稳定 ID、历史归档和部署索引 |
| [`project-adapter.md`](references/project-adapter.md) | 与现有项目和其他 Skill 的兼容方式 |

### 安装与验证

将此目录复制到 Codex 的 Skill 目录：

```text
<CODEX_HOME>/skills/project-engineering/
```

可以显式使用 `$project-engineering`，也可以让项目任务的 Skill 检索自动选择它。结构检查可以使用 Skill Creator 提供的校验工具。手册辅助脚本支持：

```text
python scripts/handbook.py check <path-to-project-handbook> --history
python scripts/handbook.py lookup <path-to-project-handbook> T.DEPLOY
```

这些命令只能检查文件结构和索引导航，不能代替构建、集成测试、真实联调、设备验收或人工确认。

### 设计原则

保持技术栈中立，优先使用当前有效证据，逐步加载上下文，明确记录不确定性，优先采用小而可回滚的改动。项目规则应当帮助智能体继续工作，而不是把某个项目的包名、某次失败尝试或某套部署结构变成所有项目的固定规则。

## English documentation

### What this is

`project-engineering` is a Codex Skill for long-lived software projects. It helps an agent take over an unfamiliar repository, understand its constraints, implement changes, organize verification, handle release and deployment work, and preserve confirmed business and technical knowledge for later conversations or agents.

It is independent of Java, Go, Vue, or any particular project layout. The project’s own rules and evidence determine its languages, frameworks, databases, and deployment model.

### Search terms

Software project engineering skill, repository onboarding, code implementation, bug fixing, refactoring, code review, batch testing, integration testing, release management, deployment workflow, rollback, database migration, technical handbook, business handbook, project handoff, agent workflow, cross-stack development.

### What it handles

- **Project onboarding**: Resolves the project root, reads applicable `AGENTS.md` files and handbook entry points, identifies relevant modules, and avoids unrelated projects, backups, dependencies, and generated output.
- **Context retrieval**: Loads current business rules, technical rules, and deployment records first. Historical versions are retrieved by stable IDs when an investigation needs them, so a new conversation does not reload the entire history.
- **Cross-stack development**: Follows the project’s existing architecture, module boundaries, and coding conventions without assuming package names, frameworks, directory layouts, or server topology.
- **Architecture and compatibility**: Checks data ownership, public interfaces, existing callers, migrations, and previous behavior before editing. New persistence belongs in the owning module, and existing contracts remain usable when the request does not change them.
- **Business constraints**: Turns qualification, identity, resource limits, state, idempotency, time windows, permissions, data ownership, and revocation rules into retrievable constraints mapped to code, configuration, database, and tests. A business rule cannot live only in a chat or in one person’s memory.
- **Minimal business model**: Adds fields, states, ledgers, interfaces, and workflow steps only for confirmed requirements. Do not add speculative fields or processes without a real read/write path, acceptance criterion, or source of truth.
- **Coding standards and quality boundaries**: Follows the project’s naming, layering, exception, transaction, logging, comment, migration, API, and file-size rules. Standards keep later changes readable, reviewable, and reversible rather than replacing design judgment with mechanical formatting.
- **DDD domain modeling**: In the AI-assisted development era, faster code generation makes module ownership and business boundaries a primary risk in many monolithic systems. Distributed architecture still has valid operational uses, but its team-collaboration benefit is less decisive when a small team and agents maintain one system. DDD supplies explicit bounded contexts, aggregates, entities, value objects, domain services, repositories, and module boundaries so generated code does not move unrelated business into shared layers or write another module’s data directly.
- **Design patterns and reuse**: AI tends to keep adding a new requirement to the current file until a controller, service, or component owns too many responsibilities. Design patterns provide recognizable structural constraints that place variation in a strategy, factory, adapter, template, state, or domain service. Recognize existing patterns before extending them, preventing both single-file growth and abstractions that have no real variation point.
- **Batch-oriented testing**: This addresses the tendency of AI testing to verify one point at a time and then compensate with excessive defensive reruns. After reaching a page, the agent scans the whole page within the current workflow for untested features, states, buttons, error messages, permission differences, and data presentation. It does not repeat login and navigation just to verify two buttons. Valid prerequisite evidence is reused. Retesting is limited to claims affected by code, configuration, role, environment, state, or invalidated evidence. Reads come before writes, and cancellation, deletion, and cleanup come last.
- **Long-task control**: Governs the full failure chain of long-running iteration. It prevents style, interaction, and capability drift caused by independent implementations, scattered hard-coded values, duplicated logic, retained obsolete code, temporary routes, stale comments, and outdated plans. Before execution, it produces a reviewable plan covering reuse points, change boundaries, failure handling, acceptance evidence, release authorization, and rollback. Implementation, review, and human acceptance remain separate. Repeated failure triggers premise rechecking instead of unlimited retries, recurring issues become project rules, and releases retain a documented recovery entry.
- **Release and deployment**: Maintains an index of branches, revisions, artifacts, services, hosts, ports, domains, configuration sources, migrations, health checks, backups, rollback paths, and unresolved gaps. Upload, review, publication, deployment, and acceptance are recorded separately.
- **Knowledge indexing and cross-conversation handoff**: These are one mechanism. The project is not a pile of documents in README. It uses a layered structure of an entry README, stable-ID indexes, current business and technical handbooks, a deployment index, evidence directories, and historical snapshots. When developers, product staff, and users describe the same business scenario differently, stable IDs connect prototypes, decisions, code, configuration, tests, and release evidence so current rules, historical rules, facts, and open questions remain distinguishable. After context compression or a conversation or agent change, the next agent reads the indexes and current snapshots first, then retrieves task-specific evidence. This prevents incomplete migration, stale rules being reused, and fixed defects returning.

### When to use it

Use it for project onboarding, feature work, debugging, code review, testing, configuration, database migration, release, deployment, rollback, documentation maintenance, and agent handoff. Ordinary questions, standalone prose, and unrelated one-off file tasks do not require this Skill.

### How it works

The entry point is [`SKILL.md`](SKILL.md). It loads only the references required by the current task instead of reading every document on every run.

The recommended handbook layout inside an existing project documentation root is:

```text
<project-root>/docs/project-handbook/
├── README.md
├── index.json
├── active/
│   ├── business/business-iteration-handbook.md
│   └── technical/technical-iteration-handbook.md
├── history/
└── evidence/
```

The index is a retrieval map rather than a directory listing. Each record has a stable ID, current status, scope, source evidence, related code or configuration, verification revision, and history links. Daily work reads the active area and task-relevant evidence. History is loaded for conflict investigation, regression analysis, or version tracing.

Handbook generation and maintenance are local by default. The Skill does not commit, push, upload, publish, or deploy them unless the user explicitly authorizes that action. Deployment passwords, keys, tokens, and connection material stay in private configuration outside the repository. Handbooks record only the location and field names.

### Reference files

| File | Purpose |
|---|---|
| [`agent-handoff.md`](references/agent-handoff.md) | Startup flow for a new conversation, new agent, or compressed context |
| [`long-task.md`](references/long-task.md) | Long-task planning, review, stop-loss, recovery, and handoff |
| [`development.md`](references/development.md) | General development boundaries and repository rules |
| [`frontend.md`](references/frontend.md) | Frontend development, compatibility, and interface verification |
| [`backend.md`](references/backend.md) | Backend architecture, data boundaries, and API rules |
| [`batch-testing.md`](references/batch-testing.md) | Batch test coverage and test evidence |
| [`design-rationale.md`](references/design-rationale.md) | Problems addressed, design reasons, and expected outcomes |
| [`origin-pain-points.md`](references/origin-pain-points.md) | Full design basis derived from recurring collaboration problems |
| [`handbook-maintenance.md`](references/handbook-maintenance.md) | Two handbooks, stable IDs, history, and deployment indexing |
| [`project-adapter.md`](references/project-adapter.md) | Compatibility with existing projects and other Skills |

### Installation and validation

Copy this directory to the Codex Skill directory:

```text
<CODEX_HOME>/skills/project-engineering/
```

Invoke it explicitly with `$project-engineering`, or let normal Skill discovery select it for project work. Use the validator provided by Skill Creator for structural checks when available. The handbook helper supports:

```text
python scripts/handbook.py check <path-to-project-handbook> --history
python scripts/handbook.py lookup <path-to-project-handbook> T.DEPLOY
```

These commands validate structure and index navigation. They do not replace builds, integration tests, real integration, device acceptance, or human confirmation.

### Design principles

Keep the workflow stack-neutral, evidence-based, and progressively disclosed. Prefer small reversible changes and explicit uncertainty. Project rules should help an agent continue work without turning one project’s package names, one failed attempt, or one deployment topology into a universal rule.
