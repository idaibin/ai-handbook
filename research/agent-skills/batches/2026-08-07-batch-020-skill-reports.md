# Agent Skills Deep Analysis — Batch 020 Skill Reports

- Batch: `2026-08-07-batch-020`
- Repository-scoped skill reports: **42**
- Evidence level: actual `SKILL.md` / equivalent repository content read
- Runtime validation: **not executed**
- Rule: upstream or externally fetched skills are not counted as repository-scoped skills.

## phronetic-ai/agentskills :: pdf

- Path: `skills/pdf/SKILL.md`
- Purpose: PDF extraction, creation, merging/splitting, forms, OCR, and document processing workflows.
- Structure: instruction-heavy skill with referenced supporting files and command/tool examples.
- Evidence: actual `SKILL.md` read. The repository SDK can discover resources and scripts, but this batch did not execute PDF tooling.
- Status: `source-read`; runtime `not_executed`.

## phronetic-ai/agentskills :: xlsx

- Path: `skills/xlsx/SKILL.md`
- Purpose: spreadsheet creation, editing, formulas, formatting, analysis, and verification.
- Structure: prescriptive spreadsheet workflow with formula/recalculation/error-checking requirements and supporting scripts/resources.
- Evidence: actual `SKILL.md` read. The skill explicitly requires recalculation/verification steps; those steps were not run in this batch.
- Status: `source-read`; runtime `not_executed`.

## phronetic-ai/agentskills :: pptx

- Path: `skills/pptx/SKILL.md`
- Purpose: presentation reading, editing, creation, OOXML inspection, and slide-generation workflows.
- Structure: progressive instructions covering content extraction, raw XML, creation, design, and helper scripts.
- Evidence: actual `SKILL.md` read. No PowerPoint generation or rendering was executed.
- Status: `source-read`; runtime `not_executed`.

## phronetic-ai/agentskills :: docx

- Path: `skills/docx/SKILL.md`
- Purpose: DOCX creation/editing, tracked changes, comments, OOXML manipulation, and redlining workflows.
- Structure: decision-tree workflow with detailed references for OOXML and document generation.
- Evidence: actual `SKILL.md` read. No document conversion, OOXML edit, or package round-trip was executed.
- Status: `source-read`; runtime `not_executed`.

## phronetic-ai/agentskills :: canvas-design

- Path: `skills/canvas-design/SKILL.md`
- Purpose: create original static visual design artifacts from an explicit design philosophy.
- Structure: two-stage philosophy-then-artifact workflow with strong visual/craft constraints.
- Evidence: actual `SKILL.md` read. No PNG/PDF artifact generation was executed.
- Status: `source-read`; runtime `not_executed`.

## phronetic-ai/agentskills :: algorithmic-art

- Path: `skills/algorithmic-art/SKILL.md`
- Purpose: generative art using p5.js, seeded randomness, parameter exploration, and algorithmic systems.
- Structure: philosophy stage followed by implementation, with templates/assets intended to constrain the generated viewer.
- Evidence: actual `SKILL.md` read. No browser execution or generated sketch validation was performed.
- Status: `source-read`; runtime `not_executed`.

## phronetic-ai/agentskills :: theme-factory

- Path: `skills/theme-factory/SKILL.md`
- Purpose: apply curated or generated color/font themes to presentation and document artifacts.
- Structure: theme showcase + theme selection + application workflow; theme specifications live in supporting files.
- Evidence: actual `SKILL.md` read. No theme application was executed.
- Status: `source-read`; runtime `not_executed`.

## phronetic-ai/agentskills :: frontend-design

- Path: `skills/frontend-design/SKILL.md`
- Purpose: create production-grade frontend interfaces with an explicit, distinctive aesthetic direction.
- Structure: heuristic design guidance emphasizing purpose, tone, constraints, differentiation, typography, motion, layout, and visual detail.
- Evidence: actual `SKILL.md` read. No UI build or browser validation was executed.
- Status: `source-read`; runtime `not_executed`.

## phronetic-ai/agentskills :: webapp-testing

- Path: `skills/webapp-testing/SKILL.md`
- Purpose: test local web applications with Playwright and server lifecycle helpers.
- Structure: reconnaissance-then-action workflow; points to `scripts/with_server.py` and Playwright patterns.
- Evidence: actual `SKILL.md` read. No Playwright or local server process was executed.
- Status: `source-read`; runtime `not_executed`.

## phronetic-ai/agentskills :: web-artifacts-builder

