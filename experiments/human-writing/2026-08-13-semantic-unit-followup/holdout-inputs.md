# Holdout generator inputs

These neutral cases contain no expected decisions or labels.

## H01

Protected: `cache`; `TTL`

Instruction: Without adding, removing, or altering facts, rewrite as a bullet list with one item per claim. Preserve protected spans verbatim. Return only the finished text.

Input:

The cache reduces repeated reads. It does not guarantee freshness. The caller must choose a TTL and an invalidation policy.

## H02

Instruction: 不增删事实，改成每项对应一个可独立执行动作的条目列表。只返回成品。

Input:

发布前备份数据库。发布后检查错误率。若错误率超过阈值，回滚版本并保留日志。

## H03

Protected: `公开报告`; `客户标识`

Instruction: 不增删或改动事实，改成每项对应一条完整政策的列表。protected 必须字面保留。只返回成品。

Input:

公开报告可以对外分享。含有客户标识的附件不得对外分享。完成脱敏并获得审批后，该附件可以分享。

## H04

Instruction: Without changing facts, rewrite as exactly three bullets. Return only the finished text.

Input:

The SDK supports retries. Retries do not make a non-idempotent write safe. The audit log records submitted actions. It does not prove that the remote service applied them. Staging passed its smoke test. Production behavior remains unverified.

## H05

Instruction: 去掉模板化表达，保持编号列表和全部事实。只返回成品。

Input:

1. 冻结输入；2. 生成候选；3. 对照来源复核。

## H06

Instruction: 去掉空泛衔接和冗余强调，保持一个段落，不增删事实。只返回成品。

Input:

从整体上看，需要特别指出的是，本次测试覆盖了本地路径，但没有覆盖远端服务，因此结果可以说明本地流程可运行，却不能证明生产环境已经就绪。
