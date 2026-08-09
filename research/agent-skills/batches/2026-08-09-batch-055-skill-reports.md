# Agent Skills Individual Reports — Batch 055

- observed_at: `2026-08-09`
- status: `structure-reviewed`
- runtime_validation: `not_executed`
- new_repository_scoped_skill_reports: `5`
- dedup_rule: exact previously reviewed Skill blobs/trees are not reported again; distinct content identities may receive repository-scoped variant reports.

## `jovd83/context-density-optimizer` — 1 report

### `context-density-optimizer`

- **Content identity:** fixed tree `8d2d570bd1df52fa22ea246d5725b9343b8bba10`; `SKILL.md` blob `f4035b9dc21e2bab87d4e89d514fd9a8526d2dc6`.
- **Verified:** context-audit Skill that defines a task horizon and classifies material as `KEEP`, `CONDENSE`, `DEFER`, or `DROP`, while protecting authoritative constraints and avoiding automatic file/repository mutation.
- **Value:** explicit decision taxonomy, authority preservation, uncertainty handling, and a useful separation between trigger-selection evaluation and downstream audit-quality evaluation.
- **Risk/gap:** README/badge still identifies version 2.0.0 while `SKILL.md` is 2.1.0; the Telemetry & Logging section is duplicated; the PowerShell eval wrapper and README contain a personal absolute Windows path. The saved 8-case trigger result is 4 pass / 4 fail, but stderr shows the four positive failures coincide with `[WinError 2]`, so that artifact cannot be treated as a demonstrated Skill-quality regression. Automated trigger checks also explicitly do not evaluate downstream audit quality.
- **Validation:** README, `SKILL.md`, eval corpus, eval README, wrapper, saved JSON result/stderr, and evaluation guide inspected. Eval suite not executed in this batch.
- **Reuse recommendation:** retain the task-horizon + KEEP/CONDENSE/DEFER/DROP contract and separate trigger/output eval layers; require portable dependency resolution, environment preflight, and result provenance before using saved eval outcomes as regression evidence.

## `FM7077/Easyimage-uploader` — 1 report

### `easyimage-uploader`

- **Content identity:** fixed tree `d87cfd1ba1bdeb48cf32d45efea7879e5d230407`; `SKILL.md` blob `077ff0cfa99511797ddd595048dc5c556a2e2d87`.
- **Verified:** operational Skill for uploading an existing local image to an EasyImages 2.0 server through `scripts/upload_easyimage.py`, with README/API references and explicit configuration priority.
- **Value:** the Skill keeps the file path as the primary input, avoids unnecessary image interpretation, normalizes API output, tells the agent not to echo the token, and hides delete capability unless explicitly requested.
- **Risk/gap:** execution performs an external network write. CLI `--token` can leak a secret through shell history/process arguments; both HTTP and HTTPS are accepted; the full image/multipart payload is assembled in memory; the multipart boundary is fixed. No repository-local test/eval suite was found.
- **Validation:** README, `SKILL.md`, Python helper, and API reference inspected; no EasyImages server or network request executed.
- **Reuse recommendation:** preserve the explicit output/failure contract and secret-non-echo rule, but move destination authorization and credential provisioning to a centralized capability layer; prefer HTTPS plus environment/secret-file injection over CLI secrets.

## `fr4ngou/claude-code-longrun-skill` — 1 report

### `claude-code-longrun`

- **Content identity:** fixed tree `e8518a45c623c5965edb02276d1f221ff494091f`; `SKILL.md` blob `8977865f952edfc5fbf6b82d01e27a853b3b5216`.
- **Verified:** long-running Claude Code workflow using tmux persistence, a parent/operator role split, a task file, low-frequency monitoring, and explicit session preservation for follow-up work.
- **Value:** clear separation between main task ownership and session-driving responsibility; the task template explicitly records goal, project/context, constraints, requested work, validation, deliverable, and escalation.
- **Risk/gap:** the recommended launch is `claude --permission-mode bypassPermissions`, which expands execution authority. The operation reference also says the operator sends `claude --print` while the concrete example launches interactive Claude with `--permission-mode bypassPermissions`. No test/eval harness is present.
- **Validation:** README, `SKILL.md`, operation examples, and task template inspected; no tmux or Claude Code process executed.
- **Reuse recommendation:** keep persistent-session ownership, low-frequency monitoring, and explicit task/validation contracts; remove permission bypass from the Skill's default path and require a higher-level authorization decision for any expanded filesystem/command/network access.

