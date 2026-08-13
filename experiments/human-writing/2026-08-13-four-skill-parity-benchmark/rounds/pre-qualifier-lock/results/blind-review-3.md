# Blind review packet

Judge packet 3; skill identities are withheld.

## Scoring rubric

Score each dimension independently from 1 to 5. Use 2 and 4 for cases between anchors.

- **Fidelity:** 5 = every fact, actor, relation, scope, modality and uncertainty is preserved; 3 = a localized omission/strength change is present but the main conclusion remains usable; 1 = invented facts or a material reversal. Record every factual omission/addition or modality/claim-strength change as `hard_issue`. A localized hard issue caps Fidelity at 3; a material reversal caps it at 1.
- **Instruction/structure:** 5 = all explicit format and scope requirements are met and claims are grouped by coherent semantic unit; 3 = compliant but noticeably fragmented, merged, or structurally awkward; 1 = required format/scope is ignored.
- **Clarity:** 5 = immediately understandable with precise referents and relationships; 3 = understandable after rereading or scanning avoidable density; 1 = ambiguous or internally confusing.
- **Naturalness:** 5 = direct, idiomatic professional prose without staged transitions or mechanical cadence; 3 = noticeable checklist/template rhythm or awkward phrasing; 1 = strongly formulaic or unidiomatic.
- **Restraint:** 5 = removes only reader-visible problems and keeps already-effective wording; 3 = needless splitting, polishing, or normalization without factual damage; 1 = extensive unnecessary rewriting or voice flattening.

The reference is a style and fidelity aid, not the only valid wording. Do not reward literal similarity by itself. A protected-span pass does not prove semantic fidelity.

## C01

Case-specific criterion: Keep the five storage/automation responsibilities distinct and preserve normative modality, especially automatic-only limits.

### Input

在整体信息治理框架下，需要从多个层面进行系统性把握。首先，GitHub 主要用于保存公开、结构化、可版本化的事实和规范。其次，Google Drive 承担私有、受版权保护、大型或二进制原始资产的保存职责。再次，ChatGPT Library 用于保存工作副本和固定快照，但不应被视为唯一事实源。与此同时，Google Sheets 虽然可以作为筛选和运营视图，却不得成为唯一的任务状态或研究证据来源。最后需要强调的是，自动化可以完成发现、去重、校验和候选生成，但不能自动提升证据等级、发布生产 Skill，也不能把局部成功宣称为生产完成。

### Reference

- GitHub 保存公开、结构化、可版本化的事实和规范。
- Google Drive 保存私有、受版权保护、大型或二进制原始资产。
- ChatGPT Library 保存工作副本和固定快照，不作为唯一事实源。
- Google Sheets 可以作为筛选和运营视图，但不得成为唯一任务状态或研究证据来源。
- 自动化可以发现、去重、校验和生成候选；不能自动提升证据等级、发布生产 Skill 或把局部成功宣称为生产完成。

### Candidate A

- GitHub 用于保存公开、结构化、可版本化的事实和规范。
- Google Drive 用于保存私有、受版权保护、大型或二进制原始资产。
- ChatGPT Library 用于保存工作副本和固定快照，但不是唯一事实源。
- Google Sheets 可以作为筛选和运营视图，但不能成为唯一的任务状态或研究证据来源。
- 自动化可以完成发现、去重、校验和候选生成。
- 自动化不能提升证据等级。
- 自动化不能发布生产 Skill。
- 自动化不能把局部成功宣称为生产完成。

### Candidate B

- GitHub 主要用于保存公开、结构化、可版本化的事实和规范。
- Google Drive 用于保存私有、受版权保护、大型或二进制原始资产。
- ChatGPT Library 用于保存工作副本和固定快照，但不应被视为唯一事实源。
- Google Sheets 可以作为筛选和运营视图，但不得成为唯一的任务状态或研究证据来源。
- 自动化可以完成发现、去重、校验和候选生成，但不能自动提升证据等级、发布生产 Skill，或把局部成功宣称为生产完成。

### Candidate C

- GitHub 主要用于保存公开、结构化、可版本化的事实和规范。
- Google Drive 承担私有、受版权保护、大型或二进制原始资产的保存职责。
- ChatGPT Library 用于保存工作副本和固定快照，但不应被视为唯一事实源。
- Google Sheets 可以作为筛选和运营视图，但不得成为唯一的任务状态或研究证据来源。
- 自动化可以完成发现、去重、校验和候选生成，但不能自动提升证据等级、发布生产 Skill，也不能把局部成功宣称为生产完成。

### Candidate D

- GitHub 用于保存公开、结构化、可版本化的事实和规范。
- Google Drive 用于保存私有、受版权保护、大型或二进制原始资产。
- ChatGPT Library 用于保存工作副本和固定快照。
- ChatGPT Library 不应被视为唯一事实源。
- Google Sheets 可以作为筛选和运营视图。
- Google Sheets 不得成为唯一的任务状态或研究证据来源。
- 自动化可以完成发现、去重、校验和候选生成。
- 自动化不能提升证据等级。
- 自动化不能发布生产 Skill。
- 自动化不能把局部成功宣称为生产完成。

## C02

Case-specific criterion: Keep each preference, counter-limit, before/after action, and stopping condition paired with the claim it qualifies.

### Input

