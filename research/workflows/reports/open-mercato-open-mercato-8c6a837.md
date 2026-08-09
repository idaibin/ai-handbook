# open-mercato/open-mercato workflow assessment

- Fixed commit: `8c6a83752b0c6717e086b40a9fd7aa8fa950be06`
- Content identity: `git-tree:47f6b78e1492f6e63d72cf90a48457e2ff859d6a`
- Evidence: `source_validated`
- Subtype/topic fit: `skill-defined spec-to-code implementation workflow`; `fit`
- Topic rationale: The default skill tier installs om-implement-spec into the canonical agent skills directory, and its workflow defines spec selection, phase iteration, code generation, tests, documentation, human gates, progress persistence, and final verification.
- Runtime execution: none

## Verified

- The README presents Open Mercato as an architecture-aware AI harness with spec-first development and autonomous skills that can implement whole features with unit and integration tests.
- The root agent router assigns spec lifecycle implementation to om-implement-spec and states that local skills are installed by tier into a canonical .agents/skills directory.
- The default core tier declares om-implement-spec, package.json exposes yarn install-skills, and install-skills.sh consumes the selected tier list and creates .agents/skills/om-implement-spec as a symlink to its repo-local skill directory.
- The skill metadata declares natural-language triggers including implement spec, implement phases, build from spec, and code the spec. Its input contract is a target spec plus an optional phase subset; absent a subset, all phases are processed sequentially.
- Pre-flight requires locating and fully reading the spec, reading routed AGENTS guidance, loading the code-review checklist and lessons, and scoping requested phases.
- The monorepo skill has a mandatory first human gate asking whether the feature belongs in an external extension or core; selecting core requires a second explicit confirmation, and the workflow says not to continue without it.
- Each selected phase follows plan, implementation, unit tests, conditional integration tests, documentation, self-review, persisted spec progress update, then final generation/build/lint/test/integration/migration verification after all phases.
- The durable progress format is embedded in the target spec: phase states include Done, In Progress, and Not Started, with per-step checkboxes and date/notes fields.
- Side-effect guidance requires mutation guards for custom writes, atomic multi-phase database flushing, and firing external side effects and cache invalidation only after commit.
- The skill declares parallel subagents only for independent files and sequential execution for dependent work, but no executable dispatcher or scheduler in the sampled repository consumes that policy.
- The only retry-related workflow text is a product-code retryLastMutation requirement and Playwright --retries=0; no spec-implementation retry/backoff control is declared and consumed.
- The create-app copy of om-implement-spec is materially different from the monorepo copy: it removes the extension/core human gate, changes context paths and final validation commands, so identical workflow behavior is not portable across the two installed contexts.
- Installer-layout tests execute the installer against fixtures and assert canonical/local/external skill link behavior; overlay tests assert scaffolding assets and external-skill dependency closure, but neither test executes om-implement-spec's spec-to-code behavior.

## Inference

- The subtype is evidence-backed because the installed artifact is a SKILL.md procedure rather than a compiled workflow engine: the external agent runtime interprets the phase protocol and performs edits and commands.
- Updating the spec after every phase gives a human-readable recovery anchor, but resuming safely still requires an agent to reconstruct repository state and validate that checkboxes match actual code.
- The review and validation gates reduce unsafe code side effects, yet they are instruction-level controls without a machine-enforced transaction spanning source edits, tests, documentation, and spec updates.
- Default-tier installation and scaffold packaging make the workflow broadly reusable, while divergence between monorepo and create-app copies creates behavior and governance drift risk.

## Not verified

- Not verified: which agent runtimes parse the skill description and how natural-language trigger phrases are matched or prioritized.
- Not verified: actual subagent scheduling, dependency enforcement, cancellation, timeout, retry, or failure-resume behavior.
- Not verified: automatic reconciliation between persisted spec status and the real working tree after interruption or partial failure.
- Not verified: enforcement of the extension/core confirmation outside an agent following the monorepo prompt faithfully.
- Not verified: consumption of .ai/agentic.config.json validation.commands or qaGate by om-implement-spec itself; the skill also declares its own non-identical final command sequence.
- Not verified: rollback or compensating actions for partially completed code edits, migrations, generated files, spec edits, or external side effects.
- Not verified: end-to-end spec implementation results, tests, CI status, or runtime behavior at the fixed commit because nothing was executed.

## Operational-control trace

