# Agent Skills Deep Analysis — Batch 058

- observed_at: `2026-08-09`
- status: `structure-reviewed`
- runtime_validation: `not_executed`
- source_queue: `sources/catalog/batches/agentskills-created-2026-04-16-deterministic.json`
- repositories_completed: `10`
- root_readmes_directly_read: `10`
- repository_skill_files_read: `10`
- direct_unique_skill_body_reviews: `3`
- direct_unique_git_trees: `3`
- new_repository_scoped_skill_reports: `0`

## Completion gate

Every repository counted below passed the repository-specific gate: live GitHub identity, current Stars observation, fixed commit/tree capture, direct root `README.md` read, direct root `SKILL.md` read, and content identity inspection. Recursive structure inspection was performed for each of the three exact Git trees; repositories sharing an exact tree inherit the identical structure only after their own README/Skill gate. No repository was marked complete from queue/search metadata alone.

| Repository | Stars | Fixed revision | Git tree | `SKILL.md` blob | Content action |
| --- | ---: | --- | --- | --- | --- |
| `fjhua1/html-ppt-skill` | 0 | `9f99b12b1245b05e8db1c3efc9844a3961e041c0` | `656ebee6d1e4f3a6b3ea808ed32c5bc361b2fd11` | `05d9ea037f9a664e9af53403222e7dac7bef6135` | exact-tree reuse; prior report Batch 052 |
| `kobe2423man/html-ppt-skill` | 0 | `376dfe5e777c2bce28a7368a8355212451a3e33b` | `c9b2a942d2d5bb1639acf5fd943060ccba3f7cf3` | `bf96c77d2a9882d903142229ae028e3eb8e361a4` | exact-tree reuse; prior report Batch 055 |
| `mingchen666/html-ppt-skill` | 0 | `f3a8435d3901697d5ac5e64d356c933637e43107` | `c7a57a16de00fb96b207188c4433630f1cde883e` | `0250b9ac962e2673d8a1b2a88f5782ad0378aba5` | exact-tree reuse; prior report Batch 051 |
| `junyangren/html-ppt-skill` | 0 | `9f99b12b1245b05e8db1c3efc9844a3961e041c0` | `656ebee6d1e4f3a6b3ea808ed32c5bc361b2fd11` | `05d9ea037f9a664e9af53403222e7dac7bef6135` | exact-tree reuse; prior report Batch 052 |
| `Joe-fly/html-ppt-skill` | 0 | `376dfe5e777c2bce28a7368a8355212451a3e33b` | `c9b2a942d2d5bb1639acf5fd943060ccba3f7cf3` | `bf96c77d2a9882d903142229ae028e3eb8e361a4` | exact-tree reuse; prior report Batch 055 |
| `edwardqiu1976/html-ppt-skill` | 0 | `376dfe5e777c2bce28a7368a8355212451a3e33b` | `c9b2a942d2d5bb1639acf5fd943060ccba3f7cf3` | `bf96c77d2a9882d903142229ae028e3eb8e361a4` | exact-tree reuse; prior report Batch 055 |
| `shlwsh/html-ppt-skill` | 0 | `376dfe5e777c2bce28a7368a8355212451a3e33b` | `c9b2a942d2d5bb1639acf5fd943060ccba3f7cf3` | `bf96c77d2a9882d903142229ae028e3eb8e361a4` | exact-tree reuse; prior report Batch 055 |
| `59330857/html-ppt-skill` | 0 | `9f99b12b1245b05e8db1c3efc9844a3961e041c0` | `656ebee6d1e4f3a6b3ea808ed32c5bc361b2fd11` | `05d9ea037f9a664e9af53403222e7dac7bef6135` | exact-tree reuse; prior report Batch 052 |
| `Upcreat/html-ppt-skill` | 0 | `376dfe5e777c2bce28a7368a8355212451a3e33b` | `c9b2a942d2d5bb1639acf5fd943060ccba3f7cf3` | `bf96c77d2a9882d903142229ae028e3eb8e361a4` | exact-tree reuse; prior report Batch 055 |
| `s459517271/html-ppt-skill` | 0 | `f3a8435d3901697d5ac5e64d356c933637e43107` | `c7a57a16de00fb96b207188c4433630f1cde883e` | `0250b9ac962e2673d8a1b2a88f5782ad0378aba5` | exact-tree reuse; prior report Batch 051 |