关于课程、书籍和仓库的使用，可以从以下几个方面形成系统认识。首先，课程、电子书和 Awesome List 只是候选输入，并不意味着已经完成学习。其次，虽然官方来源应被优先考虑，但官方自述依然无法替代独立运行验证。再次，对于同一个问题，应优先保留一个主来源，其他来源则可用于考察不同实现、核对冲突或收集失败案例。此外，在进入课程前，需要先明确它将填补哪个 Output 缺口，并在完成后更新来源卡、知识图谱以及实验/应用证据。总体而言，候选池可以很大，但一旦新来源不再带来新模式或新证据，就应停止扩张并转向实践。

### Reference

- 课程、电子书和 Awesome List 是候选输入，不代表已经学习。
- 官方来源优先，但官方自述仍不能替代独立运行验证。
- 同一问题优先保留一个主来源；其他来源用于不同实现、冲突核对或失败案例。
- 进入课程前先写明它填补哪个 Output 缺口；完成后更新来源卡、知识图谱和实验/应用证据。
- 候选池可以很大；当新来源不再提供新模式或证据时停止扩张，转向实践。

### Candidate A

- 课程、电子书和 Awesome List 只是候选输入，不代表已经完成学习。
- 官方来源应优先，但官方自述不能替代独立运行验证。
- 对于同一个问题，优先保留一个主来源，其他来源可用于考察不同实现、核对冲突或收集失败案例。
- 进入课程前，先明确它将填补哪个 Output 缺口；完成后，更新来源卡、知识图谱和实验/应用证据。
- 候选池可以很大，但新来源不再带来新模式或新证据时，应停止扩张并转向实践。

### Candidate B

- 课程、电子书和 Awesome List 只是候选输入，并不意味着已经完成学习。
- 官方来源应被优先考虑，但官方自述无法替代独立运行验证。
- 对于同一个问题，应优先保留一个主来源，其他来源可用于考察不同实现、核对冲突或收集失败案例。
- 进入课程前，需要先明确它将填补哪个 Output 缺口，并在完成后更新来源卡、知识图谱以及实验/应用证据。
- 候选池可以很大，但一旦新来源不再带来新模式或新证据，就应停止扩张并转向实践。

### Candidate C

- 课程、电子书和 Awesome List 只是候选输入，不代表已经完成学习。
- 官方来源应被优先考虑。
- 官方自述不能替代独立运行验证。
- 对于同一个问题，应优先保留一个主来源。
- 其他来源可用于考察不同实现、核对冲突或收集失败案例。
- 进入课程前，需要明确它将填补哪个 Output 缺口。
- 完成课程后，需要更新来源卡、知识图谱以及实验/应用证据。
- 候选池可以很大。
- 新来源不再带来新模式或新证据时，应停止扩张并转向实践。

### Candidate D

- 课程、电子书和 Awesome List 是候选输入，不代表已经完成学习。
- 官方来源应优先，但官方自述不能替代独立运行验证。
- 对于同一个问题，应优先保留一个主来源；其他来源用于考察不同实现、核对冲突或收集失败案例。
- 进入课程前，需要明确它将填补哪个 Output 缺口；完成后，需要更新来源卡、知识图谱和实验/应用证据。
- 候选池可以很大；新来源不再带来新模式或新证据时，应停止扩张并转向实践。

## C03

Case-specific criterion: Preserve the difference between design focus, authorization, and licensing; do not turn an interpretation boundary into categorical unusability.

### Input

从整体上看，该项目的恢复与停止设计主要针对实时语音会话中的瞬时失败、抢话以及媒体管线进行优化，而不能被理解为面向任意长任务的可持久化 checkpoint。与此同时，需要认识到房间权限并不等同于 agent 工具授权；如果应用暴露高风险 function tools，就还需要增加审批/策略层。此外，虽然代码本体采用 Apache-2.0，但在使用仓库所含或关联的 LiveKit 专有模型时，仍有必要单独审查 MODEL_LICENSE 中关于框架绑定与训练用途的限制。

### Reference

- 其恢复与停止设计明显优化实时语音会话的瞬时失败、抢话和媒体管线，而不是任意长任务的可持久化 checkpoint。
- 房间权限不是 agent 工具授权；应用若暴露高风险 function tools，需要另加审批/策略层。
- 代码本体为 Apache-2.0，但使用仓库所含/关联的 LiveKit 专有模型时还需单独审查 MODEL_LICENSE 的框架绑定与训练用途限制。

### Candidate A

- 该项目的恢复与停止设计针对实时语音会话中的瞬时失败、抢话以及媒体管线进行优化，不能被理解为面向任意长任务的可持久化 checkpoint。
- 房间权限不等同于 agent 工具授权；如果应用暴露高风险 function tools，还需要增加审批/策略层。
- 代码本体采用 Apache-2.0，但使用仓库所含或关联的 LiveKit 专有模型时，仍需单独审查 MODEL_LICENSE 中关于框架绑定与训练用途的限制。

### Candidate B

- 该项目的恢复与停止设计针对实时语音会话中的瞬时失败、抢话以及媒体管线进行了优化。
- 这种设计不是面向任意长任务的可持久化 checkpoint。
- 房间权限不等同于 agent 工具授权。
- 应用暴露高风险 function tools 时，还需要增加审批/策略层。
- 代码本体采用 Apache-2.0。
- 使用仓库所含或关联的 LiveKit 专有模型时，需要单独审查 MODEL_LICENSE 中关于框架绑定与训练用途的限制。

