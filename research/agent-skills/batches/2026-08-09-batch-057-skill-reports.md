# Agent Skills Individual Reports — Batch 057

- observed_at: `2026-08-09`
- status: `structure-reviewed`
- runtime_validation: `not_executed`
- new_repository_scoped_skill_reports: `1`
- dedup_rule: exact previously reviewed Git trees / Skill blobs are reused only after each repository identity independently passes live identity/Stars and direct repository-content gates.

## `html-ppt` — tree `c9b2a942d2d5bb1639acf5fd943060ccba3f7cf3`

- **Skill blob:** `bf96c77d2a9882d903142229ae028e3eb8e361a4`.
- **Freshly gated repository identities:** `ZWONJAVA/html-ppt-skill`, `RonaldXDZ/html-ppt-skill`, `hhy5277/html-ppt-skill`, `xiaobaiyg09/html-ppt-skill`, `hlong026/html-ppt-skill`, `chatchatbio/html-ppt-skill`, `ajayit233-rgb/html-ppt-skill`, `jerrydawson/html-ppt-skill`.
- **Prior report authority:** Batch 055 content-addressed `html-ppt` report.
- **Fresh verification:** every identity had live metadata/Stars, fixed revision/tree, direct root README, and direct root `SKILL.md` read. The exact tree/Skill identity matches the previously reviewed content.
- **Verified structure:** static HTML/CSS/JS presentation package with token-driven themes, reusable full-deck and single-page templates, references, keyboard/animation runtime, scaffolding/render scripts, examples, and stored visual artifacts.
- **Known gaps reconfirmed:** 31 layouts coexist with stale “none of the 30 fit” prose; stored screenshots are not reproduced test results; the renderer is macOS-specific and uses `--no-sandbox`.
- **Count action:** repository coverage +8; new report count +0.

## `html-ppt` — tree `656ebee6d1e4f3a6b3ea808ed32c5bc361b2fd11`

- **Skill blob:** `05d9ea037f9a664e9af53403222e7dac7bef6135`.
- **Freshly gated repository identity:** `jhzerone/html-ppt-skill`.
- **Prior report authority:** Batch 052 14-deck snapshot.
- **Fresh verification:** live metadata/Stars, fixed revision/tree, direct README, and direct `SKILL.md` read; the content identity exactly matches the previously reviewed snapshot.
- **Verified structure:** 36 themes, 14 full-deck templates, 31 single-page layouts, 27 CSS animations, 20 canvas FX modules, references, runtime, render/scaffold scripts, and stored screenshot artifacts.
- **Count action:** repository coverage +1; new report count +0.

## `g199209/html-ppt-skill::html-ppt` — tree `16a56bc7f8d36a5514b39415090152d1ed6f0890`

- **Repository:** `g199209/html-ppt-skill`.
- **Stars observed:** `0`.
- **Fixed revision:** `a3bd95fe56bd749c1a1ab0e3cfa953a3dbabb362`.
- **Skill blob:** `f9737b38dedbb50bf6b7f0a8950e6408560b2d32`.
- **Status:** new content identity; counted as one new individual Skill report.

### Purpose and routing contract

`html-ppt` routes presentation/PPT/slide/deck requests into a static HTML/CSS/JS authoring workflow. The Skill instructs the agent to establish audience/content, theme, and starting template before authoring; then scaffold from an existing template, replace demo content, add restrained animation, keep presenter-only text inside notes, and render via the bundled script when needed. The routing layer delegates detailed theme/layout/animation/full-deck catalogs to `references/`, which is a useful progressive-disclosure pattern.

### Repository structure

The pinned tree contains root `README.md` and `SKILL.md`; `assets/` with base tokens, 36 theme files, runtime code, 27 CSS animations, FX runtime and 20 canvas modules; `references/` with five detailed guides/catalogs; `templates/` with starter/showcase files, 14 full-deck templates and 31 single-page layouts; `scripts/new-deck.sh`; `scripts/render.sh`; `scripts/verify-output/` PNG artifacts; and a demo deck. No build system is required for normal use.

### Distinctive implementation change

Relative to the shared `9f99b12b...` ancestor, this fork is four commits ahead and modifies `SKILL.md`, `assets/base.css`, `assets/runtime.js`, authoring/animation references, the starter/demo deck, and representative single-page templates. The central change is a fixed 1920×1080 design stage: runtime code creates/reuses `.deck-stage`, moves slide children into it when absent, computes `min(viewportWidth/1920, viewportHeight/1080)`, scales that stage, and independently scales cloned overview thumbnails. Base CSS carries matching design dimensions and a larger fixed-canvas type scale. This is a real behavior change, not just repository metadata or README divergence.

### Scripts and references

`new-deck.sh` is conservative: it checks arguments/template existence, refuses to overwrite an existing output directory, creates a new example directory, and rewrites asset-relative paths. `render.sh` validates its input file and Chrome executable, then launches headless Chrome for one or multiple `#/N` slide captures. `references/authoring-guide.md` defines the workflow from audience/theme selection through in-browser review and PNG export.

### Validation and eval evidence

The tree contains 56 stored PNGs under `scripts/verify-output/`—36 theme-showcase images and 20 animation-showcase images—but no assertion-based visual comparator, browser E2E test, or Skill behavioral eval was found. The current batch did not execute those scripts or reproduce the images. The artifacts therefore demonstrate repository evidence only, not a passing runtime result.

### Findings and gaps

The fixed-canvas design is internally coherent between `base.css` and `runtime.js`, but it adds viewport-scaling and overview-cloning behavior that needs browser-level verification across representative aspect ratios and sizes. Documentation drift remains: the Skill advertises 31 layouts while retaining the stale “none of the 30 fit” instruction, and the README is still the inherited older blob rather than documentation of the fork-specific fixed-stage behavior. `render.sh` remains tied to the macOS Chrome path, uses `--no-sandbox`, and uses a literal class grep for automatic slide count, so it is not a portable regression gate.

### Recommended reusable pattern

Keep the repository's progressive-disclosure split (`SKILL.md` → references → templates/assets/scripts), but make inventories machine-derived and add a browser verification layer that exercises the fixed 1920×1080 stage at multiple viewport sizes, navigation/hash behavior, overview scaling, speaker notes visibility, and deterministic screenshots. Separate screenshot generation from screenshot assertions so artifact existence cannot be confused with test success.

## Batch report accounting

- qualified repository identities completed: `10`
- unique exact Git trees: `3`
- unique directly reviewed Skill bodies: `3`
- new repository-scoped/content-addressed Skill reports: `1`
- cumulative repository-scoped Skill reports: `3088`

## Validation boundary

These reports are source-level analyses. No repository scripts, browser sessions, builds, tests, evals, renders, package installs, or screenshot comparisons were executed. Existing screenshots and documented runtime behavior remain source evidence only.