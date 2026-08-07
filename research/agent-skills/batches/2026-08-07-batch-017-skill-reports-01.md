# Agent Skills individual reports — Batch 017

- Observed at: 2026-08-07 16:00 +08:00
- Batch: `2026-08-07-batch-017`
- Repository-scoped skill identities: **25**
- Evidence state: `structure-reviewed`
- Runtime validation: `not_executed`

## Evidence labels

- `direct-body-reviewed`: the current `SKILL.md` body was directly read during this batch.
- `catalog-verified`: the identity was verified from a repository-maintained current inventory, while representative bodies and repository support surfaces were directly inspected.

The report does not assign remote marketplace entries, dependency-owned skills, README examples, or linked external skills to the repository that merely indexes or installs them.

## `kambleakash0/agent-skills` — 13 skills

Current README inventory: `git-workflow`, `code-review`, `english-humanizer`, `grill-master`, `spec-writer`, `slice-the-spec`, `incremental-tdd`, `deep-codebase-audit`, `spec-to-plan`, `domain-glossary`, `script-writer`, `teach-me`, `context-pack`.

| Skill | Evidence | Finding |
| --- | --- | --- |
| `git-workflow` | `catalog-verified` | Guided Git workflow identity is present in the maintained README inventory. |
| `code-review` | `catalog-verified` | Review workflow identity covers correctness, security, performance, and style in the current inventory. |
| `english-humanizer` | `catalog-verified` | Text-humanization skill is explicitly inventoried. |
| `grill-master` | `direct-body-reviewed` | `skills/grill-master/SKILL.md` enforces clarification before planning, one focused question at a time, explicit assumptions, repository-grounded answers when available, and a shared-understanding checkpoint. |
| `spec-writer` | `catalog-verified` | Requirements/PRD authoring identity is present in the maintained inventory. |
| `slice-the-spec` | `catalog-verified` | Vertical-slice decomposition identity is present in the maintained inventory. |
| `incremental-tdd` | `catalog-verified` | TDD workflow identity is present in the maintained inventory. |
| `deep-codebase-audit` | `catalog-verified` | Architecture/codebase audit identity is present in the maintained inventory. |
| `spec-to-plan` | `catalog-verified` | PRD-to-implementation-plan identity is present in the maintained inventory. |
| `domain-glossary` | `catalog-verified` | DDD-style ubiquitous-language/glossary identity is present in the maintained inventory. |
| `script-writer` | `catalog-verified` | Long-form/script writing identity is present in the maintained inventory. |
| `teach-me` | `direct-body-reviewed` | `skills/teach-me/SKILL.md` is a stateful teaching workflow built around `MISSION.md`, learning records, curated `RESOURCES.md`, incremental lessons, and explicit citation/verification requirements. |
| `context-pack` | `catalog-verified` | Conversation-handoff/context-pack identity is present in the maintained inventory. |

Repository support surfaces reviewed: root README/structure, `skills/grill-master/SKILL.md`, `skills/teach-me/SKILL.md`, and the `teach-me` reference format surface. The repository also contains three MCP servers; those are not counted as skills.

## `jeremyeder/dgx-agentskills` — 5 skills

Current README inventory: `spark-setup`, `spark-models`, `spark-hybrid`, `spark-vpn`, `spark-vms`.

| Skill | Evidence | Finding |
| --- | --- | --- |
| `spark-setup` | `direct-body-reviewed` | `skills/spark-setup/SKILL.md` defines ordered, restartable provisioning phases, explicit prerequisite checks, deployment, and final health/GPU/model validation steps. |
| `spark-models` | `catalog-verified` | Model-management skill is listed in the maintained repository inventory. |
| `spark-hybrid` | `catalog-verified` | Hybrid local/remote workflow skill is listed in the maintained repository inventory. |
| `spark-vpn` | `catalog-verified` | VPN/connectivity skill is listed in the maintained repository inventory. |
| `spark-vms` | `catalog-verified` | VM-management skill is listed in the maintained repository inventory. |

Repository support surfaces reviewed include `skills/`, MCP implementation/test structure, `skills/spark-setup/SKILL.md`, and `tests/mcp-server/status.test.ts`. The test file covers system/GPU parsing and an `nvidia-smi` failure path, but tests were not executed in this batch.

## `cesareth/hermes-turkce-skills` — 4 skills

