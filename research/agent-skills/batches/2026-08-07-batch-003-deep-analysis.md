# GitHub Skills Deep Analysis — Batch 003

- Observed at: `2026-08-07T03:00:45+08:00`
- Queue source: `sources/catalog/github-agent-skills-index-latest.json`
- Repositories completed: `10`
- Individual skills reviewed: `23`
- Completion state: `structure-reviewed`
- Runtime validation: `not_executed`

A repository is counted only after its GitHub identity and displayed star count were checked and actual repository content was read. This batch inspected README or equivalent documentation, every identified `SKILL.md`, and representative scripts, references, tests, or evaluation assets where available. No third-party script, installer, renderer, API client, test suite, or generated workflow was executed.

## Batch summary

| Repository | GitHub repository ID | Stars observed | Skills | Main evidence inspected | Result |
|---|---:|---:|---:|---|---|
| `knight6669/knight-imagetopptx-skill` | `1234039920` | `87` | 1 | README, `SKILL.md`, asset validator, bundled reconstruction assets | structure-reviewed |
| `maxazure/video-editing-skill` | `1188135727` | `161` | 1 | README, `SKILL.md`, approval-receipt implementation and tests | structure-reviewed |
| `muxuuu/serenity-skill` | `1228558220` | `3.7k` | 1 | README, `SKILL.md`, scoring script, evaluation cases | structure-reviewed |
| `naive-kun/naive-video-skill` | `1290626763` | `77` | 1 | README, root router Skill, structural/privacy validator | structure-reviewed |
| `ningzimu/image-to-editable-ppt-skill` | `1245952606` | `1.9k` | 1 | multilingual README, Skill contract, CLI/state/worker architecture | structure-reviewed |
| `obra/superpowers` | `1073224795` | `267.8k` | 14 | README and all 14 identified `SKILL.md` files | structure-reviewed |
| `oldred-byte/ec-visual-skill` | `1230019633` | `56` | 1 | README, `SKILL.md`, reference architecture | structure-reviewed |
| `op7418/guizang-ppt-skill` | `1219042200` | `23,315` | 1 | README, `SKILL.md`, template/reference/validation workflow | structure-reviewed |
| `op7418/guizang-social-card-skill` | `1251263546` | `6.0k` | 1 | README, `SKILL.md`, Playwright validator | structure-reviewed |
| `p697/youmind-skill` | `1163955630` | `46` | 1 | README, `SKILL.md`, API client | structure-reviewed; deprecated upstream |

Star values are observations from GitHub on the stated date and can change. Values displayed by GitHub in abbreviated form are retained as displayed.

## 1. `knight6669/knight-imagetopptx-skill`

### Identity and content evidence

- Public repository, default branch `main`.
- Skill: `knight-imagetopptx-skill`.
- Read: `README.md`, `SKILL.md`, `scripts/check_rebuild_assets.py`, and the documented asset/output layout.
- Key blobs inspected:
  - `README.md`: `b3e045d2b70cea3748c79acc3504b6bc910bae9e`
  - `scripts/check_rebuild_assets.py`: `9166b58f6f9ad13a3e8fb4ff190bdcb1632be4c3`

### Architecture and workflow

The package reconstructs screenshot-, image-, PDF-, or image-only-slide input into editable PowerPoint output. Its workflow separates editable text and simple native geometry from visuals that remain generated image assets. The Skill defines input normalization, element inventory, visual classification, text fitting, PPTX construction, rendering, local crop comparison, and final validation.

The bundled validator checks transparent asset bounds, padding, edge contact, and empty-alpha failures. The design therefore treats asset provenance and geometry as explicit QA inputs instead of relying only on visual inspection.

### Strengths and limits

- Strong separation between native-editable and generated visual layers.
- Explicit CJK text and OOXML/font handling.
- Contains reusable validation code and example reconstruction artifacts.
- Depends on image generation, compatible fonts, and a working presentation renderer.
- Visual similarity and editability were not runtime-tested in this review.

## 2. `maxazure/video-editing-skill`

### Identity and content evidence

- Public repository, default branch `main`.
- Skill: `video-editing`.
- Read: README, root `SKILL.md`, `scripts/approval_receipt.py`, `tests/test_approval_receipt.py`, and repository references to publish-package and pipeline-manifest tooling.
- Key blobs inspected:
  - `scripts/approval_receipt.py`: `0897ad8fd3f02ce6bd80fa8e2fc21b6a5a14963b`
  - `tests/test_approval_receipt.py`: `17f04b1078de84996e7a0ce3af3b1e7a86a5b09c`

