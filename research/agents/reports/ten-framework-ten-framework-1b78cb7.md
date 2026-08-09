# TEN-framework/ten-framework agent assessment

- Fixed commit: `1b78cb725910d6f63389ef4ae69b182854d5b9d9`
- Content identity: `git-tree:7b33640de9aa26cebefcae7b6daebab2f8167a26`
- Default branch: `main`
- License: `Custom source-available license based on Apache-2.0 with additional deployment restrictions`
- Evidence: `source_validated`
- Subtype/topic fit: `realtime-multimodal-agent-framework`; `fit`
- Runtime execution: none

## Verified

- Repository identity, public/non-archived status, main default branch, and the requested fixed commit were verified; the commit resolves to Git tree 7b33640de9aa26cebefcae7b6daebab2f8167a26.
- License countercheck: the root LICENSE embeds Apache-2.0 but adds restrictions forbidding hosting on end-user devices and deployment that competes with Agora; it should not be represented as plain Apache-2.0.
- README claim: TEN presents itself as an open-source framework for low-latency real-time multimodal conversational AI, composed from interchangeable STT, LLM, TTS, memory, transport, and tool extensions.
- Source validation: the voice-assistant example defines a runtime graph of typed extensions and explicit cmd/data/audio connections; the main control extension receives ASR/user/tool-registration events and orchestrates LLM, TTS, transcript, and RTC flush paths.
- Source validation: Agent has separate ordered asyncio queues for ASR and LLM events, sequential callback dispatch, cancellable LLM handler tasks, and lifecycle stop that cancels consumers and the LLM executor.
- Source validation: LLMExec owns an in-memory message context, consumes queued user inputs, registers tools with a tool-name to source-extension map, sends chat_completion commands, dispatches tool_call commands to the registered source, appends function call/results, and recursively re-enters the LLM after a successful tool result.
- Source validation: model routing is extension-based. The inspected OpenAI LLM2 adapter translates TEN messages and tool metadata into an AsyncOpenAI request, supports configurable base_url/model/api_key, streams reasoning/text/tool-call events, and declares ten_ai_base and ten_runtime dependencies in its manifest.
- Permission-boundary countercheck: graph connections constrain which extensions exchange named commands/data, but the inspected Agent accepts tool_register and later routes model-selected calls without a human approval or per-call authorization policy.
- Source validation: interruption flushes queued input, sends an abort for the current LLM request, cancels the active task, flushes TTS and RTC, and stop cancels both consumer loops. Core extension APIs also expose configure/init/start/stop/deinit lifecycle hooks.
- Source validation and limitation: the example's conversation context is an in-memory list with no persistence or truncation in LLMExec; property.json sets max_memory_length on the LLM extension, but the dependency implementing ten_ai_base behavior is not present in this fixed tree, so enforcement was not established.
- Testing/CI source validation: AI Agents CI performs format, lint, extension tests, and Go server tests for selected examples; the task runner discovers every extension directory containing tests. The repository also has broad platform/core workflows and an extension tester API supporting single-extension and graph modes with timeouts.
- Fixed-commit feature evidence: the iFLYTEK ASR extension added at this commit includes committed offline tests for protocol frames, real local WebSocket transport, reconnection, stale-connection isolation, finalize behavior, errors, metrics, config, dumps, and result mapping.
- Security countercheck: OpenAIChatGPT logs the full config.api_key during initialization, which is a source-level credential-exposure risk if production logging is enabled.

## Inference

- TEN's agent boundary is best understood as a graph-orchestrated real-time extension pipeline rather than a single monolithic ReAct loop.
- Explicit graph wiring and tool-source routing provide structural isolation between extensions, but do not by themselves authorize model-selected side effects.
- Queueing, cancellation, abort, flush, lifecycle hooks, and extension-level reconnection form a credible recovery toolkit for real-time sessions, though crash durability and replay are not established.
- The breadth of committed workflows and extension tests suggests mature engineering practices, but the concrete voice-assistant main-control loop lacks direct committed tests in its own example directory.