## `Hellomikiyazi/typewriter-video` — 1 report

### `typewriter-video`

- **Content identity:** fixed tree `6977546c62d8c4d59331ac02e4ad52395944eb90`; `SKILL.md` blob `5fa4eade34174eacfcd2f6cd2b69c904e62dfa68`.
- **Verified:** agentskills.io-format Remotion Skill with a bundled React/TypeScript template, themes, audio/font assets, references, A-roll synchronization guidance, and video preview/render commands.
- **Value:** progressive disclosure between `SKILL.md`, engine source, and references; a deterministic `validate-timing.ts` helper was added to analyze overruns/stalls/timing errors before visual review.
- **Risk/gap:** `package.json` exposes `studio`, `render`, and `still` only; the timing validator, tests, lint, and typecheck are not wired into an automated project gate. Setup/troubleshooting can install packages, clone repositories, download assets, and render output, all of which are side-effectful. Presence of the timing validator does not prove it passes.
- **Validation:** README, `SKILL.md`, recursive tree, package scripts, and timing-validator source/change inspected; npm install/build/render/validator not executed.
- **Reuse recommendation:** keep deterministic timing validation as a pre-visual-review stage, but expose it as a first-class script/CI gate and distinguish type/build/timing checks from actual rendered visual verification.

## `PlatoTheOne/html-ppt-skill` — 1 content-addressed variant report

### `html-ppt` — tree `c9b2a942d2d5bb1639acf5fd943060ccba3f7cf3`

- **Content identity:** `SKILL.md` blob `bf96c77d2a9882d903142229ae028e3eb8e361a4`. Exact content reused by `heimdall-muliy/html-ppt-skill`, `herradaburciaga793-dev/html-ppt-skill`, `allice1203-cloud/html-ppt-skill`, and `1025m/html-ppt-skill` after each repository passed an independent README + `SKILL.md` content gate.
- **Verified:** static HTML/CSS/JS presentation Skill with 36 themes, 14 full-deck templates, 31 page layouts, 27 CSS animations, 20 canvas FX modules, references/catalogs, scaffold scripts, keyboard runtime, and a headless-Chrome screenshot renderer.
- **Value:** token-driven theming, template-first authoring, clear layout/theme/animation separation, speaker-note separation from audience content, and content-addressed reuse across repository forks/copies.
- **Risk/gap:** `SKILL.md` advertises 31 layouts but later refers to “none of the 30”; `scripts/render.sh` hardcodes the macOS Chrome path and uses `--no-sandbox`. The repository's stored verification screenshots are artifacts, not a reproduced validation result for this batch; there is no assertion-based cross-platform visual regression gate established here.
- **Validation:** per-repository README/`SKILL.md` gates plus shared tree and render-script inspection; browser rendering and screenshot comparison not executed.
- **Reuse recommendation:** retain token/layout/template decomposition and presenter-note boundary; make rendering portable/configurable, avoid disabling browser sandbox by default, and add deterministic screenshot comparison with explicit tolerances/provenance.

## Exact-tree reuse without new reports

- `heimdall-muliy/html-ppt-skill`, `herradaburciaga793-dev/html-ppt-skill`, `allice1203-cloud/html-ppt-skill`, and `1025m/html-ppt-skill` reuse the `c9b2a942...` report above only after direct per-repository content gates.
- `hekiki/html-ppt-skill` fixed tree `c7a57a16de00fb96b207188c4433630f1cde883e` was already reported from upstream `lewislulu/html-ppt-skill` in Batch 051, so Batch 055 records repository coverage without creating another Skill report.

## Batch validation boundary

These five reports are source-level, repository-scoped/content-addressed analyses. `runtime_validation=not_executed` applies to every entry. Saved eval results, validators, screenshots, scripts, and render assets are recorded as repository evidence only and are never interpreted as successful execution in this batch.
