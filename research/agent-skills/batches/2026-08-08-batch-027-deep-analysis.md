# GitHub Skills Catalog deep analysis — Batch 027

Observed: `2026-08-08`

Status: `structure-reviewed`

Runtime validation: `not_executed`

## Scope and completion rule

This batch continued from the persisted GitHub Skills / Agent Skills indexed queue and completed content-level review for **10 repository entries**. A repository was counted only after repository identity and a point-in-time star count were verified and actual repository content was inspected. Metadata-only matches were not promoted to completed skill repositories.

For exact snapshots or mirrors, Git commit identity was used as the content-deduplication key. When a target repository matched a commit that had already been content-reviewed in Batch 026, that exact prior tree review was reused instead of generating duplicate skill reports. When a target was ahead of a reviewed tree, the commit delta was inspected before reusing the prior review.

Third-party builds, installers, APIs, model providers, scripts, tests, eval runners, firmware tools, or other repository code were **not executed**. Source/test presence is not recorded as runtime success.

## Batch result

| Repository | Repo id | Stars observed | Reviewed revision | Content-level classification | Local skill reports | Result |
|---|---:|---:|---|---|---:|---|
| `zyq5428/zephyr-agent-skills` | 1194502551 | 0 | `431ef375fadc8cd22cdbee53311ec5807d505657` | `zephyr_rtos_skill_collection` | 21 | structure-reviewed |
| `liangyongqin/zephyr-agent-skills` | 1194276522 | 0 | `d1ba906ec587339bc93e466e212248ccac21e4bf` | `zephyr_rtos_packaging_variant` | 0 | reference / dedupe |
| `blackwell-systems/agentskills-cli` | 1193377004 | 2 | `31f35119e4ed0e8165313ee3f1a7e8938cb481cf` | `skill_tooling_with_bundled_skill` | 1 | structure-reviewed |
| `gplm0/agentskills` | 1193771717 | 0 | `b5ce2a438123f9f9c9b167c5af297c048f15395b` | `official_agent_skills_spec_snapshot` | 0 | reference / dedupe |
| `TracyHe/agentskills` | 1192229698 | 0 | `5e7f3e2c4c9f5464fe342bf2fea72367a914e9b4` | `official_agent_skills_spec_snapshot_docs_delta` | 0 | reference / dedupe |
| `chlin1983/agentskills` | 1192286383 | 0 | `b5ce2a438123f9f9c9b167c5af297c048f15395b` | `official_agent_skills_spec_snapshot` | 0 | reference / dedupe |
| `ghwoodard/agentskills` | 1192922480 | 0 | `b5ce2a438123f9f9c9b167c5af297c048f15395b` | `official_agent_skills_spec_snapshot` | 0 | reference / dedupe |
| `puppetls/agentskills` | 1192689086 | 0 | `b5ce2a438123f9f9c9b167c5af297c048f15395b` | `official_agent_skills_spec_snapshot` | 0 | reference / dedupe |
| `xhoanggiang/agentskills` | 1192381797 | 0 | `b5ce2a438123f9f9c9b167c5af297c048f15395b` | `official_agent_skills_spec_snapshot` | 0 | reference / dedupe |
| `camillanapoles/skills_agentskills_reference` | 1192975744 | 0 | `b5ce2a438123f9f9c9b167c5af297c048f15395b` | `official_agent_skills_spec_snapshot` | 0 | reference / dedupe |
| **Total** | — | — | — | — | **22** | **10 queue entries content-reviewed** |

Star values are point-in-time observations verified with owner/repository-scoped GitHub repository searches using exact `stars:N` predicates.

## Repository analyses

### 1. `zyq5428/zephyr-agent-skills`

**Verified**

- Public repository id `1194502551`, default branch `main`; observed stars: `0`.
- Reviewed revision: `431ef375fadc8cd22cdbee53311ec5807d505657`.
- `README.md` describes a Zephyr RTOS Agent Skills collection with a master catalog under `skills/zephyr-index/references/skill_catalog.md`, a Claude Code marketplace surface, and a per-skill structure of `SKILL.md`, `references/`, `scripts/`, and `assets/` where applicable.
- The master catalog enumerates **21 consolidated skills** across foundations/workflows, hardware/peripherals, connectivity, and production/advanced domains.
- All 21 current `SKILL.md` bodies were directly read in this run. The individual reports are persisted in `2026-08-08-batch-027-skill-reports.md`.
- `zephyr-index` provides a navigation contract backed by `references/decision_tree.md` and `scripts/task_skill_match.py`. The router is a local CSV keyword scorer; no model or external service is required for routing.
- Representative automation sources were inspected rather than merely listed: `task_skill_match.py`, `security-updates/scripts/mcuboot_version_guard.py`, and `testing-debugging/scripts/twister_smoke.py`. The Twister helper can invoke the local `twister` executable and parse `twister.json`; it was not run.
- The skill contracts consistently include validation checklists and explicit references/scripts/assets sections. No repository-wide eval runner was executed or claimed to pass.

