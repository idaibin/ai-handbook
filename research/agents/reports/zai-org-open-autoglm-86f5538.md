# zai-org/Open-AutoGLM agent assessment

- Fixed commit: `86f55382982fb054e8fc98ca80609dff8a2cdc3c`
- Content identity: `git-tree:8ee1217deb8a7efe257747efd644aa9e20f89180`
- Default branch: `main`
- License: `Apache-2.0`
- Evidence: `source_validated`
- Subtype/topic fit: `mobile-gui-agent`; `conditional_fit`
- Runtime execution: none

## Verified

- Repository identity, public/non-archived status, main default branch, and the requested fixed commit were verified; the commit resolves to Git tree 8ee1217deb8a7efe257747efd644aa9e20f89180.
- The repository LICENSE is the unmodified Apache License 2.0 text, and setup.py classifies the package as Apache-licensed.
- README claim: Phone Agent is described as a multimodal mobile assistant using ADB/HDC/iOS device control, a vision-language model, sensitive-operation confirmation, and manual takeover.
- Source validation: PhoneAgent.run implements a screenshot-and-current-app observation loop, sends each observation to an OpenAI-compatible model, parses one action, executes it, appends the assistant response, and repeats until finish or max_steps (default 100).
- Source validation: model routing is a single configurable OpenAI-compatible client (base_url, api_key, model_name), while action routing is a fixed allowlist of Launch, Tap, Type, Swipe, Back, Home, Double Tap, Long Press, Wait, Take_over, Note, Call_API, and Interact handlers.
- Source validation: conversation state is process-local self._context plus a step counter; prior screenshots are removed after each step while textual observations and assistant responses remain. No checkpoint or durable memory store appears in the inspected core path.
- Source validation: do(...) output is parsed with Python AST plus ast.literal_eval rather than eval, and only names in the fixed handler map can dispatch device actions.
- Source validation and countercheck: sensitive confirmation is enforced only for Tap actions containing a model-supplied message field; the Chinese prompt tells the model to add this field for financial/payment/privacy taps, but the English prompt does not define that convention.
- Source validation and countercheck: Android screenshot capture can mark a fallback image is_sensitive=True, but PhoneAgent._execute_step does not inspect that flag before calling the model; therefore the README statement that sensitive black screens automatically request takeover is not established by this core path.
- Source validation: stop paths include explicit finish, user cancellation of a confirmed sensitive Tap, model/parse exceptions converted to terminal results, and the max_steps bound. Prompt-level recovery asks the model to wait, adjust coordinates, retry navigation, or finish after repeated search failure.
- Countercheck: README documents pytest tests/, but this fixed tree contains no tests directory and no GitHub Actions workflow; only issue/PR templates are present under .github.
- Release/readiness clue: setup.py labels version 0.1.0 and Development Status Alpha, provides a console entry point, and has a placeholder project URL rather than the canonical repository URL.

## Inference

- This is a clear single-agent perception/action loop, but its state model is session-local and its reliability depends heavily on model compliance with the prompt.
- The AST parser and fixed handler map reduce arbitrary-code execution risk, but they do not constitute a permission policy for device side effects.
- Because confirmation depends on a model-authored message field and only gates Tap, the advertised sensitive-operation mechanism is weaker and narrower than a deterministic policy engine.
- Absence of committed tests and CI at this revision materially lowers confidence in regressions, cross-device behavior, and the README's broader platform claims.

## Not verified

- No package installation, import, unit test, CLI command, model request, ADB/HDC/XCTest connection, screenshot, or device action was executed.
- The accuracy of screen understanding, planning, coordinate selection, supported-app mappings, and end-to-end task completion was not verified.
- Automatic takeover on sensitive screens was not verified and is not wired in the inspected Android core loop.
- iOS and HarmonyOS parity, remote ADB security, credential handling, and behavior on real payment/login/captcha pages were not validated.
- No benchmark/eval harness, durable recovery, concurrent-session isolation, usage/cost budget, release automation, or published package provenance was established.

## Limitations

- Static source review at one fixed commit only; runtime behavior was intentionally not executed.
- The iOS agent is structurally parallel to the Android agent but was not read line-by-line to the same depth.
- README statements are treated as claims unless the corresponding implementation path was directly inspected.

## Evaluation

| Dimension | Score (1–5) |
| --- | ---: |
| `agent_boundary` | 4 |
| `context_and_state` | 2 |
| `tool_and_permission_boundary` | 2 |
| `stop_and_recovery` | 3 |
| `verification` | 1 |
| `concurrency_and_cost` | 2 |
| `production_readiness` | 2 |

Scores are comparative judgments derived from the fixed-source evidence above; they are not runtime benchmarks.

## Evidence URLs

- https://github.com/zai-org/Open-AutoGLM/commit/86f55382982fb054e8fc98ca80609dff8a2cdc3c
- https://github.com/zai-org/Open-AutoGLM/blob/86f55382982fb054e8fc98ca80609dff8a2cdc3c/README_en.md
- https://github.com/zai-org/Open-AutoGLM/blob/86f55382982fb054e8fc98ca80609dff8a2cdc3c/LICENSE
- https://github.com/zai-org/Open-AutoGLM/blob/86f55382982fb054e8fc98ca80609dff8a2cdc3c/phone_agent/agent.py
- https://github.com/zai-org/Open-AutoGLM/blob/86f55382982fb054e8fc98ca80609dff8a2cdc3c/phone_agent/actions/handler.py
- https://github.com/zai-org/Open-AutoGLM/blob/86f55382982fb054e8fc98ca80609dff8a2cdc3c/phone_agent/model/client.py
- https://github.com/zai-org/Open-AutoGLM/blob/86f55382982fb054e8fc98ca80609dff8a2cdc3c/phone_agent/adb/screenshot.py
- https://github.com/zai-org/Open-AutoGLM/blob/86f55382982fb054e8fc98ca80609dff8a2cdc3c/phone_agent/config/prompts_en.py
- https://github.com/zai-org/Open-AutoGLM/blob/86f55382982fb054e8fc98ca80609dff8a2cdc3c/setup.py
