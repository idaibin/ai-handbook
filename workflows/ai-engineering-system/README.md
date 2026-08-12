# AI Engineering System Workflow

- **Version:** `0.4.0`
- **Status:** active
- **Canonical owner:** `idaibin/ai-handbook`
- **Canonical path:** `workflows/ai-engineering-system/`

本目录是个人 AI Engineering System 的唯一权威工作流。ChatGPT Work、下游仓库和自动化任务只保存当前版本指针或本仓库定义的交接合同，不复制整套规范。

## 0. 启动与任务路由

执行重要任务前：

1. 记录当前 `ai-handbook` 完整 commit SHA；
2. 必须读取 [`operating-principles.md`](operating-principles.md)；
3. 根据 [`task-routing.md`](task-routing.md) 只加载匹配任务的 policy、workflow、instruction 和 prompt；
4. 当前用户明确要求优先；无法读取必须文件时停止修改和外部写入。

`chatgpt-project-instructions.md` 只保存上述远端入口，不再复制本目录规范。

## 1. 目标

建立可持续的闭环：

```text
信息发现
→ 去重与质量筛选
→ 按需学习与汇总
→ 知识图谱
→ 实验与真实项目验证
→ Review 与证据裁决
→ 知识输出 / Skill / 项目变更 / 实时 Feed
→ 运行反馈
→ 方法和工作流升级
```

成功标准不是“收集了多少链接”，而是：

- 来源身份可追溯；
- 结论与证据范围匹配；
- 方法可重复；
- 实验可证伪；
- 真实项目可以验证；
- 输出能够被检索、执行或复用；
- 失败能够反馈并改变后续方法。

## 2. 两条输入通道

### 2.1 持续发现通道

用于持续发现新仓库、官方文档、课程、论文、书籍、产品发布和行业事件。

允许的深度：

```text
身份核对 + 去重 + 分类 + 初筛 + 候选优先级
```

禁止直接声明：

```text
已学习 / 已理解 / 已验证 / 可用于生产 / 可晋级 Skill
```

### 2.2 委派研究通道

只有用户明确委派、项目出现能力缺口或已有实验失败时，才进入深度研究。

研究开始前必须写清：

- 问题；
- 目标输出；
- 约束；
- 失败条件；
- 所需证据范围；
- 选择主来源的理由。

## 3. 标准阶段

### Stage 0 — Intake

输入可以是用户提供的地址、GitHub Stars、自动发现结果、项目缺口或实时事件。

输出：稳定对象 ID、原始地址、来源时间和触发原因。

### Stage 1 — Normalize

对来源执行 canonical identity 解析和去重。

GitHub 仓库优先使用 repository ID；URL 规范化只作为辅助键。历史重试、批次和状态事件必须与唯一对象分开。

### Stage 2 — Screen

根据领域选择稳定来源，而不是固定依赖某个平台。优先顺序通常是：

```text
官方规范 / 官方文档 / 官方仓库 / 原始论文或披露
→ 可复现实验和独立验证
→ 高质量二手分析
→ 社区信号
```

X、Reddit、论坛和个人博客只在提供独特信号、失败案例或原始作者说明时使用；它们不是默认权威来源。

### Stage 3 — Research

固定主来源版本、记录阅读范围和 locator，提取原子结论、边界、反例、冲突观点和开放问题。

GitHub 元数据、Stars、搜索摘要或 README 标题不能替代源码、测试、官方文档或实际运行证据。

### Stage 4 — Synthesize

将研究结果更新为：

- 主题摘要；
- 知识图谱节点和关系；
- 方案候选；
- Prompt 模式；
- 实践假设；
- 证据债务。

### Stage 5 — Validate

验证方式按主张选择：

```text
静态与结构验证
→ 本地确定性实验
→ 目标仓库构建/测试
→ 目标运行时或集成验证
→ 生产或真实用户证据
```

较低层证据不能提升为较高层完成声明。

### Stage 6 — Route

