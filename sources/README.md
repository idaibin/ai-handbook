# 来源目录

`sources/` 保存候选来源、固定阅读证据和来源治理记录。它不是“已完成学习清单”。

- [catalog.yaml](catalog.yaml)：现有候选来源台账；历史字段按原证据解释，不自动升级。
- [inbox/](inbox/README.md)：用户提供、GitHub Stars 或自动发现的待筛选来源。
- [coverage/](coverage/README.md)：固定提交上的来源角色覆盖和验证工具。
- [distillation-ledger.yaml](distillation-ledger.yaml)：历史局部蒸馏记录，不代表整个来源已完成研究。
- [github-ai-repositories.yaml](github-ai-repositories.yaml)：已有 GitHub 候选池。
- [历史 Agent Skills 来源索引](catalog/github-agent-skills-index.md)：保留元数据索引、分组运行记录与暂停边界，不重启采集。

按主题取用见[Handbook 地图](../maps/README.md)。本目录是来源权威入口，不另造平行台账。
蒸馏记录的 `source_id` 可关联 GitHub 候选池的同名 `id` 与固定 `commit_sha`；不能把该关联省略后认定没有固定来源。
两项既有蒸馏产物的 `artifact` 已固定到原仓提交 `e13f311b2240c881523f15aee9f548d3d70da471`（2026-08-03 可达历史中首次／最后文件改动；2026-10-27 核到与当前内容一致）。原产物和台账声明的 2026-07-31 日期保留，但尚无当天产物的 Git 字节证据，不能把固定链接倒推为该日版本。

产物正文仍由独立仓 `idaibin/knowledge-distillation` 拥有；Handbook 仅保存引用、局部覆盖和适用边界。两份 IR 均为 `draft / level_3`，要求发布审查；历史结构校验、来源支持和 `distilled` 不等于当前运行验证、跨场景收益或可执行 Skill。台账的 `mcp-servers` 与产物的 `mcp-reference-servers` 指向同一固定来源，保留各自稳定 ID。

原仓 MIT 与上游来源许可分别核对；`public` 访问不表示发布审查已通过。两产物明确只保留转化笔记，不复制源文或替代原来源。2026-10-27 的固定根许可核验保留 MCP 的迁移／文档许可差异和 Langfuse 的 EE／第三方例外，不把历史 `Not verified` 粗改成单一许可证，也不把根许可核验称为全量权利链验证。

2026-10-27 核到的范围：catalog 有 4 个顶层条目（含课程集合和仓库候选池）；Inbox 有 9 个唯一记录；coverage manifest 有 12 个主来源；蒸馏有 2 簇、10 个局部来源引用。这些集合重叠、层级不同，不能相加为独立已验证资产总数。完整阅读、许可／成本、新鲜度和外部资产状态仍按每条证据核实。

统一来源规则见 [`../workflows/ai-engineering-system/source-management.md`](../workflows/ai-engineering-system/source-management.md)，状态合同见 [`../workflows/ai-engineering-system/state-model.yaml`](../workflows/ai-engineering-system/state-model.yaml)。

## 双循环

阶段与最小证据包见既有[产出驱动学习路径](../roadmap/learning-path.md)。这是方法参考，不自动启用发现任务、执行实验或恢复历史输出路由。

### 持续发现

持续发现只完成：

```text
发现 → canonical identity → 去重 → 分类 → 初筛 → 候选
```

来源可以来自 GitHub、官方文档、课程、论文、书籍、Release、新闻、公司披露或社区信号。发现不等于阅读、理解、验证或推荐。

### 按需深研

只有存在明确问题、项目缺口或用户委派时才进入：

```text
问题 → 主来源 → 固定版本 → 实际阅读 → 证据记录
→ 汇总与知识图谱 → 实验或项目应用 → Review
```

## 来源选择

来源按领域选择稳定主来源，不固定依赖 X、Reddit 或其他单一平台。一般优先级：

```text
官方规范 / 官方文档 / 官方仓库 / 原始论文或披露
→ 可复现实验和独立验证
→ 高质量二手分析
→ 社区信号
```

社区内容只有在提供独特失败案例、原始作者说明或官方来源缺失的信息时才进入候选；点赞、转发、评论数和账号影响力不是正确性证据。

## GitHub 来源

GitHub 仓库优先保存 repository ID、canonical `owner/name`、默认分支、观察时间和固定 commit。

- Star 数只是发现优先级，不是质量证明。
- Awesome List、资源索引和 GitHub Stars 是发现入口，不是其所列内容的直接证据。
- description、搜索摘要和 README 标题不能替代实际阅读。
- 声称研究 Skill、Agent、架构或测试时，必须读取对应文件或源码入口。
- 重试、批次和多次领取是历史事件，不能增加唯一仓库数。

## 状态

不要使用一个 `status` 同时表示发现、阅读、证据和完成。至少分开：

- `discovery_status`；
- `reading_status`；
- `verification_status`；
- `freshness_status`；
- `workflow_status`；
- `handoff_status`。

`partial` 只表示指定范围未完成，不能被宣称为完整研究。

## 来源卡最小内容

每个进入深研的来源至少记录：

- stable source ID 和 canonical URL；
- 来源类型、领域和来源角色；
- 固定版本、章节、路径或 locator；
- 实际阅读范围；
- 原子结论；
- 来源支持边界；
- 推断、反例和开放问题；
- 许可证、版权或访问边界；
- 观察时间和新鲜度。

来源卡模板见 [`../templates/source-note.md`](../templates/source-note.md)。

## 用户提供来源

用户提供的地址直接进入高优先级 Inbox，但默认仍是：

```yaml
discovery_status: discovered
reading_status: unread
verification_status: unverified
```

当前已提供地址见 [`inbox/user-provided.yaml`](inbox/user-provided.yaml)。重复地址只保留一个 canonical 记录。

## 输出边界

- 来源、研究和证据保留在 `ai-handbook`。
- 实时事件经核验后写入 `feeds-hub`。
- 知识性对外内容交给 `knowledge-distillation`。
- 稳定执行能力交给 `idaibin/skills`。
- 大型、私有或受版权保护原始资产保存到 Google Drive，GitHub 只保存索引和哈希。
