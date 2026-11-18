# 批量测试与覆盖复用

这是本 Skill 的核心测试要求：围绕当前主线，以页面/状态为批次覆盖尚未测过的功能，复用前置过程，不能为了同页两个按钮重复完整登录导航流程。

## 为什么采用批量思维

Codex 在不确定覆盖范围时，容易采用过量的防御性测试：反复登录、重复打开同一页面、把已经有证据的流程重新走一遍，最后消耗大量时间，却没有增加新的验证结论。批量测试把目标从“尽可能多点击”改成“用最少的路径证明当前任务需要证明的断言”。

先列出本次任务的功能、状态和风险，再按页面、身份、数据、平台和环境分组。一次到达页面后，合并检查该主线中尚未覆盖的相关动作；已有有效证据的登录、导航和夹具直接复用。无副作用读取先做，写操作随后做，会改变前置条件的取消、删除和清理最后做。只有改动影响了断言，或者证据因版本、角色、环境或状态变化而失效时，才安排针对性复测。

## Batch testing rationale

Codex can react to uncertainty with excessive defensive testing: repeated logins, repeated navigation, and full reruns of flows that already have evidence. This consumes time without producing a new conclusion. Batch testing changes the objective from clicking as much as possible to proving the claims required by the current task with the fewest representative paths.

List the features, states, and risks first, then group them by page, identity, data, platform, and environment. After reaching a page once, cover the related unverified actions on that workflow together and reuse valid login, navigation, and fixture evidence. Run read-only checks before writes, and leave cancellation, deletion, and cleanup until the end because they change the preconditions. Schedule a targeted retest only when a change affects an assertion or when evidence is invalidated by a version, role, environment, or state change.

## 计划与台账

先列任务内的功能/断言，而非逐按钮行程。台账字段：feature_id、page_or_step、case、身份/数据/环境、代码与配置版本、状态（untested/pass/fail/blocked）、证据、retest_reason。没有证据的口头“测过”不自动算通过。

到达页面后，查看本次主线范围内未覆盖的功能及关键状态；同页无关功能不扩展为全站测试。先做共享状态下无副作用的断言，再做写操作，最后是退出/删除等破坏前置条件的操作。相互独立的读检查可并行；同一用户、订单、库存或浏览器状态的写操作按依赖顺序执行，不能为了批量引入竞争。

例如同页“查看详情”和“导出”未测：一次登录到页，先核对列表和详情，返回当前页再导出。列表已测且版本/角色/状态相同则复用；不要又从登录开始。后端多个接口共享夹具也同理。

## 何时需要复测

不要“每到一页全部重测”，也不要“测过一次永久免测”。覆盖标识必须包含角色/人员、数据状态、平台、环境和相关版本。变更影响依赖、上次证据失效、状态被测试改变，或存在跨环境差异时，重测受影响断言并记录原因。正常导航前置行为可以重复，但不必重复宣称新的覆盖或重新完整验收。

优先一条代表性业务链，结合风险补充失败、边界、幂等、权限、身份切换、并发和上下游一致性。不是所有任务都要跑全矩阵；纯文案等低影响变更采用足够的定向验证。已有通用测试/平台差异证据可复用，不重复验通用框架功能。

## 实测与交接

调用适用测试 Skill 执行工具操作，并维护上述台账。测试计划、静态审查、构建、mock、接口联调、浏览器/真机检查分别报告；没有执行不写 pass。

长任务中把台账存到本任务现有证据目录，恢复时只补未测、失败修复后或失效项。报告覆盖/未覆盖、原因及证据。测试数据只清理本任务创建且已授权清理的数据；保留有价值的回归用例。
