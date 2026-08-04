# Lesson 01 Evidence — Coding Agent Runtime Model

## Status

in_progress

## Fixed Source

Repository:

```text
openai/codex
```

Commit:

```text
9873cba8ce6d14e650e12cdc0dddd159ae6613d7
```

## Research Question

What is a Thread in Codex Runtime?

Is it only conversation history, or does it represent an execution context?

---

# Verified Facts

## F1. Thread is a protocol-level entity

Evidence:

```text
codex-rs/app-server-protocol/schema/typescript/v2/Thread.ts
```

The protocol exposes a `Thread` type.

Observed fields include:

- id
- sessionId
- forkedFromId
- parentThreadId
- ephemeral
- section
- status
- cwd
- source
- gitInfo
- turns

Source:

`Thread.ts` at commit `9873cba8ce6d14e650e12cdc0dddd159ae6613d7`

Conclusion:

Thread is more than an unnamed chat transcript container.

---

## F2. Thread contains lifecycle relationships

Evidence:

Fields:

```text
forkedFromId
parentThreadId
sessionId
status
```

Observation:

The protocol model represents lineage and runtime status.

Conclusion:

Thread has lifecycle semantics.

---

## F3. Thread contains Turns

Evidence:

```text
Thread.turns: Array<Turn>
```

Source:

`Thread.ts`

Conclusion:

Thread is a container for structured execution history, not only messages.

---

## F4. Turn contains ThreadItems

Evidence:

```text
Turn.items: Array<ThreadItem>
```

Source:

`Turn.ts`

Observed fields:

- status
- error
- startedAt
- completedAt
- durationMs

Conclusion:

A Turn represents a bounded execution unit with lifecycle information.

---

## F5. ThreadItem represents multiple execution events

Evidence:

`ThreadItem.ts` defines multiple item variants:

- userMessage
- agentMessage
- plan
- reasoning
- commandExecution
- fileChange
- mcpToolCall
- dynamicToolCall
- collabAgentToolCall
- subAgentActivity
- contextCompaction

Conclusion:

The runtime model is not message-only. It models heterogeneous execution events.

---

# Current Model

Verified model:

```text
Thread
 |
 +-- Turns
       |
       +-- ThreadItems
             |
             +-- Message
             +-- Reasoning
             +-- Tool Execution
             +-- File Change
             +-- Agent Collaboration
             +-- Context Events
```

---

# Inference

## I1. Thread is closer to an Agent Execution Context than a Chat Session

Reason:

- lifecycle fields exist;
- turns have execution timing;
- items represent tool and state events.

Confidence:

medium-high

Still requires:

- runtime implementation reading;
- persistence flow reading;
- recovery behavior validation.

---

# Not Verified

- How Thread state is persisted internally.
- Whether Thread is event-sourced.
- How recovery/replay works.
- Whether this model generalizes to all Agent frameworks.
- Whether Rustzen should adopt the same abstraction.

---

# Next Research

1. Read Rust Thread Manager implementation.
2. Verify creation/resume/fork lifecycle.
3. Analyze persistence and recovery.
4. Design minimal runtime experiment.
