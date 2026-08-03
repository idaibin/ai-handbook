# 来源目录

`sources/` 保存候选来源、固定阅读证据和来源治理记录。它不是“已完成学习清单”。

- `catalog.yaml`：现有候选来源台账；历史字段按原证据解释，不自动升级。
- `inbox/`：用户提供、GitHub Stars 或自动发现的待筛选来源。
- `coverage/`：固定提交上的来源角色覆盖和验证工具。
- `distillation-ledger.yaml`：历史局部蒸馏记录，不代表整个来源已完成研究。
- `github-ai-repositories.yaml`：已有 GitHub 候选池。

统一来源规则见 [`../workflows/ai-engineering-system/source-management.md`](../workflows/ai-engineering-system/source-management.md)，状态合同见 [`../workflows/ai-engineering-system/state-model.yaml`](../workflows/ai-engineering-system/state-model.yaml)。

## 双循环

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