**Analysis**

- The strongest reusable design is the **hub + specialized-skill** split: `zephyr-index` handles discovery while domain skills keep implementation guidance scoped.
- Progressive disclosure is concrete rather than nominal: the hub points to task routing artifacts, while each specialized skill points to narrower reference files and local helper scripts.
- The collection is unusually consistent in skill shape, which makes automated linting and catalog generation more feasible than in heterogeneous repositories.
- Validation sections are mostly checklists; they are not evidence that firmware builds, hardware behavior, Twister suites, power measurements, or protocol interoperability actually passed.

**Not verified**

- Zephyr builds, `west`, Twister/Ztest, hardware-in-the-loop behavior, BLE/network/USB/CAN behavior, firmware signing, power measurements, or helper-script execution.

### 2. `liangyongqin/zephyr-agent-skills`

**Verified**

- Public repository id `1194276522`; observed stars: `0`.
- Reviewed revision: `d1ba906ec587339bc93e466e212248ccac21e4bf`.
- The repository contains the shared Zephyr tree revision `431ef375fadc8cd22cdbee53311ec5807d505657` used above.
- Comparing that shared revision to the current head shows exactly **one changed file**: `.claude-plugin/marketplace.json`.
- `README.md` has the same blob SHA as the reviewed Zephyr source (`ae02f86e3ffb6f5d1acb8c966e80e6b9eccfc112`).
- The changed marketplace file explicitly exposes the aggregate `zephyr-skills` plugin plus individual entries for the same 21 skill directories.

**Content-level correction**

- This is a packaging/distribution variant of the reviewed Zephyr collection, not an independent skill corpus. The shared skill tree is content-identical at the common commit, so generating another 21 reports would duplicate evidence. Local skill reports emitted: `0`.

### 3. `blackwell-systems/agentskills-cli`

**Verified**

- Public repository id `1193377004`; observed stars: `2`.
- Reviewed revision: `31f35119e4ed0e8165313ee3f1a7e8938cb481cf`.
- `README.md` defines a Rust CLI for Agent Skills validation and decomposition. Its two principal commands are `lint` and `decompose`; it also documents vendor-extension detection and multi-provider semantic analysis with a mechanical fallback.
- `src/main.rs` confirms the executable exposes only `Decompose` and `Lint` subcommands at the reviewed head.
- `src/commands/decompose.rs` shows the actual command flags, dry-run and interactive behavior, provider selection, routing-style handling, filesystem write path, and inline Rust unit tests for argument parsing and options. Those tests were read but not run.
- The bundled `skills/progressive-disclosure-guide/SKILL.md` was directly read and is reported separately.

**Finding**

- The bundled skill is **stale relative to the current CLI**: it repeatedly instructs users to run `agentskills upgrade ...`, while the current executable and README use `agentskills decompose ...`. This is a real source-level contract mismatch, not a runtime inference.
- The bundled skill also says to ask for confirmation before mutation, while the current CLI supports both explicit `--interactive` confirmation and non-interactive application. Consumers should therefore rely on current CLI semantics, not the stale bundled walkthrough, until the skill is updated.

**Not verified**

- `cargo build`, `cargo test`, `cargo clippy`, provider integrations, decomposition output quality, filesystem mutations, or generated routing behavior.

### 4. `gplm0/agentskills`

**Verified**

- Public repository id `1193771717`; observed stars: `0`.
- Reviewed revision: `b5ce2a438123f9f9c9b167c5af297c048f15395b`.
- `README.md` has the official Agent Skills README blob SHA `98534c18d286e0a651f74028666b1ae97db687ed` and describes specification, documentation, and reference SDK content rather than a local production-skill catalog.
- This exact commit was already content-reviewed in Batch 026 through `dev-juha/agentskills` and `netover/agentskills`.

**Content-level correction**

- Exact official specification/reference snapshot. No duplicate skill reports emitted.

### 5. `TracyHe/agentskills`

**Verified**

