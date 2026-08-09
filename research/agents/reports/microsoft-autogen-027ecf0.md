# microsoft/autogen agent assessment

- Fixed commit: `027ecf0a379bcc1d09956d46d12d44a3ad9cee14`
- Content identity: `027ecf0a379bcc1d09956d46d12d44a3ad9cee14:README=25f7cc162ae92c3988966d85cce173ff6df48020;assistant=8b8316fb0a7c04d32165dd0cf76d914aa00fed08;team=60f222912387d37be37f457ad486d51060255966;termination=f0ba274ebe721bfe6601aad2340ef71b06cea565;runtime=3a8a8d714ff0a214f224b4b9c8fc2ff2ec3d1f18`
- Default branch: `main`
- License: `CC-BY-4.0`
- Evidence: `source_validated`
- Subtype/topic fit: `multi-agent-runtime`; `fit`
- Runtime execution: none

## Verified

- README describes Core (event-driven local/distributed runtime), AgentChat (opinionated high-level agents/teams), Extensions (providers/tools), Studio and Bench, while explicitly warning that AutoGen is in maintenance mode, community-managed, and not recommended for new projects.
- AssistantAgent is the main high-level loop entry: it adds incoming messages to a configurable ChatCompletionContext, lets Memory providers update context, gets model output, executes requested workbench tools, feeds results back, and optionally reflects for a final answer.
- Tool routing is explicit through model-client FunctionCall outputs and one or more Workbench instances. Multiple calls are executed concurrently with asyncio.gather; provider-level parallel_tool_calls must be disabled to force serial calls.
- AssistantAgent max_tool_iterations defaults to 1 and must be at least 1. It stops early when the model returns text, stops at the configured tool-iteration cap, or performs one extra reflection inference when enabled.
- Context/state are first-class: unbounded, buffered and token-limited model contexts exist; memories inject retrieved content; AssistantAgent save/load persists model context; Workbench tools can save/load state; teams save/load each participant and manager through AgentRuntime.
- Group-chat teams register participants and a manager on an AgentRuntime, use topic subscriptions and an output queue, and default to an embedded SingleThreadedAgentRuntime with unhandled background exceptions surfaced for the team.
- Team stop conditions are composable and include stop-message, max-message, text-mention, token-usage, timeout, handoff, external, source-match, text-message and function-call conditions; max_turns is a separate optional cap. Graceful external termination is distinguished from cancellation, which may leave inconsistent state.
- Runtime failures are propagated through futures; the embedded team runtime is configured not to ignore background handler exceptions. CancellationToken links to pending futures. CodeExecutorAgent has an optional model-guided retry loop, defaulting to zero retries.
- The inspected generic AssistantAgent/Workbench path exposes no framework-wide per-tool human approval mode. Human participation is modeled through UserProxy/Handoff/ExternalTermination/intervention patterns, and README warns to connect only trusted MCP servers. Sandbox/permission characteristics depend on the selected executor or extension.
- Verification/release artifacts remain substantial: 53 Python test files and roughly 106 .NET test source files were enumerated, with Python package checks/integration/coverage, memory backend jobs, .NET multi-platform unit/integration/AOT jobs, CodeQL, docs and Python/.NET publishing workflows.

## Inference

- AutoGen still has a mature separation between event runtime, chat agents, teams, model contexts, memories and workbenches, but its maintenance-mode status materially lowers suitability for greenfield production adoption.
- Cost and liveness controls are good when users configure max_tool_iterations, max_turns or a termination condition; a team can remain open-ended when neither team cap nor termination is supplied.
- Tool safety is extension-specific: a Workbench is a capability boundary, but generic execution does not itself require approval, so trusted-tool composition and sandbox selection are application responsibilities.

## Not verified

- No tests, model providers, distributed runtime/gateway, MCP workbench, code executor, Docker sandbox, memory provider, Studio UI, Bench evaluation, or pause/resume scenario was run.
- No live CI status, actual coverage, package vulnerability posture, benchmark accuracy, API compatibility, release cadence or migration completeness to Microsoft Agent Framework was independently verified.
- README statements about stable release availability and cross-language/distributed behavior were not exercised.
- A complete audit of every extension/provider/executor and the legacy 0.2/.NET surfaces was out of scope.

## Limitations

- Behavioral validation focuses on the current Python AgentChat/Core path at the fixed commit; the repository also contains legacy and .NET implementations.
- Repository archive=false is not equivalent to active feature development; the fixed README explicitly declares maintenance mode.
- Without execution, the maximum defensible evidence level is source_validated.

## Evaluation

| Dimension | Score (1–5) |
| --- | ---: |
| `agent_boundary` | 4 |
| `context_and_state` | 4 |
| `tool_and_permission_boundary` | 2 |
| `stop_and_recovery` | 4 |
| `verification` | 4 |
| `concurrency_and_cost` | 4 |
| `production_readiness` | 2 |

Scores are comparative judgments derived from the fixed-source evidence above; they are not runtime benchmarks.

## Evidence URLs

- https://github.com/microsoft/autogen/tree/027ecf0a379bcc1d09956d46d12d44a3ad9cee14
- https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/README.md
- https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/python/packages/autogen-agentchat/src/autogen_agentchat/agents/_assistant_agent.py
- https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_base_group_chat.py
- https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/python/packages/autogen-agentchat/src/autogen_agentchat/conditions/_terminations.py
- https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/python/packages/autogen-core/src/autogen_core/_single_threaded_agent_runtime.py
- https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/python/packages/autogen-agentchat/tests/test_assistant_agent.py
- https://github.com/microsoft/autogen/blob/027ecf0a379bcc1d09956d46d12d44a3ad9cee14/.github/workflows/checks.yml
- https://api.github.com/repos/microsoft/autogen