| 产物类型 | 目标 |
| --- | --- |
| 实时产品、开源、科技或金融事件 | `feeds-hub` |
| 课程、文章、知识卡、图像/视频知识内容包 | `knowledge-distillation` |
| 已批准的公开知识节点和关系 | `blog`，通过固定版本的公开导出 |
| 稳定、重复、可执行的方法 | `idaibin/skills` |
| 具体代码、配置和项目测试 | 对应目标项目仓库 |
| 来源、知识图谱、实验、审计和晋级决策 | `ai-handbook` |

### Stage 7 — Observe And Improve

收集以下反馈：

- 搜索遗漏和重复；
- 来源过期；
- Skill 误触发、漏触发和执行失败；
- 内容错误、边界不清和版权风险；
- 真实项目中的集成、性能和运行差异；
- 自动化写入失败和未闭合任务。

任何方法升级必须先记录反馈和反例，再增加评估，最后修改规范。

## 4. ChatGPT Work 与执行环境

ChatGPT Work 负责：

- 信息研究；
- 任务编排；
- 内容生成；
- 证据审查；
- 工作流和状态收口。

Codex Cloud、Codex Local、自有服务器或目标环境负责：

- clone 固定仓库版本；
- 安装候选 Skill；
- 修改代码；
- 构建、测试和运行；
- 提供 diff、日志和可复现证据。

macOS 原生能力必须在真实 Mac 环境验证；Linux 云端结果不能替代系统权限、签名、公证或原生交互证据。

## 5. 自动化边界

允许自动化：

- 增量发现；
- canonical 去重；
- GitHub Stars 导入；
- 链接和新鲜度检查；
- Feed 候选生成与数据校验；
- Schema、Validator 和 CI；
- 未闭合状态提醒；
- 只读状态报告。

禁止无监督自动化：

- 高频批量深读大量仓库；
- 自动把 `partial` 或元数据提升为完成；
- 自动修改证据等级；
- 自动发布生产 Skill；
- 自动部署到生产；
- 在外部写入失败后重复研究同一对象；
- 通过降低门禁让新方法自我通过。

## 6. 版本和升级

使用语义版本：

- `PATCH`：不改变行为的文字、链接和示例修正；
- `MINOR`：新增来源类型、交接合同、可选阶段或评估；
- `MAJOR`：修改仓库职责、核心状态、证据等级或晋级规则。

升级流程：

```text
反馈 → 反例 → 修改假设 → 新增 Evaluation
→ 候选规范 → 真实任务试运行 → 独立 Review
→ 合并 main → 更新 CHANGELOG → 按需打 tag
```

AI 可以提出修改和生成候选补丁，但不能自己降低证据标准、批准自己的晋级或绕过用户授权。

## 7. 关联文件

- [`operating-principles.md`](operating-principles.md)：项目目标、范围、证据原则、反优化循环、输出与产物规则。
- [`task-routing.md`](task-routing.md)：按任务类型加载最小必要规则和 Prompt。
- [`workflow.yaml`](workflow.yaml)：机器可读流程。
- [`ownership.yaml`](ownership.yaml)：仓库职责。
- [`state-model.yaml`](state-model.yaml)：状态与证据模型。
- [`source-management.md`](source-management.md)：来源发现、筛选和维护。
- [`storage-policy.md`](storage-policy.md)：GitHub、Drive、Library、Sheets 的存储边界。
- [`delivery-recovery.md`](delivery-recovery.md)：独立分支、阶段提交、push、Drive 兜底与恢复。
- [`skill-validation.md`](skill-validation.md)：候选 Skill 的真实项目验证。
- [`knowledge-publication.md`](knowledge-publication.md)：`feeds-hub → ai-handbook → blog` 的内容重构、公开导出与迁移合同。
- [`handoffs/`](handoffs/)：跨仓库交接合同。
- [`evals/routing.yaml`](evals/routing.yaml)：路由和边界回归案例。
- [`chatgpt-project-instructions.md`](chatgpt-project-instructions.md)：ChatGPT Work 项目指令版本。
