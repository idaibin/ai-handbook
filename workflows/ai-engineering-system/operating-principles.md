# AI Engineering Lab Operating Principles

本文件定义 AI Engineering Lab 的长期目标、范围和执行原则。所有重要任务都必须先读取本文件；任务特定规则由 [`task-routing.md`](task-routing.md) 继续路由。

## 1. Purpose

本项目用于研究、验证和沉淀 AI 辅助软件工程方法：

- 学习和实践 AI Agent、Skills、Workflow、Evaluation 与 Knowledge Engineering；
- 在真实项目中验证 AI 协作方式；
- 将有效方法沉淀为规范、工具和可复用 Skills；
- 建立持续优化的 AI Engineering System。

核心闭环：

```text
知识输入 → 理解分析 → 实践验证 → Review 评估
→ 沉淀方法 → 复用 → 持续优化
```

## 2. Scope

本项目关注：

- AI 工程实践、Agent、Skills 与 Workflow 设计；
- 软件开发流程、架构分析和技术决策；
- Research、Review 与 Evaluation 方法；
- AI 知识蒸馏和工程能力建设；
- Rustzen 系列项目、`idaibin/skills`、`knowledge-distillation` 及其他 AI 工程实验项目。

## 3. Working Principles

### Evidence First

所有结论必须区分：

- **Verified**：有当前代码、文档、运行结果或其他直接证据；
- **Inference**：基于证据的推断，并说明依据和限制；
- **Not verified**：尚未验证，并说明缺少的证据和验证方式。

禁止用推测替代验证、用历史结果替代当前验证、用构建成功替代运行成功，或用部分结果代表整体结论。

### Reality Over Theory

技术方案、仓库、工具或 Skill 优先判断：是否真实可用、能否复现、是否降低复杂度、能否转化为工程能力。不得仅因方案更新、更流行或更复杂就替换已有实践。

### Research Quality

研究优先使用原始来源，固定来源版本与阅读范围，区分作者观点和验证事实，提炼可实践的方法，并通过实验或真实项目验证价值。研究目标不是收集信息，而是形成可复用能力。

### Real Validation

涉及代码、部署、测试或 Skill 时，优先读取实际代码与配置，使用真实环境，执行必要构建和测试，验证实际行为并保存关键证据。无法完成时必须说明限制、已完成内容和证据缺口。

## 4. Anti Optimization Loop

当目标明确、验证方式明确且风险可接受时，进入执行阶段。执行优先产生真实结果，不继续寻找理论最优方案。

重大修改必须由实际失败、新证据或明确约束变化触发。禁止在缺少执行反馈时扩大范围、以方案优化代替验证，或进行大规模重构。

## 5. Multi-project Relationship

AI Engineering Lab 负责方法研究、技术分析、实验设计和跨项目经验总结。各目标仓库拥有自己的代码、版本、规范、测试和运行事实；`idaibin/skills` 拥有稳定可复用能力；Knowledge Repository 拥有结构化知识资产。

不同项目保持独立事实来源。跨项目成果通过版本化 Artifact 和 handoff 传递，不直接复制未经验证的结论。

## 6. Output Requirements

研究、设计、Review 或验证输出应按任务需要覆盖：

1. 目标、范围与完成条件；
2. 已验证事实；
3. 推断与未验证假设；
4. 风险、限制和剩余证据缺口；
5. 验证方式与结果；
6. 可执行结论；
7. 经验证后可沉淀的经验。

输出优先清晰、可执行和可验证。不得作无证据的确定性声明，也不得用过度展开的方案代替执行。

## 7. Artifact Rules

重要产物必须保存到稳定位置：

- 项目代码、脚本和规范：对应 GitHub 仓库；
- 长期知识与研究资料：Knowledge Repository 或 ChatGPT Library；
- 验证结果与运行证据：项目定义的 artifacts 目录；
- 临时文件与中间产物：临时工作目录。

临时目录不算长期交付。重要结果必须能重新读取、追溯来源并复现或重新验证。详细存储与恢复规则见 [`storage-policy.md`](storage-policy.md) 和 [`delivery-recovery.md`](delivery-recovery.md)。

## 8. Continuous Improvement

重要任务结束后，复盘有效方法、失败原因、可优化步骤和复用边界。只有经过真实验证的方法，才升级为长期规范、Skill 或工具；没有新证据时不启动新一轮优化。

长期目标是形成可持续提升的个人 AI Engineering System：

```text
学习 → 实践 → 验证 → 沉淀 → 复用 → 优化
```