## Deep-analysis findings

### 1. Ten repository identities collapse to three previously reviewed exact content identities

Three repositories resolve to tree `656ebee6...`, five to `c9b2a942...`, and two to presenter-mode tree `c7a57a16...`. Their `SKILL.md` blobs also match the previously reviewed content identities exactly. Repository coverage therefore increases by ten, while the individual Skill-report count does not increase. This preserves the distinction between repository identity and content identity instead of manufacturing duplicate reports for forks.

### 2. The package architecture remains a useful progressive-disclosure example

Across all three content identities, root `SKILL.md` is the agent-facing routing contract; `references/` contains detailed catalogs and authoring guidance; `assets/` contains tokens, themes, runtime, and animation modules; `templates/` contains reusable full-deck and single-page structures; and `scripts/` handles scaffolding/rendering. The presenter-mode tree expands this with `README.zh-CN.md`, `references/presenter-mode.md`, and a substantially larger runtime while preserving the same high-level separation.

### 3. Manual inventory drift remains visible in both older and presenter-mode content

The older Skill advertises 31 layouts while retaining an instruction to add a layout only if none of the “30” fit. The presenter-mode content advertises 15 full-deck templates, but portions of its README/Skill project-structure and starting-point prose still refer to 14. These are source-level verified documentation inconsistencies and support deriving inventory counts from the tree rather than maintaining them in several prose locations.

### 4. Screenshot generation is not equivalent to behavioral or visual-regression validation

`scripts/render.sh` hard-codes `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`, launches Chrome with `--no-sandbox`, and writes 1920×1080 screenshots. The trees contain stored verification PNGs, but no assertion-based image comparator, browser E2E suite, or dedicated Skill behavioral eval was found by source inspection/search. Screenshot existence is therefore artifact evidence, not a passing test result.

### 5. Presenter mode materially increases runtime behavior without matching browser E2E evidence

The presenter content adds a popup window with current/next iframe previews, speaker-script and timer cards, drag/resize persistence in `localStorage`, cross-window synchronization through `BroadcastChannel`, and iframe navigation through `postMessage`. Documentation calls the previews pixel-perfect and synchronization smooth, but no automated browser test was found that proves popup creation, cross-window synchronization, storage restoration, preview switching, or failure handling. These remain implementation/documentation claims, not runtime-validated conclusions.

### 6. A content-addressed catalog avoids repeated analysis while retaining repository provenance

This batch is a clean example of why catalog state should keep three dimensions separately: repository identity and Stars, exact revision/tree/blob identity, and validation state. All ten identities were independently gated, yet no new Skill body existed. Reusing prior content reports after exact-tree confirmation prevents inflated report counts without losing fork/repository provenance.

## Validation boundary

This batch read live repository metadata and Stars, fixed current commits/trees, every repository's root README and `SKILL.md`, recursive structure for all three unique trees, the screenshot render script, and presenter-mode reference material. Source search found no dedicated eval/test suite for the representative content identities. No repository script, package install, browser session, render, build, test, eval, network API, or screenshot comparison was executed. `runtime_validation=not_executed` is retained.

## Progress

- repositories_structure_reviewed_total: `580`
- repository_scoped_skill_reports_total: `3088`
- canonical_eligible_basis: `2088`
- arithmetic_remaining_estimate: `1508`
- canonical_reconciliation: `pending`
- next_unresolved_candidate: `wonderbench/html-ppt-skill`
