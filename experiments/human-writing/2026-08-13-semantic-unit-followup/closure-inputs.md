# Closure inputs

## R01

Instruction: 不增删或改动任何事实，改成每项对应一个事实的条目列表。只返回成品。

Input:

官方来源优先。官方自述仍不能替代独立运行验证。同一问题优先保留一个主来源。其他来源用于不同实现、冲突核对或失败案例。

## R02

Protected: `Agent`; `run identity/history`

Instruction: Without adding, removing, or altering facts, rewrite as a bullet list with one item per claim. Preserve every protected span verbatim. Return only the finished text.

Input:

Durability is an integration capability. It is not an automatic property of every Agent run. Plain in-process runs require the caller to persist run identity/history and external state.

## R03

Protected: `cache`; `TTL`

Instruction: Without adding, removing, or altering facts, rewrite as a bullet list with one item per claim. Preserve protected spans verbatim. Return only the finished text.

Input:

The cache reduces repeated reads. It does not guarantee freshness. The caller must choose a TTL and an invalidation policy.

## R04

Instruction: 不增删事实，改成条目列表；每项表达一个完整决策。只返回成品。

Input:

候选池可以继续扩大。当新来源不再提供新模式或证据时停止扩张。停止后转向实践。进入课程前先写明它填补哪个 Output 缺口。完成后更新来源卡和实验/应用证据。

## R05

Instruction: 去掉模板化表达，每项单独一行，保持编号列表和全部事实。只返回成品。

Input:

1. 校验输入格式；2. 运行测试；3. 记录失败原因；4. 发布结果。

## R06

Instruction: 不增删事实，改成每项对应一条完整政策的列表。只返回成品。

Input:

默认使用已验证模板。其他模板只用于兼容性测试或失败复现。测试通过不代表模板可以进入生产环境。
