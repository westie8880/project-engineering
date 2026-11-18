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
- **批量测试**：这是为了解决 Codex 容易出现的过量防御性测试。它不把“多测几遍”当成质量，而是先列出当前任务真正需要证明的断言，再按页面、状态、身份、数据和环境分组。到达一个页面后，一次性检查当前主线中尚未覆盖的相关功能，复用相同的登录、导航和夹具；已经有有效证据的前置步骤不再机械重跑。共享状态下先做无副作用检查，再做写操作，最后处理会改变前置条件的取消、删除或清理动作。只有代码、配置、角色、环境、状态或上次证据发生影响时，才针对受影响断言复测。
- **长任务管理**：执行前明确目标和边界，实施与复查分开进行。修复得到确认后删除被替代的错误尝试，连续失败时停止无效重试并更换排查方向。
- **发布与部署**：维护分支、版本、制品、服务、主机、端口、域名、配置来源、迁移、健康检查、备份、回滚和待解决问题的部署索引。上传、代码审查、发布、部署和验收分别记录。
- **业务与技术手册**：维护互相映射的业务迭代手册和技术迭代手册。当前规则放在活动区，废弃规则保留在历史区，并记录生效范围、替代原因和关联证据。
- **新智能体交接**：新对话先读取项目说明、索引、适配器、当前手册和部署记录，再开始工作。先报告已识别的项目范围、当前版本和下一步动作，然后承接已有进度。

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
- **Batch-oriented testing**: This prevents Codex from responding to uncertainty with excessive defensive testing. It first lists the claims the task must prove, then groups them by page, state, identity, data, and environment. Once a workflow reaches a page, related unverified actions on the current path are checked together while valid login, navigation, and fixture evidence is reused. Side-effect-free checks come before writes, and destructive actions such as cancellation, deletion, or cleanup come last. Retesting is limited to claims affected by code, configuration, role, environment, state, or invalidated evidence.
- **Long-task control**: Establishes scope before execution and separates implementation from review. After a fix is confirmed, superseded attempts are removed. Repeated failures trigger a change of approach instead of unlimited retries.
- **Release and deployment**: Maintains an index of branches, revisions, artifacts, services, hosts, ports, domains, configuration sources, migrations, health checks, backups, rollback paths, and unresolved gaps. Upload, review, publication, deployment, and acceptance are recorded separately.
- **Business and technical handbooks**: Maintains linked business-iteration and technical-iteration handbooks. Current rules stay active, while superseded rules remain in history with scope, replacement reason, and evidence.
- **New-agent handoff**: A new conversation reads the project overview, indexes, adapter, current handbooks, and deployment records before asking for basics. It reports the resolved scope, current revision, and next action, then continues from recorded progress.

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
