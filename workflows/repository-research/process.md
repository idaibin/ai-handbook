# Process Contract

## 1. Index lane

索引任务只做发现与排队，不读出“已完成深研”的结论。

每次运行必须：

1. 读取 topic 配置、canonical index、最近 run report 和最近 retrospective；
2. 选择配置中的下一个确定性 shard；同一 shard 不重复创建新批次；
3. 记录完整 query、页码、每页数量、终止条件、执行时间和访问限制；
4. 规范化 `owner/name`，以不区分大小写的 repository identity 去重；
5. 区分 fork、archive、mirror、empty、adjacent 和 unclear，不因 Star 自动纳入；
6. 写入原始 batch、run report 和 provisional candidate；
7. 只有 reconciliation 完成后才更新 canonical totals 与 deep-analysis queue；
8. 发布不可变 snapshot，字段至少包含 `snapshot_id`、`source_commit`、`status=ready`、候选身份和内容指纹；
9. 生成本批 retrospective，并提交一个原子 commit。

索引状态：`discovered | metadata_verified | eligible | held | rejected`。

## 2. Deep-analysis lane

深度分析只从 `status=ready` 的不可变 snapshot 领取候选；不得直接从搜索结果挑选并计入完成数。若最新索引尚未 ready，使用上一个 ready snapshot 或安全退出，不能读取半成品。调度分钟只负责触发，不代表索引与深度任务已经完成交接。

领取时写入 `claim_id`、`run_id`、`claimed_at`、`lease_expires_at` 和原 snapshot item；写后重新读取确认。lease 未过期不得由另一批覆盖；过期回收必须保留旧 claim 记录。

### Repository gate

每个 repository identity 至少固定并记录：

- canonical URL、owner/name、默认分支、license、archive/fork 状态；
- observed Stars 与时间；
- fixed commit、tree；
- root README、目录树和 topic 配置要求的关键文件；
- evidence URLs、读取范围和未读取项。

### Content gate

用 fixed tree、关键 blob 或等价可复现指纹建立 `content_id`。完全相同内容可以复用已有内容分析，但每个 repository identity 仍需独立通过 metadata/README gate。报告必须同时给出：

- `repositories_reviewed`；
- `unique_contents_reviewed`；
- `analyses_reused`；
- `new_analysis_reports`。

不得用 fork 数量放大独立研究数量。

### Evidence levels

| Level | Meaning |
| --- | --- |
| `metadata_verified` | 只核对仓库身份与元数据 |
| `structure_reviewed` | 固定版本并读取要求的源码/文档结构 |
| `source_validated` | 通过源码、测试或静态工具核实关键声明 |
| `runtime_validated` | 实际运行核心路径并保存运行证据 |

低层级不能替代高层级。没有运行不得写 `runtime_validated`。

### Batch rule

默认目标为 topic 配置给出的 qualified repository identity 上限，并应达到 `deep_minimum_new_content`；若时间、访问、上下文、合格候选或证据不足，完成实际可验证数量并记录原因。低于 `minimum_stars` 的仓库只有在它是官方规范、官方实现或不可替代的一手来源时才能例外纳入，并必须记录理由。不得用低 Star fork、重复内容或浅层摘要凑数。每批必须产出：

- Markdown analysis report；
- machine-readable progress JSON；
- content/repository dedup mapping；
- retrospective；
- 更新后的 latest pointer；
- 一个原子 commit。

每个 topic 只有配置中 `canonical_state` 指向的文件可写累计状态。历史 progress、batch 和 latest 文件均是不可变证据或兼容视图，不得被当作第二状态权威。兼容视图必须从 canonical state 生成，并通过 `schemas/state.schema.json` 校验。

提交后重新读取 main，确认 commit、latest pointer、累计值和下一候选一致。任何不一致都标为 `write_verification_failed`，不得宣称本批完成。

## 3. Retrospective loop

每次 index 和 deep-analysis 结束都必须读取上一批复盘并回答：

1. 本批计划、实际完成、held/failed/reused 数量；
2. 哪个质量门禁失败，提供具体样本；
3. 上一批 `action_id` 是否实际应用，用 before/after 指标判断保留或回滚；
4. 下一批只选择一个变化，写明假设、指标和回滚条件；
5. 若没有实际失败、新证据或约束变化，保持方法版本不变。

复盘结构必须通过 `schemas/retrospective.schema.json`。核心证据门槛、状态 schema 和权威路径不能由单次定时运行静默修改；需要单独提交规范变更。

不得通过降低文件覆盖、证据等级、去重门槛或写回验证来提高吞吐量。

## 4. Concurrency and delegation

可以并行读取彼此独立的仓库；canonical queue、latest pointer、累计状态和 GitHub 提交只能由主执行者串行更新。子代理只返回证据包，不直接争抢或覆盖共享状态。

## 5. Stop conditions

遇到以下情况停止当前批次并保存可恢复状态：

- topic 配置或 canonical queue 不可读取；
- GitHub/来源身份无法固定；
- 与已有批次发生领取或写回冲突；
- 无法确认 main 写回成功；
- 需要登录、付费或高风险外部操作且没有授权。
