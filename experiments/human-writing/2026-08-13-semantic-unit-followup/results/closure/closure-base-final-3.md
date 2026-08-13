## R01

- 官方来源优先。
- 官方自述仍不能替代独立运行验证。
- 同一问题优先保留一个主来源。
- 其他来源用于不同实现、冲突核对或失败案例。

## R02

- Durability is an integration capability.
- It is not an automatic property of every Agent run.
- Plain in-process runs require the caller to persist run identity/history and external state.

## R03

- The cache reduces repeated reads.
- It does not guarantee freshness.
- The caller must choose a TTL and an invalidation policy.

## R04

- 候选池可以继续扩大。
- 当新来源不再提供新模式或证据时，停止扩张。
- 停止后，转向实践。
- 进入课程前，先写明它填补哪个 Output 缺口。
- 完成后，更新来源卡和实验/应用证据。

## R05

1. 校验输入格式。
2. 运行测试。
3. 记录失败原因。
4. 发布结果。

## R06

- 默认使用已验证模板。
- 其他模板只用于兼容性测试或失败复现。
- 测试通过不代表模板可以进入生产环境。

## 约束与读取记录

完整约束：正式 fixed-revision baseline closure 运行 3。只允许读取 `<materialized>/hw-semantic-baseline/` 的 `SKILL.md` 及其为当前任务明确要求的 references，以及 `<materialized>/hw-semantic-closure-inputs.md`；禁止读取 criteria、候选、其他文件和任何结果。执行 R01–R06，写入 `<run-output>/closure-base-final-3.md`，标题 `## R01`…`## R06`，仅成品；末尾记录完整约束、baseline SHA `aa73fec2f8630886b7d60b066f1de4deff96b60a` 与实际读取文件。用 `apply_patch`。

Baseline SHA：`aa73fec2f8630886b7d60b066f1de4deff96b60a`

实际读取文件：

- `<materialized>/hw-semantic-baseline/SKILL.md`
- `<materialized>/hw-semantic-baseline/references/fact-integrity.md`
- `<materialized>/hw-semantic-baseline/references/style-diagnostics.md`
- `<materialized>/hw-semantic-baseline/references/quality-rubric.md`
- `<materialized>/hw-semantic-closure-inputs.md`