### Architecture and workflow

This is an end-to-end, local-first editing workflow covering intake, transcription, source review, multicamera timing, rough cut, story/hook design, generation planning, revision, render, subtitle/export, review packages, approval receipts, and publishing artifacts.

A particularly concrete subsystem is the approval receipt. It binds explicitly reviewed project files to SHA-256 hashes, rejects paths outside the project, avoids following symlinks, detects files that change during hashing, and states that the receipt is not an authenticated identity or digital signature. Tests cover current, changed, missing, symlinked, duplicated, self-referential, traversal, volatile-artifact, and CLI strict-mode cases.

### Strengths and limits

- Reversible/source-bound editing is treated as a core invariant.
- Review evidence is byte-bound rather than represented by a prose claim alone.
- Substantial test and script surface is present.
- The repository is operationally large and depends on multiple media tools.
- No test, renderer, or media workflow was executed in this review.

## 3. `muxuuu/serenity-skill`

### Identity and content evidence

- Public repository, default branch `main`.
- Skill: `serenity-skill`.
- Read: README, `SKILL.md`, scoring script, and behavior evaluation cases.
- Key blobs inspected:
  - `SKILL.md`: `a139f330ed3297ef8ab0750ed4aba7fd7e1217e8`
  - `scripts/serenity_scorecard.py`: `1b6db36513a1ce49b5fd9c0eefb776afa9c05c79`
  - `evals/test-cases.md`: `5b9a9451af818941a8e58e29a0689db32ae4ee7f`

### Architecture and workflow

The Skill is a source-backed investment-research workflow, not a trading executor. It translates a market narrative into system changes, maps value-chain layers, identifies hard-to-scale constraints, builds a company universe, grades source quality, ranks research priorities, states failure conditions, and ends with concrete verification steps. It explicitly requires current sources for unstable claims.

The scorecard script applies fixed weights and penalties to a JSON input and emits JSON or Markdown. Evaluation cases cover current-theme research, single-company challenge, hype control, cross-market sourcing, one-question learning mode, and plain-language output.

### Strengths and limits

- Separates value-chain-layer priority from company priority.
- Contains explicit source-quality and risk boundaries.
- Includes deterministic scoring and written behavior tests.
- Score weights are heuristic and are not evidence of investment performance.
- No live-data research or script execution was performed.

## 4. `naive-kun/naive-video-skill`

### Identity and content evidence

- Public repository, default branch `main`.
- Skill: `talking-head-video-pipeline`.
- Read: README, root `SKILL.md`, and `tools/validate_skill.py`.
- Key blobs inspected:
  - `SKILL.md`: `0d1b150459ab9514add108c51f3957936c966b36`
  - `tools/validate_skill.py`: `548930d0d27ac2367c82359ed8a527b3dea66c3a`

### Architecture and workflow

One public Skill acts as a router into internal workflow modules for initialization, rough cut, captions, design, preview, export, revision, status, diagnostics, learning, retrospective, and migration. The project maintains a small state machine from `initialized` through `final_ready`, preserves original media, uses the current working video's main audio as the clock, and requires preview approval before final export unless explicitly waived.

The validator checks frontmatter, exactly one exposed `SKILL.md`, required workflow/files, state-template version consistency, broken Markdown links, private absolute paths, possible secrets, and destructive recursive-deletion patterns.

### Strengths and limits

- Clear single-entry routing and project-local state.
- Explicit recovery, privacy, typography, evidence-readability, and non-destructive rules.
- Structural and privacy constraints are executable rather than prose-only.
- Depends on FFmpeg, Python, Node, HyperFrames/GSAP, fonts, and browser/media behavior.
- No validator or video workflow was executed.

## 5. `ningzimu/image-to-editable-ppt-skill`

### Identity and content evidence

- Public repository, default branch `main`.
- Skill: `image-to-editable-ppt` at `skills/image-to-editable-ppt/SKILL.md`.
- Read: English README, Skill contract, and documented CLI, manifest, image-backend, worker, and state-transition contracts.
- Key Skill blob: `8c009d898d7b8a4a986c4e5134a51c23e80ff28c`.

