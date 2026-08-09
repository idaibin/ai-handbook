# Agent Skills Deep Analysis — Batch 055

- observed_at: `2026-08-09`
- status: `structure-reviewed`
- runtime_validation: `not_executed`
- queue_source: `sources/catalog/batches/agentskills-created-2026-04-16-deterministic.json`
- qualified_repository_identities_completed: `10`
- root_readmes_directly_read: `10`
- skill_or_equivalent_files_directly_read: `10`
- direct_unique_skill_body_reviews: `6`
- unique_git_trees: `6`
- new_repository_scoped_skill_reports: `5`
- completion_rule: repository identity and current Stars were verified, a fixed revision/tree was established, and actual repository content was read before completion. Metadata-only candidates were not promoted.

## Summary

Batch 055 advances the existing indexed queue by ten qualified repository identities. Three entries that had been indexed as adjacent search hits (`jovd83/context-density-optimizer`, `FM7077/Easyimage-uploader`, and `Hellomikiyazi/typewriter-video`) were promoted only after direct repository-content gates proved they are genuine Agent Skill packages. `agent-skills-manager/mempalace` was encountered in queue order but rejected after its fixed tree and README showed an application/package-manager repository rather than a Skill package, so it was not used to fill the ten completed identities.

No repository code, tests, evals, builds, browser flows, live APIs, package installs, external uploads, Claude Code sessions, video renders, or presentation renders were executed. Existing result files and verification artifacts were inspected as repository evidence only.

| Repository | Stars | Fixed revision | Fixed tree | New reports | Result |
|---|---:|---|---|---:|---|
| `jovd83/context-density-optimizer` | 0 | `e2544b2e7dec33589194ee541b3ebcf3e1a3bf67` | `8d2d570bd1df52fa22ea246d5725b9343b8bba10` | 1 | structure-reviewed; adjacent hit promoted after content gate |
| `FM7077/Easyimage-uploader` | 0 | `80e44a4df40763ade46a776f18aea44b44db5b2a` | `d87cfd1ba1bdeb48cf32d45efea7879e5d230407` | 1 | structure-reviewed; adjacent hit promoted after content gate |
| `fr4ngou/claude-code-longrun-skill` | 0 | `9e8af4e15ba1c940d9f889fe89d28c73506f425d` | `e8518a45c623c5965edb02276d1f221ff494091f` | 1 | structure-reviewed |
| `Hellomikiyazi/typewriter-video` | 0 | `840b118318b0faa1b7dc82cca35ef67d790c0ee7` | `6977546c62d8c4d59331ac02e4ad52395944eb90` | 1 | structure-reviewed; adjacent hit promoted after content gate |
| `PlatoTheOne/html-ppt-skill` | 0 | `376dfe5e777c2bce28a7368a8355212451a3e33b` | `c9b2a942d2d5bb1639acf5fd943060ccba3f7cf3` | 1 | structure-reviewed; new content-addressed html-ppt variant |
| `heimdall-muliy/html-ppt-skill` | 0 | `376dfe5e777c2bce28a7368a8355212451a3e33b` | `c9b2a942d2d5bb1639acf5fd943060ccba3f7cf3` | 0 | structure-reviewed; exact-tree reuse |
| `herradaburciaga793-dev/html-ppt-skill` | 0 | `376dfe5e777c2bce28a7368a8355212451a3e33b` | `c9b2a942d2d5bb1639acf5fd943060ccba3f7cf3` | 0 | structure-reviewed; exact-tree reuse |
| `allice1203-cloud/html-ppt-skill` | 0 | `376dfe5e777c2bce28a7368a8355212451a3e33b` | `c9b2a942d2d5bb1639acf5fd943060ccba3f7cf3` | 0 | structure-reviewed; exact-tree reuse |
| `hekiki/html-ppt-skill` | 0 | `f3a8435d3901697d5ac5e64d356c933637e43107` | `c7a57a16de00fb96b207188c4433630f1cde883e` | 0 | structure-reviewed; exact-tree content already reported from upstream `lewislulu/html-ppt-skill` in Batch 051 |
| `1025m/html-ppt-skill` | 0 | `376dfe5e777c2bce28a7368a8355212451a3e33b` | `c9b2a942d2d5bb1639acf5fd943060ccba3f7cf3` | 0 | structure-reviewed; exact-tree reuse |

Stars are point-in-time observations from GitHub during this run.

## Repository analyses

### 1. `jovd83/context-density-optimizer`

**Verified**

