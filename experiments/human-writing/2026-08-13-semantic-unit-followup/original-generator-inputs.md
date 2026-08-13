# Generator inputs

The ten cases use neutral IDs. Source locations, references, condition labels, and expected decisions are intentionally omitted.

## T01

Protected: `GitHub`; `Google Drive`; `ChatGPT Library`; `Google Sheets`; `生产 Skill`

Instruction: 在不增删或改动任何事实的前提下，去除模板化 AI 腔、空泛衔接和冗余强调。改写为每项对应一个事实的条目列表；protected 必须字面保留。不要添加解释，只返回成品。

Input:

在整体信息治理框架下，需要从多个层面进行系统性把握。首先，GitHub 主要用于保存公开、结构化、可版本化的事实和规范。其次，Google Drive 承担私有、受版权保护、大型或二进制原始资产的保存职责。再次，ChatGPT Library 用于保存工作副本和固定快照，但不应被视为唯一事实源。与此同时，Google Sheets 虽然可以作为筛选和运营视图，却不得成为唯一的任务状态或研究证据来源。最后需要强调的是，自动化可以完成发现、去重、校验和候选生成，但不能自动提升证据等级、发布生产 Skill，也不能把局部成功宣称为生产完成。

## T02

Protected: `Awesome List`; `Output`; `来源卡`; `知识图谱`; `实验/应用证据`

Instruction: 在不增删或改动任何事实的前提下，去除模板化 AI 腔、空泛衔接和冗余强调。改写为每项对应一个事实的条目列表；protected 必须字面保留。不要添加解释，只返回成品。

Input:

关于课程、书籍和仓库的使用，可以从以下几个方面形成系统认识。首先，课程、电子书和 Awesome List 只是候选输入，并不意味着已经完成学习。其次，虽然官方来源应被优先考虑，但官方自述依然无法替代独立运行验证。再次，对于同一个问题，应优先保留一个主来源，其他来源则可用于考察不同实现、核对冲突或收集失败案例。此外，在进入课程前，需要先明确它将填补哪个 Output 缺口，并在完成后更新来源卡、知识图谱以及实验/应用证据。总体而言，候选池可以很大，但一旦新来源不再带来新模式或新证据，就应停止扩张并转向实践。

## T03

Protected: `checkpoint`; `agent`; `function tools`; `Apache-2.0`; `LiveKit`; `MODEL_LICENSE`

Instruction: 在不增删或改动任何事实的前提下，去除模板化 AI 腔、空泛衔接和冗余强调。改写为每项对应一个事实的条目列表；protected 必须字面保留。不要添加解释，只返回成品。

Input:

从整体上看，该项目的恢复与停止设计主要针对实时语音会话中的瞬时失败、抢话以及媒体管线进行优化，而不能被理解为面向任意长任务的可持久化 checkpoint。与此同时，需要认识到房间权限并不等同于 agent 工具授权；如果应用暴露高风险 function tools，就还需要增加审批/策略层。此外，虽然代码本体采用 Apache-2.0，但在使用仓库所含或关联的 LiveKit 专有模型时，仍有必要单独审查 MODEL_LICENSE 中关于框架绑定与训练用途的限制。

## T04

Protected: `typed graph execution`; `run identity/history`; `approval/deferred flows`; `Agent`; `provider/native-tool`; `CI`; `runtime_validated`

Instruction: Without adding, removing, or altering facts, remove formulaic AI phrasing, padded transitions, and redundant emphasis. Rewrite as a bullet list with one item per claim, and preserve every protected span verbatim. Return only the finished text.

Input:

When viewed from a holistic perspective, it is worth noting that typed graph execution, explicit run identity/history, structured tool outcomes, approval/deferred flows, usage budgets, and cancellation snapshots collectively make the framework's agent lifecycle unusually explicit and auditable. At the same time, durability should be understood as an integration capability, rather than as an automatic property attached to every Agent run, because plain in-process runs still require callers to persist histories and external state. Moreover, although provider breadth and profile normalization can reduce adapter friction, it would not be appropriate to infer equivalent behavior across every provider/native-tool combination solely from common interfaces. Finally, the repository presents strong production engineering signals in its source and CI design; however, since this review executed nothing, runtime correctness and provider-service behavior remain below runtime_validated.

## T05

Protected: `` `--verify-remote` ``; `` `gh api` ``; `path/tree blob SHA`; `Git blob SHA`; `locator`; `Markdown`; `` `SECURITY.md#security` ``; `` `Not verified` ``; `token`

Instruction: 在不增删或改动任何事实的前提下，去除模板化 AI 腔、空泛衔接和冗余强调。保持技术细节与代码标记；protected 必须字面保留。不要添加解释，只返回成品。

Input:

从远端验证的整体流程来看，`--verify-remote` 会通过已经认证的 `gh api`，以固定方式读取 commit、递归 tree 与 blob。具体而言，它会校验 path/tree blob SHA，下载 blob 后重新计算 Git blob SHA，并进一步在内容中检查 locator。对于分号复合 locator，每个片段都必须匹配；Markdown `# heading` 或 `path.md#heading` 只会匹配 Markdown heading，其中 emoji 和空白可以归一；代码 symbol 按完整标识符匹配，自由文本则按明确的大小写/空白归一短语匹配。也正因如此，`SECURITY.md#security` 不会仅因为正文出现普通 security 一词而通过。如果认证、网络或 GitHub 配额不可用，流程会以 `Not verified` 非零失败，不会静默跳过，也不会输出 token。