### Architecture and workflow

The required `editppt` CLI owns run state. `prepare` normalizes pages and creates manifests; single-page work is explicitly claimed by the parent agent, while multi-page work is dispatched to page workers. `run record` accepts only page output that passes manifest-driven validation. `run finalize` rebuilds the final deck from authoritative page manifests, preserving page order and validating media and notes provenance.

The package defines states including `pending`, `dispatched`, `recorded`, `accepted`, and `complete`. Dispatched workers are treated as active leases and cannot be reset merely for being slow. The image-backend order and allowed fallback conditions are explicit, and external processing is restricted to task-local images, prompts, masks, and references.

### Strengths and limits

- Strong ownership boundaries between orchestrator and page workers.
- Manifest authority, resumability, provenance, and explicit lost-worker recovery are well specified.
- Prevents a full-slide raster plus superficial editable-text overlay from being accepted as a valid reconstruction.
- High operational and token complexity; depends on OCR, image backends, subagents, presentation tooling, and external services.
- The repository itself does not promise pixel-perfect reconstruction; no conversion was run here.

## 6. `obra/superpowers`

### Identity and content evidence

- Public repository, default branch `main`.
- Read: root README and all 14 Skill definitions listed below.
- The repository also contains multi-harness adapters, hooks/extensions, infrastructure tests, and an external behavior-evaluation workflow.

### Architecture and workflow

Superpowers is a composable software-development method. The intended closed loop is requirements exploration and design approval, isolated workspace setup, implementation planning, task execution through fresh subagents or a separate execution session, TDD, task/final review, fresh verification, and controlled branch integration.

Several Skills use hard gates. `brainstorming` blocks implementation before approved design; `test-driven-development` blocks production code without a witnessed failing test; `systematic-debugging` blocks fixes before root-cause investigation; `verification-before-completion` blocks success claims without fresh command evidence; branch completion blocks integration until the full test suite is green.

### Strengths and limits

- Strong end-to-end connection between planning, isolated execution, review, validation, and integration.
- Explicit state/recovery ledger and file-based handoffs reduce context-loss failures in long subagent workflows.
- Supports multiple coding-agent harnesses and documents adaptation points.
- Rules are deliberately strict and verbose; context and process overhead can be high for small tasks.
- Some mandatory interaction gates do not fit every autonomous or non-interactive runtime without adaptation.
- No plugin installation, evaluation harness, or test suite was run.

## 7. `oldred-byte/ec-visual-skill`

### Identity and content evidence

- Public repository, default branch `main`.
- Skill: `ec-visual`.
- Read: README, `SKILL.md`, and the reference architecture covering input routing, visual DNA, color, message-picture patterns, head images, detail pages, production, and proof grammar.
- Key blobs inspected:
  - `README.md`: `6ef64bb86a448ee51a86901ed6ce7f5911bedeb7`
  - `SKILL.md`: `84eb81c212b115de1074be515a2c5ead86765f4a`

### Architecture and workflow

The workflow produces a coordinated set of five marketplace head images and ten detail-page screens. It routes product facts, maps buyer concerns to evidence, extracts visual language without copying reference scenes, creates a product/brand-first color system, assigns each screen a concrete picture-only proof statement, and requires one unified approval table before prompt writing or generation.

Hard rules cover claim safety, product presence by message rather than default, no decorative icons, consumer-facing copy, set-level visual diversity, task-folder isolation, and validation/regeneration of each image and the set.

### Strengths and limits

- Converts subjective visual work into inspectable planning and acceptance rules.
- Strong claim-safety and reference-transfer boundaries.
- No scripts, automated tests, or formal eval suite were found in the inspected structure.
- Fixed five-plus-ten output shape and visual doctrine may not fit every commerce task.
- Image-model behavior and visual checks were not executed.

## 8. `op7418/guizang-ppt-skill`

### Identity and content evidence

- Public repository, default branch `main`.
- Skill: `guizang-ppt-skill`.
- Read: README, `SKILL.md`, documented templates, layouts, themes, presenter-mode, screenshot-treatment, checklist, and validator workflow.

### Architecture and workflow

The Skill generates a single-file horizontal HTML presentation using either an editorial/e-ink system or a Swiss-grid system. It includes slide navigation, overview, presenter view, audience display synchronization, notes, timing/rehearsal tools, optional generated images, and a static low-performance fallback.