- Path: `skills/web-artifacts-builder/SKILL.md`
- Purpose: scaffold and bundle complex React/Tailwind/shadcn HTML artifacts.
- Structure: initialize → develop → bundle → share → optional test, backed by shell helpers.
- Evidence: actual `SKILL.md` read. No scaffold, npm install, bundling, or browser test was executed.
- Status: `source-read`; runtime `not_executed`.

## phronetic-ai/agentskills :: slack-gif-creator

- Path: `skills/slack-gif-creator/SKILL.md`
- Purpose: create animated GIFs optimized for Slack constraints.
- Structure: animation guidance plus reusable Python/PIL-oriented utilities and output constraints.
- Evidence: actual `SKILL.md` read. No GIF generation or size/quality validation was executed.
- Status: `source-read`; runtime `not_executed`.

## phronetic-ai/agentskills :: internal-comms

- Path: `skills/internal-comms/SKILL.md`
- Purpose: produce common internal communications using type-specific reference examples.
- Structure: classify communication type, load the corresponding example/reference, then follow its format and tone.
- Evidence: actual `SKILL.md` read. No end-to-end communication task was evaluated.
- Status: `source-read`; runtime `not_executed`.

## phronetic-ai/agentskills :: doc-coauthoring

- Path: `skills/doc-coauthoring/SKILL.md`
- Purpose: structured collaborative authoring for proposals, technical specs, decision documents, and similar long-form work.
- Structure: context gathering → refinement/structure → reader testing, with explicit exit conditions and iteration behavior.
- Evidence: actual `SKILL.md` read. No reader-testing experiment was run.
- Status: `source-read`; runtime `not_executed`.

## phronetic-ai/agentskills :: skill-creator

- Path: `skills/skill-creator/SKILL.md`
- Purpose: design or update Agent Skills using concise instructions, progressive disclosure, scripts, references, and assets.
- Structure: detailed authoring guidance plus `scripts/init_skill.py`, `scripts/package_skill.py`, `scripts/quick_validate.py`, and references.
- Validation surface read: `scripts/quick_validate.py` checks `SKILL.md`, YAML frontmatter, allowed properties, required `name`/`description`, naming rules, and length constraints.
- Status: `source-read`; validator `not_executed`.

## phronetic-ai/agentskills :: mcp-builder

- Path: `skills/mcp-builder/SKILL.md`
- Purpose: guide MCP server research, design, implementation, tool schemas, transport choices, and evaluation.
- Structure: staged workflow with language-specific references and MCP design guidance.
- Evidence: actual `SKILL.md` read. No MCP server was built or evaluated.
- Status: `source-read`; runtime `not_executed`.

## phronetic-ai/agentskills :: brand-guidelines

- Path: `skills/brand-guidelines/SKILL.md`
- Purpose: apply Anthropic-oriented colors, typography, and visual styling to artifacts.
- Structure: declarative palette/typography guidance with application rules.
- Evidence: actual `SKILL.md` read. No artifact styling validation was performed.
- Status: `source-read`; runtime `not_executed`.

## trancong12102/agentskills :: code-search

- Path: `plugins/ora/skills/code-search/SKILL.md`
- Purpose: route local codebase searches to exact-text, semantic, symbol, AST, or git tools based on query shape.
- Structure: compact routing policy; explicitly requires reading load-bearing source locations after synthesized semantic-search answers.
- Evidence: actual `SKILL.md` read.
- Status: `source-read`; search tools `not_executed`.

## trancong12102/agentskills :: ast-grep

- Path: `plugins/ora/skills/ast-grep/SKILL.md`
- Purpose: structural code search and outline generation using ast-grep.
- References read: `plugins/ora/skills/ast-grep/references/rule-reference.md` documents atomic, relational, and composite rules plus `stopBy` behavior.
- Evidence: actual skill and rule reference read.
- Status: `source-read`; ast-grep `not_executed`.

## trancong12102/agentskills :: lib-docs

- Path: `plugins/ora/skills/lib-docs/SKILL.md`
- Purpose: prefer author-published `llms.txt` / `llms-full.txt` documentation, then fall back to Context7 when unavailable.
- Script read: `plugins/ora/skills/lib-docs/scripts/llms-probe.sh` probes common llms.txt locations, follows redirects, filters HTML soft-404s, reports approximate size, and deduplicates final URLs.
- Status: `source-read`; probe script and external services `not_executed`.

## trancong12102/agentskills :: repo-research