### Candidate C

- 该项目针对实时语音会话中的瞬时失败、抢话和媒体管线优化恢复与停止设计，不提供面向任意长任务的可持久化 checkpoint。
- 房间权限不等于 agent 工具授权；应用暴露高风险 function tools 时，还需要审批/策略层。
- 代码本体采用 Apache-2.0；使用仓库所含或关联的 LiveKit 专有模型时，仍需单独审查 MODEL_LICENSE 中关于框架绑定和训练用途的限制。

### Candidate D

- 该项目的恢复与停止设计针对实时语音会话中的瞬时失败、抢话和媒体管线进行了优化，不能理解为面向任意长任务的可持久化 checkpoint。
- 房间权限不等于 agent 工具授权；如果应用暴露高风险 function tools，还需要增加审批/策略层。
- 代码本体采用 Apache-2.0，但使用仓库所含或关联的 LiveKit 专有模型时，仍需单独审查 MODEL_LICENSE 中关于框架绑定与训练用途的限制。

## C04

Case-specific criterion: Preserve the four explicit arguments and every evidence ceiling, including that durability is not automatic for every Agent run.

### Input

When viewed from a holistic perspective, it is worth noting that typed graph execution, explicit run identity/history, structured tool outcomes, approval/deferred flows, usage budgets, and cancellation snapshots collectively make the framework's agent lifecycle unusually explicit and auditable. At the same time, durability should be understood as an integration capability, rather than as an automatic property attached to every Agent run, because plain in-process runs still require callers to persist histories and external state. Moreover, although provider breadth and profile normalization can reduce adapter friction, it would not be appropriate to infer equivalent behavior across every provider/native-tool combination solely from common interfaces. Finally, the repository presents strong production engineering signals in its source and CI design; however, since this review executed nothing, runtime correctness and provider-service behavior remain below runtime_validated.

### Reference

- The combination of typed graph execution, explicit run identity/history, structured tool outcomes, approval/deferred flows, usage budgets, and cancellation snapshots makes the framework's agent lifecycle unusually explicit and auditable.
- Durability is an integration capability rather than an automatic property of every Agent run; plain in-process runs still require the caller to persist histories and external state.
- Provider breadth and profile normalization reduce adapter friction, but equivalent behavior across every provider/native-tool combination cannot be inferred solely from common interfaces.
- The repository shows strong production engineering signals from source and CI design, while runtime correctness and provider-service behavior remain below runtime_validated because nothing was executed in this review.

### Candidate A

- typed graph execution, explicit run identity/history, structured tool outcomes, approval/deferred flows, usage budgets, and cancellation snapshots make the framework's agent lifecycle unusually explicit and auditable.
- Durability is an integration capability, not an automatic property of every Agent run.
- Plain in-process runs still require callers to persist histories and external state.
- Provider breadth and profile normalization can reduce adapter friction.
- Common interfaces alone do not establish equivalent behavior across every provider/native-tool combination.
- The repository's source and CI design show strong production engineering signals.
- This review executed nothing, so runtime correctness and provider-service behavior remain below runtime_validated.

### Candidate B

- The framework uses typed graph execution, explicit run identity/history, structured tool outcomes, approval/deferred flows, usage budgets, and cancellation snapshots to make its agent lifecycle explicit and auditable to an uncommon degree.
- Durability depends on integration and does not accompany every Agent run. Callers of plain in-process runs must persist histories and external state.
- Provider breadth and profile normalization can reduce adapter friction. Common interfaces do not establish equivalent behavior across every provider/native-tool combination.
- The repository's source and CI design show strong production engineering. This review executed nothing, so runtime correctness and provider-service behavior remain below runtime_validated.

### Candidate C

- typed graph execution, explicit run identity/history, structured tool outcomes, approval/deferred flows, usage budgets, and cancellation snapshots make the framework's agent lifecycle unusually explicit and auditable.
- Durability is an integration capability, not an automatic property of every Agent run, because callers must still persist histories and external state for plain in-process runs.
- Provider breadth and profile normalization can reduce adapter friction, but common interfaces alone do not establish equivalent behavior across every provider/native-tool combination.
- The repository's source and CI design show strong production engineering, but this review executed nothing, so runtime correctness and provider-service behavior remain below runtime_validated.

### Candidate D

- typed graph execution, explicit run identity/history, structured tool outcomes, approval/deferred flows, usage budgets, and cancellation snapshots collectively make the framework's agent lifecycle unusually explicit and auditable.
- Durability is an integration capability, not an automatic property of every Agent run: plain in-process runs still require callers to persist histories and external state.
- Provider breadth and profile normalization can reduce adapter friction, but common interfaces alone do not establish equivalent behavior across every provider/native-tool combination.
- The repository shows strong production engineering signals in its source and CI design. Because this review executed nothing, runtime correctness and provider-service behavior remain below runtime_validated.

## C05

Case-specific criterion: Preserve the complete verification chain, locator matching modalities, counterexample, and fail-closed behavior.

### Input