- The fixed tree contains an Agent Skill with `SKILL.md`, references, an OpenAI manifest, trigger-eval data/results, and a PowerShell eval wrapper.
- The Skill defines a bounded context-audit workflow using `KEEP`, `CONDENSE`, `DEFER`, and `DROP`; it explicitly protects authoritative constraints and does not perform automatic file/repository mutation.
- README/version documentation has drift: README content/badges still describe `2.0.0`, while the fixed `SKILL.md` metadata and latest change are `2.1.0`.
- The `SKILL.md` contains the same Telemetry & Logging subsection twice.
- The trigger-eval corpus contains eight cases, four expected-trigger and four expected-non-trigger. The committed latest result records four passes and four failures, but all four positive failures coincide with an environment/tool launch failure (`[WinError 2]`) in stderr. The artifact therefore does not establish a Skill trigger-quality regression.
- The eval wrapper and README contain a machine-specific Windows path under `C:\Users\jochi\...`, so the checked-in harness is not portable as written.
- The eval README explicitly limits the automated suite to trigger behavior rather than downstream context-audit quality; a separate prose evaluation guide defines output-quality scenarios/checklists.

**Inference**

- Separating trigger selection from output-quality evaluation is a useful pattern, but the harness needs portable dependency discovery and environment preflight before its results can serve as reproducible regression evidence.

**Not verified**

- Trigger accuracy in a working Claude/evaluator environment or audit-output quality on real tasks.

### 2. `FM7077/Easyimage-uploader`

**Verified**

- The fixed tree contains a root `SKILL.md`, README, `scripts/upload_easyimage.py`, configuration example, and EasyImages API reference.
- The Skill resolves server/token configuration in an explicit priority order and instructs the agent not to echo the token or expose the delete URL unless requested.
- The Python helper performs a real network write: it reads the local image, builds multipart data, and sends `POST /api/index.php` to a configured EasyImages server, then normalizes the response as JSON.
- The helper permits both `http://` and `https://`; it also supports passing the token via `--token`, which can expose a credential through command history/process arguments.
- The multipart body is constructed in memory and uses a fixed boundary string. No repository-local tests/evals were found in the reviewed package.

**Inference**

- External-upload authorization, destination policy, and secret injection should be enforced above this Skill rather than implied by activation. Environment/config-based credentials are safer defaults than command-line secrets.

**Not verified**

- EasyImages API behavior, upload success/failure handling against a live service, large-file behavior, or TLS/security posture.

### 3. `fr4ngou/claude-code-longrun-skill`

**Verified**

- The package contains one Skill plus task-file and operation-example references.
- It uses a two-agent architecture: the parent creates a tmux session/task file; an operator drives Claude Code through that session, monitors at low frequency, and preserves the session for follow-up turns.
- The task template explicitly separates goal, project context, constraints, requested work, validation, deliverable, and escalation.
- The prescribed Claude Code launch command is `claude --permission-mode bypassPermissions`. This expands execution authority rather than preserving a default permission boundary.
- The operation reference has documentation drift: prose says the operator sends `claude --print`, while the actual example launches interactive Claude with `--permission-mode bypassPermissions`.
- No tests/evals are present in the fixed tree.

**Inference**

- Session persistence and low-frequency monitoring are useful long-task patterns, but permission mode should be a separately authorized policy decision. A Skill should not silently widen command/filesystem/network authority merely because long-running execution was requested.

**Not verified**

- tmux behavior, Claude Code execution, session recovery, monitoring correctness, or follow-up context reuse.

### 4. `Hellomikiyazi/typewriter-video`

**Verified**

- The repository is a real agentskills.io-format Skill backed by a Remotion/React template, bundled fonts/audio assets, references, and rendering source.
- `SKILL.md` directs the agent through template copy, npm install, engine/reference reading, content authoring, preview, and render steps. It may also download/recover external assets when missing.
- The latest fixed revision includes `validate-timing.ts`, a deterministic timing-analysis helper intended to catch overruns, stalls, and timing mistakes before visual review.
- `package.json` exposes `studio`, `render`, and `still` commands but does not wire the timing validator, tests, lint, or typecheck into an automated validation script.

**Inference**

- The timing validator is meaningful verification source, but until it is wired into an executable gate and run, its presence is not equivalent to a passing regression suite. Package installation, asset downloads, and rendering are side effects that should remain explicitly authorized.

**Not verified**

- npm installation, Remotion build/render behavior, timing-validator output, audio/visual correctness, or generated video quality.

### 5–8 and 10. Shared `html-ppt` tree (`PlatoTheOne`, `heimdall-muliy`, `herradaburciaga793-dev`, `allice1203-cloud`, `1025m`)