| Skill | Evidence | Finding |
| --- | --- | --- |
| `turkce-asistan` | `direct-body-reviewed` | Turkish writing/editing skill with explicit audience/tone rules, language consistency checks, templates, and a linked language reference. |
| `kvkk-denetim` | `direct-body-reviewed` | Turkish privacy-compliance guidance skill with an explicit legal-information disclaimer, structured review checklist, templates, and a linked law reference. The bundled checker is heuristic and is not treated as legal validation. |
| `resmi-yazi` | `direct-body-reviewed` | Formal-writing/petition skill provides document structure, templates, information-gathering steps, privacy cautions for identity numbers, and a recommendation to seek professional legal review for legal processes. |
| `turkce-kod` | `direct-body-reviewed` | Turkish software-documentation skill covers comments, naming, commit messages, README structure, logs/errors, terminology, and a final consistency checklist. |

Support surface reviewed: `kvkk-denetim/scripts/kvkk_check.py`. It uses regex-based presence/risk checks and a simple weighted score, so Batch 017 records it as a quick heuristic helper rather than evidence of legal correctness.

## `nxl801/obsidian-official-cli-skill` — 1 skill

| Skill | Evidence | Finding |
| --- | --- | --- |
| `obsidian-official-cli` | `direct-body-reviewed` | Retrieval-first workflow around the official Obsidian CLI: narrow search/context before reads, structured output when parsing, graph/metadata commands for expansion, and explicit write-safety boundaries for mutating commands. |

Reference reviewed: `obsidian-official-cli/references/official-cli-commands.md`, which organizes search/read, links, tags/properties, tasks, and output-shaping commands. Repository claims about real-vault testing were not independently re-executed in this batch.

## `siddontang/tidb-x-skill` — 1 skill

| Skill | Evidence | Finding |
| --- | --- | --- |
| `tidb-x` | `direct-body-reviewed` | A single database-knowledge skill describing TiDB X concepts and agent-state patterns such as durable memory/context and auditable state. Product/performance statements inside the skill are repository-authored claims and were not independently benchmarked here. |

No repository-level scripts, tests, or eval suite were observed in the reviewed root structure.

## `antgly/law-of-demeter-swift-skill` — 1 skill

| Skill | Evidence | Finding |
| --- | --- | --- |
| `law-of-demeter-swift` | `direct-body-reviewed` | Strict Swift code-review guidance for structural reach-through. It pairs aggressive chain-detection heuristics with explicit false-positive guardrails, Swift-style API naming, minimal refactoring order, severity classification, and anti-regression checks. |

No repository-level scripts, references, tests, or eval suite were observed in the reviewed root structure.

## Repositories with zero local skill reports

The following four batch repositories are deliberately retained as repository analysis objects while contributing **zero** repository-scoped skill identities:

| Repository | Content classification | Reason for zero local skill reports |
| --- | --- | --- |
| `gigantsc/agentskills-hermes` | `specification_reference_sdk` | Repository contains the Agent Skills specification/documentation/reference surfaces; repository search surfaced no local `SKILL.md`. Linked example skills are external. |
| `suprunoff/skills-catalog` | `awesome_index_research_catalog` | Static research/catalog site. Repository search surfaced no local `SKILL.md`; marketplace/catalog entries are outbound indexed content. |
| `YoavLax/AgentEval` | `skill_tooling_validator` | Python validator/quality-gate implementation and tests for skill/agent files; no bundled repository-scoped skill package was surfaced. |
| `kayaman/agentskills` | `skill_tooling_package_manager` | Rust package manager that fetches/installs skills from other repositories and tracks them in a lockfile; bundled local skill content is not the product. |

## Count reconciliation

```text
kambleakash0/agent-skills                 13
jeremyeder/dgx-agentskills                 5
gigantsc/agentskills-hermes                0
cesareth/hermes-turkce-skills              4
suprunoff/skills-catalog                    0
YoavLax/AgentEval                           0
nxl801/obsidian-official-cli-skill          1
kayaman/agentskills                         0
siddontang/tidb-x-skill                     1
antgly/law-of-demeter-swift-skill           1
---------------------------------------------
total                                      25
```

## Validation boundary

This artifact records source/content review. Repository code, tests, scripts, installers, CLIs, cloud services, and eval runners were **not executed**. `direct-body-reviewed` means a current skill body was read; `catalog-verified` means identity/count was grounded in a maintained repository inventory plus representative direct content inspection. Neither label implies runtime correctness.