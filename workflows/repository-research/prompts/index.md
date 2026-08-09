# Scheduled Prompt: Topic Repository Index

执行 `<TOPIC>` 的一次 GitHub 仓库索引批次。

开始前必须从 `idaibin/ai-handbook` 的 `main` 分支重新读取：

1. `workflows/repository-research/process.md`；
2. `workflows/repository-research/topics/<TOPIC>.toml`；
3. topic 配置指定的 canonical index、最近 run report 和最近 retrospective。

先严格执行 process 的 Usage quota gate；额度触发停止条件时，不得开始索引，并按规定同步、暂停六条任务和返回 Chat 恢复指令。额度不可观测时必须标记 `quota_not_observable`，不得伪造数值。

严格执行 process 的 Index lane。仅做发现、元数据核实、规范化、去重、分类、reconciliation 与队列写入；不得执行深度分析，不得把索引候选标记为已研究。每次运行使用 topic 配置的下一个确定性 shard，保存 query、分页和终止证据。

批次结束必须写 retrospective，只允许选择一个有证据的方法变化；reconciliation 完成后发布带 `snapshot_id/status=ready/source_commit` 的不可变 snapshot，更新 canonical state，并以一个原子 commit 写入 `main`。提交后重新读取 main 验证 commit、snapshot 与状态一致。若无法读取规范、固定查询、确认写回或安全解决冲突，停止并报告，不凭历史 prompt 继续。

最终回复只报告：quota gate 状态；topic、batch/shard、实际新增/重复/held/rejected 数、canonical 是否变化、commit、写回验证、唯一方法变化、下一 shard；若触发 quota_stop，改为报告停止原因、精确额度证据、同步 commit、六条任务暂停结果和 Chat 恢复指令。
