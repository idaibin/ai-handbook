# trpc-group/trpc-agent-go workflow assessment

- Fixed commit: `c6988c7ef0d511a656301121b011a3105d6ea784`
- Content identity: `git-tree:9ad51d7bc26700a6c0d71a24cfa2dbdd123da4ff`
- Evidence: `source_validated`
- Subtype/topic fit: `checkpointed interruptible Pregel-style agent graph runtime`; `strong_fit`
- Runtime execution: none

## Verified

- The project identifies GraphAgent as a type-safe graph workflow system with conditional routing and production observability, and names human-in-the-loop business processes as a use case.
- StateGraph is the primary builder contract: callers define a state schema, add nodes and edges, set entry and finish points, compile the graph, and pass it to an Executor.
- Executor uses a Pregel-style bulk-synchronous execution engine by default and keeps per-run mutable state in ExecutionContext so one executor can be shared across concurrent invocations.
- The checkpoint contract persists channel values and versions, next nodes, tasks, pending writes, parent relationships, resume metadata, and deterministic pending-write sequence numbers.
- CheckpointSaver supports read, list, checkpoint writes, intermediate writes, an atomic PutFull operation for checkpoint plus pending writes, lineage deletion, and close.
- Interrupt emits an InterruptError carrying prompt, key/task, node, step, timestamp, path, rerun policy, and optional next-node frontier; ResumeCommand supplies either a single resume value or a keyed resume map.
- Resume consumption is one-shot, while used interrupt values are cached in state so re-executing the same interrupted node returns the same value rather than consuming or requesting another value.
- RetryPolicy is configurable per node or executor with maximum attempts, exponential backoff, jitter, elapsed-time budget, per-attempt timeout, and explicit error predicates; no retry occurs when no condition matches.
- The runtime emits typed graph, node, Pregel-step, channel/state-update, checkpoint, tool, and interrupt events and instruments workflow/model/tool execution with OpenTelemetry spans and error status.
- Source tests cover checkpoint creation and event gating, checkpoint storage failures and saver panics, retry success with downstream exactly once, absence of retry without policy, barrier coordination, and interrupt/resume value reuse.

## Inference

- The subtype follows directly from the Pregel executor, graph builder, checkpoint/pending-write model, and first-class interrupt/resume protocol.
- Deterministic write sequencing, atomic saver capability, and reused interrupt values support replay safety, but they do not make arbitrary user node or tool side effects exactly-once.
- Human approval can be modeled by interrupting with a prompt and resuming with a decision, but the library does not itself provide reviewer assignment, authorization, deadlines, or an approval inbox.
- The public builder/options and storage interface make the workflow engine highly reusable across applications and saver implementations.

## Not verified

- Not verified: durability and transactional behavior of any concrete checkpoint backend under process crash or network partition.
- Not verified: exactly-once execution for external tools or arbitrary node functions during retry, replay, or resume.
- Not verified: a production human-approval UI, reviewer identity/authorization, escalation, or timeout policy.
- Not verified: end-to-end execution, benchmark results, test results, and current CI status at the fixed commit.
- Not verified: compatibility guarantees for serialized checkpoints across library versions.

## Limitations

- Read-only review of 12 selected files at the exact commit; no Go tests, examples, checkpoint stores, or workflows were executed.
- Evidence level is capped at source_validated; scores use 1 (weak/not present in sampled evidence) through 5 (strong source evidence).
- Concrete saver implementations and integrations were intentionally outside the file budget.

## Evaluation

| Dimension | Score (1–5) |
| --- | ---: |
| `trigger_and_contract` | 5 |
| `state_and_resume` | 5 |
| `idempotency` | 4 |
| `side_effect_control` | 3 |
| `human_gate` | 4 |
| `observability` | 5 |
| `validation` | 5 |
| `reuse_value` | 5 |

Scores are comparative judgments derived from fixed-source evidence, not runtime benchmarks.

## Evidence URLs

- https://github.com/trpc-group/trpc-agent-go/blob/c6988c7ef0d511a656301121b011a3105d6ea784/README.md#L28-L54
- https://github.com/trpc-group/trpc-agent-go/blob/c6988c7ef0d511a656301121b011a3105d6ea784/graph/state_graph.go#L55-L87
- https://github.com/trpc-group/trpc-agent-go/blob/c6988c7ef0d511a656301121b011a3105d6ea784/graph/state_graph.go#L631-L1059
- https://github.com/trpc-group/trpc-agent-go/blob/c6988c7ef0d511a656301121b011a3105d6ea784/graph/executor.go#L47-L88
- https://github.com/trpc-group/trpc-agent-go/blob/c6988c7ef0d511a656301121b011a3105d6ea784/graph/checkpoint.go#L100-L190
- https://github.com/trpc-group/trpc-agent-go/blob/c6988c7ef0d511a656301121b011a3105d6ea784/graph/resume.go#L16-L60
- https://github.com/trpc-group/trpc-agent-go/blob/c6988c7ef0d511a656301121b011a3105d6ea784/graph/interrupt.go#L18-L99
- https://github.com/trpc-group/trpc-agent-go/blob/c6988c7ef0d511a656301121b011a3105d6ea784/graph/retry.go#L22-L162
- https://github.com/trpc-group/trpc-agent-go/blob/c6988c7ef0d511a656301121b011a3105d6ea784/graph/events.go#L22-L60
- https://github.com/trpc-group/trpc-agent-go/blob/c6988c7ef0d511a656301121b011a3105d6ea784/graph/retry_test.go#L26-L80
- https://github.com/trpc-group/trpc-agent-go/blob/c6988c7ef0d511a656301121b011a3105d6ea784/graph/interrupt_test.go#L81-L100
