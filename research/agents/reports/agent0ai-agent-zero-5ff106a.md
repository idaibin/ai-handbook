# agent0ai/agent-zero agent assessment

- Fixed commit: `5ff106a2d489d17c2a3b378521a8f29fb29cf77d`
- Content identity: `5ff106a2d489d17c2a3b378521a8f29fb29cf77d:README=5596007d11e9e827f87f5307ad0d6b31439214c0;agent=62beb8bc149267d5720586ddd4695f2b679fd172;models=e1fa5c42304fb46f6bb092011cb9dd48fb2edca8;history=f0ee4c0df9f485a9c8ff32e78858d0187bf4d063;response=9e2532b5b75cc4233a8973063eb75a1af2153d29`
- Default branch: `main`
- License: `MIT`
- Evidence: `source_validated`
- Subtype/topic fit: `general-computer-agent`; `fit`
- Runtime execution: none

## Verified

- README presents Agent Zero as a Dockerized full-computer agent framework with projects, project-isolated memory/secrets/settings, skills/plugins, host bridge, and subordinate-agent cooperation.
- The primary loop is Agent.monologue(): nested while-true loops build a prompt, call the configured chat model, parse native/function or JSON tool requests, execute them, append history, and return only when a tool response has break_loop=true.
- Model and tool routing are explicit: model configuration flows into unified_turn/LiteLLMTransport; tool lookup prefers configured MCP tools and falls back to local tool classes discovered through the agent/profile hierarchy.
- Context/state are separated into AgentContext (context registry, task, pause, data/output_data, log), per-Agent History with topic/bulk compression, Responses API state, and an optional memory plugin that recalls and writes vector-backed memories.
- Subordinate delegation constructs a child Agent sharing the parent AgentContext, stores superior/subordinate links, runs the child monologue, seals the child history topic, and returns its report to the superior.
- Parallel work is an explicit tool: jobs use isolated child/background contexts, support await/collect/cancel, reject nested parallel direct workers, and disallow response/document_query inside the wrapper; native Responses parallel tool calls are disabled by default and mapped into this controlled wrapper.
- Stop behavior is tool-driven: ResponseTool validates nonempty text and returns break_loop=true. The default consecutive malformed/repeated-output circuit breaker is 5 at this commit. User pause/intervention and task kill paths are also present.
- Failure handling includes extension hooks, repairable tool errors fed back into history, transient model-call retries only before any streamed chunk (default 2 retries, 1.5 seconds), and a cost circuit breaker for unusable outputs. The outer monologue otherwise has no general iteration cap in the inspected core loop.
- Tool execution invokes local or MCP tools directly after schema normalization and before/after hooks. No repository-wide, default human approval gate comparable to per-tool approval_mode was found in the inspected core path; isolation is primarily deployment/project/context based.
- The tree contains 125 test_*.py files covering model routing, parallel work, prompt protocol, retry, memory, security and UI contracts. The only root GitHub build/release workflow inspected is Docker publishing/release creation; no general pytest CI workflow is present at this commit.

## Inference

- The framework is optimized for a persistent, inspectable autonomous workspace rather than a narrowly bounded request/response SDK.
- Project/container isolation reduces blast radius, but host-bridge or broad shell/browser capabilities require deployment-level policy because the core execution path does not enforce universal per-call approval.
- The explicit parallel wrapper improves observability and recursion control, but cost remains configuration- and prompt-dependent because the main loop has no overall default turn budget.

## Not verified

- No tests, Docker image, browser, model provider, MCP server, memory backend, Time Travel operation, or host connector was executed.
- No live CI status, release artifact integrity, image signing/SBOM, benchmark quality, latency, token cost, or production incident history was verified.
- README claims such as 100+ plugins, hardware/platform compatibility, and practical project isolation were not independently exercised.
- A complete permission/security audit of every built-in tool, plugin, Web UI endpoint, connector and secret path was out of scope.

## Limitations

- Static inspection was concentrated on the Python orchestration core and representative tests/plugins at the fixed commit.
- GitHub owner/name/default branch/archive metadata is a current API observation, while behavior findings are pinned to the fixed commit.
- Without execution, the maximum defensible evidence level is source_validated.

## Evaluation

| Dimension | Score (1–5) |
| --- | ---: |
| `agent_boundary` | 4 |
| `context_and_state` | 4 |
| `tool_and_permission_boundary` | 2 |
| `stop_and_recovery` | 3 |
| `verification` | 3 |
| `concurrency_and_cost` | 4 |
| `production_readiness` | 3 |

Scores are comparative judgments derived from the fixed-source evidence above; they are not runtime benchmarks.

## Evidence URLs

- https://github.com/agent0ai/agent-zero/tree/5ff106a2d489d17c2a3b378521a8f29fb29cf77d
- https://github.com/agent0ai/agent-zero/blob/5ff106a2d489d17c2a3b378521a8f29fb29cf77d/README.md
- https://github.com/agent0ai/agent-zero/blob/5ff106a2d489d17c2a3b378521a8f29fb29cf77d/agent.py
- https://github.com/agent0ai/agent-zero/blob/5ff106a2d489d17c2a3b378521a8f29fb29cf77d/models.py
- https://github.com/agent0ai/agent-zero/blob/5ff106a2d489d17c2a3b378521a8f29fb29cf77d/helpers/parallel_tools.py
- https://github.com/agent0ai/agent-zero/blob/5ff106a2d489d17c2a3b378521a8f29fb29cf77d/tools/response.py
- https://github.com/agent0ai/agent-zero/blob/5ff106a2d489d17c2a3b378521a8f29fb29cf77d/tests/test_unusable_response_loop.py
- https://api.github.com/repos/agent0ai/agent-zero
