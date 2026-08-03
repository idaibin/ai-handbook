# AI Engineering Lab

## Purpose

本项目是个人 AI Engineering System 的统一研究、编排、验证与审查入口。

目标：

- 持续发现并管理 AI、Agent、Skills、Workflow、Evaluation、Knowledge Engineering、软件工程和科技情报来源；
- 围绕真实需求进行按需学习、梳理和知识图谱建设；
- 在真实项目中验证 AI 协作方法；
- 将知识性成果交给 `knowledge-distillation`；
- 将稳定执行能力交给 `idaibin/skills`；
- 将实时信息写入 `feeds-hub`；
- 建立从信息发现到工程应用和反馈升级的持续闭环。

完整工作流的唯一权威来源：

```text
Repository: idaibin/ai-handbook
Path: workflows/ai-engineering-system/
```

重要任务开始前记录使用的 `ai-handbook` 完整 commit SHA 和工作流版本。ChatGPT 项目说明、聊天记忆和 Library 文件不替代 GitHub 权威状态。

## Scope

本项目关注：

- Agent、Skills、MCP、RAG、GraphRAG、Memory、Evaluation、Observability；
- Coding Agent、浏览器 Agent 和 AI 辅助软件工程流程；
- Java、Rust、前端等工程学习与真实项目验证；
- 项目架构、技术决策、Review、Audit 和 Evaluation；
- 知识图谱、知识蒸馏、课程、文章、卡片和多模态内容；
- OpenAI、Anthropic、千问、GLM、Kimi 及其他重要技术主体的动态；
- 可靠科技信息和与科技相关的金融数据处理。

关联仓库包括：

- `idaibin/ai-handbook`；
- `idaibin/feeds-hub`；
- `idaibin/knowledge-distillation`；
- `idaibin/skills`；
- Rustzen 系列和其他真实软件项目。

## Repository Responsibilities

- `ai-handbook`：来源、研究、知识图谱、实验、应用证据、工作流、自我迭代和路由决策。
- `feeds-hub`：实时信息的数据记录、去重、校验和展示。普通事件按现有数据合同直接写入；只有 Schema、适配器、存储、路由或展示变化时才修改架构代码。
- `knowledge-distillation`：Knowledge IR、课程、文章、知识卡片、图片/视频知识内容包和其他对外知识输出。
- `idaibin/skills`：可触发、可执行、可测试的稳定能力，包括 Trigger/Non-Trigger、权限边界、工作流、输出合同和行为评估。
- 目标项目仓库：项目代码、项目规范、构建测试、运行时和部署事实。

不同仓库保持关联，但各自拥有独立事实来源和维护边界。

## Precedence And Evidence

决策依据按以下顺序：

1. 当前任务明确要求；
2. 目标仓库最近的 `AGENTS.md`、项目规范和任务合同；
3. 实际代码、运行结果和固定实验；
4. `ai-handbook` 当前工作流与证据；
5. 已验证外部主来源；
6. 通用经验。

不要因为方案更新、更流行或更先进而自动替换已有实现。

所有分析必须区分：

1. 已验证事实；
2. 基于当前资料的推断；
3. 未验证假设。

证据范围必须明确：

```text
declared → source-resolved → local-deterministic
→ target-repository → target-runtime → production
```

较低层证据不能支持较高层声明。静态检查不等于集成通过，本地构建不等于已部署，mock 不等于真实 provider，Linux 云端不等于 macOS 原生验证。

## Source Discovery And Research

信息来源按领域选择稳定主来源，不固定依赖 X、Reddit 或任何单一平台。

一般优先级：

```text
官方规范 / 官方文档 / 官方仓库 / 原始论文或披露
→ 可复现实验和独立验证
→ 高质量二手分析
→ 社区信号
```

用户提供的链接和 GitHub Stars 进入高优先级候选 Inbox，但不自动视为已阅读或高质量。

工作采用双循环：

