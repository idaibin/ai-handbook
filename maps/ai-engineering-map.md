# AI Engineering Map v0.3

## Purpose

AI Engineering 研究如何让 AI 能力成为可组合、可验证、可复用的工程能力。

核心问题：

> How AI works, acts and integrates into engineering systems.

该领域不关注单一模型排名，而关注稳定能力、系统设计和真实验证。

---

## Capability Map

```text
AI Engineering

├── Model Capability
│   ├── Reasoning
│   ├── Generation
│   ├── Multimodal
│   └── Context Handling
│
├── Agent System
│   ├── Agent Loop
│   ├── Planning
│   ├── Tool Calling
│   ├── Memory
│   └── Delegation
│
├── Skill System
│   ├── Capability Packaging
│   ├── Instruction Design
│   ├── Trigger Rules
│   └── Validation
│
├── Tool Integration
│   ├── MCP
│   ├── Plugins
│   ├── APIs
│   └── External Services
│
├── Workflow Engineering
│   ├── Task Routing
│   ├── Human Approval
│   ├── State Management
│   └── Automation
│
├── Harness Engineering
│   ├── Environment Control
│   ├── Context Injection
│   ├── Evaluation Loop
│   └── Safety Boundary
│
└── Evaluation
    ├── Benchmark
    ├── Fixture
    ├── Regression
    └── Production Evidence
```

---

## Core Workflow

```text
Problem Definition
        ↓
Capability Selection
        ↓
Source Research
        ↓
Knowledge Model
        ↓
Prototype
        ↓
Evaluation
        ↓
Real Project Integration
        ↓
Feedback
```

---

## Agent System Model

```text
User Intent
    ↓
Planning
    ↓
Tool Selection
    ↓
Execution
    ↓
Observation
    ↓
Artifact
    ↓
Review / Approval
    ↓
Commit
```

重点研究：

- Agent architecture
- Tool boundary
- Permission model
- State tracking
- Human-in-the-loop

---

## Skill Model

Skill 是稳定可复用能力的封装。

标准生命周期：

```text
Research
 ↓
Pattern
 ↓
Skill Prototype
 ↓
Behavior Evaluation
 ↓
Stable Skill
 ↓
Maintenance
```

进入 `idaibin/skills` 前必须具备：

- 明确输入输出；
- 可重复执行；
- 正负例；
- 验证证据。

---

## MCP / Plugin / Tool Model

关注：

```text
AI Model
    ↓
Tool Interface
    ↓
Permission Boundary
    ↓
External Capability
    ↓
Result Artifact
```

研究重点：

- 接入方式
- 权限控制
- 数据边界
- 错误恢复
- 可观察性

---

## Harness Engineering

Harness 负责提供 AI 执行环境。

包括：

- Context Assembly
- Repository Access
- Tool Configuration
- Memory Strategy
- Evaluation Hooks
- Execution Constraints

目标：

让 AI 在确定环境中稳定完成任务。

---

## Evaluation Model

任何 AI Engineering 能力必须区分：

| 层级 | 证据 |
| --- | --- |
| Concept | 理论和文档 |
| Prototype | 小规模实验 |
| Validated | 可重复验证 |
| Production | 真实项目证据 |

评估关注：

- Correctness
- Reliability
- Cost
- Latency
- Maintainability
- Failure Boundary

---

## Related Projects

当前关联：

- `idaibin/skills`
- `idaibin/forgeway`
- `idaibin/feeds-hub`
- `idaibin/rustzen-admin`

---

## Future Research

后续逐步完善：

- Agent Framework
- Skill Ecosystem
- MCP Ecosystem
- Harness Patterns
- AI Coding Workflow
- Multi-Agent System
- Evaluation Infrastructure
