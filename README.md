# AI Engineering Handbook v0.2

`ai-handbook` 是个人 AI Engineering System 的**学习与治理控制面**。它负责维护来源、研究、知识图谱、实验、应用证据、跨仓库路由和自我迭代规范；它不是课程收藏夹，也不替代下游代码或内容仓库。

每个结论必须区分：

1. 已验证事实；
2. 基于当前证据的推断；
3. 未验证假设。

静态阅读、本地测试、目标运行时和生产验证必须分开记录，不能向上替代。

## 系统职责

| 对象 | 权威职责 | 不承担的职责 |
| --- | --- | --- |
| `idaibin/ai-handbook` | 来源目录、研究队列、知识图谱、实验、应用证据、工作流治理和晋级决策 | 不保存所有大型原始资产，不直接拥有生产 Skill |
| `idaibin/feeds-hub` | 实时信息的数据记录、去重、校验和展示 | 不承担长期知识蒸馏；普通事件更新不应触发架构改造 |
| `idaibin/knowledge-distillation` | Knowledge IR、课程、文章、知识卡片、图片/视频知识内容包及对外知识输出 | 不拥有生产执行 Skill；实际执行能力由 Skills 或目标工具承担 |
| `idaibin/skills` | 可触发、可执行、可测试的稳定能力 | 不保存大规模来源、课程正文和研究历史 |
| 目标项目仓库 | 项目代码、项目规范、真实构建与运行证据 | 不替代跨项目学习与方法治理 |
| ChatGPT Work | 研究、编排、审查和任务入口 | 不替代 GitHub 的版本化权威状态 |

完整职责与路由规范见 [`workflows/ai-engineering-system/`](workflows/ai-engineering-system/README.md)。

## 双循环工作方式

### 持续发现

持续发现只完成：

```text
发现 → 规范化身份 → 去重 → 分类 → 质量初筛 → 候选队列
```

它可以覆盖 GitHub、官方文档、课程、论文、书籍、新闻和社区信号，但不等于已经阅读、理解或验证。

### 按需深研

只有存在明确问题、交付缺口或用户委派时才进入：

```text
问题定义 → 选择主来源 → 固定版本 → 阅读证据
→ 汇总与知识图谱 → 可证伪实验 → 真实项目应用
→ 独立 Review → 路由到下游 → 反馈迭代
```

候选池可以很大；深度研究必须小批次、按问题 Pull，不以仓库数量或 Star 数替代学习质量。

## 输出路由

```text
实时事件                  → feeds-hub
知识性对外内容            → knowledge-distillation
稳定、可执行能力          → idaibin/skills
项目代码和项目级验证      → 对应项目仓库
研究、证据、实验与决策    → ai-handbook
大型/私有/受版权保护资产  → Google Drive，并在 GitHub 保存索引
```

## 状态与证据

状态必须按维度保存，而不是压缩成一个 `completed` 或 `partial`：

- 发现状态；
- 阅读状态；
- 证据状态；
- 新鲜度状态；
- 工作流状态；
- 下游交接状态。

统一状态合同见 [`state-model.yaml`](workflows/ai-engineering-system/state-model.yaml)。

## 目录

- `maps/`：能力地图和知识关系。
- `roadmap/`：以产出和门禁驱动的学习路径。
- `sources/`：候选来源、固定阅读证据和来源治理。
- `experiments/`：固定输入、oracle、baseline/treatment、运行结果与应用案例。
- `templates/`：来源和研究记录模板。
- `workflows/`：AI Engineering System 的唯一权威工作流、存储规范、交接合同和评估。

## 维护边界

- GitHub 保存公开、结构化、可版本化的事实和规范。
- Google Drive 保存私有、受版权保护、大型或二进制原始资产。
- ChatGPT Library 保存工作副本和固定快照，不作为唯一事实源。
- Google Sheets 可以作为筛选和运营视图，但不得成为唯一任务状态或研究证据来源。
- 自动化可以发现、去重、校验和生成候选；不能自动提升证据等级、发布生产 Skill 或把局部成功宣称为生产完成。

当前规范版本：`ai-engineering-system v0.2.0`。
