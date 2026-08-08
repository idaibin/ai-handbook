# Agent Skills deep analysis — Batch 045

Date: 2026-08-08

## Scope and completion gate

This batch continued from the existing indexed queue at `aminrj/Anthropic-Cybersecurity-Skills` and stopped after ten genuinely qualified repository identities were completed.

A repository was counted as complete only after GitHub identity and observed Stars were checked, a concrete revision was pinned, repository structure was inspected, README and `SKILL.md` or equivalent skill bodies were read directly, and scripts/references/evals were inspected when present. Index metadata alone was never accepted as completion evidence.

No repository runtime, build, test, or LLM eval suite was executed in this batch. Source files and eval definitions were inspected only. Therefore runtime validation remains `not_executed`.

## Batch metrics

| Metric | Result |
|---|---:|
| Qualified repository identities completed | 10 |
| README direct reads | 10 |
| `SKILL.md` direct reads | 22 |
| Unique skill bodies directly reviewed | 17 |
| Unique Git content trees among completed identities | 5 |
| New canonical individual skill reports | 14 |
| Structure-reviewed repositories, cumulative | 450 |
| Individual skill reports, cumulative | 2927 |
| Frozen eligible basis | 2088 |
| Arithmetic remaining estimate | 1638 |
| Runtime/build/test/eval execution | not_executed |

The remaining estimate is only `2088 - 450`. Historical cross-repository canonical reconciliation remains pending, so `1638` must not be interpreted as a reconciled unique-repository remainder.

## Completed repository identities

| Repository | Stars observed | Pinned revision | Git tree | Direct content gate | Canonical result |
|---|---:|---|---|---|---|
| `aminrj/Anthropic-Cybersecurity-Skills` | 0 | `4ae0be7f4806596e94958ac343379e9c9b3111d2` | `5dd2ce82978a50cd014d4b310f5993bf5bba6f43` | README + representative Skill + 754-skill inventory/structure | maps to existing Cybersecurity lineage |
| `Aizenkyel/Anthropic-Cybersecurity-Skills` | 0 | `4ae0be7f4806596e94958ac343379e9c9b3111d2` | `5dd2ce82978a50cd014d4b310f5993bf5bba6f43` | README + representative Skill | exact-tree mirror; existing canonical report |
| `CodeHemP/Anthropic-Cybersecurity-Skills` | 0 | `4ae0be7f4806596e94958ac343379e9c9b3111d2` | `5dd2ce82978a50cd014d4b310f5993bf5bba6f43` | README + representative Skill | exact-tree mirror; existing canonical report |
| `TPFLegionaire/Anthropic-Cybersecurity-Skills` | 0 | `4ae0be7f4806596e94958ac343379e9c9b3111d2` | `5dd2ce82978a50cd014d4b310f5993bf5bba6f43` | README + representative Skill | exact-tree mirror; existing canonical report |
| `stehessel/agentskills` | 0 | `a3285d168613e95080d3e332e0d2488b75368067` | `09bb585bdd3c0bd5f11ccb447367929dfa068567` | README + all 5 Skills + executable helpers + references | 5 new canonical reports |
| `mkobit/chezmoi-skills` | 1 | `5197fe69daf95a4b729cba87890eb349be33f95d` | `1c2a117dc313fba9d80ca3727bd9cb02468e6744` | README + all 9 Skills + references + validator + contract evals + Promptfoo workflow | 9 new canonical reports |
| `langfeng1314/dreamina-cli-skill` | 0 | `75e0a69a99f21a9c706045a0f6227b1b0804f886` | `dcd5dd83daec1b0786f92740876c949310bba95c` | README + root Skill | exact-tree Dreamina mirror; existing canonical report |
| `huangzhen9527007/dreamina-cli-skill` | 0 | `75e0a69a99f21a9c706045a0f6227b1b0804f886` | `dcd5dd83daec1b0786f92740876c949310bba95c` | README + root Skill | exact-tree Dreamina mirror; existing canonical report |
| `letsmotion/dreamina-cli-skill` | 0 | `75e0a69a99f21a9c706045a0f6227b1b0804f886` | `dcd5dd83daec1b0786f92740876c949310bba95c` | README + root Skill | exact-tree Dreamina mirror; existing canonical report |
| `saxster/skills` | 0 | `4d322538be8b9ce98fca29b0eef26d67bff1fe82` | `32d2d4cb75cf113fbc8e145d7c52672832e34a2d` | README + representative `clean-architecture` Skill | exact-tree Wondel mirror; existing canonical report |

## Repository findings

### `stehessel/agentskills`

This is a real five-Skill APM collection, not an Agent Skills specification fork. At the pinned revision, the actual skill roots are under `.apm/skills/`: `beadflow`, `reviewer`, `sculptor`, `session-viewer`, and `treeflow`.

Positive patterns:

- The collection separates planning/task-state, review, ideation, session inspection, and parallel orchestration into distinct Skills rather than one monolithic prompt.
- `reviewer` requires discovery before findings, tech-stack-specific checklist selection, spec traceability, and concrete `file:line` evidence.
- `sculptor` uses file-backed state plus explicit approval gates and a hard boundary against implementation.
- `session-viewer` and `treeflow` contain real Python helpers rather than only prose.
- `treeflow` maintains a JSON registry using temp-file replacement and includes phase-gate/build-wiring concepts.

Verified issues and limitations:

- README structure is stale after the repository moved Skills into `.apm/skills/`; the prose tree still depicts skill directories at repository root.
- No repository-local `tests` or `eval` entries were found in the pinned tree. The executable helpers therefore have implementation evidence but no local behavioral proof in this revision.
- `tf.py` invokes multiple dynamically constructed commands through `subprocess.run(..., shell=True)`. Several values originate from bead IDs, file paths, summaries, and build commands. This is an avoidable command-construction risk and should be replaced with argument arrays plus explicit validation where possible.
- `tf.py` chooses the first matching `context-*` directory containing a registry; multiple active context directories make selection dependent on filesystem iteration rather than an explicit plan identifier.
- `beadflow` and `treeflow` contain absolute process rules such as treating every strategic action as a Beads update. That may be useful in the intended workflow, but it is too strong as a general policy and can create unnecessary state churn.
- `beadflow` contains inconsistent initialization wording: one path says to initialize automatically when a goal exists, while another error-handling path says to confirm before initialization.
- `reviewer`'s fixed “10–15 representative files” discovery quantity is a heuristic rather than a completeness criterion; very small and very large repositories need risk-based sampling instead.

### `mkobit/chezmoi-skills`

This is a nine-Skill collection with a stronger verification surface than most catalog entries in this queue. It includes structured references, a TypeScript validator, per-Skill JSON eval definitions, Promptfoo configuration, and a scheduled live-eval workflow.

Positive patterns:

- All nine Skills are deliberately thin routers into references, keeping top-level bodies compact.
- `scripts/validate.ts` checks frontmatter constraints, internal links, prose format, and actual tokenizer-based body budgets.
- The eval corpus includes positive and negative trigger examples, command correctness, and safety-oriented expectations.
- `promptfooconfig.yaml` defines baseline-vs-skill-enhanced LLM comparisons rather than only static document linting.
- The scheduled GitHub workflow records benchmark outputs separately from source code and uses repository secrets for provider credentials.

Critical validation boundary:

The local `scripts/test-contracts.ts` rule-based evaluator is partly tautological and must not be interpreted as independent behavioral evidence. For `skill_selection` it returns the test case's declared target skill; for command tests with an `exact_command` it returns that expected command directly. Its token accounting also uses a simple character-length approximation. Those checks can validate test plumbing and assertion schemas, but they cannot prove that an autonomous agent selected or generated the correct behavior.

The Promptfoo path is the materially stronger behavioral layer, but it was not executed in this batch. No pass rate is claimed here.

### Exact-tree mirror groups

Four Cybersecurity identities share the exact pinned tree `5dd2ce...`, three Dreamina identities share `dcd5dd...`, and `saxster/skills` maps to the already reviewed Wondel tree `32d2d4...`. Each identity was still content-gated with direct README/Skill reads before completion, but canonical individual reports were not duplicated.

The Cybersecurity lineage remains a large inventory: the pinned index declares 754 Skills. This batch did not convert inventory size into body-level deep-analysis counts; only the representative body directly read for the identity gate is counted in this batch's direct body-review metric.

## Reclassified or skipped index entries

The queue was not trusted blindly. The following entries encountered before the ten-qualified boundary were not marked complete:

- `dbiswas/agentskills`, `Suneelm5/agentskills`, `wuxinlilele/agentskills`, `jinjingforever/agentskills`, `zhidong010/agentskills`, `xiukun/agentskills`, `chiragce17/agentskills`: Agent Skills specification/documentation/reference implementation lineage rather than local Skill collections. `jinjingforever/agentskills` was additionally checked at its current revision; its changes remain documentation/client-showcase changes inside the specification repository.
- `skills-il/bundles`: bundle/catalog manifests with `bundle.json` content and no local `SKILL.md` package at the inspected revision.
- `carlosmarte/agentskills-repo-version` and `DnXLogic/agentskills-mcp`: tooling entries, not catalog Skill bodies.
- `ma-serra/AgentSkills.legal-Multi-Contract-Analyzer`: application/browser repository with a large internal `skills.json`, not an AgentSkill package at the inspected revision.

These are reclassifications or skips, not completed repositories.

## Batch boundary

`gigantsc/skills-hermes-` was pre-inspected while resolving the queue and is an exact Wondel tree mirror, but it is the next qualified identity after the ten-repository Batch 045 boundary. It is deliberately **not** marked complete here.

Next unresolved qualified queue identity: `gigantsc/skills-hermes-`.