- **retry** — declaration: No workflow retry policy; retryLastMutation is an implementation rule and integration tests explicitly use --retries=0. Consumption: No spec-to-code retry loop, backoff, attempt counter, or failure classifier was found in the selected files. Credit: `none`.
- **concurrency** — declaration: Parallel subagents are allowed only for independent files; dependent work must be sequential. Consumption: No repository executor maps dependency information to actual subagent dispatch; execution depends on an external agent harness interpreting SKILL.md. Credit: `declaration_only`.
- **iteration** — declaration: For each selected spec phase, run steps 1-7; after all targeted phases, run final verification. Consumption: The same skill requires a status-table and detailed-checkbox update after each phase, providing a procedural phase cursor, but no executable loop or run-state engine exists in the sampled source. Credit: `procedural_partial`.
- **approval** — declaration: Ask extension-versus-core before code and ask a second confirmation for core modifications. Consumption: The monorepo skill explicitly says only continue after confirmation and repeats the gate in its MUST rules; however enforcement is prompt-level and the create-app mirror omits the gate. Credit: `strong_procedural_monorepo_only`.

## Limitations

- Read-only source review of 12 selected files at the exact commit; directory and filename listings were used for orientation, but no installer, test, skill, agent, build, or CI workflow was run.
- Evidence level is capped at source_validated. Scores use 1 for weak/absent evidence and 5 for strong source evidence.
- Control scores follow declaration-to-consumption discipline: unconsumed signatures or prompt declarations do not receive implementation credit.
- The analysis treats the monorepo om-implement-spec artifact as primary and records the divergent create-app copy as a portability limitation.

## Evaluation

| Dimension | Score (1–5) |
| --- | ---: |
| `trigger_and_contract` | 4 |
| `state_and_resume` | 3 |
| `idempotency` | 2 |
| `side_effect_control` | 4 |
| `human_gate` | 4 |
| `observability` | 3 |
| `validation` | 4 |
| `reuse_value` | 4 |

Scores are comparative judgments derived from fixed-source evidence, not runtime benchmarks.

## Files read

- `README.md`
- `LICENSE`
- `AGENTS.md`
- `package.json`
- `.ai/agentic.config.json`
- `.ai/specs/AGENTS.md`
- `.ai/skills/tiers.json`
- `.ai/skills/om-implement-spec/SKILL.md`
- `scripts/install-skills.sh`
- `packages/create-app/agentic/shared/ai/skills/om-implement-spec/SKILL.md`
- `packages/create-app/src/lib/install-skills-layout.test.ts`
- `packages/create-app/src/lib/agentic-skills-standalone-overlays.test.ts`

## Evidence URLs

- https://github.com/open-mercato/open-mercato/blob/8c6a83752b0c6717e086b40a9fd7aa8fa950be06/README.md#L12-L23
- https://github.com/open-mercato/open-mercato/blob/8c6a83752b0c6717e086b40a9fd7aa8fa950be06/AGENTS.md#L123-L140
- https://github.com/open-mercato/open-mercato/blob/8c6a83752b0c6717e086b40a9fd7aa8fa950be06/.ai/skills/tiers.json#L35-L50
- https://github.com/open-mercato/open-mercato/blob/8c6a83752b0c6717e086b40a9fd7aa8fa950be06/scripts/install-skills.sh#L603-L648
- https://github.com/open-mercato/open-mercato/blob/8c6a83752b0c6717e086b40a9fd7aa8fa950be06/.ai/skills/om-implement-spec/SKILL.md#L1-L47
- https://github.com/open-mercato/open-mercato/blob/8c6a83752b0c6717e086b40a9fd7aa8fa950be06/.ai/skills/om-implement-spec/SKILL.md#L51-L111
- https://github.com/open-mercato/open-mercato/blob/8c6a83752b0c6717e086b40a9fd7aa8fa950be06/.ai/skills/om-implement-spec/SKILL.md#L123-L181
- https://github.com/open-mercato/open-mercato/blob/8c6a83752b0c6717e086b40a9fd7aa8fa950be06/.ai/skills/om-implement-spec/SKILL.md#L187-L223
- https://github.com/open-mercato/open-mercato/blob/8c6a83752b0c6717e086b40a9fd7aa8fa950be06/.ai/specs/AGENTS.md#L37-L56
- https://github.com/open-mercato/open-mercato/blob/8c6a83752b0c6717e086b40a9fd7aa8fa950be06/.ai/specs/AGENTS.md#L72-L93
- https://github.com/open-mercato/open-mercato/blob/8c6a83752b0c6717e086b40a9fd7aa8fa950be06/packages/create-app/agentic/shared/ai/skills/om-implement-spec/SKILL.md#L1-L36
- https://github.com/open-mercato/open-mercato/blob/8c6a83752b0c6717e086b40a9fd7aa8fa950be06/packages/create-app/src/lib/install-skills-layout.test.ts#L9-L20
- https://github.com/open-mercato/open-mercato/blob/8c6a83752b0c6717e086b40a9fd7aa8fa950be06/packages/create-app/src/lib/install-skills-layout.test.ts#L100-L148
- https://github.com/open-mercato/open-mercato/blob/8c6a83752b0c6717e086b40a9fd7aa8fa950be06/.ai/agentic.config.json#L8-L36
