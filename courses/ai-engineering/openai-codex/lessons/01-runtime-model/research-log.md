# Lesson 01 — Runtime Model Research Log

## Status

in_progress

## Research Question

为什么 Coding Agent 需要独立 Runtime，而不是简单的 Chat Interface？

## Fixed Basis

Repository:

```yaml
repository: openai/codex
branch: main
commit: pending
```

当前先建立研究记录，固定 commit 后补充精确引用。

## Investigation Scope

```text
codex-rs
├── core
├── protocol
├── app-server
├── exec
└── skills
```

## Questions

1. Runtime 是否独立于 UI/client？
2. Thread / Turn / Item 是否是核心领域模型？
3. Tool execution 是否作为事件流管理？
4. Approval、Policy、Sandbox 如何参与执行生命周期？
5. 状态恢复和持久化如何设计？

## Evidence Collection

待补充：

- fixed commit
- source locator
- symbol reference
- tests

## Current Hypothesis

一个可扩展 Coding Agent 需要 Runtime 层管理：

- state
- events
- tools
- approvals
- persistence
- recovery

该假设需要通过源码和测试验证。

## Project Mapping Candidates

- ask-ai event history
- skill execution feedback
- repository review lifecycle

## Verification Status

not_completed
