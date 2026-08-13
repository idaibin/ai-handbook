## T11

- 官方来源优先，但官方自述仍不能替代独立运行验证。
- 同一问题优先保留一个主来源，其他来源用于不同实现、冲突核对或失败案例。

## T12

- Durability is an integration capability, not an automatic property of every Agent run; plain in-process runs require the caller to persist run identity/history and external state.

## T13

1. 校验输入格式
2. 运行测试
3. 记录失败原因
4. 发布结果

## T14

- 候选池可以继续扩大；当新来源不再提供新模式或证据时，停止扩张并转向实践。
- 进入课程前，先写明它填补哪个 Output 缺口。
- 完成后，更新来源卡和实验/应用证据。

## T15

- 代码本体采用 Apache-2.0；仓库所含或关联的专有模型不因此自动适用该许可，使用这些模型前需单独审查 MODEL_LICENSE。
- 房间权限只管理房间访问，不等同于 function tools 的授权；高风险工具还需审批层。

## T16

- Provider breadth reduces adapter friction, but common interfaces do not establish equivalent behavior across every provider.
- Source and CI design show strong production engineering signals; nothing was executed in this review, so runtime correctness remains unvalidated.
- The framework exposes explicit approval waitpoints; prompt wording alone does not provide the same human gate.

## 约束与实际读取文件

- 约束：仅读取指定候选技能的 `SKILL.md`、当前任务明确要求的 references，以及对抗输入；未读取其他文件或任何结果；仅使用 `apply_patch` 写入本文件。
- 实际读取文件：
  - `<materialized>/hw-semantic-candidate/SKILL.md`
  - `<materialized>/hw-semantic-candidate/references/fact-integrity.md`
  - `<materialized>/hw-semantic-candidate/references/content-modes.md`
  - `<materialized>/hw-semantic-candidate/references/style-diagnostics.md`
  - `<materialized>/hw-semantic-candidate/references/quality-rubric.md`
  - `<materialized>/hw-semantic-adversarial-inputs.md`