The workflow checks upstream updates without automatically pulling, captures seven major requirement groups, builds narrative/page rhythm, copies a seed template, selects locked layout structures, validates the result, opens it in a browser, and iterates. Stable slide IDs and presenter notes are treated as part of formal presentation planning.

### Strengths and limits

- Templates, layout vocabulary, and a concrete checklist make visual output reproducible.
- Presenter and audience-mode concerns extend beyond static slide generation.
- Single-file HTML is easy for an agent to edit and deliver.
- It is not a collaborative or native `.pptx` workflow and can depend on browser, CDN, WebGL, fonts, and local rendering behavior.
- No deck or validator was run.

## 9. `op7418/guizang-social-card-skill`

### Identity and content evidence

- Public repository, default branch `main`.
- Skill: `guizang-social-card-skill`.
- Read: README, `SKILL.md`, repository references, and `validate-social-deck.mjs`.
- Validator blob: `7fda20be272ed6708fbda2ab510468bf24766463`.

### Architecture and workflow

This package generates 3:4 social-card sets, paired 21:9 and 1:1 WeChat covers, and short layout-bound motion cards from user-supplied video. It uses editorial or Swiss seed templates, extracts a page story, routes category-specific capabilities, requires evidence images for suitable content types, selects layout recipes, renders HTML with Playwright, and packages final PNG or motion outputs in a task folder.

The Playwright validator inspects every poster section and implements checks for overflow, footer collision, excessive Swiss display weight, minimum readable font size, portrait-density bands, title caps, browser-default figure margin drift, visual bounds, and title spacing. It exits nonzero on failures.

### Strengths and limits

- Strong platform-ratio, evidence-layer, subject-avoidance, and text/readability guidance.
- Automated validation covers real computed layout rather than only static source checks.
- Explicitly states categories and visual styles it cannot reliably produce.
- Depends on Playwright/browser/fonts and, for motion outputs, media and mobile publishing workflows.
- No HTML rendering, validation, or media packaging was executed.

## 10. `p697/youmind-skill`

### Identity and content evidence

- Public repository, default branch `main`.
- Skill: `youmind`.
- The repository README marks the project deprecated and no longer maintained.
- Read: README, `SKILL.md`, and `scripts/api_client.py`.
- Key blobs inspected:
  - `SKILL.md`: `376a405bc73c5752e8153c53304640de39e6f8da`
  - `scripts/api_client.py`: `2ef429b3407ed567e47c431a74062ec632b17e27`

### Architecture and workflow

The Skill routes board, material, chat, generation, and artifact-extraction operations through HTTP APIs. Browser automation is restricted to authentication bootstrap or refresh. Local cookie/browser state is kept under `data/` and is explicitly excluded from commits.

The API client resolves board URLs, loads current cookies from a browser/CDP path or saved state, parses server-sent events, performs board and chat operations, and uploads files through a SHA-256-derived signed-URL flow before attaching them to a board.

### Strengths and limits

- Clean intent boundary between browser authentication and API business operations.
- Explicit local state and hashed upload flow.
- Upstream deprecation is a material adoption blocker.
- The client relies on an unofficial/private API surface and cookie/session assumptions that can change without compatibility guarantees.
- No authentication, API operation, or upload was executed.

## Individual skill reports

