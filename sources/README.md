# 来源目录

`catalog.yaml` 是候选来源台账，不是已完成清单。任何来源先使用 [来源卡模板](../templates/source-note.md) 记录，再决定是否进入实验。

## 收录与核验

1. 仅收录用户提供的链接、来源官方页面或项目官方仓库。
2. 分开记录 `source_verification` 与 `learning_status`：前者说明来源到当前摘要的映射是否已核对，后者说明个人是否阅读、复现和应用。
3. 记录解决的问题、对应阶段、可交付 Output 和预期证据。
4. 同题来源依照 README 的去重原则保留主来源，其余作为交叉验证或淘汰候选。

## GitHub 与 X 扩展来源

- GitHub 仓库优先选择检查时超过 1000 Star、未归档的项目官方仓库，并固定检查日期、默认分支和提交 SHA。
- Star 只是发现信号，不是质量或正确性证明。是否进入蒸馏仍取决于问题匹配、可定位证据、许可、风险边界和实验价值。
- 同一问题只保留一个主来源；框架替代品、供应商自述和性能数字只作为交叉验证，不能相互叠加成“多数即正确”。
- X 只接收有稳定 URL、作者、日期和具体主张的内容。能回链官方仓库、文档、论文或独特失败证据时才入库；点赞、转发和账号影响力不作为正确性证据。
- `source_checked` 只表示来源与摘要映射已核对；只有实际阅读、复现、应用或蒸馏后，才按证据提升 `learning_status`。

当前 GitHub 候选池见 [`github-ai-repositories.yaml`](github-ai-repositories.yaml)。本轮没有为了凑数量强行纳入 X 推文；后续仅在其提供 GitHub/官方文档没有的可复核信息时补充。

已完成的局部蒸馏范围单独登记在 [`distillation-ledger.yaml`](distillation-ledger.yaml)。该台账只对点名的固定提交与 README 章节声明 `distilled`，不把局部提炼扩大成“整个仓库已学习”。

## 两个基线资源

- [Agent Learning Hub](https://github.com/datawhalechina/Agent-Learning-Hub)：路线与门禁。
- [ai-agents-from-zero](https://github.com/didilili/ai-agents-from-zero)：Python 最小实验教材。

两者均为用户提供的候选输入。本轮已核对其公开 README/目录结构，但没有运行仓库案例；个人学习、实验复现和项目适配状态仍是 `unverified`。不要把来源核对等同于课程完成或工程验证。
