# AI Engineering Lab v0.1 冻结归档与 v0.2 重启基线

- 日期：2026-08-22（Asia/Tokyo）
- v0.1 最终 GitHub 基线：`idaibin/ai-handbook@fb61beeac1ac18dba4fd064cdefd892f5b4052eb`
- v0.1 状态：`ARCHIVED`
- v0.2 状态：`FROZEN_PENDING_MVP_SELECTION`

## 结论

v0.1 产生了大量可追溯的研究、规范、代码与媒体候选资产，但没有证明“多项目、多阶段、统一系统”本身创造了足够价值。主要失败不是实现能力，而是没有用真实结果约束范围：设计、Registry、Workflow、资产和实验的增长速度超过了可使用结果。

从本记录生效起：停止所有旧执行链、定时研究、项目扩展、架构扩展和资产批量生产。历史内容保留为证据，不再作为待办自动续接。只有一个经批准的 MVP 可以重新进入执行。

## 已核实的冻结快照

| 对象 | 固定事实 | v0.2 处置 |
| --- | --- | --- |
| `ai-handbook` | `main` 为 `fb61bee...`；旧入口声明四条产品路线、五类共享能力和长链路工作流 | 冻结旧工作流；本文件和 v0.2 入口取代其执行权 |
| Story Studio / 班超 EP01 | 当前系列状态记录为 G07、`2/10`，活动单元为 Hero Brush；`production_ready: false`、`publication_ready: false` | 停止 Hero Brush、Writing Surface、24 集扩展及 Production Agent MVP |
| Forgeway | 最新文档交接基线为 `4afd4d8...`；最后标注为运行代码的基线为 `6dcd835...`；存在有限 canary/vertical-slice 证据，但不能证明通用交付系统价值 | 保留代码和证据；停止扩展、评测和新架构 |
| Skills | `main` 为 `5573877...`；已有包、测试与研究资产，但本次没有重新执行其测试，也没有完成稳定的裸模型/Skill/Forgeway收益对照 | 保留已验证能力；停止新增 Skill 和批量研究 |
| Createway | Registry 中仅为 defined，仓库未创建 | 归档候选，不启动 |
| feeds-hub | Registry 标为 active；本次未重新核实运行时 | 冻结，不扩大 Research/Insights |
| rustzen-admin | Registry 标为 active；本次未重新核实运行时 | 冻结，不由本轮改动产品代码 |

状态纠正：`2026-08-20-banchao-ep01-g07-asset-reconciliation.yaml` 仍写 `1/10`，它是较早快照；后续 `2026-08-21-banchao-series-production-architecture.yaml` 与 Drive Task 状态均为 `2/10`。两者不应被压缩成同一个“最新状态”。

## v0.1 反思

1. 把“可以实现”当成“值得实现”。
2. 把架构完整、规范齐全、资产数量和测试通过当成用户价值。
3. 多项目并行，缺少唯一优先级和停止条件。
4. 先建系统再找场景，导致验证成本随系统同步增长。
5. 历史 Task、Drive 状态、GitHub 文档和自动化同时保留执行权，造成状态漂移与重复工作。

## v0.2 唯一执行规则

任何工作必须先有一份不超过一页的 `MVP_BRIEF`，并同时满足：

- 一个真实用户或使用者；
- 一个高频或高痛问题；
- 一个可直接使用的结果；
- 最多 7 天得到首个结果；
- 一个客观验收指标；
- 一个明确停止条件；
- 不新增平台、通用 Registry、通用 Workflow 或新项目。

执行循环只有：

`Problem → Smallest Result → Run → Evidence → Keep / Change / Stop`

在 `MVP_BRIEF` 经用户明确批准前，不执行旧 Task，不生成新资产，不修改产品代码，不启动新研究。

## MVP 选择门禁

候选只能比较三个维度：用户价值、验证成本、最短反馈时间。一次只选一个；不预设 7～14 天，不因项目已有投入而优先。MVP 可以小到一天，只要能产生可使用结果和真实反馈。

批准后只允许创建：

1. 一页 `MVP_BRIEF`；
2. 最小产物；
3. 一份运行证据；
4. 一份 keep/change/stop 决策。

除此之外不创建治理资产。

## 恢复入口

恢复任何 v0.1 项目前，必须引用本记录，说明为什么它优于其他候选，并重新核实现状。历史 commit、Drive 文件和 Task 只作为证据，不自动恢复为 active。