## T06

Protected: `Activepieces`; `Trigger.dev`; `Hexabot`; `exactly-once`; `LLM`; `“Workflow”`; `five malformed`; `three multi-root JSON files`; `SSH`; `` `active=true` ``; `Golutra`

Instruction: Without adding, removing, or altering facts, remove formulaic AI phrasing, padded transitions, and redundant emphasis. Preserve the numbered-list form and every protected span verbatim. Return only the finished text.

Input:

The cross-repository findings can be understood across five key dimensions. First and foremost, **durability and side-effect safety are separate properties**: although Activepieces, Trigger.dev and Hexabot persist or reconstruct execution well, none can automatically make every external action exactly-once. A reusable design therefore combines workflow state with action-specific idempotency keys, result recording and explicit compensation. Second, **human-in-the-loop is often weaker than its label**. Activepieces and Trigger.dev provide explicit waitpoints, whereas several other candidates depend on prompt wording, LLM-interpreted free text, a debug pause or a user-operated pause button; these mechanisms should not receive the same human-gate score. Third, **“Workflow” spans at least seven implementation subtypes**. A flat score for a scheduler, prompt protocol, template pack and durable engine hides their contracts, so reports record a subtype without relaxing the shared evidence gate. Fourth, **template collections need collection-level validation plus per-template risk review**. One collection lacked a license; the larger one contained five malformed and three multi-root JSON files plus an unattended privileged SSH update path. Popularity and `active=true` are not safety evidence. Finally, **README claims require fixed-source confirmation**: Golutra has a durable dispatch outbox, but source search did not find the advertised custom workflow import/export implementation, and its month-long autonomous coordinator is explicitly future work.

## T07

Protected: `Global AGENTS`; `45 行`; `UserPromptSubmit`; `` `240000` ``; `4`; `` `adaptive-collaboration` ``; `` `spawn_agent` ``; `2026-08-11`; `57`; `15`; `208`; `100`

Instruction: 在不增删或改动任何事实的前提下，去除模板化 AI 腔。若原文已经自然紧凑，保持原样。protected 必须字面保留。不要添加解释，只返回成品。

Input:

- Global AGENTS 已压缩为 45 行，没有模型名称、角色路由、Hook、并发、等待或长会话流程；
- UserPromptSubmit 路由 Hook 和旧强制委派脚本均不再生效；
- 自动压缩阈值为 `240000`，真实模型上下文窗口没有因此被缩小；
- 最大并发线程数为 4，Agent 角色继续由结构化配置维护；
- `adaptive-collaboration` Skill 通过结构校验，并能被新的 Codex prompt 发现；
- 本地统计脚本在一次 session 扫描中同时聚合 token、等待与真实 `spawn_agent` 参数；
- 2026-08-11 的一次本地短窗口回放包含 57 个去重 session 和 15 次真实 spawn；15 次均使用无历史继承，未出现全历史继承、字段省略、非法值或参数解析失败；
- 同一短窗口仍观察到 208 次等待调用，其中 100 次属于连续等待首轮之后的请求。

## T08

Protected: `Star`; `Awesome List`; `GitHub Stars`; `description`; `README`; `Skill`; `Agent`

Instruction: 在不增删或改动任何事实的前提下，去除模板化 AI 腔。若原文已经自然紧凑，保持原样。protected 必须字面保留。不要添加解释，只返回成品。

Input:

- Star 数只是发现优先级，不是质量证明。
- Awesome List、资源索引和 GitHub Stars 是发现入口，不是其所列内容的直接证据。
- description、搜索摘要和 README 标题不能替代实际阅读。
- 声称研究 Skill、Agent、架构或测试时，必须读取对应文件或源码入口。
- 重试、批次和多次领取是历史事件，不能增加唯一仓库数。

## T09

Protected: `canonical`; `Eval`; `许可证`; `安全边界`; `固定版本`

Instruction: 在不增删或改动任何事实的前提下，去除模板化 AI 腔。若原文已经自然紧凑，保持原样。protected 必须字面保留。不要添加解释，只返回成品。

Input:

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

Protected: `canonical index`; `run report`; `retrospective`; `shard`; `` `owner/name` ``; `repository identity`; `fork`; `archive`; `mirror`; `empty`; `adjacent`; `unclear`; `reconciliation`; `canonical totals`; `deep-analysis queue`; `` `snapshot_id` ``; `` `source_commit` ``; `` `status=ready` ``; `commit`

Instruction: 在不增删或改动任何事实的前提下，去除模板化 AI 腔。若原文已经自然紧凑，保持原样。protected 必须字面保留。不要添加解释，只返回成品。

Input:

1. 读取 topic 配置、canonical index、最近 run report 和最近 retrospective；
2. 选择配置中的下一个确定性 shard；同一 shard 不重复创建新批次；
3. 记录完整 query、页码、每页数量、终止条件、执行时间和访问限制；
4. 规范化 `owner/name`，以不区分大小写的 repository identity 去重；
5. 区分 fork、archive、mirror、empty、adjacent 和 unclear，不因 Star 自动纳入；
6. 写入原始 batch、run report 和 provisional candidate；
7. 只有 reconciliation 完成后才更新 canonical totals 与 deep-analysis queue；
8. 发布不可变 snapshot，字段至少包含 `snapshot_id`、`source_commit`、`status=ready`、候选身份和内容指纹；
9. 生成本批 retrospective，并提交一个原子 commit。