从远端验证的整体流程来看，`--verify-remote` 会通过已经认证的 `gh api`，以固定方式读取 commit、递归 tree 与 blob。具体而言，它会校验 path/tree blob SHA，下载 blob 后重新计算 Git blob SHA，并进一步在内容中检查 locator。对于分号复合 locator，每个片段都必须匹配；Markdown `# heading` 或 `path.md#heading` 只会匹配 Markdown heading，其中 emoji 和空白可以归一；代码 symbol 按完整标识符匹配，自由文本则按明确的大小写/空白归一短语匹配。也正因如此，`SECURITY.md#security` 不会仅因为正文出现普通 security 一词而通过。如果认证、网络或 GitHub 配额不可用，流程会以 `Not verified` 非零失败，不会静默跳过，也不会输出 token。

### Reference

`--verify-remote` 通过已认证的 `gh api` 固定读取 commit、递归 tree 和 blob：校验 path/tree blob SHA，下载 blob 后重新计算 Git blob SHA，并在内容中检查 locator。分号复合 locator 的每个片段都必须匹配；Markdown `# heading` 或 `path.md#heading` 只匹配 Markdown heading（emoji/空白可归一），代码 symbol 按完整标识符匹配，自由文本按明确的大小写/空白归一短语匹配。因此 `SECURITY.md#security` 不会因正文中出现普通 security 一词通过。认证、网络或 GitHub 配额不可用时，会以 `Not verified` 非零失败，绝不静默跳过，也不输出 token。

### Candidate A

`--verify-remote` 通过已经认证的 `gh api`，以固定方式读取 commit、递归 tree 与 blob。它校验 path/tree blob SHA，下载 blob 后重新计算 Git blob SHA，并检查内容中的 locator。

分号复合 locator 的每个片段都必须匹配。Markdown `# heading` 或 `path.md#heading` 只匹配 Markdown heading，其中 emoji 和空白可以归一。代码 symbol 按完整标识符匹配，自由文本按明确的大小写/空白归一短语匹配。因此，`SECURITY.md#security` 不会因正文出现普通 security 一词而通过。

认证、网络或 GitHub 配额不可用时，流程以 `Not verified` 非零失败，不会静默跳过或输出 token。

### Candidate B

`--verify-remote` 通过已认证的 `gh api`，以固定方式读取 commit、递归 tree 和 blob。它会校验 path/tree blob SHA，下载 blob 后重新计算 Git blob SHA，并检查内容中的 locator。对于分号复合 locator，每个片段都必须匹配。Markdown `# heading` 或 `path.md#heading` 只匹配 Markdown heading，其中 emoji 和空白可以归一。代码 symbol 按完整标识符匹配，自由文本则按明确的大小写/空白归一短语匹配。因此，`SECURITY.md#security` 不会仅因正文出现普通 security 一词而通过。如果认证、网络或 GitHub 配额不可用，流程会以 `Not verified` 非零失败，不会静默跳过，也不会输出 token。

### Candidate C

`--verify-remote` 会通过已经认证的 `gh api`，以固定方式读取 commit、递归 tree 与 blob。它会校验 path/tree blob SHA，下载 blob 后重新计算 Git blob SHA，并在内容中检查 locator。

对于分号复合 locator，每个片段都必须匹配；Markdown `# heading` 或 `path.md#heading` 只匹配 Markdown heading，其中 emoji 和空白可以归一；代码 symbol 按完整标识符匹配，自由文本按明确的大小写/空白归一短语匹配。因此，`SECURITY.md#security` 不会仅因正文出现普通 security 一词而通过。

如果认证、网络或 GitHub 配额不可用，流程会以 `Not verified` 非零失败，不会静默跳过，也不会输出 token。

### Candidate D

`--verify-remote` 通过已认证的 `gh api` 固定读取 commit、递归 tree 和 blob。它会校验 path/tree blob SHA，下载 blob 后重新计算 Git blob SHA，并检查内容中的 locator。

对于分号复合 locator，每个片段都必须匹配。Markdown `# heading` 或 `path.md#heading` 只匹配 Markdown heading，其中 emoji 和空白可以归一。代码 symbol 按完整标识符匹配，自由文本按明确的大小写/空白归一短语匹配。因此，`SECURITY.md#security` 不会仅因正文出现普通 security 一词而通过。

如果认证、网络或 GitHub 配额不可用，流程会以 `Not verified` 非零失败；它不会静默跳过，也不会输出 token。

## C06

Case-specific criterion: Preserve all five findings, counts, examples, and especially the scope word automatically in the exactly-once limitation.

### Input

The cross-repository findings can be understood across five key dimensions. First and foremost, **durability and side-effect safety are separate properties**: although Activepieces, Trigger.dev and Hexabot persist or reconstruct execution well, none can automatically make every external action exactly-once. A reusable design therefore combines workflow state with action-specific idempotency keys, result recording and explicit compensation. Second, **human-in-the-loop is often weaker than its label**. Activepieces and Trigger.dev provide explicit waitpoints, whereas several other candidates depend on prompt wording, LLM-interpreted free text, a debug pause or a user-operated pause button; these mechanisms should not receive the same human-gate score. Third, **“Workflow” spans at least seven implementation subtypes**. A flat score for a scheduler, prompt protocol, template pack and durable engine hides their contracts, so reports record a subtype without relaxing the shared evidence gate. Fourth, **template collections need collection-level validation plus per-template risk review**. One collection lacked a license; the larger one contained five malformed and three multi-root JSON files plus an unattended privileged SSH update path. Popularity and `active=true` are not safety evidence. Finally, **README claims require fixed-source confirmation**: Golutra has a durable dispatch outbox, but source search did not find the advertised custom workflow import/export implementation, and its month-long autonomous coordinator is explicitly future work.

