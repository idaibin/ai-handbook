# nanobrowser/nanobrowser workflow assessment

- Fixed commit: `322384f8b4d48d8614343e51efca68c85e64f90b`
- Tree/content: `git-tree:46b20cf51f29ec5468fb68f20488b3b22dc836d9`
- Observed: 13,540 Stars; `master`; not forked or archived
- License: Apache-2.0
- Evidence: `source_validated`; runtime not validated
- Subtype/topic fit: `in-memory-agent-control-loop`; fit, not durable

## Verified

A same-extension side-panel connection sends `new_task`, follow-up, pause, resume, cancel or replay messages to a background executor. A Planner iterates with a Navigator; Navigator completion is rechecked by Planner. Defaults bound execution to 100 steps, three failures and periodic planning. Task/step/action events record start, success, failure, pause, resume and cancel.

Pause is an in-memory flag and there is no live-task durable checkpoint. Optional history can replay browser actions with element-index correction and per-step retry. Effects include navigation, clicks, text input, keys and tab changes. No idempotency key or side-effect classification was found, so replay can duplicate submissions. Sensitive-action approval exists in prompt text; action registration does not enforce an approval-required state. Manual pause/cancel is not an action-level gate.

## Inference

This is an executable bounded agent loop with optional replay, not a recoverable workflow runtime. Prompt-only approval is a meaningful safety weakness for browser side effects.

## Not verified

The extension, browser, models, replay reliability, sensitive-action blocking, builds and tests were not run. Only a guardrail unit-test file, not executor workflow tests, was found.

Evidence: [entry](https://github.com/nanobrowser/nanobrowser/blob/322384f8b4d48d8614343e51efca68c85e64f90b/chrome-extension/src/background/index.ts), [executor](https://github.com/nanobrowser/nanobrowser/blob/322384f8b4d48d8614343e51efca68c85e64f90b/chrome-extension/src/background/agent/executor.ts), [navigator](https://github.com/nanobrowser/nanobrowser/blob/322384f8b4d48d8614343e51efca68c85e64f90b/chrome-extension/src/background/agent/agents/navigator.ts).
