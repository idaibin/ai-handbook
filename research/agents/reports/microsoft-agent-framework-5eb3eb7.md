# microsoft/agent-framework agent assessment

- Fixed commit: `5eb3eb745e16324ac7bffb1dbe006d8f13c8d993`
- Content identity: `5eb3eb745e16324ac7bffb1dbe006d8f13c8d993:README=c26c8c90dff27725b6d203ca537f84344e043621;agents=05606d0a5fc47aa09daee42e5523eca2a9a0a333;tools=e7760c9cbdf2513bd48fe4a9477ea22aeaa33afd;sessions=893bb96e52604b5f2ed99cc8514e55a0e3a11de3;checkpoint=2b267979e996a7c855aac4a61aff99ad08567005`
- Default branch: `main`
- License: `MIT`
- Evidence: `source_validated`
- Subtype/topic fit: `multi-agent-runtime`; `strong_fit`
- Runtime execution: none

## Verified

- README calls Microsoft Agent Framework a production-grade .NET/Python framework and claims sequential, concurrent, handoff and group workflows with checkpointing, streaming, human-in-the-loop, time travel, observability and provider flexibility.
- Agent boundaries are protocol-first: SupportsAgentRun defines run/session behavior; Agent owns name/instructions/client/tools/middleware while provider clients own model-specific requests. Delegation exposes another agent as a sanitized function tool.
- The standard Agent.run pipeline normalizes messages, runs context/history providers and middleware, calls the selected chat client, and persists the response through session/history gates. AgentLoopMiddleware optionally re-invokes the agent until a predicate or judge says stop.
- The automatic tool loop is bounded by default: max_iterations=40 LLM roundtrips, max_consecutive_errors_per_request=3, with optional max_function_calls. The source documents max_function_calls as best-effort because a parallel batch can exceed the limit before the post-batch check.
- Multiple tool calls are executed concurrently with copied contextvars and asyncio.gather. Concurrent, sequential, handoff, group-chat and Magentic orchestration builders are separate workflow layers.
- FunctionTool has per-tool approval_mode (never_require by default, always_require opt-in). Mixed batches pause before execution when approval is required; requests/responses are persisted in AgentSession state and the outer loop exits rather than bypassing approval. Declaration-only tools also become user-input pauses.
- Context/state support is broad: AgentSession has typed state and service session IDs; in-memory/file history and session stores persist messages/snapshots; compaction and context providers shape model input. File identifiers are safely encoded for portable filenames.
- Workflow checkpoints include lineage, iteration, executor states and pending requests. In-memory and atomic file stores exist; file paths are constrained to the storage root and deserialization restricts types unless explicitly allowlisted.
- Stop/recovery controls include loop predicates/judges, default 10 work-loop cap (judge default 5), middleware termination, approval escape, function-call/error budgets, cancellation, workflow idle/pending-request states, checkpoint restore, and orchestration retry knobs. Explicit None can opt into unbounded harness loops.
- Verification/release signals are extensive: 74 Python test files and roughly 630 .NET test source files were enumerated, with Python unit/integration/coverage/sample/type checks, .NET build/test/coverage matrices, CodeQL, and release-triggered package publishing workflows.

## Inference

- Among the three repositories, this has the clearest separation between model adapters, agent abstraction, tool policy, durable session state and graph workflow execution.
- Production readiness is strengthened by explicit budgets, approval pauses, checkpoint safety controls, telemetry and broad CI, but safe defaults still depend on tool authors opting into approval and applications setting a total function-call budget.
- The high-level Agent API is intentionally thinner than the workflow/harness layers; autonomous continuation is composed through middleware or workflow orchestration rather than hardwired into every agent call.

## Not verified

- No Python/.NET tests, samples, package builds, checkpoints, hosted agents, model providers, MCP/A2A servers, telemetry exporters, or deployment targets were executed.
- No live CI conclusion, coverage percentage, signed package provenance, benchmark score, release SLA, API compatibility guarantee, or cloud durability behavior was independently verified.
- The README's production-grade and time-travel claims were not validated under fault injection or real multi-process/cloud conditions.
- The .NET implementation was sampled through its source layout and CI signals but the detailed behavioral findings emphasize the Python implementation.

## Limitations

- This is static source validation at one fixed commit in a large multi-language monorepo.
- Test-file counts are repository enumeration signals, not proof of test pass rate or behavioral coverage.
- GitHub metadata is current API state; source conclusions are fixed-commit state; without execution the evidence level cannot exceed source_validated.

## Evaluation

| Dimension | Score (1–5) |
| --- | ---: |
| `agent_boundary` | 5 |
| `context_and_state` | 5 |
| `tool_and_permission_boundary` | 4 |
| `stop_and_recovery` | 5 |
| `verification` | 5 |
| `concurrency_and_cost` | 5 |
| `production_readiness` | 5 |

Scores are comparative judgments derived from the fixed-source evidence above; they are not runtime benchmarks.

## Evidence URLs

- https://github.com/microsoft/agent-framework/tree/5eb3eb745e16324ac7bffb1dbe006d8f13c8d993
- https://github.com/microsoft/agent-framework/blob/5eb3eb745e16324ac7bffb1dbe006d8f13c8d993/README.md
- https://github.com/microsoft/agent-framework/blob/5eb3eb745e16324ac7bffb1dbe006d8f13c8d993/python/packages/core/agent_framework/_agents.py
- https://github.com/microsoft/agent-framework/blob/5eb3eb745e16324ac7bffb1dbe006d8f13c8d993/python/packages/core/agent_framework/_tools.py
- https://github.com/microsoft/agent-framework/blob/5eb3eb745e16324ac7bffb1dbe006d8f13c8d993/python/packages/core/agent_framework/_sessions.py
- https://github.com/microsoft/agent-framework/blob/5eb3eb745e16324ac7bffb1dbe006d8f13c8d993/python/packages/core/agent_framework/_harness/_loop.py
- https://github.com/microsoft/agent-framework/blob/5eb3eb745e16324ac7bffb1dbe006d8f13c8d993/python/packages/core/agent_framework/_workflows/_checkpoint.py
- https://github.com/microsoft/agent-framework/blob/5eb3eb745e16324ac7bffb1dbe006d8f13c8d993/.github/workflows/python-tests.yml
- https://github.com/microsoft/agent-framework/blob/5eb3eb745e16324ac7bffb1dbe006d8f13c8d993/.github/workflows/dotnet-build-and-test.yml
- https://api.github.com/repos/microsoft/agent-framework
