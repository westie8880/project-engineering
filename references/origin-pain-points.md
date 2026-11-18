# 项目工程 Skill 的问题来源与设计响应

## 中文说明

这份文档把项目长期协作中反复出现的问题整理成可检索的设计依据。它记录问题本身、造成的后果以及 Skill 应采取的机制。它不是某个项目的业务规则，也不替代项目自己的手册。

### 1. 上下文压缩和对话迁移

**问题**：长对话会频繁压缩上下文。新对话或新智能体拿不到完整的改动历史、当前分支、环境关系、已验证范围和未完成事项，导致用户重新交代背景，或者已经修复的问题再次被改坏。

**机制**：入口 README、稳定 ID 索引、当前快照、证据目录和交接记录组成可迁移的项目状态。新对话按固定顺序读取当前信息，历史记录按问题加载，不依赖聊天摘要承载全部状态。

### 2. 产品、开发和用户的业务理解冲突

**问题**：产品描述的场景、开发理解的规则、用户实际要求、原型文案和代码行为可能不一致。单靠某个人的记忆无法判断哪一个版本有效。

**机制**：把用户决策、业务规则、原型、代码、配置、测试和发布记录用稳定 ID 关联。记录来源、当前状态、适用范围和待确认事项，出现冲突时先对证据，不用旧聊天内容直接覆盖当前规则。

### 3. 当前规则和历史规则混在一起

**问题**：规则多次调整后，旧方案仍留在文档、代码注释或上下文中。智能体读取到旧内容后，可能恢复已废弃的限制、流程或数据口径。

**机制**：当前规则进入 active 区，废弃规则进入 history 区，历史记录保留生效时间、替代原因和关联证据。默认只加载当前快照，排查历史问题时再加载指定历史 ID。

### 4. 知识没有索引结构

**问题**：资料虽然存在，但没有入口、稳定 ID、模块映射和证据链。新操作人只能全文搜索或依赖聊天回忆，容易漏读关键部署、数据或业务决定。

**机制**：入口 README 指向索引，索引指向业务手册、技术手册、部署索引、证据和历史。每条知识记录应能回答它是什么、适用于哪里、当前是否有效、来源是什么、关联哪些代码和配置。

### 5. 新项目无法直接使用规则

**问题**：如果手册只记录当前项目的包名、模块名和接口，换一个新项目后就失去作用。只靠持续补充也无法解决新项目初次接手时缺少结构的问题。

**机制**：Skill 先提供通用的项目接入、架构识别、手册初始化和证据记录流程，再由项目适配器映射真实语言、框架、目录和部署方式。未知内容明确记录为缺口，不伪造完整理解。

### 6. Skill 之间互相覆盖或无法协作

**问题**：项目工程、前端、后端、测试、文档和部署 Skill 可能各自要求不同流程。规则写死后，容易重复读取、互相冲突或阻止专用 Skill 发挥作用。

**机制**：项目工程 Skill 负责范围、证据、批次、交接和发布边界。框架和工具 Skill 负责具体实现。通过 references 和项目适配器划分职责，不把某个技术栈的细节写成所有 Skill 的硬规则。

### 7. AI 逐点测试和过量防御性测试

**问题**：AI 往往一次只测一个按钮或一条断言。为了显得谨慎，又重复登录、导航和完整流程，测试时间变长，测试数据被反复改变，却没有增加新的结论。

**机制**：到达一个页面后扫描当前主线尚未覆盖的功能、状态、按钮、异常提示、权限差异和数据展示。共享前置只走一次，已有效证据直接复用。读取先于写入，破坏状态的动作最后执行。

### 8. 错误尝试和过期代码残留

**问题**：多次调整后，错误实现、临时路由、旧文案、死注释和备用分支可能继续留在项目中。后续智能体重新扫描时，无法区分当前实现和失败尝试。

**机制**：确认修复后清理被替代代码和无用测试资产。保留必要的失败证据和变更记录，但不让失败实现继续作为可调用路径或当前规则。

### 9. 分支、环境、域名和部署关系混乱

**问题**：开发、测试、预发布和生产分支及服务器经常发生错配。只记录“已部署”无法判断代码版本、服务端口、数据库、域名和客户端配置是否成套，容易出现测试客户端连接生产服务或生产流量仍指向旧服务。

