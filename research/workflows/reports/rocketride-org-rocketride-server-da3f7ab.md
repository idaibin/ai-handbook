# rocketride-org/rocketride-server workflow assessment

- Fixed commit: `da3f7abdf61ce06ea5732df624fa9546e46bbd52`
- Content identity: `f3c4de9c9ea098bbc864162539a38e294e9c8546`
- Evidence: `source_validated`
- Subtype/topic fit: `bounded_parallel_wave_planning_agent`; `fit`
- Topic rationale: The primary reusable unit is an agent workflow that plans host-tool calls, executes them, records results, and replans or synthesizes an answer.
- Runtime execution: none

## Verified

- IInstance exposes the workflow both through a questions lane and as a parent-agent tool; its contract requires a non-empty string query and permits an optional object context.
- services.json declares max_waves with default 10 and range 1-50; RocketRideDriver loads it and rocketride_agent.py consumes it in for wave_num in range(self._max_waves). Empty plans terminate early and exhaustion falls through to synthesis.
- executor.py declares _MAX_WORKERS=8 and consumes it as min(_MAX_WORKERS, len(tagged)) for ThreadPoolExecutor; indexed result slots preserve planned order despite concurrent completion.
- require_tool_call is parsed into AgentBase._require_tool_call, actual host calls append to context.invoked_tools, and run_agent rejects completion when the list is empty. memory.peek is deliberately local and does not satisfy the guard; integration tests cover no-tool fabrication, memory.peek-only, serial, and parallel cases.
- Each call maintains waves, scratch state, trace data, and raw tool results in per-run memory; IGlobal constructs a shared driver described as stateless across runs.
- Tool exceptions are converted into structured error results that can be presented to a later planning wave; no automatic bounded retry loop was found in the inspected Wave implementation.
- The workflow emits planning, thought, running, and completion events, and returns trace/run metadata including run_id, waves, scratch state, timestamps, and tool-call count.
- The repository is MIT licensed and its CI definition includes cross-platform builds/tests on repository events, manual dispatch, and a weekly schedule.

## Inference

- A later wave can adapt to a failed tool result, but this is model-directed replanning rather than a declared retry policy and is not scored as retry control.
- The wave trace is useful for within-run diagnosis, but because inspected state is per-call memory it is unlikely to support process-crash resume without an external persistence layer.
- Parallel execution improves throughput for independent tools but can concurrently trigger external side effects whose ordering is not transactional.

## Not verified

- _TOOL_TIMEOUT_S=120 is declared and documented, but no consumption or timeout enforcement was found; the advertised tool timeout therefore receives no credit.
- No durable checkpoint, persisted run state, or restart/resume path was found for an interrupted wave run.
- No idempotency key, deduplication ledger, compensating transaction, or general side-effect classification was found for host-tool calls.
- No human approval gate or approval state transition was found in the inspected agent path.
- Strict schema validation for each model-produced tool-call object beyond argument coercion/error capture was not established.
- No code or tests were executed, and current CI status, deployment behavior, and branch protection were not checked.

## Limitations

- Read-only source review at the fixed commit; runtime services and external tool implementations were not exercised.
- The assessment is scoped to the RocketRide Wave agent and its shared AgentBase rather than every node and execution path in the monorepo.
- Only the listed key files were used for scoring.

## Evaluation

| Dimension | Score (1–5) |
| --- | ---: |
| `trigger_and_contract` | 4 |
| `state_and_resume` | 2 |
| `idempotency` | 1 |
| `side_effect_control` | 2 |
| `human_gate` | 1 |
| `observability` | 4 |
| `validation` | 4 |
| `reuse_value` | 4 |

Scores are comparative judgments derived from fixed-source evidence, not runtime benchmarks.

## Files read

- `README.md`
- `LICENSE`
- `nodes/src/nodes/agent_rocketride/README.md`
- `nodes/src/nodes/agent_rocketride/services.json`
- `nodes/src/nodes/agent_rocketride/IInstance.py`
- `nodes/src/nodes/agent_rocketride/IGlobal.py`
- `nodes/src/nodes/agent_rocketride/rocketride_agent.py`
- `nodes/src/nodes/agent_rocketride/planner.py`
- `nodes/src/nodes/agent_rocketride/executor.py`
- `packages/ai/src/ai/common/agent/agent.py`
- `packages/ai/tests/ai/common/agent/test_require_tool_call_integration.py`
- `.github/workflows/ci.yml`

## Evidence URLs

- https://github.com/rocketride-org/rocketride-server/tree/da3f7abdf61ce06ea5732df624fa9546e46bbd52
- https://github.com/rocketride-org/rocketride-server/blob/da3f7abdf61ce06ea5732df624fa9546e46bbd52/nodes/src/nodes/agent_rocketride/services.json
- https://github.com/rocketride-org/rocketride-server/blob/da3f7abdf61ce06ea5732df624fa9546e46bbd52/nodes/src/nodes/agent_rocketride/rocketride_agent.py
- https://github.com/rocketride-org/rocketride-server/blob/da3f7abdf61ce06ea5732df624fa9546e46bbd52/nodes/src/nodes/agent_rocketride/executor.py
- https://github.com/rocketride-org/rocketride-server/blob/da3f7abdf61ce06ea5732df624fa9546e46bbd52/packages/ai/src/ai/common/agent/agent.py
- https://github.com/rocketride-org/rocketride-server/blob/da3f7abdf61ce06ea5732df624fa9546e46bbd52/packages/ai/tests/ai/common/agent/test_require_tool_call_integration.py
- https://github.com/rocketride-org/rocketride-server/blob/da3f7abdf61ce06ea5732df624fa9546e46bbd52/.github/workflows/ci.yml
