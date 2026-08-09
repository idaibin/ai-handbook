# moazbuilds/CodeMachine-CLI workflow assessment

- Fixed commit: `572def63eb808e95b18ccf6c69a13d7a13fe06fd`
- Content identity: `github:moazbuilds/CodeMachine-CLI@572def63eb808e95b18ccf6c69a13d7a13fe06fd`
- Evidence: `source_validated`
- Subtype/topic fit: `resumable_interactive_multi_agent_cli_state_machine`; `fit`
- Runtime execution: none

## Verified

- The workflow definition is JavaScript: the Ali template declares interactive questions, selectable options, full/partial workflow scope, track/condition/controller concepts, and ordered resolved agent steps.
- runWorkflow is the CLI execution entry. It ensures workspace structure, resolves a tracked template, marks it active, filters steps by track and conditions, creates event/status services, and delegates execution to WorkflowRunner.
- Startup preflight is centralized: the template and imported agent packages are loaded, onboarding needs are derived, and required specifications are validated before execution. The project-name check is explicitly disabled by a TODO because of a persistence bug.
- Resume is concrete and durable at the CLI workspace level: StepIndexManager supplies getResumeInfo/startIndex, and Ctrl+C cleanup persists controller or step session IDs and monitoring IDs so an interrupted agent session can continue.
- WorkflowRunner composes a state machine, user/controller input providers, workflow mode, abort controller, step session, pause/skip/stop/mode-change signals, and fresh-step execution.
- Crash recovery differentiates autonomous and manual modes. Autonomous mode sends RESUME then a continuation prompt and waits for an agent response; manual mode records STEP_COMPLETE and returns to an awaiting/paused state for user input.
- A human gate exists in controller-first execution: the controller phase blocks until complete and user-confirmed. Manual input providers and pause/stop signals offer additional operator control.
- Observability is first-class in the sampled source: a workflow event bus/status service, monitoring IDs, debug logs written under .codemachine/logs, and OpenTelemetry dependencies are present.
- The package defines bun test/coverage scripts, but the inspected build workflow primarily builds binaries and marks some smoke execution checks continue-on-error; no test-running CI step was observed in the bounded sample.

## Inference

- This is a resumable interactive multi-agent CLI state machine: the distinctive value is preserving engine session identity and switching between human/controller/autonomous input modes across steps.
- Workspace/session persistence makes long-running continuation credible, but the explicit preflight TODO shows persistence behavior was still evolving at this commit.
- Because step agents can execute coding CLIs, side effects inherit the selected engine and prompts; the orchestrator provides stop/pause/controller gates, not a transactional sandbox.

## Not verified

- Not verified: generic task-level retry counts, exponential backoff, or per-side-effect idempotency keys; crash continuation is verified in source, but replay safety is not.
- Not verified: exactly-once semantics for file edits, shell commands, git operations, network calls, or spawned agents.
- Not verified: complete state transition table, because the bounded sample read the state module barrel and runner/recovery consumers rather than every state-machine implementation file.
- Not verified: end-to-end controller confirmation and resumed engine sessions were not run.
- Not verified: current CI success at the fixed commit, and no test-running job was established from the inspected build workflow.

## Limitations

- Static review of 11 files at the fixed commit; no CLI workflow, coding engine, tests, or CI jobs were executed.
- Only the Ali workflow template was sampled; custom templates and individual agent prompts may materially change side effects and approval behavior.
- State/input modules were sampled through their public barrels and runner/recovery consumers, so lower-level implementation details remain outside scope.

## Evaluation

| Dimension | Score (1–5) |
| --- | ---: |
| `trigger_and_contract` | 4 |
| `state_and_resume` | 5 |
| `idempotency` | 2 |
| `side_effect_control` | 3 |
| `human_gate` | 4 |
| `observability` | 5 |
| `validation` | 3 |
| `reuse_value` | 5 |

Scores are comparative judgments derived from fixed-source evidence, not runtime benchmarks.

## Evidence URLs

- https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/README.md
- https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/LICENSE
- https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/package.json
- https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/templates/workflows/ali.workflow.js
- https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/src/workflows/run.ts
- https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/src/workflows/preflight.ts
- https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/src/workflows/state/index.ts
- https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/src/workflows/runner/index.ts
- https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/src/workflows/input/index.ts
- https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/src/workflows/recovery/index.ts
- https://github.com/moazbuilds/CodeMachine-CLI/blob/572def63eb808e95b18ccf6c69a13d7a13fe06fd/.github/workflows/build.yml
