# Blind A/B review

Review six writing transformations. The labels are randomized independently by case. Do not infer or identify their source.

## Rubric

Score each candidate 1–5 on five dimensions:

- **Fidelity:** 5 preserves every fact, relation, qualifier, protected span, and claim strength; 3 has a small omission or shift that does not reverse the conclusion; 1 invents, removes, or materially changes a claim.
- **Instruction/structure:** 5 fully obeys the requested form and groups each main assertion with conditions, limits, exceptions, reasons, or consequences needed to interpret it while keeping independent actions separate; 3 is usable but over-splits or over-merges; 1 violates the requested form or changes the argument through structure.
- **Clarity:** 5 makes relationships immediately clear; 3 requires the reader to reconstruct one relationship; 1 is confusing or contradictory.
- **Naturalness:** 5 reads like concise human editorial prose; 3 is mechanical or awkward but usable; 1 is strongly templated or unnatural.
- **Restraint:** 5 makes only changes with concrete reader benefit; 3 includes noticeable formatting or wording churn; 1 substantially rewrites effective material without benefit.

A **hard issue** is any invented or removed fact, changed modality/actor/status, missing protected span, or explicit instruction violation. A hard issue caps Fidelity and Instruction/structure at 2. For each case, score A and B, mark hard issue true/false with evidence, and give `Ranking: A > B`, `Ranking: B > A`, or `Ranking: A = B`. Do not use differences not visible in this packet.

## T11

Instruction: 不增删或改动任何事实，改成每项对应一个事实的条目列表。只返回成品。

Source: 官方来源优先。官方自述仍不能替代独立运行验证。同一问题优先保留一个主来源。其他来源用于不同实现、冲突核对或失败案例。

### A

- 官方来源优先，但官方自述不能替代独立运行验证。
- 同一问题优先保留一个主来源；其他来源用于不同实现、冲突核对或失败案例。

### B

- 官方来源优先。
- 官方自述仍不能替代独立运行验证。
- 同一问题优先保留一个主来源。
- 其他来源用于不同实现、冲突核对或失败案例。

## T12

Protected: `Agent`; `run identity/history`

Instruction: Without adding, removing, or altering facts, rewrite as a bullet list with one item per claim. Preserve every protected span verbatim. Return only the finished text.

Source: Durability is an integration capability. It is not an automatic property of every Agent run. Plain in-process runs require the caller to persist run identity/history and external state.

### A

- Durability is an integration capability.
- Durability is not an automatic property of every Agent run.
- Plain in-process runs require the caller to persist run identity/history and external state.

### B

- Durability is an integration capability, not an automatic property of every Agent run; plain in-process runs require the caller to persist run identity/history and external state.

## T13

Instruction: 去掉模板化表达，保持编号列表和全部事实。只返回成品。

Source: 1. 校验输入格式；2. 运行测试；3. 记录失败原因；4. 发布结果。

### A

1. 校验输入格式；2. 运行测试；3. 记录失败原因；4. 发布结果。

### B

1. 校验输入格式；
2. 运行测试；
3. 记录失败原因；
4. 发布结果。

## T14

Instruction: 不增删事实，改成条目列表；每项表达一个完整决策。只返回成品。

Source: 候选池可以继续扩大。当新来源不再提供新模式或证据时停止扩张。停止后转向实践。进入课程前先写明它填补哪个 Output 缺口。完成后更新来源卡和实验/应用证据。

### A

- 候选池可以继续扩大。
- 当新来源不再提供新模式或证据时，停止扩张并转向实践。
- 进入课程前，先写明它填补哪个 Output 缺口。
- 完成后，更新来源卡和实验/应用证据。

### B

- 候选池可以继续扩大；当新来源不再提供新模式或证据时，停止扩张，转向实践。
- 进入课程前，先写明它填补哪个 Output 缺口；完成后，更新来源卡和实验/应用证据。

## T15

Protected: `Apache-2.0`; `MODEL_LICENSE`; `function tools`

Instruction: 在不改变事实的前提下，压成两个条目。protected 必须字面保留。只返回成品。

Source: 代码本体采用 Apache-2.0。仓库所含或关联的专有模型不因此自动适用该许可。使用这些模型前需单独审查 MODEL_LICENSE。房间权限只管理房间访问。它不等同于 function tools 的授权。高风险工具还需审批层。

### A

- 代码本体采用 Apache-2.0，但仓库所含或关联的专有模型不因此自动适用该许可；使用这些模型前，需单独审查 MODEL_LICENSE。
- 房间权限只管理房间访问，不等同于 function tools 的授权；高风险工具还需审批层。

### B

- 代码本体采用 Apache-2.0；仓库所含或关联的专有模型不因此自动适用该许可，使用这些模型前需单独审查 MODEL_LICENSE。
- 房间权限只管理房间访问，不等同于 function tools 的授权；高风险工具还需审批层。

## T16

Instruction: Without changing facts, rewrite as exactly three bullets. Return only the finished text.

Source: Provider breadth reduces adapter friction. Common interfaces do not establish equivalent behavior across every provider. Source and CI design show strong production engineering signals. Nothing was executed in this review, so runtime correctness remains unvalidated. The framework exposes explicit approval waitpoints. Prompt wording alone does not provide the same human gate.

### A

- Provider breadth reduces adapter friction, but common interfaces do not establish equivalent behavior across every provider.
- Source and CI design show strong production engineering signals. Nothing was executed in this review, so runtime correctness remains unvalidated.
- The framework exposes explicit approval waitpoints. Prompt wording alone does not provide the same human gate.

### B

- Provider breadth reduces adapter friction, but common interfaces do not establish equivalent behavior across every provider.
- Source and CI design show strong production engineering signals; because nothing was executed in this review, runtime correctness remains unvalidated.
- The framework exposes explicit approval waitpoints; prompt wording alone does not provide the same human gate.