- Path: `plugins/ora/skills/repo-research/SKILL.md`
- Purpose: research external repository source, issues, PRs, releases, and git history using intent-specific tooling.
- Structure: routes concept questions, exact-symbol searches, deep dives, and issue/PR/release lookups to different mechanisms; warns that synthesized answers require source verification.
- Evidence: actual `SKILL.md` read.
- Status: `source-read`; external research toolchain `not_executed`.

## trancong12102/agentskills :: pkg-versions

- Path: `plugins/ora/skills/pkg-versions/SKILL.md`
- Purpose: query latest versions and deprecation status for public packages across multiple ecosystems.
- Structure: thin operational wrapper around `scripts/get-versions.py` with a fixed TSV result contract.
- Evidence: actual `SKILL.md` read.
- Status: `source-read`; deps.dev/script execution `not_executed`.

## jason-allen-oneal/openclaw-skill-scanner :: openclaw-skill-scanner

- Path: `SKILL.md`
- Purpose: gate OpenClaw skill installation with a security scan; quarantine or block high-severity findings while allowing lower-severity findings with warnings.
- Scripts read: `scripts/scan_and_add_skill.sh` stages the decision, parses severity counts from a scanner report, blocks High/Critical unless forced, and installs permitted directories.
- References read: `references/openclaw-skill-scan.service` defines the oneshot systemd user service for automatic scanning.
- Status: `source-read`; external scanner/systemd/runtime `not_executed`.

## civitai/civitai-gen-skill :: civitai-gen

- Path: `civitai-gen/SKILL.md`
- Purpose: unified media-generation workflow covering image, video, audio, transcription, batching, experiment sweeps, and cost estimation through Civitai APIs.
- Implementation read: `civitai-gen/generate.mjs` uses a zero-dependency Node CLI and separates API/image/video/audio domain modules; workflow follows submit → poll → download.
- Test surface read: `civitai-gen/test/smoke-test.mjs` separates read-only checks from write tests that may consume service credits.
- Status: `source-read`; no API calls, generation, downloads, or smoke tests executed.

## SherifEldeeb/agentskills :: docx

- Path: `skills/baseline/docx/SKILL.md`
- Purpose: read, create, modify, and template Word documents with Python tooling.
- Structure: capability/quick-start/usage-oriented baseline skill with explicit Python compatibility and dependencies.
- Status: `source-read`; runtime `not_executed`.

## SherifEldeeb/agentskills :: xlsx

- Path: `skills/baseline/xlsx/SKILL.md`
- Purpose: spreadsheet reading, creation, formulas, formatting, charts, and analysis.
- Structure: baseline skill centered on `openpyxl`/`pandas` workflows.
- Status: `source-read`; runtime `not_executed`.

## SherifEldeeb/agentskills :: pptx

- Path: `skills/baseline/pptx/SKILL.md`
- Purpose: create, read, modify, and template PowerPoint presentations.
- Structure: baseline `python-pptx` workflow with examples and presentation-specific operations.
- Status: `source-read`; runtime `not_executed`.

## SherifEldeeb/agentskills :: pdf

- Path: `skills/baseline/pdf/SKILL.md`
- Purpose: PDF reading, generation, merge/split, forms, watermarking, and conversion-oriented work.
- Structure: Python-focused baseline skill using PDF libraries listed in compatibility metadata.
- Status: `source-read`; runtime `not_executed`.

## SherifEldeeb/agentskills :: research

- Path: `skills/baseline/research/SKILL.md`
- Purpose: gather and synthesize web/API/feed information into structured research outputs with source tracking.
- Structure: network-capable baseline skill with requests/HTML/feed processing examples.
- Status: `source-read`; network research workflow `not_executed`.

## SherifEldeeb/agentskills :: image-generation

- Path: `skills/baseline/image-generation/SKILL.md`
- Purpose: generate defensive-report visuals such as diagrams, charts, risk matrices, and timelines.
- Structure: Python visualization examples using Pillow, matplotlib, and Graphviz-oriented tooling.
- Status: `source-read`; image generation `not_executed`.

## SherifEldeeb/agentskills :: soc-operations

- Path: `skills/cybersecurity/soc-operations/SKILL.md`
- Purpose: defensive SOC alert triage documentation, shift handovers, metrics, IOC tracking, and standardized reporting.
- Structure: domain workflow examples backed by utility-style Python APIs referenced by the skill.
- Status: `source-read`; defensive workflow/runtime `not_executed`.