### Reference

1. **Durability and side-effect safety are separate properties.** Activepieces, Trigger.dev and Hexabot persist or reconstruct execution well, yet none can automatically make every external action exactly-once. The reusable design is to combine workflow state with action-specific idempotency keys, result recording and explicit compensation.
2. **Human-in-the-loop is often weaker than its label.** Activepieces and Trigger.dev expose explicit waitpoints. Several other candidates rely on prompt wording, free-text interpreted by an LLM, a debug pause or a user-operated pause button. Those mechanisms should not receive the same human-gate score.
3. **“Workflow” spans at least seven implementation subtypes.** Comparing a scheduler, prompt protocol, template pack and durable engine on one flat score hides their contracts. Reports therefore record a subtype without relaxing the shared evidence gate.
4. **Template collections need collection-level validation plus per-template risk review.** One collection had no license; the larger collection had five malformed and three multi-root JSON files, and included an unattended privileged SSH update path. Popularity and `active=true` are not safety evidence.
5. **README claims require fixed-source confirmation.** Golutra contains a durable dispatch outbox, but source search did not locate the advertised custom workflow import/export implementation; its month-long autonomous coordinator is explicitly future work.

### Candidate A

1. Activepieces, Trigger.dev and Hexabot persist or reconstruct execution well, but durability and side-effect safety are separate properties. None can automatically make every external action exactly-once. A reusable design combines workflow state with action-specific idempotency keys, result recording and explicit compensation.
2. Human-in-the-loop is often weaker than its label. Activepieces and Trigger.dev provide explicit waitpoints, while several other candidates depend on prompt wording, LLM-interpreted free text, a debug pause or a user-operated pause button. These mechanisms should not receive the same human-gate score.
3. “Workflow” spans at least seven implementation subtypes. A flat score for a scheduler, prompt protocol, template pack and durable engine hides their contracts, so reports record a subtype without relaxing the shared evidence gate.
4. Template collections need collection-level validation and per-template risk review. One collection lacked a license. The larger one contained five malformed and three multi-root JSON files, along with an unattended privileged SSH update path. Popularity and `active=true` are not safety evidence.
5. README claims require fixed-source confirmation. Golutra has a durable dispatch outbox, but source search did not find the advertised custom workflow import/export implementation. Its month-long autonomous coordinator is explicitly future work.

### Candidate B

1. **Durability and side-effect safety are separate properties.** Activepieces, Trigger.dev and Hexabot persist or reconstruct execution well, but none can automatically make every external action exactly-once. A reusable design combines workflow state with action-specific idempotency keys, result recording and explicit compensation.
2. **Human-in-the-loop is often weaker than its label.** Activepieces and Trigger.dev provide explicit waitpoints, whereas several other candidates depend on prompt wording, LLM-interpreted free text, a debug pause or a user-operated pause button. These mechanisms should not receive the same human-gate score.
3. **“Workflow” spans at least seven implementation subtypes.** A flat score for a scheduler, prompt protocol, template pack and durable engine hides their contracts, so reports record a subtype without relaxing the shared evidence gate.
4. **Template collections need collection-level validation plus per-template risk review.** One collection lacked a license; the larger one contained five malformed and three multi-root JSON files plus an unattended privileged SSH update path. Popularity and `active=true` are not safety evidence.
5. **README claims require fixed-source confirmation.** Golutra has a durable dispatch outbox, but source search did not find the advertised custom workflow import/export implementation, and its month-long autonomous coordinator is explicitly future work.

### Candidate C

1. Durability and side-effect safety are separate properties. Activepieces, Trigger.dev and Hexabot persist or reconstruct execution well, but none can automatically make every external action exactly-once. A reusable design combines workflow state with action-specific idempotency keys, result recording and explicit compensation.
2. Human-in-the-loop is often weaker than its label. Activepieces and Trigger.dev provide explicit waitpoints. Several other candidates depend on prompt wording, LLM-interpreted free text, a debug pause or a user-operated pause button; these mechanisms should not receive the same human-gate score.
3. “Workflow” spans at least seven implementation subtypes. A flat score for a scheduler, prompt protocol, template pack and durable engine hides their contracts, so reports record a subtype without relaxing the shared evidence gate.
4. Template collections need collection-level validation and per-template risk review. One collection lacked a license. The larger one contained five malformed and three multi-root JSON files, plus an unattended privileged SSH update path. Popularity and `active=true` are not safety evidence.
5. README claims require fixed-source confirmation. Golutra has a durable dispatch outbox, but source search did not find the advertised custom workflow import/export implementation. Its month-long autonomous coordinator is explicitly future work.

### Candidate D

1. **Durability and side-effect safety are separate properties.** Activepieces, Trigger.dev and Hexabot persist or reconstruct execution well, but none can make every external action exactly-once on its own. A reusable design combines workflow state with action-specific idempotency keys, result recording and explicit compensation.
2. **Human-in-the-loop often falls short of its label.** Activepieces and Trigger.dev provide explicit waitpoints. Several other candidates depend on prompt wording, LLM-interpreted free text, a debug pause or a user-operated pause button; these mechanisms should not receive the same human-gate score.
3. **“Workflow” covers at least seven implementation subtypes.** A flat score for a scheduler, prompt protocol, template pack and durable engine hides their contracts, so reports record a subtype without relaxing the shared evidence gate.
4. **Template collections need collection-level validation and per-template risk review.** One collection lacked a license. The larger collection contained five malformed and three multi-root JSON files plus an unattended privileged SSH update path. Popularity and `active=true` provide no safety evidence.
5. **README claims require fixed-source confirmation.** Golutra has a durable dispatch outbox, but source search did not find the advertised custom workflow import/export implementation. Its month-long autonomous coordinator remains explicit future work.