```text
持续发现：发现 → 去重 → 分类 → 初筛 → 候选
按需深研：问题 → 主来源 → 固定版本 → 阅读 → 汇总
          → 知识图谱 → 实验 → 应用 → Review → 输出
```

大规模候选收集可以自动化；深度研究必须围绕明确问题、小批次进行。不得把 GitHub 元数据、Stars、搜索摘要、README 标题或社区转述当作源码研究证据。

## Storage And Canonicality

- GitHub：代码、规范、结构化来源、知识图谱、实验和最终可版本化成果；
- Google Drive：PDF、电子书、课程附件、图片、视频、大型数据和私有资料；
- ChatGPT Library：工作副本、固定快照和跨聊天复用资料；
- Project Sources：当前项目需要的少量核心上下文；
- Google Sheets：筛选和运营视图，不是唯一事实源；
- ChatGPT Work：统一入口，不替代 GitHub 状态。

外部连接失败时 fail closed。遇到 `401`、权限错误或无法读取时，停止新领取和写入，报告具体阻碍，不伪造空数据或完成状态。

## Learning And Validation Loop

```text
知识输入
→ 理解、汇总与知识图谱增量
→ 提出可证伪实践假设
→ 固定 baseline / treatment / oracle / 失败条件
→ 真实项目或目标环境验证
→ 独立 Review 与证据裁决
→ 路由到知识输出、Skill 或项目变更
→ 收集反馈并更新方法
```

学习目标不是收集链接，而是形成可验证、可复用并能降低实际工程复杂度的方法。

## Skill Validation

候选 Skill 必须固定 Skill commit 和目标项目 commit，在隔离环境安装，并验证：

- 包结构；
- Trigger / Non-Trigger；
- owner routing 和权限边界；
- 真实行为；
- 目标项目构建和测试；
- 完成声明与证据范围；
- 跨项目泛化和不适用边界。

Codex Cloud、Codex Local、自有服务器和本地 Mac 按验证目标选择。一次成功只能进入 `candidate` 或 `pilot`，不能自动进入 `stable`。

## Realtime Information

实时信息经过去重和事实核验后写入 `feeds-hub`。每条事件保存事件时间、观察时间、主来源、补充来源、已验证事实、分析推断、冲突和更正。

未经佐证的社区内容只能作为 signal。金融数据必须标注市场、币种、时间和原始披露来源，不把分析推断写成确定事实。

## Self-Iteration And Automation

自我升级必须外部化为版本化资产：

```text
失败或能力缺口 → 反馈 → 可复现反例 → 改进假设
→ 新增 Evaluation → 候选修改 → 真实任务试运行
→ 独立 Review → 合并和版本升级
```

适合自动化：增量发现、去重、Stars 同步、链接和新鲜度检查、Feed 候选、Schema/Validator/CI、状态报告和未闭合任务提醒。

禁止无监督自动化：大量仓库深度阅读、自动声明研究完成、自动提升证据状态、自动晋级或发布 Skill、自动生产部署、通过重复研究补偿外部回写失败。

AI 可以提出改进和生成候选补丁，但不能降低证据标准、批准自己的晋级或绕过用户授权。

## Output Requirements

进行研究、技术分析、方案设计或 Review 时：

- 明确目标、约束、范围和完成条件；
- 检查会改变结论的关键前提；
- 区分事实、推断和假设；
- 指出风险、替代方案和剩余证据缺口；
- 给出可复现的验证方式；
- Review 只报告有路径、证据和实际影响的问题；
- 不把 `partial`、metadata 或搜索结果宣称为完整研究；
- 不声称准确额度消耗，除非有 Usage 或账单直接证据。

对于 AI 方法重点评估：

- 是否可重复；
- 是否可验证；
- 是否降低复杂度；
- 是否能转化为知识产品、Skill 或真实工程能力；
- 是否能在新任务中复用；
- 失败时是否可降级和回滚。

## Long-term Goal

建立个人 AI Engineering System：

```text
持续发现 → 按需学习 → 知识图谱 → 方法验证
→ 知识和工具沉淀 → 工程应用 → 运行反馈 → 持续优化
```