## SherifEldeeb/agentskills :: incident-response

- Path: `skills/cybersecurity/incident-response/SKILL.md`
- Purpose: defensive incident lifecycle documentation, timeline analysis, evidence tracking, containment records, and reporting.
- Structure: incident/timeline/evidence workflow examples with standard-library compatibility declared.
- Status: `source-read`; runtime `not_executed`.

## SherifEldeeb/agentskills :: threat-intelligence

- Path: `skills/cybersecurity/threat-intelligence/SKILL.md`
- Purpose: defensive CTI workflows including IOC extraction/normalization, threat profiling, ATT&CK mapping, and reporting.
- Structure: domain instructions plus utility API examples; optional network fetching is declared separately.
- Status: `source-read`; feed/network/runtime `not_executed`.

## SherifEldeeb/agentskills :: vulnerability-management

- Path: `skills/cybersecurity/vulnerability-management/SKILL.md`
- Purpose: defensive vulnerability intake, prioritization, remediation tracking, exceptions, metrics, and reporting.
- Structure: domain workflow examples for scanner findings and remediation state.
- Status: `source-read`; scanner ingestion/runtime `not_executed`.

## SherifEldeeb/agentskills :: grc

- Path: `skills/cybersecurity/grc/SKILL.md`
- Purpose: governance/risk/compliance documentation, control assessment, risk registers, compliance tracking, and audit support.
- Structure: domain workflow examples with standard-library compatibility declared.
- Status: `source-read`; runtime `not_executed`.

## editframe/skills :: composition

- Path: `composition/SKILL.md`
- Purpose: build video compositions with Editframe HTML web components or React.
- References: extensive media/timing/rendering/reference tree; `composition/references/render-to-video.md` was read and documents browser/WebCodecs and React rendering flows.
- Status: `source-read`; rendering `not_executed`.

## editframe/skills :: editframe-api

- Path: `editframe-api/SKILL.md`
- Purpose: JavaScript/TypeScript API client workflows for renders, file upload/processing, transcription, downloads, and signed URLs.
- Structure: API function index plus reference-oriented guidance for files and browser access.
- Status: `source-read`; API calls `not_executed`.

## editframe/skills :: editframe-cli

- Path: `editframe-cli/SKILL.md`
- Purpose: local/cloud render, preview, transcription, and supporting command-line workflows.
- Structure: concise command entrypoint delegating detail to references for rendering, preview, cloud, transcription, and utilities.
- Status: `source-read`; CLI `not_executed`.

## editframe/skills :: editframe-create

- Path: `editframe-create/SKILL.md`
- Purpose: scaffold new Editframe video projects from supported templates.
- Structure: quick-start scaffolding workflow with references for templates, getting started, and agent-skill installation.
- Status: `source-read`; scaffolding/npm execution `not_executed`.

## editframe/skills :: editor-gui

- Path: `editor-gui/SKILL.md`
- Purpose: assemble custom video editor interfaces from timeline, preview, playback, transform, hierarchy, and editor-shell components.
- Structure: reference-index skill pointing to focused GUI component documents.
- Status: `source-read`; UI/runtime `not_executed`.

## editframe/skills :: vite-plugin

- Path: `vite-plugin/SKILL.md`
- Purpose: integrate Editframe local development into Vite, including JIT media handling, local assets, caching, and visual regression support.
- Metadata: identifies `@editframe/vite-plugin`, beta version metadata, and a proprietary license marker.
- Status: `source-read`; plugin install/tests `not_executed`.

## editframe/skills :: webhooks

- Path: `webhooks/SKILL.md`
- Purpose: configure and consume render/file event webhooks with signature verification and operational guidance.
- Reference read: `webhooks/references/security.md` specifies HMAC-SHA256 validation, raw-body handling, timing-safe comparison, and replay/timestamp considerations.
- Status: `source-read`; webhook delivery/API tests `not_executed`.

## tiann/execplan-skill :: execplan

- Path: `SKILL.md`
- Purpose: require a self-contained execution plan for complex features/significant refactors or when explicitly requested.
- Reference read: `references/PLANS.md` defines a living, novice-executable plan with observable outcomes, exact repository context/commands, validation, recovery, milestones, evidence, and mandatory progress/decision/discovery/retrospective sections.
- Structure: intentionally minimal `SKILL.md`; most durable methodology lives in one authoritative reference.
- Status: `source-read`; no execution-plan implementation experiment was run.
