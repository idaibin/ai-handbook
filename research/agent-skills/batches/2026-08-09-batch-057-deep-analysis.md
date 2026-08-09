# Agent Skills Deep Analysis — Batch 057

- observed_at: `2026-08-09`
- status: `structure-reviewed`
- runtime_validation: `not_executed`
- source_queue: `sources/catalog/batches/agentskills-created-2026-04-16-deterministic.json`
- repositories_completed: `10`
- root_readmes_directly_read: `10`
- repository_skill_files_read: `10`
- direct_unique_skill_body_reviews: `3`
- direct_unique_git_trees: `3`
- new_repository_scoped_skill_reports: `1`

## Completion gate

Every repository counted below passed the fixed-revision gate: live GitHub repository identity, current Stars observation, fixed commit/tree capture, direct root `README.md` read, direct root `SKILL.md` read, and content identity inspection. Exact-tree reuse was applied only after the repository-specific content gate. No repository was marked complete from indexed/search metadata alone.

| Repository | Stars | Fixed revision | Git tree | `SKILL.md` blob | Content action |
| --- | ---: | --- | --- | --- | --- |
| `ZWONJAVA/html-ppt-skill` | 0 | `376dfe5e777c2bce28a7368a8355212451a3e33b` | `c9b2a942d2d5bb1639acf5fd943060ccba3f7cf3` | `bf96c77d2a9882d903142229ae028e3eb8e361a4` | exact-tree reuse; prior report Batch 055 |
| `RonaldXDZ/html-ppt-skill` | 0 | `376dfe5e777c2bce28a7368a8355212451a3e33b` | `c9b2a942d2d5bb1639acf5fd943060ccba3f7cf3` | `bf96c77d2a9882d903142229ae028e3eb8e361a4` | exact-tree reuse; prior report Batch 055 |
| `hhy5277/html-ppt-skill` | 0 | `376dfe5e777c2bce28a7368a8355212451a3e33b` | `c9b2a942d2d5bb1639acf5fd943060ccba3f7cf3` | `bf96c77d2a9882d903142229ae028e3eb8e361a4` | exact-tree reuse; prior report Batch 055 |
| `xiaobaiyg09/html-ppt-skill` | 0 | `376dfe5e777c2bce28a7368a8355212451a3e33b` | `c9b2a942d2d5bb1639acf5fd943060ccba3f7cf3` | `bf96c77d2a9882d903142229ae028e3eb8e361a4` | exact-tree reuse; prior report Batch 055 |
| `hlong026/html-ppt-skill` | 1 | `376dfe5e777c2bce28a7368a8355212451a3e33b` | `c9b2a942d2d5bb1639acf5fd943060ccba3f7cf3` | `bf96c77d2a9882d903142229ae028e3eb8e361a4` | exact-tree reuse; prior report Batch 055 |
| `chatchatbio/html-ppt-skill` | 0 | `376dfe5e777c2bce28a7368a8355212451a3e33b` | `c9b2a942d2d5bb1639acf5fd943060ccba3f7cf3` | `bf96c77d2a9882d903142229ae028e3eb8e361a4` | exact-tree reuse; prior report Batch 055 |
| `ajayit233-rgb/html-ppt-skill` | 0 | `376dfe5e777c2bce28a7368a8355212451a3e33b` | `c9b2a942d2d5bb1639acf5fd943060ccba3f7cf3` | `bf96c77d2a9882d903142229ae028e3eb8e361a4` | exact-tree reuse; prior report Batch 055 |
| `jerrydawson/html-ppt-skill` | 0 | `376dfe5e777c2bce28a7368a8355212451a3e33b` | `c9b2a942d2d5bb1639acf5fd943060ccba3f7cf3` | `bf96c77d2a9882d903142229ae028e3eb8e361a4` | exact-tree reuse; prior report Batch 055 |
| `jhzerone/html-ppt-skill` | 0 | `9f99b12b1245b05e8db1c3efc9844a3961e041c0` | `656ebee6d1e4f3a6b3ea808ed32c5bc361b2fd11` | `05d9ea037f9a664e9af53403222e7dac7bef6135` | exact-tree reuse; prior report Batch 052 |
| `g199209/html-ppt-skill` | 0 | `a3bd95fe56bd749c1a1ab0e3cfa953a3dbabb362` | `16a56bc7f8d36a5514b39415090152d1ed6f0890` | `f9737b38dedbb50bf6b7f0a8950e6408560b2d32` | new content identity; new Skill report |

