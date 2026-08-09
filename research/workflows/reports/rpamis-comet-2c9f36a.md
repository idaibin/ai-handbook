# rpamis/comet workflow assessment

- Fixed commit: `2c9f36aeed6db0fdd30c28cb7a3e97fda47bdecf`
- Content identity: `git-tree:9be09217625966076edb204e871ff1d9fa49302e`
- Evidence: `source_validated`
- Subtype/topic fit: `checkpointed_guarded_skill_engine`; `strong_fit`
- Runtime execution: none

## Verified

- The engine contract defines running, waiting, completed, and failed run states, with current step, iteration, pending action, retry counters, and references to trajectory, context, artifacts, and checkpoint files.
- A deterministic run starts at the skill definition's entry step; adaptive runs require an externally supplied Agent candidate. Action IDs are deterministic hashes of run ID, iteration, and step ID.
- Before an action is exposed, guardrails enforce maximum iterations, allowlists for skills/tools/agents, per-reference user confirmation, and a per-action retry budget.
- Accepted actions move the run to waiting and persist a pending-action record. Resume without an outcome returns that same pending action; mismatches or a missing pending file fail closed.
- A failed outcome clears the pending slot, returns the run to running, and increments the retry counter. A successful deterministic outcome advances the step and iteration, completing when the resolver returns no next step.
- Run state and all run references are validated; absolute paths, parent traversal, invalid statuses, negative iterations, and malformed retry maps are rejected.
- The run store constrains paths to the change directory and applies explicit byte limits to trajectory, artifacts, context, pending action, and checkpoint data.
- Manual execution snapshots the skill and binds the run to its hash, appends ordered trajectory events, merges returned artifacts, evaluates step/completion scopes, and forbids skill upgrades while an action is pending.
- The native workflow documented in README binds approval to a contract hash, returns failed verification to Build through bounded repair, and uses protected I/O, locks, CAS, and recoverable transactions for runtime/archive data.
- CI is triggered by pull requests and selected push branches and runs workflow lint, build determinism, coverage, multi-Node tests, multi-OS runtime smoke/package E2E, static evals, browser E2E, and a final all-jobs-must-pass gate.

## Inference

- The stable action ID plus the persisted pending-action check provides replay resistance for the coordinator, but idempotency of the invoked external skill/tool still depends on that implementation.
- The combination of machine-owned run state, append-only trajectory, checkpoints, and a skill snapshot makes the engine reusable for resumable local workflows whose side effects can be represented as explicit actions.
- Human approval is stronger in the documented Native lifecycle than in the generic engine: the engine supports confirmation-required references, while Native additionally binds approval to the current requirements hash.

## Not verified

- No runtime command, test suite, CI run, crash-injection scenario, or concurrent writer scenario was executed.
- Atomicity and durability guarantees of protected-run-file.ts were not inspected within the file budget.
- The semantics and idempotency of arbitrary invoked skills, tools, handoffs, and their external side effects are not verified.
- Adaptive-agent candidate generation and approval UX are not verified.
- Repository branch-protection settings and whether CI is currently green are not verified.

## Limitations

- Source-only review at the fixed commit; evidence level cannot exceed source_validated.
- The repository contains separate Native, Classic, and generic Engine surfaces; this review emphasizes the generic Engine and uses README evidence for Native governance.
- Only 11 key files were read, so helper implementations and the broader test matrix were sampled rather than exhaustively inspected.

## Evaluation

| Dimension | Score (1–5) |
| --- | ---: |
| `trigger_and_contract` | 4 |
| `state_and_resume` | 5 |
| `idempotency` | 4 |
| `side_effect_control` | 4 |
| `human_gate` | 4 |
| `observability` | 5 |
| `validation` | 5 |
| `reuse_value` | 5 |

Scores are comparative judgments derived from fixed-source evidence, not runtime benchmarks.

## Evidence URLs

- https://github.com/rpamis/comet/blob/2c9f36aeed6db0fdd30c28cb7a3e97fda47bdecf/domains/engine/loop.ts
- https://github.com/rpamis/comet/blob/2c9f36aeed6db0fdd30c28cb7a3e97fda47bdecf/domains/engine/manual-run.ts
- https://github.com/rpamis/comet/blob/2c9f36aeed6db0fdd30c28cb7a3e97fda47bdecf/domains/engine/guardrails.ts
- https://github.com/rpamis/comet/blob/2c9f36aeed6db0fdd30c28cb7a3e97fda47bdecf/domains/engine/state.ts
- https://github.com/rpamis/comet/blob/2c9f36aeed6db0fdd30c28cb7a3e97fda47bdecf/domains/engine/run-store.ts
- https://github.com/rpamis/comet/blob/2c9f36aeed6db0fdd30c28cb7a3e97fda47bdecf/.github/workflows/ci.yml