## Not verified

- No build, format check, lint, unit test, extension test, ASR guarder, graph integration test, Docker image, Go server test, or live RTC/STT/LLM/TTS session was executed.
- README latency/quality claims, production scalability, audio quality, provider interoperability, and real iFLYTEK service validation were not independently verified.
- The ten_ai_base implementation used by LLM2 extensions is installed by the package manager and was not present in the inspected fixed tree; its memory limits, retries, and internal orchestration remain unverified.
- Durable checkpoints, process-crash recovery, replay semantics, exactly-once tool execution, tenant isolation, tool approvals, and secret redaction were not established.
- Release publishing semantics were not deeply inspected in this pass; repository workflows show build/test and manual extension publishing surfaces but no runtime result was checked.

## Limitations

- Static source review at one fixed commit only; runtime behavior was intentionally not executed.
- The monorepo is very large. Review focused on the representative voice-assistant graph, its OpenAI LLM adapter, core lifecycle/test APIs, the fixed commit's iFLYTEK tests, and CI orchestration rather than every extension/provider.
- Root LICENSE wording materially conflicts with a simple README badge interpretation; this report uses the text of LICENSE as controlling evidence.

## Evaluation

| Dimension | Score (1–5) |
| --- | ---: |
| `agent_boundary` | 4 |
| `context_and_state` | 3 |
| `tool_and_permission_boundary` | 2 |
| `stop_and_recovery` | 4 |
| `verification` | 4 |
| `concurrency_and_cost` | 3 |
| `production_readiness` | 3 |

Scores are comparative judgments derived from the fixed-source evidence above; they are not runtime benchmarks.

## Evidence URLs

- https://github.com/TEN-framework/ten-framework/commit/1b78cb725910d6f63389ef4ae69b182854d5b9d9
- https://github.com/TEN-framework/ten-framework/blob/1b78cb725910d6f63389ef4ae69b182854d5b9d9/LICENSE
- https://github.com/TEN-framework/ten-framework/blob/1b78cb725910d6f63389ef4ae69b182854d5b9d9/README.md
- https://github.com/TEN-framework/ten-framework/blob/1b78cb725910d6f63389ef4ae69b182854d5b9d9/ai_agents/agents/examples/voice-assistant/tenapp/property.json
- https://github.com/TEN-framework/ten-framework/blob/1b78cb725910d6f63389ef4ae69b182854d5b9d9/ai_agents/agents/examples/voice-assistant/tenapp/ten_packages/extension/main_python/agent/agent.py
- https://github.com/TEN-framework/ten-framework/blob/1b78cb725910d6f63389ef4ae69b182854d5b9d9/ai_agents/agents/examples/voice-assistant/tenapp/ten_packages/extension/main_python/agent/llm_exec.py
- https://github.com/TEN-framework/ten-framework/blob/1b78cb725910d6f63389ef4ae69b182854d5b9d9/ai_agents/agents/examples/voice-assistant/tenapp/ten_packages/extension/main_python/extension.py
- https://github.com/TEN-framework/ten-framework/blob/1b78cb725910d6f63389ef4ae69b182854d5b9d9/ai_agents/agents/ten_packages/extension/openai_llm2_python/openai.py
- https://github.com/TEN-framework/ten-framework/blob/1b78cb725910d6f63389ef4ae69b182854d5b9d9/.github/workflows/ai_agents.yaml
- https://github.com/TEN-framework/ten-framework/blob/1b78cb725910d6f63389ef4ae69b182854d5b9d9/ai_agents/Taskfile.yml
- https://github.com/TEN-framework/ten-framework/blob/1b78cb725910d6f63389ef4ae69b182854d5b9d9/ai_agents/agents/ten_packages/extension/iflytek_asr_python/tests/test_client.py