## N01

Case-specific criterion: The input is already compact; evaluate exact preservation under the explicit conditional no-op instruction.

### Input

- Global AGENTS 已压缩为 45 行，没有模型名称、角色路由、Hook、并发、等待或长会话流程；
- UserPromptSubmit 路由 Hook 和旧强制委派脚本均不再生效；
- 自动压缩阈值为 `240000`，真实模型上下文窗口没有因此被缩小；
- 最大并发线程数为 4，Agent 角色继续由结构化配置维护；
- `adaptive-collaboration` Skill 通过结构校验，并能被新的 Codex prompt 发现；
- 本地统计脚本在一次 session 扫描中同时聚合 token、等待与真实 `spawn_agent` 参数；
- 2026-08-11 的一次本地短窗口回放包含 57 个去重 session 和 15 次真实 spawn；15 次均使用无历史继承，未出现全历史继承、字段省略、非法值或参数解析失败；
- 同一短窗口仍观察到 208 次等待调用，其中 100 次属于连续等待首轮之后的请求。

### Reference

- Global AGENTS 已压缩为 45 行，没有模型名称、角色路由、Hook、并发、等待或长会话流程；
- UserPromptSubmit 路由 Hook 和旧强制委派脚本均不再生效；
- 自动压缩阈值为 `240000`，真实模型上下文窗口没有因此被缩小；
- 最大并发线程数为 4，Agent 角色继续由结构化配置维护；
- `adaptive-collaboration` Skill 通过结构校验，并能被新的 Codex prompt 发现；
- 本地统计脚本在一次 session 扫描中同时聚合 token、等待与真实 `spawn_agent` 参数；
- 2026-08-11 的一次本地短窗口回放包含 57 个去重 session 和 15 次真实 spawn；15 次均使用无历史继承，未出现全历史继承、字段省略、非法值或参数解析失败；
- 同一短窗口仍观察到 208 次等待调用，其中 100 次属于连续等待首轮之后的请求。

### Candidate A

- Global AGENTS 已压缩为 45 行，没有模型名称、角色路由、Hook、并发、等待或长会话流程；
- UserPromptSubmit 路由 Hook 和旧强制委派脚本均不再生效；
- 自动压缩阈值为 `240000`，真实模型上下文窗口没有因此被缩小；
- 最大并发线程数为 4，Agent 角色继续由结构化配置维护；
- `adaptive-collaboration` Skill 通过结构校验，并能被新的 Codex prompt 发现；
- 本地统计脚本在一次 session 扫描中同时聚合 token、等待与真实 `spawn_agent` 参数；
- 2026-08-11 的一次本地短窗口回放包含 57 个去重 session 和 15 次真实 spawn；15 次均使用无历史继承，未出现全历史继承、字段省略、非法值或参数解析失败；
- 同一短窗口仍观察到 208 次等待调用，其中 100 次属于连续等待首轮之后的请求。

### Candidate B

- Global AGENTS 已压缩为 45 行，没有模型名称、角色路由、Hook、并发、等待或长会话流程；
- UserPromptSubmit 路由 Hook 和旧强制委派脚本均不再生效；
- 自动压缩阈值为 `240000`，真实模型上下文窗口没有因此被缩小；
- 最大并发线程数为 4，Agent 角色继续由结构化配置维护；
- `adaptive-collaboration` Skill 通过结构校验，并能被新的 Codex prompt 发现；
- 本地统计脚本在一次 session 扫描中同时聚合 token、等待与真实 `spawn_agent` 参数；
- 2026-08-11 的一次本地短窗口回放包含 57 个去重 session 和 15 次真实 spawn；15 次均使用无历史继承，未出现全历史继承、字段省略、非法值或参数解析失败；
- 同一短窗口仍观察到 208 次等待调用，其中 100 次属于连续等待首轮之后的请求。

### Candidate C

- Global AGENTS 已压缩为 45 行，没有模型名称、角色路由、Hook、并发、等待或长会话流程；
- UserPromptSubmit 路由 Hook 和旧强制委派脚本均不再生效；
- 自动压缩阈值为 `240000`，真实模型上下文窗口没有因此被缩小；
- 最大并发线程数为 4，Agent 角色继续由结构化配置维护；
- `adaptive-collaboration` Skill 通过结构校验，并能被新的 Codex prompt 发现；
- 本地统计脚本在一次 session 扫描中同时聚合 token、等待与真实 `spawn_agent` 参数；
- 2026-08-11 的一次本地短窗口回放包含 57 个去重 session 和 15 次真实 spawn；15 次均使用无历史继承，未出现全历史继承、字段省略、非法值或参数解析失败；
- 同一短窗口仍观察到 208 次等待调用，其中 100 次属于连续等待首轮之后的请求。

### Candidate D

