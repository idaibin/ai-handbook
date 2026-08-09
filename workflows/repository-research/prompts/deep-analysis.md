# Scheduled Prompt: Topic Repository Deep Analysis

执行 `<TOPIC>` 的一次 GitHub 仓库深度分析批次。

开始前必须从 `idaibin/ai-handbook` 的 `main` 分支重新读取：

1. `workflows/repository-research/process.md`；
2. `workflows/repository-research/topics/<TOPIC>.toml`；
3. topic 配置指定的 reconciled eligible queue、deep progress、最近 batch report 和最近 retrospective。

严格执行 process 的 Deep-analysis lane。只消费 `status=ready` 的不可变 snapshot，并通过带 lease 的 claim 领取；不得把相邻调度时间当成交接完成。目标为 topic 配置中的批次上限，但质量高于数量。每个 repository identity 必须独立通过 gate；用 fixed tree/blob 建立 content identity，重复内容复用既有分析并单独计数，不能把 fork 数量当成独立研究数量。按 topic 的 required 文件逐项核读；静态阅读、source validation 和 runtime validation 分开记录。

可按需委派子代理并行读取独立仓库，但只有主执行者能更新 canonical queue、累计状态、latest pointer 和 GitHub commit。每个子代理必须返回固定版本、已读文件、直接证据、推断、未验证项和建议 evidence level。

批次结束必须写 retrospective，只允许选择一个有证据的方法变化；生成分析报告、progress JSON、dedup mapping、latest pointer，并以一个原子 commit 写入 `main`。提交后重新读取 main 验证 commit、latest pointer、累计值和下一候选一致。若任何写回验证失败，不得宣称完成。

最终回复只报告：topic、实际 repositories/unique contents/reused/new reports、evidence levels、commit、写回验证、唯一方法变化、下一候选和明确未验证项。