- Public repository id `1192229698`; observed stars: `0`.
- Reviewed revision: `5e7f3e2c4c9f5464fe342bf2fea72367a914e9b4`.
- `README.md` uses the same official blob SHA `98534c18d286e0a651f74028666b1ae97db687ed`.
- Comparing the previously reviewed official snapshot `b5ce2a438123f9f9c9b167c5af297c048f15395b` to this head shows only two documentation-presentation files changed: `docs/favicon.svg` and `docs/snippets/LogoCarousel.jsx`.

**Content-level correction**

- Specification/reference snapshot with a docs-only visual delta. No skill/spec semantic delta requiring new skill reports was found.

### 6. `chlin1983/agentskills`

**Verified**

- Public repository id `1192286383`; observed stars: `0`.
- Head is exactly `b5ce2a438123f9f9c9b167c5af297c048f15395b`; `README.md` has official blob SHA `98534c18d286e0a651f74028666b1ae97db687ed`.

**Content-level correction**

- Exact official specification/reference snapshot already content-reviewed in Batch 026. No independent skill reports.

### 7. `ghwoodard/agentskills`

**Verified**

- Public repository id `1192922480`; observed stars: `0`.
- Head is exactly `b5ce2a438123f9f9c9b167c5af297c048f15395b`; `README.md` has official blob SHA `98534c18d286e0a651f74028666b1ae97db687ed`.

**Content-level correction**

- Exact official specification/reference snapshot already content-reviewed in Batch 026. No independent skill reports.

### 8. `puppetls/agentskills`

**Verified**

- Public repository id `1192689086`; observed stars: `0`.
- Head is exactly `b5ce2a438123f9f9c9b167c5af297c048f15395b`; `README.md` has official blob SHA `98534c18d286e0a651f74028666b1ae97db687ed`.

**Content-level correction**

- Exact official specification/reference snapshot already content-reviewed in Batch 026. No independent skill reports.

### 9. `xhoanggiang/agentskills`

**Verified**

- Public repository id `1192381797`; observed stars: `0`.
- Head is exactly `b5ce2a438123f9f9c9b167c5af297c048f15395b`; `README.md` has official blob SHA `98534c18d286e0a651f74028666b1ae97db687ed`.

**Content-level correction**

- Exact official specification/reference snapshot already content-reviewed in Batch 026. No independent skill reports.

### 10. `camillanapoles/skills_agentskills_reference`

**Verified**

- Public repository id `1192975744`; observed stars: `0`.
- Head is exactly `b5ce2a438123f9f9c9b167c5af297c048f15395b`; `README.md` has official blob SHA `98534c18d286e0a651f74028666b1ae97db687ed`.

**Content-level correction**

- Despite the different repository name, this is the same official specification/reference snapshot. No independent skill reports.

## Cross-batch findings

1. **Exact commit reuse prevents false catalog inflation.** Five repositories in this batch are byte-for-byte snapshots of the same already-reviewed official Agent Skills commit, and a sixth is that snapshot plus docs-only presentation changes.
2. **Distribution metadata can diverge without changing skill bodies.** `liangyongqin/zephyr-agent-skills` changes only marketplace packaging after a shared Zephyr skill-tree commit; that should not produce 21 duplicate skill records.
3. **Large domain collections can still be structurally disciplined.** The Zephyr collection uses a consistent hub/specialist split, explicit references/scripts/assets, and per-skill validation checklists.
4. **A bundled skill can drift from its implementation.** `blackwell-systems/agentskills-cli` currently exposes `decompose`, while its bundled guide still instructs `upgrade`. Catalog reports should track this as a source-level correctness issue.
5. **Runtime claims remain separate from source review.** Presence of validation checklists, scripts, or unit tests is evidence of an intended verification surface, not evidence of a successful run.

## Queue handling and exclusions

- `shubha-es/AgentSkills` was checked during queue triage and is currently an empty repository (`size: 0`). It was not counted as one of the 10 completed content reviews and should be reclassified/held rather than treated as a skill collection.
- Several larger unique collections encountered while walking the same indexed queue were **not** marked complete because this run did not finish their full individual-skill review. They remain pending for a later batch. No metadata-only completion was recorded for them.

## Validation boundary

`structure-reviewed` in this batch means repository identity and exact star observation were checked; actual repository content was read; all local `SKILL.md` bodies were directly inspected for the two independent skill-bearing surfaces counted here (21 Zephyr skills + 1 bundled CLI guide); representative material scripts/references were inspected; and exact-commit/delta evidence was used to deduplicate reference snapshots.

It does **not** mean any build, test suite, firmware workflow, CLI mutation, provider integration, external API, hardware test, or eval runner succeeded. Runtime validation remains `not_executed`.
