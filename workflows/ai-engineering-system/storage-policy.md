# Storage And Canonicality Policy

本文件定义 GitHub、Google Drive、ChatGPT Library、Project Sources 和 Google Sheets 的职责。当前变更只建立规范，不创建外部目录。

## 1. 权威存储矩阵

| 内容 | 权威位置 | 备注 |
| --- | --- | --- |
| 代码、Schema、工作流、状态模型、结构化来源索引 | GitHub | 可 diff、Review、回滚和固定 commit |
| 来源阅读证据、知识图谱、实验定义和文本结果 | GitHub | 必须删除本地绝对路径和私有内容 |
| PDF、电子书、课程附件、原始图片、视频、大型数据 | Google Drive | 私有或受版权保护内容不进入公开仓库 |
| 固定审查包、当前常用资料、外部表格快照 | ChatGPT Library | 工作副本，不是唯一事实源 |
| 当前项目所需的少量核心文件 | ChatGPT Project Sources | 只保留精选上下文，不做大型归档 |
| 筛选、运营查看和人工处理视图 | Google Sheets | 从权威数据生成或定期 reconciliation |
| 聊天上下文和记忆 | ChatGPT Work | 不能替代仓库状态和证据 |

## 2. GitHub 保存规则

GitHub 中保存：

- canonical URL、稳定对象 ID 和固定 commit；
- 来源分类、状态和阅读范围；
- locator、原子结论、边界和开放问题；
- 实验输入、oracle、脚本、关键结果和 Review；
- 外部资产的逻辑 ID、文件名、哈希、访问级别和存储类型；
- 跨仓库交接和晋级决策。

公开仓库不得保存：

- 付费或受版权保护资料全文；
- 私有 Google Drive 链接；
- 本地绝对路径；
- 密钥、Token、Cookie 或账号信息；
- 无必要的大型二进制和重复生成资产。

## 3. Google Drive 规划目录

以下是后续安装时建议创建的目录；本规范提交本身不创建它们：

```text
AI Engineering Lab/
├── 00-Inbox/
├── 10-Sources/
│   ├── Public-Snapshots/
│   ├── Private-Licensed/
│   ├── Courses/
│   └── Papers-And-Books/
├── 20-Media/
│   ├── Images/
│   ├── Video/
│   └── Audio/
├── 30-Datasets/
├── 40-Exports/
│   ├── Sheets/
│   ├── Reports/
│   └── Review-Packages/
└── 90-Archive/
```

命名规则：

```text
<project>__<asset-type>__<topic>__<yyyy-mm-dd>__v<nn>.<ext>
```

示例：

```text
ai-handbook__snapshot__github-source-catalog__2026-08-03__v01.xlsx
knowledge-distillation__output__lesson-001-cards__2026-08-03__v02.zip
```

GitHub 中只保存类似以下索引：

```yaml
asset_id: lesson-001-source-pdf
storage: google_drive
canonical_filename: ai-course-lesson-001.pdf
sha256: null
access: private
copyright_status: licensed_or_user_owned
```

## 4. ChatGPT Library 与 Project Sources

Library 用于跨聊天复用：

- 当前阅读 PDF；
- 固定审查包；
- Google Sheets 导出快照；
- 图片和视频工作素材；
- 生成的文档、表格和演示稿。

Library 中的副本不会自动跟随 GitHub 或 Drive 更新。使用前要核对文件日期、版本和哈希。

Project Sources 只加入当前任务需要的核心文件。完整工作流通过 GitHub 指针读取，不在 Project Sources 中长期保存多个重复版本。

## 5. Google Sheets 使用规则

Sheets 只作为运营视图或人工筛选界面。唯一仓库数、状态和进度必须从 canonical identity 重新计算，不能直接相信历史累计字段。

数据模型至少分开：

- 唯一对象；
- 当前状态；
- 尝试记录；
- 批次记录；
- 证据记录；
- 同步状态。

写入必须幂等；外部回写失败后保留本地结果并标记 `sync_status: write_failed`，禁止重新研究同一对象来补偿写入失败。

## 6. 连接失败处理

每个外部读写批次先执行：

```text
身份检查 → 读取 metadata → 读取固定测试对象 → 确认目标可写
```

处理规则：

- `401`：停止；报告认证失效；等待重新授权；不领取新任务。
- `403`：停止；报告权限或组织策略边界。
- `429`：有界退避；不得无限重试。
- 写入失败：保存本地/仓库结果，记录待同步状态，不重复研究。

任何连接错误都不能被解释成“数据为空”或“研究完成”。

## 7. GitHub Push 失败时的 Drive 兜底

代码与版本化文档仍以 GitHub commit 为权威。push 失败且有已验证成果时，Google Drive 可以保存灾难恢复副本，但不能替代远端交付。

- 已 commit 的变更导出为 Git bundle，不散装上传源码；
- 报告、截图、录屏和其他非 Git 资产按“仓库 / 任务或分支”持续保存；
- 每个恢复目录保存 manifest，记录 basis、branch、完整 commit SHA、验证状态、资产 SHA-256、失败原因和同步状态；
- 上传后读取 metadata 确认文件存在；
- 后续 AI 先读取 manifest，恢复、校验并重新 push；
- GitHub 远端完整 SHA 未核验前，状态保持 `not_persisted` / `write_failed`。

具体流程与目录格式见 [`delivery-recovery.md`](delivery-recovery.md)。
