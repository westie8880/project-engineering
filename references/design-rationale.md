# 设计动机与解决的问题 / Design rationale and problems addressed

## 中文说明

### 1. 项目接入与有界检索

**痛点**：新对话或新智能体经常重新扫描仓库，读到备份、生成物和历史资料。上下文变长后，当前规则被旧规则冲淡，操作人还要重复解释项目背景。

**设计**：先解析项目根目录、`AGENTS.md`、手册入口、当前分支和部署索引，再按任务读取当前记录。历史资料只在排查对应问题时按稳定 ID取用。

**结果**：减少重复询问和无效扫描，让新对话从项目已经确认的基线继续。

### 2. 跨技术栈兼容

**痛点**：工程规则容易绑定某个项目的 Java 包名、Vue 目录或服务器结构，换项目后无法使用，甚至诱导智能体把示例结构硬套到真实仓库。

**设计**：规则描述能力和边界，不写死语言、框架、包名、目录或部署平台。项目适配器负责映射实际技术栈，专用 Skill 负责具体框架和工具。

**结果**：同一套项目工程流程可以和 Java、Go、Vue、React、Python、移动端、H5 及其他 Skill 协同。

### 3. 架构与兼容性检查

**痛点**：局部修复容易绕过模块边界、重复实现已有逻辑、破坏旧调用方。问题可能暂时消失，后续却出现接口不一致、数据归属错误或迁移遗漏。

**设计**：修改前确认数据归属、调用方、公开接口、迁移和旧行为。新增持久化放进正确模块，已有契约在需求未改变时保持可用。

**结果**：把“能跑”提升为“在现有系统里能长期维护和兼容”。

### 4. 批量测试

**痛点**：Codex 容易用重复登录、重复导航和重复端到端流程应对不确定性，形成过量防御性测试，消耗时间并污染测试数据。

**设计**：按页面、身份、数据、平台和环境建立未测断言清单，复用有效前置证据，合并同一主线上的相关动作。读检查先做，写操作随后做，取消、删除和清理最后做。

**结果**：用最少的代表性路径覆盖最多的新断言，既避免漏测，也避免把已经证明的路径反复重跑。

### 5. 长任务失控与错误尝试治理

**痛点**：长期迭代会同时出现多种失控现象：页面和组件各自实现导致样式与交互漂移，固定值散落在多个文件，同一逻辑被重复编写，旧代码和临时路由持续残留，早期方案和过期文档继续被采用。长对话中又会叠加多次修正、错误实现和过期方案，用户确认新逻辑后，后续智能体仍可能读到旧代码并恢复错误行为。

**设计**：执行前形成负责人可读的方案，说明复用点、最小改动面、异常处理、兼容性、验收证据、发布授权和回滚路径。把需求拆解、实施、代码复查、分层测试、人工验收和清理作为独立阶段。确认修复后删除被替代的尝试、临时路由、过期文案和无用测试资产；连续失败时重新检查前提，邀请独立复查或更换方案；反复出现的问题沉淀为项目规则。发布前保留最后可用版本和安全恢复入口。

**结果**：长任务不会只靠当前对话记忆推进。代码、文档、测试、发布和回滚状态各有证据，项目不会随着迭代积累越来越多相互冲突的实现。

### 6. 发布、部署与环境隔离

**痛点**：测试环境、正式环境、分支、域名、端口和服务器容易混淆。只记住“已经部署”无法回答部署了哪一版、连接哪套数据库、如何回滚，以及小程序为什么仍然访问旧服务。

**设计**：为分支、提交、制品、服务、主机、端口、域名、配置来源、数据库、健康检查和回滚路径建立部署索引。上传、发布、部署和验收分别记录，并在执行前核对目标环境。

**结果**：换对话或换操作人后，可以直接恢复环境事实，降低误切正式环境和测试数据串线的风险。

### 7. 知识索引、业务技术对齐与跨对话交接

**痛点**：代码人员、产品人员和用户对同一业务场景的描述可能不一致，聊天记录、原型、代码和配置也可能互相冲突。对话过长后频繁压缩上下文，换一个对话或智能体时，改动很难一次性迁移，已经修复的问题还可能被旧规则重新带回来。

**设计**：建立分层索引，而不是把所有资料堆在 README。入口 README 指向稳定 ID 索引，索引再指向当前业务手册、当前技术手册、部署索引、证据目录和历史快照。业务手册记录规则、状态、例外和用户决策，技术手册记录语言、框架、模块、接口、数据和部署映射。原型、决策、代码、配置、测试和发布证据通过稳定 ID 关联。当前规则放活动区，旧规则进入历史区并记录生效范围、替代原因和证据。

**交接方式**：上下文压缩或更换工具后，新智能体先读入口 README、索引、适配器、当前快照、部署记录和活动证据，再报告范围、版本、环境和下一步动作。