- Global AGENTS 已压缩为 45 行，没有模型名称、角色路由、Hook、并发、等待或长会话流程；
- UserPromptSubmit 路由 Hook 和旧强制委派脚本均不再生效；
- 自动压缩阈值为 `240000`，真实模型上下文窗口没有因此被缩小；
- 最大并发线程数为 4，Agent 角色继续由结构化配置维护；
- `adaptive-collaboration` Skill 通过结构校验，并能被新的 Codex prompt 发现；
- 本地统计脚本在一次 session 扫描中同时聚合 token、等待与真实 `spawn_agent` 参数；
- 2026-08-11 的一次本地短窗口回放包含 57 个去重 session 和 15 次真实 spawn；15 次均使用无历史继承，未出现全历史继承、字段省略、非法值或参数解析失败；
- 同一短窗口仍观察到 208 次等待调用，其中 100 次属于连续等待首轮之后的请求。

## N02

Case-specific criterion: The input is already compact; evaluate exact preservation under the explicit conditional no-op instruction.

### Input

- Star 数只是发现优先级，不是质量证明。
- Awesome List、资源索引和 GitHub Stars 是发现入口，不是其所列内容的直接证据。
- description、搜索摘要和 README 标题不能替代实际阅读。
- 声称研究 Skill、Agent、架构或测试时，必须读取对应文件或源码入口。
- 重试、批次和多次领取是历史事件，不能增加唯一仓库数。

### Reference

- Star 数只是发现优先级，不是质量证明。
- Awesome List、资源索引和 GitHub Stars 是发现入口，不是其所列内容的直接证据。
- description、搜索摘要和 README 标题不能替代实际阅读。
- 声称研究 Skill、Agent、架构或测试时，必须读取对应文件或源码入口。
- 重试、批次和多次领取是历史事件，不能增加唯一仓库数。

### Candidate A

- Star 数只是发现优先级，不是质量证明。
- Awesome List、资源索引和 GitHub Stars 是发现入口，不是其所列内容的直接证据。
- description、搜索摘要和 README 标题不能替代实际阅读。
- 声称研究 Skill、Agent、架构或测试时，必须读取对应文件或源码入口。
- 重试、批次和多次领取是历史事件，不能增加唯一仓库数。

### Candidate B

- Star 数只是发现优先级，不是质量证明。
- Awesome List、资源索引和 GitHub Stars 是发现入口，不是其所列内容的直接证据。
- description、搜索摘要和 README 标题不能替代实际阅读。
- 声称研究 Skill、Agent、架构或测试时，必须读取对应文件或源码入口。
- 重试、批次和多次领取是历史事件，不能增加唯一仓库数。

### Candidate C

- Star 数只是发现优先级，不是质量证明。
- Awesome List、资源索引和 GitHub Stars 是发现入口，不是其所列内容的直接证据。
- description、搜索摘要和 README 标题不能替代实际阅读。
- 声称研究 Skill、Agent、架构或测试时，必须读取对应文件或源码入口。
- 重试、批次和多次领取是历史事件，不能增加唯一仓库数。

### Candidate D

- Star 数只是发现优先级，不是质量证明。
- Awesome List、资源索引和 GitHub Stars 是发现入口，不是其所列内容的直接证据。
- description、搜索摘要和 README 标题不能替代实际阅读。
- 声称研究 Skill、Agent、架构或测试时，必须读取对应文件或源码入口。
- 重试、批次和多次领取是历史事件，不能增加唯一仓库数。

## N03

Case-specific criterion: The input is already compact; evaluate exact preservation under the explicit conditional no-op instruction.

### Input

- 是否为官方或 canonical 来源；
- 是否与当前问题匹配；
- 是否有真实实现或完整内容；
- 是否有测试、Eval、示例或练习；
- 最近维护状态和归档状态；
- 许可证、版权和使用边界；
- 已知限制、安全边界和失败案例；
- 是否提供其他主来源没有的新证据；
- 是否可以固定版本并复核。

### Reference

- 是否为官方或 canonical 来源；
- 是否与当前问题匹配；
- 是否有真实实现或完整内容；
- 是否有测试、Eval、示例或练习；
- 最近维护状态和归档状态；
- 许可证、版权和使用边界；
- 已知限制、安全边界和失败案例；
- 是否提供其他主来源没有的新证据；
- 是否可以固定版本并复核。

### Candidate A

- 是否为官方或 canonical 来源；
- 是否与当前问题匹配；
- 是否有真实实现或完整内容；
- 是否有测试、Eval、示例或练习；
- 最近维护状态和归档状态；
- 许可证、版权和使用边界；
- 已知限制、安全边界和失败案例；
- 是否提供其他主来源没有的新证据；
- 是否可以固定版本并复核。

### Candidate B

- 是否为官方或 canonical 来源；
- 是否与当前问题匹配；
- 是否有真实实现或完整内容；
- 是否有测试、Eval、示例或练习；
- 最近维护状态和归档状态；
- 许可证、版权和使用边界；
- 已知限制、安全边界和失败案例；
- 是否提供其他主来源没有的新证据；
- 是否可以固定版本并复核。

### Candidate C

- 是否为官方或 canonical 来源；
- 是否与当前问题匹配；
- 是否有真实实现或完整内容；
- 是否有测试、Eval、示例或练习；
- 最近维护状态和归档状态；
- 许可证、版权和使用边界；
- 已知限制、安全边界和失败案例；
- 是否提供其他主来源没有的新证据；
- 是否可以固定版本并复核。

### Candidate D

