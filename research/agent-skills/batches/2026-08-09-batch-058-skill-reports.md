# Agent Skills Individual Reports — Batch 058

- observed_at: `2026-08-09`
- status: `structure-reviewed`
- runtime_validation: `not_executed`
- new_repository_scoped_skill_reports: `0`
- dedup_rule: exact previously reviewed Git trees / Skill blobs are reused only after each repository identity independently passes live identity/Stars and direct repository-content gates.

## `html-ppt` — tree `656ebee6d1e4f3a6b3ea808ed32c5bc361b2fd11`

- **Skill blob:** `05d9ea037f9a664e9af53403222e7dac7bef6135`.
- **Freshly gated repository identities:** `fjhua1/html-ppt-skill`, `junyangren/html-ppt-skill`, `59330857/html-ppt-skill`.
- **Prior report authority:** Batch 052 14-deck snapshot.
- **Fresh verification:** all three identities had live metadata/Stars, fixed revision/tree, direct root README, and direct root `SKILL.md` read; their exact tree and Skill body match the prior content report.
- **Verified structure:** 36 themes, 14 full-deck templates, 31 single-page layouts, 27 CSS animations, 20 canvas FX modules, references, runtime, scaffold/render scripts, examples, and stored screenshot artifacts.
- **Known gaps reconfirmed:** Skill prose still says “none of the 30 fit” despite the 31-layout inventory; render tooling is macOS-specific; stored screenshots are not assertion-based tests.
- **Count action:** repository coverage +3; new report count +0.

## `html-ppt` — tree `c9b2a942d2d5bb1639acf5fd943060ccba3f7cf3`

- **Skill blob:** `bf96c77d2a9882d903142229ae028e3eb8e361a4`.
- **Freshly gated repository identities:** `kobe2423man/html-ppt-skill`, `Joe-fly/html-ppt-skill`, `edwardqiu1976/html-ppt-skill`, `shlwsh/html-ppt-skill`, `Upcreat/html-ppt-skill`.
- **Prior report authority:** Batch 055 content-addressed `html-ppt` report.
- **Fresh verification:** all five identities had live metadata/Stars, fixed revision/tree, direct README, and direct `SKILL.md` read. Exact content matches the prior notes-safety snapshot.
- **Verified delta from the older snapshot:** presenter-only text is explicitly forbidden from visible slide markup, and `.notes` is hidden by default in base CSS; this is a useful source-level safety rule for presentation authoring.
- **Known gaps reconfirmed:** 31 layouts coexist with stale “30” prose; no dedicated behavioral eval/browser E2E was found; renderer portability and `--no-sandbox` remain concerns.
- **Count action:** repository coverage +5; new report count +0.

## `html-ppt` — tree `c7a57a16de00fb96b207188c4433630f1cde883e`

- **Skill blob:** `0250b9ac962e2673d8a1b2a88f5782ad0378aba5`.
- **Freshly gated repository identities:** `mingchen666/html-ppt-skill`, `s459517271/html-ppt-skill`.
- **Prior report authority:** Batch 051 presenter-mode content report.
- **Fresh verification:** both identities had live metadata/Stars, fixed revision/tree, direct README and `SKILL.md` reads. Recursive-tree inspection confirms the presenter-mode content identity including `README.zh-CN.md`, `references/presenter-mode.md`, the expanded runtime, templates/assets/scripts, and stored visual artifacts.
- **Verified behavior in source/docs:** S-key presenter popup; CURRENT/NEXT iframe previews; speaker-script and timer cards; draggable/resizable layout; `localStorage` persistence; `BroadcastChannel` synchronization; `postMessage` preview navigation; presenter-specific full-deck template.
- **Documentation drift:** the top-level feature inventory says 15 full-deck templates, while portions of the Skill/README still say 14 in starting-point/project-structure prose.
- **Validation gap:** no automated browser E2E or dedicated Skill behavioral eval was found to prove popup, cross-window sync, persistence, iframe navigation, or the documentation's “pixel-perfect” claim.
- **Count action:** repository coverage +2; new report count +0.

## Batch report accounting

- qualified repository identities completed: `10`
- unique exact Git trees: `3`
- unique directly reviewed Skill bodies: `3`
- new repository-scoped/content-addressed Skill reports: `0`
- cumulative repository-scoped Skill reports: `3088`

## Validation boundary

These are fresh repository gates plus content-addressed reuse of prior individual Skill reports. All ten repositories were independently read before deduplication. No repository scripts, browser sessions, builds, tests, evals, renders, package installs, or screenshot comparisons were executed; existing screenshots and runtime claims remain source/artifact evidence only.