**结果**：日常理解只加载当前快照，冲突排查可以定位证据，换对话时接的是项目状态而不是一段不完整的聊天摘要。

## English documentation

### 1. Onboarding and bounded retrieval

**Problem**: New agents often rescan repositories and ingest backups, generated files, and stale history. As context grows, current rules are diluted by obsolete decisions.

**Design**: Resolve the project root, `AGENTS.md`, handbook entry points, branch, and deployment index first. Load historical material only by stable ID when the investigation needs it.

**Outcome**: A new conversation continues from an established baseline instead of repeating discovery and background questions.

### 2. Cross-stack compatibility

**Problem**: Rules tied to one project’s Java packages, Vue directories, or server topology become unusable elsewhere and encourage copying the wrong structure.

**Design**: Describe capabilities and boundaries without hard-coding languages, frameworks, package names, directories, or deployment platforms. Project adapters map the real stack, while specialized Skills handle concrete tools.

**Outcome**: The workflow remains reusable across Java, Go, Vue, React, Python, mobile, H5, and other Skills.

### 3. Architecture and compatibility checks

**Problem**: A local fix can bypass module ownership, duplicate existing logic, or break old callers. The immediate symptom disappears while interface, data, or migration problems remain.

**Design**: Check data ownership, callers, public contracts, migrations, and previous behavior before editing. New persistence belongs to the owning module, and existing contracts remain usable unless the request changes them.

**Outcome**: The change remains maintainable and compatible inside the real system.

### 4. Batch-oriented testing

**Problem**: Codex can answer uncertainty with repeated logins, navigation, and full end-to-end reruns. This creates defensive over-testing, wastes time, and contaminates test data.

**Design**: Track unverified claims by page, identity, data, platform, and environment. Reuse valid prerequisites and combine related actions on the same workflow. Run reads first, writes next, and destructive cleanup last.

**Outcome**: Representative paths prove more new claims without either skipping affected coverage or repeating verified paths.

### 5. Long-task drift and superseded-attempt control

**Problem**: Long-running iteration accumulates several forms of drift: independent screens and components develop inconsistent styles and interactions, fixed values spread across files, equivalent logic is copied, obsolete code and temporary routes remain, and early plans or stale documentation continue to influence implementation. Long conversations then accumulate corrections, failed implementations, and obsolete alternatives. Later agents may read old code and restore a behavior that the user already rejected.

**Design**: Produce a plan that a responsible owner can review, covering reuse points, the smallest change surface, failure handling, compatibility, acceptance evidence, release authorization, and rollback. Separate requirement decomposition, implementation, code review, layered testing, human acceptance, and cleanup. Remove superseded attempts, temporary routes, stale copy, and unused test assets after confirmation. Recheck the premise or obtain an independent review after repeated failure, turn recurring problems into project rules, and retain a known-good release plus a documented recovery entry.

**Outcome**: Long tasks do not depend on conversation memory alone. Code, documentation, tests, release state, and rollback state remain evidence-backed, and the project does not accumulate conflicting implementations as iteration continues.

### 6. Release, deployment, and environment isolation

**Problem**: Test and production environments, branches, domains, ports, and hosts are easy to confuse. “It was deployed” does not identify the revision, database, rollback path, or reason a client still reaches an old service.

**Design**: Index branches, commits, artifacts, services, hosts, ports, domains, configuration sources, databases, health checks, and rollback paths. Record upload, publication, deployment, and acceptance separately and verify the target before acting.

**Outcome**: Another operator or conversation can recover environment facts without accidentally switching production or mixing test data.

### 7. Knowledge indexing, business-technical alignment, and handoff

**Problem**: Developers, product staff, and users may describe the same business scenario differently. Chat history, prototypes, code, and configuration can conflict. After context compression or a conversation or agent change, a change may be migrated incompletely and a fixed defect may return through an obsolete rule.

**Design**: Use a layered index instead of putting every fact in README. The entry README points to stable-ID indexes, which point to current business and technical handbooks, the deployment index, evidence directories, and historical snapshots. The business handbook records rules, states, exceptions, and user decisions. The technical handbook records languages, frameworks, modules, interfaces, data, and deployment mappings. Prototypes, decisions, code, configuration, tests, and release evidence are linked by stable IDs. Current rules stay active, while replaced rules move to history with scope, replacement reason, and evidence.

**Handoff**: After context compression or a tool change, the next agent reads the entry README, indexes, adapter, current snapshots, deployment records, and active evidence before reporting scope, revision, environment, and next action.

**Outcome**: Daily work loads the current snapshot, conflict investigations can locate evidence, and a new conversation inherits project state instead of reconstructing it from an incomplete chat summary.