| Repository | Skill | Role and contract | Verification evidence inspected | Main limitation |
|---|---|---|---|---|
| `knight6669/knight-imagetopptx-skill` | `knight-imagetopptx-skill` | Reconstruct visual decks into editable PPTX with text/native/image asset separation | Skill workflow and alpha/padding asset validator | Image/render/font dependent |
| `maxazure/video-editing-skill` | `video-editing` | Source-bound, reversible end-to-end video editing and delivery workflow | Receipt implementation and adversarial tests | Large multi-tool surface |
| `muxuuu/serenity-skill` | `serenity-skill` | Source-backed value-chain bottleneck research and thesis stress testing | Scorecard script and six behavior eval scenarios | Heuristic scores; not performance evidence |
| `naive-kun/naive-video-skill` | `talking-head-video-pipeline` | Stateful router for rough cut through verified final export | Structural/privacy/link validator | Media/browser dependency |
| `ningzimu/image-to-editable-ppt-skill` | `image-to-editable-ppt` | Manifest-led, worker-based reconstruction into editable PPTX | CLI/state/record/finalize contracts | High complexity and external services |
| `obra/superpowers` | `brainstorming` | Design and approval gate before implementation | Full Skill read | Interaction-heavy |
| `obra/superpowers` | `dispatching-parallel-agents` | Parallelize independent problem domains with isolated prompts | Full Skill read | Unsafe for shared-state work |
| `obra/superpowers` | `executing-plans` | Execute a written plan task by task with verification | Full Skill read | Stops on ambiguity/blockers |
| `obra/superpowers` | `finishing-a-development-branch` | Test gate and controlled merge/PR/keep/cleanup choices | Full Skill read | Requires repository/test access |
| `obra/superpowers` | `receiving-code-review` | Verify review feedback before accepting or rejecting it | Full Skill read | Deliberately strict communication flow |
| `obra/superpowers` | `requesting-code-review` | Dispatch isolated reviewers at task, feature, and merge gates | Full Skill read | Requires capable subagents |
| `obra/superpowers` | `subagent-driven-development` | Fresh implementer and reviewer loop with ledger and breaker | Full Skill read | High orchestration/context overhead |
| `obra/superpowers` | `systematic-debugging` | Root-cause-first four-phase debugging | Full Skill read | Can be excessive for trivial failures |
| `obra/superpowers` | `test-driven-development` | Mandatory witnessed red-green-refactor cycle | Full Skill read | Strong dogmatic constraints |
| `obra/superpowers` | `using-git-worktrees` | Detect or create safe isolated workspaces and verify baseline | Full Skill read | Host/tool differences require adaptation |
| `obra/superpowers` | `using-superpowers` | Require applicable Skill selection before action | Full Skill read | Very broad trigger policy |
| `obra/superpowers` | `verification-before-completion` | Require fresh command evidence before success claims | Full Skill read | Needs executable verification surface |
| `obra/superpowers` | `writing-plans` | Produce file-specific, test-first, self-reviewed implementation plans | Full Skill read | Plans can become large and repetitive |
| `obra/superpowers` | `writing-skills` | Apply TDD-like pressure scenarios to Skill authoring | Full Skill read | Behavior eval requires subagents/harness |
| `oldred-byte/ec-visual-skill` | `ec-visual` | Plan and produce claim-safe commerce image systems | Skill and nine-reference architecture | No executable test/eval observed |
| `op7418/guizang-ppt-skill` | `guizang-ppt-skill` | Generate and validate single-file HTML presentation systems | Skill/template/reference/checklist workflow | Browser/HTML rather than native PPTX |
| `op7418/guizang-social-card-skill` | `guizang-social-card-skill` | Generate static and short-motion social-card packages | Playwright computed-layout validator | Browser/media/platform dependency |
| `p697/youmind-skill` | `youmind` | API-first board/material/chat/artifact operations | Skill and API client | Deprecated and unstable private API surface |

## Cross-repository findings

1. **The strongest packages make state and evidence explicit.** Manifest files, run states, approval receipts, validators, project-local ledgers, and nonzero failure exits provide more reliable completion evidence than prose-only workflows.
2. **Visual-generation Skills remain partly model- and renderer-dependent.** They can validate geometry, paths, file structure, and some computed layout, but semantic fidelity and visual quality still require rendered-output review.
3. **Single-entry routers reduce accidental Skill proliferation.** The talking-head pipeline and editable-PPT workflow keep internal stages under references or runtime commands instead of exposing every phase as an independent Skill.
4. **Repository popularity is not a quality verdict.** Stars were recorded only as identity/context evidence; completion decisions were based on inspected content.
5. **Deprecation must override superficial feature completeness.** A structurally understandable repository can be marked analyzed while still being unsuitable for new adoption.

## Progress after this batch

- Repositories completed total: `30`
- Individual skills reviewed total: `47`
- Current index snapshot: `1256` unique repositories
- Provisionally deep-analysis eligible: `904`
- Held for identity/content review: `352`
- Estimated eligible repositories remaining: `874`

## Verification boundary

`structure-reviewed` means repository identity and displayed stars were verified, and actual documentation, Skill definitions, and available implementation/validation material were inspected. It does not mean the repository's runtime behavior, dependencies, API calls, rendered output, test suite, security, or claims were independently executed and validated.