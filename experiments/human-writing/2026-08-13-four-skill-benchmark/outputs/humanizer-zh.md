## T01

- GitHub 主要用于保存公开、结构化、可版本化的事实和规范。
- Google Drive 负责保存私有、受版权保护、大型或二进制原始资产。
- ChatGPT Library 用于保存工作副本和固定快照，但不应被视为唯一事实源。
- Google Sheets 可以作为筛选和运营视图，但不得成为唯一的任务状态或研究证据来源。
- 自动化可以完成发现、去重、校验和候选生成，但不能自动提升证据等级、发布生产 Skill，也不能把局部成功宣称为生产完成。

## T02

- 课程、电子书和 Awesome List 只是候选输入，并不意味着已经完成学习。
- 官方来源应被优先考虑，但官方自述无法替代独立运行验证。
- 对于同一个问题，应优先保留一个主来源，其他来源可用于考察不同实现、核对冲突或收集失败案例。
- 进入课程前，需要先明确它将填补哪个 Output 缺口；完成后更新来源卡、知识图谱以及实验/应用证据。
- 候选池可以很大，但新来源不再带来新模式或新证据时，就应停止扩张并转向实践。

## T03

- 该项目的恢复与停止设计主要针对实时语音会话中的瞬时失败、抢话和媒体管线进行了优化，不能理解为面向任意长任务的可持久化 checkpoint。
- 房间权限不等于 agent 工具授权；如果应用暴露高风险 function tools，还需要增加审批/策略层。
- 代码本体采用 Apache-2.0，但使用仓库所含或关联的 LiveKit 专有模型时，仍需单独审查 MODEL_LICENSE 中关于框架绑定与训练用途的限制。

## T04

- typed graph execution, explicit run identity/history, structured tool outcomes, approval/deferred flows, usage budgets, and cancellation snapshots make the framework's agent lifecycle unusually explicit and auditable.
- Durability is an integration capability, not an automatic property of every Agent run: plain in-process runs still require callers to persist histories and external state.
- Provider breadth and profile normalization can reduce adapter friction, but common interfaces alone do not establish equivalent behavior across every provider/native-tool combination.
- The repository's source and CI design show strong production engineering signals. Since this review executed nothing, runtime correctness and provider-service behavior remain below runtime_validated.

## T05

`--verify-remote` 通过已认证的 `gh api`，以固定方式读取 commit、递归 tree 与 blob。它校验 path/tree blob SHA，下载 blob 后重新计算 Git blob SHA，再检查内容中的 locator。

分号复合 locator 的每个片段都必须匹配。Markdown `# heading` 或 `path.md#heading` 只匹配 Markdown heading，其中 emoji 和空白可以归一；代码 symbol 按完整标识符匹配，自由文本则按明确的大小写/空白归一短语匹配。因此，`SECURITY.md#security` 不会仅因正文出现普通 security 一词而通过。

如果认证、网络或 GitHub 配额不可用，流程会以 `Not verified` 非零失败，不会静默跳过，也不会输出 token。

## T06

1. Activepieces、Trigger.dev and Hexabot persist or reconstruct execution well, but durability and side-effect safety are separate properties: none can automatically make every external action exactly-once. A reusable design combines workflow state with action-specific idempotency keys, result recording and explicit compensation.
2. Human-in-the-loop implementations are not equivalent. Activepieces and Trigger.dev provide explicit waitpoints, while several other candidates rely on prompt wording, LLM-interpreted free text, a debug pause or a user-operated pause button. These mechanisms should not receive the same human-gate score.
3. “Workflow” spans at least seven implementation subtypes. A flat score for a scheduler, prompt protocol, template pack and durable engine hides their contracts, so reports record a subtype without relaxing the shared evidence gate.
4. Template collections need collection-level validation and per-template risk review. One collection lacked a license; the larger one contained five malformed and three multi-root JSON files, plus an unattended privileged SSH update path. Popularity and `active=true` are not safety evidence.
5. README claims require fixed-source confirmation. Golutra has a durable dispatch outbox, but source search did not find the advertised custom workflow import/export implementation, and its month-long autonomous coordinator is explicitly future work.

## T07

- Global AGENTS 已压缩为 45 行，没有模型名称、角色路由、Hook、并发、等待或长会话流程；
- UserPromptSubmit 路由 Hook 和旧强制委派脚本均不再生效；
- 自动压缩阈值为 `240000`，真实模型上下文窗口没有因此被缩小；
- 最大并发线程数为 4，Agent 角色继续由结构化配置维护；
- `adaptive-collaboration` Skill 通过结构校验，并能被新的 Codex prompt 发现；
- 本地统计脚本在一次 session 扫描中同时聚合 token、等待与真实 `spawn_agent` 参数；
- 2026-08-11 的一次本地短窗口回放包含 57 个去重 session 和 15 次真实 spawn；15 次均使用无历史继承，未出现全历史继承、字段省略、非法值或参数解析失败；
- 同一短窗口仍观察到 208 次等待调用，其中 100 次属于连续等待首轮之后的请求。

## T08

- Star 数只是发现优先级，不是质量证明。
- Awesome List、资源索引和 GitHub Stars 是发现入口，不是其所列内容的直接证据。
- description、搜索摘要和 README 标题不能替代实际阅读。
- 声称研究 Skill、Agent、架构或测试时，必须读取对应文件或源码入口。
- 重试、批次和多次领取是历史事件，不能增加唯一仓库数。

## T09

- 是否为官方或 canonical 来源；
- 是否与当前问题匹配；
- 是否有真实实现或完整内容；
- 是否有测试、Eval、示例或练习；
- 最近维护状态和归档状态；
- 许可证、版权和使用边界；
- 已知限制、安全边界和失败案例；
- 是否提供其他主来源没有的新证据；
- 是否可以固定版本并复核。

## T10

1. 读取 topic 配置、canonical index、最近 run report 和最近 retrospective；
2. 选择配置中的下一个确定性 shard；同一 shard 不重复创建新批次；
3. 记录完整 query、页码、每页数量、终止条件、执行时间和访问限制；
4. 规范化 `owner/name`，以不区分大小写的 repository identity 去重；
5. 区分 fork、archive、mirror、empty、adjacent 和 unclear，不因 Star 自动纳入；
6. 写入原始 batch、run report 和 provisional candidate；
7. 只有 reconciliation 完成后才更新 canonical totals 与 deep-analysis queue；
8. 发布不可变 snapshot，字段至少包含 `snapshot_id`、`source_commit`、`status=ready`、候选身份和内容指纹；
9. 生成本批 retrospective，并提交一个原子 commit。

## Run metadata

- 完整任务约束：正式独立生成。只允许读取两个位置：materialized skill humanizer-zh/（先完整读 SKILL.md 和明确引用）和 generator-inputs.md。禁止读取 ai-handbook 该实验的 cases、outputs、results、README 或其他目录。按 T01–T10 各自 Instruction/Input 生成。用 apply_patch 覆盖 outputs/humanizer-zh.md，标题 `## T01`…`## T10`，末尾 Run metadata 写本条完整任务约束和实际读取文件。
- 实际读取文件：
  - materialized skill humanizer-zh/SKILL.md
  - generator-inputs.md