## Deep-analysis findings

### 1. Nine repository identities are exact-content reuse; one is a real evolved fork

Eight identities resolve to the already reviewed `c9b2a942...` tree and `bf96c77d...` Skill blob. `jhzerone/html-ppt-skill` resolves to the already reviewed `656ebee6...` tree and `05d9ea03...` Skill blob. `g199209/html-ppt-skill` is materially different: its fixed tree is `16a56bc7...` and its Skill blob is `f9737b38...`. Comparing that fork against the shared `9f99b12b...` ancestor shows four additional commits modifying `SKILL.md`, `assets/base.css`, `assets/runtime.js`, authoring/animation references, the starter deck, demo deck, and multiple single-page templates. Repository identity and content identity therefore remain separate accounting dimensions.

### 2. The evolved fork introduces a fixed 1920×1080 design canvas and viewport scaling

The new `g199209` tree changes the presentation runtime from viewport-sized slides to a fixed `1920×1080` design stage. `assets/runtime.js` creates or reuses `.deck-stage`, moves deck children into it when needed, scales the stage using the smaller viewport/design ratio, and separately rescales cloned overview thumbnails. `assets/base.css` defines matching design-width/design-height variables and significantly increases the type scale for the fixed canvas. This is a coherent approach for deterministic 16:9 authoring, but it materially expands the runtime behavior that should be browser-tested at multiple viewport sizes.

### 3. The fork keeps the useful progressive-disclosure architecture

The fixed tree retains the established structure: root `SKILL.md` as the agent-facing dispatcher; `references/` for themes, layouts, animations, full-deck templates, and authoring workflow; `assets/` for design tokens, themes, runtime, and canvas/CSS animation modules; `templates/` for reusable full-deck and single-page patterns; `scripts/new-deck.sh` for scaffolding; `scripts/render.sh` for PNG capture; and `examples/` plus stored screenshot artifacts. The separation is suitable for selective loading and avoids placing the full catalog in the routing layer.

### 4. Manual inventory drift still survives the fork

The fork advertises 31 single-page layouts, but its `SKILL.md` still says to add a new layout only when none of the “30” fit. The root README remains the same blob as the older shared snapshot, so it does not document the fork-specific 1920×1080 stage/runtime changes. This is a concrete example of implementation evolution outpacing manually maintained prose. Machine-derived inventory checks and a small documentation drift gate would reduce this class of error.

### 5. Stored screenshots are evidence artifacts, not a behavioral test suite

The evolved tree includes 56 PNGs under `scripts/verify-output/` (36 theme-showcase captures plus 20 animation-showcase captures), but the scripts directory contains only `new-deck.sh`, `render.sh`, and those stored images. No assertion-based visual comparator, browser E2E suite, or Skill behavioral eval was found in the pinned tree. Existing screenshots therefore remain source artifacts and are not promoted to “tests passed.”

### 6. Rendering remains macOS-specific and weak as a portable validation gate

`render.sh` hard-codes `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`, uses `--no-sandbox`, and counts slides for `all` by grepping the literal `class="slide"` form. It can generate screenshots on the expected macOS environment, but it is not a portable or assertion-based validation system. A stronger gate would discover/preflight Chromium, execute representative viewport/browser cases, assert slide count and navigation behavior, and compare deterministic output rather than merely writing PNG files.

## Validation boundary

This batch inspected live repository metadata, fixed commits/trees, direct README and Skill contents for all ten repository identities, the new fork's recursive tree, `scripts/new-deck.sh`, `scripts/render.sh`, `references/authoring-guide.md`, `assets/runtime.js`, stored verification artifacts, and the fork-vs-ancestor commit comparison. No repository script, browser session, render, package install, build, test, eval, screenshot comparison, or network API owned by the repositories was executed. `runtime_validation=not_executed` is retained.

## Progress

- repositories_structure_reviewed_total: `570`
- repository_scoped_skill_reports_total: `3088`
- canonical_eligible_basis: `2088`
- arithmetic_remaining_estimate: `1518`
- canonical_reconciliation: `pending`
- next_unresolved_candidate: `fjhua1/html-ppt-skill`
