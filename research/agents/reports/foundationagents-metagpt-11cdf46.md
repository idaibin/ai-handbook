# FoundationAgents/MetaGPT agent assessment

- Fixed commit: `11cdf466d042aece04fc6cfd13b28e1a70341b1f`
- Content identity: `commit:11cdf466d042aece04fc6cfd13b28e1a70341b1f:keyblobs:080c02cd-49b1d178-5dbadf9c-03a4760c`
- Default branch: `main`
- License: `MIT`
- Evidence: `source_validated`
- Subtype/topic fit: `role-based-multi-agent-framework`; `fit`
- Runtime execution: none

## Verified

- Agent boundary is implemented as Role observe/think/act execution, with REACT, BY_ORDER, and PLAN_AND_ACT modes.
- The ReAct loop has an explicit max_react_loop bound and exits when _think returns false.
- Role-local message buffers and Memory storage/index implement context capture and duplicate filtering.
- Environment routes messages and runs non-idle roles concurrently with asyncio.gather.
- Actions resolve configured LLM providers and a ToolRegistry registers and looks up tools and schemas.
- LLM completion retries ConnectionError up to three attempts with randomized exponential wait, and tracks token costs when enabled.
- Targeted unit tests cover recovered-role observation and basic memory add/delete/query behavior.

## Inference

- The combination of bounded role loops, idle detection, retry, and recovered-role state provides a credible recovery model, but durability across process crashes depends on higher-level persistence not established by these files.
- Tool registration is structurally clear, but authorization and sandbox policy are not centralized in the inspected registry.

## Not verified

- No tests, build, example, or end-to-end multi-agent workflow was executed.
- Provider credentials, external tool side effects, sandboxing, permission prompts, and tenant isolation were not validated.
- Exactly-once delivery, durable checkpoints across process crashes, and distributed concurrency semantics were not established.
- CI workflow paths and release behavior were not confirmed in this pass.

## Limitations

- Static source review at one fixed commit only.
- The repository is large; optional providers, specialized roles, RFC documents, and production deployment paths were not exhaustively read.

## Evaluation

| Dimension | Score (1–5) |
| --- | ---: |
| `agent_boundary` | 5 |
| `context_and_state` | 4 |
| `tool_and_permission_boundary` | 3 |
| `stop_and_recovery` | 4 |
| `verification` | 3 |
| `concurrency_and_cost` | 4 |
| `production_readiness` | 3 |

Scores are comparative judgments derived from the fixed-source evidence above; they are not runtime benchmarks.

## Evidence URLs

- https://github.com/FoundationAgents/MetaGPT/commit/11cdf466d042aece04fc6cfd13b28e1a70341b1f
- https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/metagpt/roles/role.py
- https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/metagpt/memory/memory.py
- https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/metagpt/environment/base_env.py
- https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/metagpt/provider/base_llm.py
- https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/tests/metagpt/roles/test_role.py
- https://github.com/FoundationAgents/MetaGPT/blob/11cdf466d042aece04fc6cfd13b28e1a70341b1f/tests/metagpt/memory/test_memory.py
