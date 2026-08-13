## H01

- The cache reduces repeated reads.
- The cache does not guarantee freshness.
- The caller must choose a TTL.
- The caller must choose an invalidation policy.

## H02

- 发布前备份数据库。
- 发布后检查错误率。
- 若错误率超过阈值，回滚版本。
- 若错误率超过阈值，保留日志。

## H03

- 公开报告可以对外分享。
- 含有客户标识的附件不得对外分享。
- 含有客户标识的附件完成脱敏并获得审批后，可以分享。

## H04

- The SDK supports retries, but retries do not make a non-idempotent write safe.
- The audit log records submitted actions, but it does not prove that the remote service applied them.
- Staging passed its smoke test, but production behavior remains unverified.

## H05

1. 冻结输入。
2. 生成候选。
3. 对照来源复核。

## H06

本次测试覆盖了本地路径，但没有覆盖远端服务，因此结果可以说明本地流程可运行，却不能证明生产环境已经就绪。

## 约束与实际读取文件

约束：仅执行 H01–H06；只读取指定基线 Skill、其对当前任务要求的 references 及 holdout 输入；未读取 criteria、候选 skill、工作区仓库或任何输出/结果文件。

实际读取文件：

- `<materialized>/hw-semantic-baseline/SKILL.md`
- `<materialized>/hw-semantic-baseline/references/fact-integrity.md`
- `<materialized>/hw-semantic-baseline/references/content-modes.md`
- `<materialized>/hw-semantic-baseline/references/style-diagnostics.md`
- `<materialized>/hw-semantic-baseline/references/reasoning-and-explanation.md`
- `<materialized>/hw-semantic-baseline/references/quality-rubric.md`
- `<materialized>/hw-semantic-holdout-inputs.md`