**机制**：部署索引记录分支、提交、制品、服务器、服务、端口、域名、配置来源、数据库、健康检查和回滚路径。部署前核对目标，部署后记录验证证据。

### 10. 发布、部署、验收和授权边界不清

**问题**：代码提交、上传、发布、部署、用户验收和数据调整经常被当成同一件事。已授权某一次操作后，后续操作可能被错误地视为自动授权。

**机制**：把提交、推送、上传、发布、部署、数据库变更和验收分别记录。每次云端操作明确目标环境、版本、授权范围和回滚方式，未授权环境不自动推进。

### 11. 测试数据、生产数据和破坏性操作混淆

**问题**：清理测试数据可能误伤生产数据，保留旧测试记录又会影响身份、资源使用、服务记录和状态判断。执行清理时，还需要区分本地、开发、测试、预发布、生产、下游和同步记录。

**机制**：数据操作记录环境、人员、订单、下游对象、影响范围和恢复方式。初始化只用于空库，已有库走增量处理。删除、清库、清额度和状态回滚都要求明确范围并保留执行证据。

### 12. 构建通过不等于功能完成

**问题**：构建成功、单元测试通过、接口返回成功、浏览器显示正常和真实业务验收证明的是不同层次。把其中一项当成全部完成，会掩盖联调、权限、数据和平台问题。

**机制**：分别记录静态检查、构建、自动化测试、接口联调、浏览器或真机验证、真实下游结果和人工验收。每层只声明它实际证明的范围。

### 13. 重复失败没有止损和升级

**问题**：同一个错误反复重试，智能体继续追加代码或测试，却没有重新检查前提。最终项目产生更多无关改动，真正原因反而更难定位。

**机制**：相同诊断连续失败后停止重试，重新核对前提，邀请独立复查或更换实现路径。记录失败方法和排除依据，防止下一个对话重复同一条错误路线。

### 14. 过度设计和需求边界漂移

**问题**：用户只要求局部业务调整、配置修正或兼容处理时，智能体可能顺手引入额外字段、台账、状态、确认流程或数据迁移，扩大风险并偏离用户真正需求。尤其是没有真实数据来源、读写路径和验收标准的“预留设计”，会让业务模型和后续维护成本持续膨胀。

**机制**：计划中明确最小变更面、明确不新增的字段、对象、状态和流程。业务模型只承载已经确认的规则，新增字段必须说明来源、读写方、生命周期和验收方式。没有实际需求支撑的预留字段和流程不得加入。需要扩大范围时先标记为独立决策，不把推断当成需求。

### 15. 业务约束没有进入工程事实

**问题**：资格、身份、资源配额、状态、幂等、时间窗口、权限、撤销规则和数据归属等约束只存在于聊天或个人记忆中。代码看似完成，实际可能规则不一致、重复产生副作用、跨主体串数据或在错误状态下允许操作。

**机制**：每条重要业务约束都要有稳定 ID，并映射到业务手册、代码入口、配置字段、数据库迁移和测试断言。实现前先核对约束，验收时逐条提供证据。

### 16. 编码规范和质量边界缺失

**问题**：不同智能体使用不同命名、分层、异常、事务、日志、注释和文件规模，项目逐渐变得不可读、难审查、难回滚。机械格式化又可能掩盖真实设计问题。

**机制**：把项目编码规范作为可读取的质量边界，约束结构、依赖、文件和方法规模、迁移、接口和日志。规范检查与业务审查分开，避免把格式通过误报成业务完成。

### 17. DDD 领域模型和模块边界被绕过

**问题**：在 AI 辅助开发时代，生成代码的速度提高后，单体项目的主要结构风险往往不再是多人同时编辑同一文件，而是 AI 不断扩大现有文件的职责。新增实体没有确认领域归属，应用服务直接调用其他模块 Mapper，跨领域逻辑散落在控制器或共享工具中，最终形成隐式耦合和无法维护的数据边界。分布式架构仍有部署、隔离和可靠性价值，但其中一部分协同开发收益在小团队与智能体共同维护单体项目时不再是首要矛盾。