**Verified**

- Each repository identity and Stars count was checked independently, and each README plus root `SKILL.md` was directly read before exact-tree reuse was accepted.
- All five identities resolve to the exact tree `c9b2a942d2d5bb1639acf5fd943060ccba3f7cf3` and the same `SKILL.md` blob `bf96c77d2a9882d903142229ae028e3eb8e361a4`.
- The package is a substantial static-HTML presentation Skill: 36 themes, 14 full-deck templates, 31 layouts, 27 CSS animations, 20 canvas FX modules, runtime navigation, references, templates, scaffolding, and a Chrome screenshot renderer.
- The Skill says there are 31 layouts but later says to create a new layout only if none of the “30” fit, a concrete stale inventory reference.
- `scripts/render.sh` hardcodes the macOS Google Chrome path and launches headless Chrome with `--no-sandbox`, so the renderer is host-specific and weakens browser sandboxing.
- Repository screenshot artifacts under `scripts/verify-output/` are evidence that files exist, not evidence that Batch 055 reproduced them.

**Inference**

- Token/theme/layout separation and template-first authoring are useful reusable design patterns. Cross-platform rendering and an assertion-based visual/regression harness would materially improve verifiability.

**Not verified**

- Browser rendering, screenshots, animations, presenter behavior, theme fidelity, or visual quality.

### 9. `hekiki/html-ppt-skill`

**Verified**

- This repository has a different evolved tree with presenter-mode runtime, `BroadcastChannel`/`postMessage` synchronization, a presenter reference, and 15 full-deck templates.
- Current top-level sections say 15 full-deck templates, while multiple stale locations still say 14; the Skill also retains the same “30” wording despite advertising 31 layouts.
- Exact tree `c7a57a16de00fb96b207188c4433630f1cde883e` was already structure-reviewed and reported through upstream `lewislulu/html-ppt-skill` in Batch 051. The current repository identity therefore increases coverage only after a direct content gate; it does not create a duplicate individual Skill report.

**Not verified**

- Presenter-window synchronization, popup behavior, preview fidelity, browser security, render scripts, screenshots, or any runtime path.

## Content-gate exclusion observed

### `agent-skills-manager/mempalace`

- Identity and 1 Star were verified at fixed revision `b8414d18fae51ee92238878ce86d54a8d7d4eb54`, tree `404f28040b2310085e81fbec79c2f924f88c0867`.
- The fixed tree contains a Python application/package-manager implementation and README but no `SKILL.md` or equivalent Skill package.
- README describes a package manager/integration environment with discovery, scanning, deployment, registry, and installer/application behavior.
- It was therefore classified as adjacent tooling/application and was **not** counted as one of the ten completed Skill repositories.

## Cross-batch findings

1. **Indexed class is provisional, not authoritative.** Three adjacent-index entries became qualified only after direct Skill/package reads; one repository with “AgentSkill” in its description was rejected after its tree proved it was tooling/application instead.
2. **A failing checked-in eval artifact is not automatically a Skill failure.** `context-density-optimizer` records four failed positive cases, but stderr ties those failures to a missing executable/environment. Result provenance must preserve environment/tool failure separately from model/Skill behavior.
3. **Eval portability is part of reproducibility.** Hard-coded personal paths and missing dependency preflights make a nominally automated evaluation non-reproducible on another host.
4. **Authorization belongs above individual Skills.** This batch includes remote file upload, permission-bypassed coding-agent execution, package/network downloads, and browser/render commands. Activation should not imply blanket authority for those effects.
5. **Content-addressed dedup prevents fork inflation.** Five html-ppt identities share one exact new tree and receive one report; `hekiki` reuses an exact tree already reported from upstream in Batch 051.
6. **Validation-source presence is not execution proof.** Timing validators, screenshot directories, eval definitions, or saved results were not converted into `runtime-validated` status.
7. **README/SKILL inventories drift.** The html-ppt variants contain 31-versus-30 and 15-versus-14 stale counts; `context-density-optimizer` also has 2.0-versus-2.1 version drift.

## Queue resume

The next unresolved indexed candidate after the ten completed identities is `LovisYuan/html-ppt-skill`. It remains subject to the same identity/Stars/fixed-revision/content gate before any completion accounting.

## Validation boundary

`structure-reviewed` means repository identity/Stars were checked, a fixed revision/tree was recorded, README and Skill/equivalent definitions were directly inspected, and scripts/references/eval surfaces were read when available and material. It does **not** mean any repository runtime, test, build, browser flow, network API, package install, external upload, coding-agent session, video render, presentation render, or eval suite executed successfully.
