## T11

- 官方来源优先。
- 官方自述仍不能替代独立运行验证。
- 同一问题优先保留一个主来源。
- 其他来源用于不同实现、冲突核对或失败案例。

## T12

- Durability is an integration capability.
- It is not an automatic property of every Agent run.
- Plain in-process runs require the caller to persist run identity/history and external state.

## T13

1. 校验输入格式。
2. 运行测试。
3. 记录失败原因。
4. 发布结果。

## T14

- 候选池可以继续扩大。
- 当新来源不再提供新模式或证据时，停止扩张。
- 停止后转向实践。
- 进入课程前，先写明它填补哪个 Output 缺口。
- 完成后，更新来源卡和实验/应用证据。

## T15

- 代码本体采用 Apache-2.0；仓库所含或关联的专有模型不因此自动适用该许可，使用这些模型前需单独审查 MODEL_LICENSE。
- 房间权限只管理房间访问，不等同于 function tools 的授权；高风险工具还需审批层。

## T16

- Provider breadth reduces adapter friction. Common interfaces do not establish equivalent behavior across every provider.
- Source and CI design show strong production engineering signals. Nothing was executed in this review, so runtime correctness remains unvalidated.
- The framework exposes explicit approval waitpoints. Prompt wording alone does not provide the same human gate.

## 约束与实际读取文件

- 约束：仅读取指定基线技能、该技能为当前任务明确要求的 references，以及指定对抗输入；未读取其他文件或任何结果；仅用 `apply_patch` 写入指定结果文件。
- 实际读取：`<materialized>/hw-semantic-baseline/SKILL.md`
- 实际读取：`<materialized>/hw-semantic-baseline/references/fact-integrity.md`
- 实际读取：`<materialized>/hw-semantic-baseline/references/quality-rubric.md`
- 实际读取：`<materialized>/hw-semantic-adversarial-inputs.md`