**机制**：使用 DDD 将单体项目划分为有业务含义的限界上下文和模块边界。实现前识别聚合、实体、值对象、领域服务、仓储和应用服务。跨领域只通过公开契约协作，不直接写其他模块数据。新增持久化实体必须有明确归属和依赖方向。

### 18. 设计模式被滥用或重复实现

**问题**：AI 喜欢沿着当前文件继续追加逻辑，直到控制器、服务或组件变成巨型文件。智能体不认识项目既有模式时，还会复制一套逻辑，或者为了“规范”增加无实际价值的工厂、策略、适配器和抽象层，造成调用链变长、职责不清和维护成本上升。

**机制**：把设计模式作为 AI 代码结构的约束工具，而不是装饰性概念。先识别现有模式和真实变化点，再决定复用、扩展或新增抽象，让变化进入策略、工厂、适配器、模板、状态或领域服务等明确位置。模式选择记录解决的变化、替代方案和影响范围，不以模式名称代替业务设计。

## English documentation

This document records the recurring engineering problems behind the Skill. It is a design rationale, not a project-specific business rule and not a replacement for the project handbooks.

### 1. Context compression and conversation migration

**Problem**: Long conversations are compressed. A new conversation or agent may lose changes, branches, environments, verified coverage, and unfinished work.

**Mechanism**: An entry README, stable-ID indexes, current snapshots, evidence directories, and handoff records form a portable project state. Current information is read in a fixed order, while history is loaded by issue instead of relying on a chat summary.

### 2. Conflicts between product, engineering, and user descriptions

**Problem**: Product scenarios, engineering interpretations, user decisions, prototypes, and runtime behavior can disagree.

**Mechanism**: Link decisions, business rules, prototypes, code, configuration, tests, and release records with stable IDs. Record source, status, scope, and open questions. Resolve conflicts against evidence rather than stale conversation text.

### 3. Current and historical rules mixed together

**Problem**: Replaced rules remain in documents, comments, or context and can be reintroduced by a later agent.

**Mechanism**: Keep active rules in an active area and superseded rules in history with effective dates, replacement reasons, and evidence. Load history only for a targeted investigation.

### 4. Missing knowledge-index structure

**Problem**: Information exists without an entry point, stable IDs, module mapping, or evidence chain. New operators depend on broad search or memory.

**Mechanism**: The entry README points to indexes, which point to business handbooks, technical handbooks, deployment records, evidence, and history. Each record identifies its meaning, scope, status, source, and related code or configuration.

### 5. No usable bootstrap for a new project

**Problem**: Rules tied to one project’s package names and modules lose value when a new project is taken over.

**Mechanism**: The Skill provides generic onboarding, architecture discovery, handbook bootstrap, and evidence workflows. A project adapter maps the real stack. Unknowns are recorded as gaps instead of being invented.

### 6. Skills that conflict or fail to cooperate

**Problem**: Project, frontend, backend, testing, documentation, and deployment Skills may impose overlapping workflows.

**Mechanism**: This Skill owns scope, evidence, batches, handoff, and release boundaries. Specialized Skills own concrete implementation and tools. References and adapters keep responsibilities compatible.

### 7. Point-by-point AI testing and defensive over-testing

**Problem**: AI verifies one button or assertion at a time, then repeats login, navigation, and full workflows. Time and test data are consumed without new conclusions.

**Mechanism**: Once a page is reached, scan the current workflow for unverified features, states, buttons, errors, permissions, and data presentation. Reuse valid prerequisites. Read before write, and execute destructive actions last.

### 8. Retained failed attempts and obsolete code

**Problem**: Failed implementations, temporary routes, stale copy, dead comments, and backup paths remain indistinguishable from the current solution.

**Mechanism**: Remove superseded code and unused test assets after confirmation. Preserve failure evidence and change records without leaving the failed implementation as an active path.

### 9. Confused branches, environments, domains, and deployments

**Problem**: Development, test, staging, and production branches or servers are mismatched. “Deployed” does not identify the revision, port, database, domain, or client configuration.

**Mechanism**: The deployment index records branch, commit, artifact, host, service, port, domain, configuration source, database, health check, and rollback path. Verify the target before deployment and record evidence afterward.