- 是否为官方或 canonical 来源；
- 是否与当前问题匹配；
- 是否有真实实现或完整内容；
- 是否有测试、Eval、示例或练习；
- 最近维护状态和归档状态；
- 许可证、版权和使用边界；
- 已知限制、安全边界和失败案例；
- 是否提供其他主来源没有的新证据；
- 是否可以固定版本并复核。

## N04

Case-specific criterion: The input is already compact; evaluate exact preservation under the explicit conditional no-op instruction.

### Input

1. 读取 topic 配置、canonical index、最近 run report 和最近 retrospective；
2. 选择配置中的下一个确定性 shard；同一 shard 不重复创建新批次；
3. 记录完整 query、页码、每页数量、终止条件、执行时间和访问限制；
4. 规范化 `owner/name`，以不区分大小写的 repository identity 去重；
5. 区分 fork、archive、mirror、empty、adjacent 和 unclear，不因 Star 自动纳入；
6. 写入原始 batch、run report 和 provisional candidate；
7. 只有 reconciliation 完成后才更新 canonical totals 与 deep-analysis queue；
8. 发布不可变 snapshot，字段至少包含 `snapshot_id`、`source_commit`、`status=ready`、候选身份和内容指纹；
9. 生成本批 retrospective，并提交一个原子 commit。

### Reference

1. 读取 topic 配置、canonical index、最近 run report 和最近 retrospective；
2. 选择配置中的下一个确定性 shard；同一 shard 不重复创建新批次；
3. 记录完整 query、页码、每页数量、终止条件、执行时间和访问限制；
4. 规范化 `owner/name`，以不区分大小写的 repository identity 去重；
5. 区分 fork、archive、mirror、empty、adjacent 和 unclear，不因 Star 自动纳入；
6. 写入原始 batch、run report 和 provisional candidate；
7. 只有 reconciliation 完成后才更新 canonical totals 与 deep-analysis queue；
8. 发布不可变 snapshot，字段至少包含 `snapshot_id`、`source_commit`、`status=ready`、候选身份和内容指纹；
9. 生成本批 retrospective，并提交一个原子 commit。

### Candidate A

1. 读取 topic 配置、canonical index、最近 run report 和最近 retrospective；
2. 选择配置中的下一个确定性 shard；同一 shard 不重复创建新批次；
3. 记录完整 query、页码、每页数量、终止条件、执行时间和访问限制；
4. 规范化 `owner/name`，以不区分大小写的 repository identity 去重；
5. 区分 fork、archive、mirror、empty、adjacent 和 unclear，不因 Star 自动纳入；
6. 写入原始 batch、run report 和 provisional candidate；
7. 只有 reconciliation 完成后才更新 canonical totals 与 deep-analysis queue；
8. 发布不可变 snapshot，字段至少包含 `snapshot_id`、`source_commit`、`status=ready`、候选身份和内容指纹；
9. 生成本批 retrospective，并提交一个原子 commit。

### Candidate B

1. 读取 topic 配置、canonical index、最近 run report 和最近 retrospective；
2. 选择配置中的下一个确定性 shard；同一 shard 不重复创建新批次；
3. 记录完整 query、页码、每页数量、终止条件、执行时间和访问限制；
4. 规范化 `owner/name`，以不区分大小写的 repository identity 去重；
5. 区分 fork、archive、mirror、empty、adjacent 和 unclear，不因 Star 自动纳入；
6. 写入原始 batch、run report 和 provisional candidate；
7. 只有 reconciliation 完成后才更新 canonical totals 与 deep-analysis queue；
8. 发布不可变 snapshot，字段至少包含 `snapshot_id`、`source_commit`、`status=ready`、候选身份和内容指纹；
9. 生成本批 retrospective，并提交一个原子 commit。

### Candidate C

1. 读取 topic 配置、canonical index、最近 run report 和最近 retrospective；
2. 选择配置中的下一个确定性 shard；同一 shard 不重复创建新批次；
3. 记录完整 query、页码、每页数量、终止条件、执行时间和访问限制；
4. 规范化 `owner/name`，以不区分大小写的 repository identity 去重；
5. 区分 fork、archive、mirror、empty、adjacent 和 unclear，不因 Star 自动纳入；
6. 写入原始 batch、run report 和 provisional candidate；
7. 只有 reconciliation 完成后才更新 canonical totals 与 deep-analysis queue；
8. 发布不可变 snapshot，字段至少包含 `snapshot_id`、`source_commit`、`status=ready`、候选身份和内容指纹；
9. 生成本批 retrospective，并提交一个原子 commit。

### Candidate D

1. 读取 topic 配置、canonical index、最近 run report 和最近 retrospective；
2. 选择配置中的下一个确定性 shard；同一 shard 不重复创建新批次；
3. 记录完整 query、页码、每页数量、终止条件、执行时间和访问限制；
4. 规范化 `owner/name`，以不区分大小写的 repository identity 去重；
5. 区分 fork、archive、mirror、empty、adjacent 和 unclear，不因 Star 自动纳入；
6. 写入原始 batch、run report 和 provisional candidate；
7. 只有 reconciliation 完成后才更新 canonical totals 与 deep-analysis queue；
8. 发布不可变 snapshot，字段至少包含 `snapshot_id`、`source_commit`、`status=ready`、候选身份和内容指纹；
9. 生成本批 retrospective，并提交一个原子 commit。
