## R01

- 官方来源优先，但官方自述仍不能替代独立运行验证。
- 同一问题优先保留一个主来源；其他来源用于不同实现、冲突核对或失败案例。

## R02

- Durability is an integration capability, not an automatic property of every Agent run; for plain in-process runs, the caller must persist run identity/history and external state.

## R03

- The cache reduces repeated reads but does not guarantee freshness, so the caller must choose a TTL and an invalidation policy.

## R04

- 候选池可以继续扩大；当新来源不再提供新模式或证据时，停止扩张并转向实践。
- 进入课程前，先写明它填补哪个 Output 缺口。
- 完成后，更新来源卡和实验/应用证据。

## R05

1. 校验输入格式
2. 运行测试
3. 记录失败原因
4. 发布结果

## R06

- 默认使用已验证模板；其他模板只用于兼容性测试或失败复现。
- 测试通过不代表模板可以进入生产环境。

## 约束

- 仅读取 `<materialized>/hw-semantic-candidate/SKILL.md`、当前任务明确要求的 references，以及 `<materialized>/hw-semantic-closure-inputs.md`。
- 未读取其他文件、目录内容或任何既有结果。
- 执行 R01–R06；各节仅保留成品。
- 使用 `apply_patch` 写入指定文件。

## 读取文件

- `<materialized>/hw-semantic-candidate/SKILL.md`
- `<materialized>/hw-semantic-candidate/references/fact-integrity.md`
- `<materialized>/hw-semantic-candidate/references/reasoning-and-explanation.md`
- `<materialized>/hw-semantic-candidate/references/style-diagnostics.md`
- `<materialized>/hw-semantic-candidate/references/quality-rubric.md`
- `<materialized>/hw-semantic-closure-inputs.md`
