# Lesson 01 — Coding Agent Runtime Model

## Question

为什么 Coding Agent 需要 Runtime，而不是简单的 Chat Interface？

## Learning Goal

理解 Coding Agent 的核心区别：

- 状态持续存在；
- 工具调用是一等事件；
- 文件修改和命令执行需要生命周期管理；
- 客户端与 Agent Runtime 可以解耦。

## Current Hypothesis

一个可扩展 Coding Agent 需要独立 Runtime 层，用于管理：

- conversation state
- tool execution
- approvals
- events
- persistence
- recovery

## Source Evidence

Status: not_started

需要补充：

- fixed repository commit
- source file locator
- architecture evidence

## Key Concepts To Verify

- Thread / Turn / Item
- Agent loop
- Event model
- Client-runtime boundary

## Exercise

构造一个最小 Agent Runtime 模型：

```
Input
  ↓
Runtime
  ↓
Tool/Event
  ↓
State Update
  ↓
Result
```

比较：

- simple chat history
- event driven agent runtime

## Project Mapping

候选映射：

- ask-ai workflow
- skill execution feedback
- repository review events

## Verification Status

Not completed.
