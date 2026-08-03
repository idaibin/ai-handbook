# Source Discovery And Research Policy

## 1. 目标

来源管理分为两个不同目标：

1. 建立广泛、去重、可分类的候选来源池；
2. 围绕真实问题选择少量高价值来源进行深度研究。

候选池规模可以达到 1000 个或更多；它不是“1000 个仓库全部完成源码研究”的承诺。

## 2. 来源类型

支持但不限于：

- GitHub 仓库；
- 官方规范和文档；
- 官方课程；
- 第三方课程；
- 论文和技术报告；
- 书籍和电子书；
- 博客、视频和播客；
- Release、Changelog 和公司公告；
- 监管披露、财报和市场数据；
- 社区帖子和讨论。

索引类仓库、Awesome List 和 GitHub Stars 是发现入口，不是其所列全部内容的直接证据。

## 3. 按领域选择稳定来源

### AI 模型和产品

```text
官方文档 / changelog / model card / 官方 GitHub
→ 原始论文和技术报告
→ 独立复现
→ 高质量媒体和社区反馈
```

### 开源软件

```text
canonical repository / release / documentation
→ source / tests / evals / security policy
→ issues and discussions
→ third-party tutorial
```

### Java、Rust、前端和软件工程

```text
语言或框架官方文档
→ Specification / RFC / JEP
→ canonical source and tests
→ 官方教程
→ 高质量书籍和社区课程
```

### AI 图像和视频

```text
模型提供方文档 / API / model card
→ 官方案例
→ 可复现实验
→ 高质量社区案例库
→ 社交信号
```

### 科技和金融

```text
公司公告 / 投资者关系 / 交易所 / 监管机构 / 政府统计
→ 原始财报或数据
→ 可靠媒体
→ 专业分析
→ 社区讨论
```

社区来源可以发现问题和失败案例，但不能单独证明产品、性能、财务或生产能力。

## 4. 用户提供地址与 GitHub Stars

用户提供的地址直接进入高优先级 Inbox，但初始状态仍是：

```yaml
discovery_status: discovered
reading_status: unread
verification_status: unverified
```

GitHub Stars 作为个人候选 Inbox 增量同步。导入不代表已筛选、已阅读或高质量。

初始地址清单见 [`../../sources/inbox/user-provided.yaml`](../../sources/inbox/user-provided.yaml)。

## 5. GitHub canonical identity

对 GitHub 仓库优先保存：

```text
repository_id
owner/name
canonical_url
default_branch
observed_commit
observed_at
```

URL 规范化应移除协议差异、`.git`、尾部斜杠、查询参数和 `/tree/`、`/blob/` 等子路径。仓库重命名要跟随 GitHub canonical identity，但保留历史别名。

尝试、重试和批次是事件历史，不能增加唯一仓库数。

## 6. 质量初筛

Star 数只能用于发现优先级。进入深研前至少检查：

- 是否为官方或 canonical 来源；
- 是否与当前问题匹配；
- 是否有真实实现或完整内容；
- 是否有测试、Eval、示例或练习；
- 最近维护状态和归档状态；
- 许可证、版权和使用边界；
- 已知限制、安全边界和失败案例；
- 是否提供其他主来源没有的新证据；
- 是否可以固定版本并复核。

## 7. 分层研究

建议使用以下深度：

| 深度 | 含义 |
| --- | --- |
| D0 | 只发现地址 |
| D1 | 身份和元数据核对 |
| D2 | 实际读取 README 或官方文档 |
| D3 | 读取关键文件、章节、测试或 Skill/Agent 文件 |
| D4 | 形成架构、方法和边界综合 |
| D5 | 完成实验或真实项目应用 |

合理漏斗示例：

```text
最多 1000 个候选
→ 约 300 个 D2
→ 约 100 个 D3/D4
→ 少量 D5
```

具体数量由新增信息是否趋于饱和和当前项目价值决定，不作为硬性 KPI。

## 8. 证据要求

不得把以下内容称为源码研究证据：

- GitHub description；
- Star 数；
- 搜索摘要；
- Awesome List 的一句介绍；
- 未打开的 README 链接；
- 社区转述。

研究记录至少包含：

- 固定来源版本；
- 实际阅读范围；
- 文件、章节或 locator；
- 原子结论；
- 来源支持边界；
- 推断和未验证项；
- 观察时间。

## 9. 新鲜度和维护

刷新频率按来源变化速度设置：

- GitHub 元数据：开始研究前或低频批量刷新；
- 固定源码证据：以 commit 为准，不因上游更新自动失效；
- 官方产品文档和新闻：按事件或定期检查；
- 教程、书籍和课程：版本变化时复核；
- 金融数据：每条记录必须带观察时间、市场和币种。

当新来源推翻旧结论时，保留历史记录并使用 `superseded`，不静默改写过去证据。