### 10. Unclear boundaries between release, deployment, acceptance, and authorization

**Problem**: Commit, push, upload, publication, deployment, acceptance, and data changes are treated as one event. Earlier authorization is incorrectly reused for later actions.

**Mechanism**: Record each event separately with its environment, revision, authorization scope, and rollback path.

### 11. Test, production, and destructive data operations mixed together

**Problem**: Test cleanup can affect production data. Retained test orders can influence login, quota, service records, and state decisions.

**Mechanism**: Record environment, people, orders, downstream objects, impact, and recovery for each data operation. Use incremental changes for existing databases and preserve execution evidence.

### 12. A passing build is not feature acceptance

**Problem**: Build success, unit tests, API responses, browser rendering, downstream results, and business acceptance prove different layers.

**Mechanism**: Report static checks, builds, automation, integration, browser or device verification, downstream facts, and human acceptance separately.

### 13. Repeated failure without stop-loss

**Problem**: The agent retries the same diagnosis and adds unrelated code or tests instead of checking the premise.

**Mechanism**: Stop after repeated failure, recheck assumptions, request independent review or change the implementation path, and record failed approaches.

### 14. Over-design and scope drift

**Problem**: A narrow request becomes extra ledgers, statuses, confirmation flows, or migrations that were never required.

**Mechanism**: State the smallest change surface and explicit exclusions in the plan. Treat scope expansion as a separate decision instead of converting inference into a requirement.

### 16. Business constraints not represented as engineering facts

**Problem**: Qualification, identity, resource limits, state, idempotency, time windows, permissions, data ownership, and revocation rules remain in chat or personal memory. The code may appear complete while applying rules inconsistently, duplicating effects, mixing data, or allowing invalid transitions.

**Mechanism**: Give important business constraints stable IDs and map them to the business handbook, code entry points, configuration fields, database migrations, and test assertions. Verify constraints before implementation and provide evidence for each one during acceptance.

### 15. Minimal business model and anti-overdesign

**Problem**: An agent may add fields, ledgers, statuses, confirmation workflows, or migrations for hypothetical future needs. These additions have no source of truth, real read/write path, or acceptance criterion, but still become part of the contract that later agents must preserve.

**Mechanism**: Add a field or workflow only when a confirmed rule requires it. The plan must state its source of truth, writers, readers, lifecycle, compatibility impact, and acceptance evidence. Do not create speculative schema, state, or audit concepts to make a local change appear more complete.

### 17. Missing coding standards and quality boundaries

**Problem**: Different agents introduce different naming, layering, exception, transaction, logging, comment, and file-size practices. The project becomes difficult to read, review, and roll back. Mechanical formatting can hide design problems.

**Mechanism**: Treat project coding standards as readable quality boundaries for structure, dependencies, file and method size, migrations, APIs, and logs. Keep standards checks separate from business review so a passing format check is not reported as feature acceptance.

### 18. DDD model and module boundaries bypassed

**Problem**: In the AI-assisted development era, faster code generation makes module ownership and business boundaries a primary risk in many monolithic systems. New entities are added without confirming domain ownership. Application services call another module’s mapper directly, while cross-domain logic spreads through controllers and shared utilities. Distributed architecture still has operational value, but its team-collaboration benefit is less decisive when a small team and agents maintain one system.

**Mechanism**: Use DDD to define business-meaningful bounded contexts and module boundaries in a monolith. Identify aggregates, entities, value objects, domain services, repositories, and application services before editing. Cross-domain work uses public contracts, and new persistence has an explicit owner and dependency direction.

### 19. Design patterns misused or reimplemented

**Problem**: AI tends to keep adding requirements to the current file until a controller, service, or component becomes a large mixed-responsibility file. When an agent fails to recognize existing patterns, it also copies logic or adds factories, strategies, adapters, and abstraction layers with no real variation point. Call chains grow while responsibilities become less clear.

**Mechanism**: Treat design patterns as structural constraints for AI-generated code, not decoration. Identify existing patterns and actual variation points before reusing, extending, or introducing an abstraction, so variation enters a strategy, factory, adapter, template, state, or domain service. Record the change being addressed, alternatives considered, and affected scope. A pattern name never substitutes for business design.
