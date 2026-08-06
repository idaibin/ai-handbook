# GitHub Skills Deep Analysis — Batch 004

- Observed at: `2026-08-07T04:13:06+08:00`
- Queue source: `sources/catalog/github-agent-skills-index-latest.json`
- Index snapshot: `1445` unique repositories, `1078` provisionally deep-analysis eligible, `367` held for review
- Repositories completed: `10`
- Individual skills reviewed: `10`
- Completion state: `structure-reviewed`
- Runtime validation: `not_executed`

A repository is counted complete only after its GitHub identity and displayed star count were checked and actual repository content was read. This batch inspected README or equivalent documentation, every identified primary `SKILL.md`, and representative scripts, references, schemas, tests, or evaluation assets where available. No third-party script, installer, renderer, API client, test suite, generated application, or external side-effect workflow was executed.

Star counts are observations from GitHub and can change. Abbreviated values are retained as displayed.

## Queue drift observed

Two queue entries were encountered but deliberately **not** marked complete:

- `Pluviobyte/rnskill`: indexed as a single/domain package, but the current repository presents a large multi-skill collection (README reports 54 skills and code search exposes many `SKILL.md` files). It requires a collection-level pass and individual-skill enumeration.
- `samber/cc-skills-golang`: indexed as a single/domain package, but the current repository is a multi-skill Go collection with `skills/`, evaluation documentation, and plugin metadata. It also requires a collection-level pass.

This is classification drift, not analysis failure. Both remain pending so metadata alone cannot create a false completion record.

## Batch summary

| Repository | GitHub repository ID | Stars observed | Skills | Main evidence inspected | Result |
|---|---:|---:|---:|---|---|
| `pmlaowangba-lab/laowangba-pmprototype-skill` | `1294567068` | `72` | 1 | README, `SKILL.md`, page-UI JSON Schema, frontend design gates | structure-reviewed |
| `ShawhinT/ai-tutor-skill` | `1118334208` | `80` | 1 | README, `SKILL.md`, research methodology, YouTube transcript script | structure-reviewed |
| `soulmujoco/EditableImage2PPTSkill` | `1227445087` | `58` | 1 | README, `SKILL.md`, layout contract, PPTX inspector | structure-reviewed |
| `SpillwaveSolutions/confluence-skill` | `1091246669` | `62` | 1 | README, `SKILL.md`, Confluence downloader, image-handling reference | structure-reviewed |
| `Tang1206cc/codex-skill-paper-formatting-skill` | `1232904067` | `130` | 1 | README, `SKILL.md`, text-comparison script, QA checklists | structure-reviewed |
| `umairalipathan1980/Claude-Skill-for-Full-Stack-Application-Development` | `1110252535` | `40` | 1 | README, `SKILL.md`, backend template, technical reference | structure-reviewed |
| `wuyoscar/GPT-Image2-Skill` | `1217942969` | `4.2k` | 1 | README, `SKILL.md`, launcher, canonical CLI, gallery router | structure-reviewed |
| `xuezheng627/daily-literature-digest-skill` | `1248305485` | `70` | 1 | README, `SKILL.md`, fetch/state script, default-config reference | structure-reviewed |
| `yaojingang/yao-meta-skill` | `1197197392` | `2.3k` | 1 | README, `SKILL.md`, eval catalog, semantic trigger evaluator | structure-reviewed |
| `Zechang-Xiong/chinese-reference-formatter-skill` | `1232049160` | `74` | 1 | README, `SKILL.md`, deterministic formatter, reference rules | structure-reviewed |

## 1. `pmlaowangba-lab/laowangba-pmprototype-skill`

### Identity and content evidence

- Public repository, default branch `main`.
- Primary skill: `product-prototype-figma`.
- Read `README.md` (`9abbcedf06a30aa8939fc085daf321c44a3c5dc1`), `SKILL.md` (`207d1d5175d7d702919b0c49eb16fcded9ea26d9`), `schema/page.ui.schema.json` (`f2c8352b0e9ffa2b0355d4475ec38f06d8ee83ad`), and `references/frontend-design-gates.md` (`000523382c3575ee2fd82008d179c83b2e9177ce`).

### Architecture and workflow

The repository turns prototype generation into an explicit stateful pipeline: derive IA from entities, roles and task chains; write a Design Plan; run an Anti-Slop review; materialize each page as `page.ui.yaml`; then build editable Figma regions and patch them incrementally. The JSON Schema constrains page IDs, B/C surface routing, page types, component kinds, and requires `meta.anti_slop: pass` before the structured page contract can represent an approved page.

The gate reference defines G0–G6. Missing design plans, failed Anti-Slop checks, schema failures, screenshot divergence, and undocumented edits block later phases instead of being treated as soft advice.

### Strengths and limits

- Strong separation of information architecture, visual contract, structured page state, and Figma mutation.
- Converts subjective visual work into explicit gates and machine-readable state.
- Supports incremental patching rather than repeated whole-page regeneration.
- Depends on Figma MCP/plugin capabilities and companion design skills.
- No executable test/eval suite was found in the inspected surface; Figma generation and visual QA were not run.

## 2. `ShawhinT/ai-tutor-skill`

### Identity and content evidence

- Public repository, default branch `main`.
- Primary skill: `ai-tutor`.
- Read `README.md` (`b5f0896763d7ce4481fa4d22b6dbc29315e5108b`), `SKILL.md` (`54c5c4b5d6ca22f247b414a69f480c245a29b6c9`), `research_methodology.md` (`6131f136a30693c47a0a6fdb99ee17816189f61e`), and `scripts/get_youtube_transcript.py` (`c82d0d06ce4ad92782fec845f2541a17c0233653`).

### Architecture and workflow

The skill selects among three explanation structures—Status Quo/Problem/Solution, What/Why/How, and What/So What/What Now—then applies plain-English-first explanation, concrete examples, progressive complexity, audience calibration, and sparing analogies. Unfamiliar or recent concepts route to a separate research methodology rather than expanding the main skill entrypoint.

The research guide defines when to research, a source-quality hierarchy, cross-source synthesis, uncertainty handling, and a YouTube transcript path. The transcript script parses common YouTube URL/ID forms, requests a transcript through `youtube-transcript-api`, optionally emits timestamps, and surfaces disabled/missing transcript failures.

### Strengths and limits

- Lean primary skill with research detail kept in a separate reference.
- Clear pedagogy and explicit source-quality/uncertainty rules.
- Script provides a concrete path from referenced video to text evidence.
- The guide's fixed “after early 2025” freshness threshold will age and should eventually become relative rather than hard-coded.
- No formal tests/evals were found; YouTube/network behavior was not executed.

## 3. `soulmujoco/EditableImage2PPTSkill`

### Identity and content evidence

- Public repository, default branch `main`.
- Primary skill: `ppt-image-to-editable-ppt`.
- Read `README.md` (`d9051adf79ed78c8ad8d2c70c23b9a89e5d06444`), `SKILL.md` (`526ad8c637afa8f592c76e963a32ee006883edd5`), `references/layout-json.md` (`17b116b6828b7043a15d9879947066d337b96819`), and `scripts/inspect_pptx.py` (`df36825f9a67e464e189359ee9fb7ae57b762841`).

### Architecture and workflow

The workflow first extracts reusable visual assets, then reconstructs slides with editable text, native shapes/lines, and independent picture objects. Layout JSON uses source-image pixel coordinates and scales them into the PowerPoint canvas, which makes the intermediate representation inspectable and reusable across single-page and batch reconstruction.

The bundled inspector opens the PPTX ZIP package, enumerates slide/media XML, extracts text runs, detects zero-byte media and known placeholder strings, writes an optional JSON report, and exits non-zero on structural failures.

### Strengths and limits

- Explicit raster-versus-editable-object boundary.
- Intermediate JSON contracts make reconstruction deterministic enough to inspect and merge.
- Structural QA is executable instead of being only a prose checklist.
- The inspector cannot establish visual fidelity to the source image by itself.
- No formal eval dataset was found; package generation/rendering was not run.

## 4. `SpillwaveSolutions/confluence-skill`

### Identity and content evidence

- Public repository, default branch `main`.
- Primary skill: `confluence`.
- Read `README.md` (`e2ef3b8588a5710d9827f36245f54d2f31a65db8`), `SKILL.md` (`2702df85560682f43f975db366a492f9d7df6135`), `scripts/download_confluence.py` (`5b2ec9780d36068c1e538d12db53e182a67de003`), and `references/image_handling_best_practices.md` (`005b75176e3ae652299561460621991b55cf3b1a`).

### Architecture and workflow

The skill treats MCP and direct REST/CLI flows as different operational tiers: MCP for reads and small text updates, REST scripts for large pages and attachments, and `mark` for Git-to-Confluence synchronization. References cover wiki markup, storage format, conversion, image handling, synchronization, and troubleshooting.

The downloader implements REST pagination, XHTML/storage-format conversion to Markdown, attachments, child-page traversal, frontmatter generation, retries/backoff, optional HTML debugging, and shared credential discovery. The image guide records concrete failure modes such as raw Confluence XML being escaped and diagram renderers interfering with ordinary attachments.

### Strengths and limits

- Practical decision matrix between MCP, REST, and sync tooling.
- Substantial executable handling for pagination, attachments, conversion, and recovery.
- References capture operational failure modes rather than only happy paths.
- Some examples are tied to a specific Atlassian MCP tool namespace and may require adaptation.
- Requires credentials and external tools; no Confluence operation or script was executed.

## 5. `Tang1206cc/codex-skill-paper-formatting-skill`

### Identity and content evidence

- Public repository, default branch `main`.
- Primary skill: `word-format-from-content-template` at `skill 包/word-format-from-content-template/SKILL.md`.
- Read README, `SKILL.md` (`b14002794e07389594d2f2ccbed31cfc94b6fdbe`), `scripts/compare_text.py` (`59b85a0698f571b8faa9878b7fc5341b17ace2e5`), and `references/quality-checklists.md` (`de18467bb00ed095526be2db19132528a1ff032a`).

### Architecture and workflow

The central contract is “format, do not rewrite.” The agent must fully read the formatting specification, treat source text as immutable, use the Word template as a layout carrier rather than a content source, turn every applicable rule into a checklist, remove template residue, and validate both formatting and content identity before delivery.

`compare_text.py` normalizes BOM/whitespace/known Word field noise, supports a looser whitespace mode, uses sequence matching to report short differences, optionally emits a unified diff, and exits non-zero on mismatch. The QA reference separately covers specification compliance, content identity, template residue, visual rendering, and delivery.

### Strengths and limits

- Strong content-preservation boundary and dual verification model.
- A deterministic text-diff helper turns a key requirement into executable evidence.
- QA separates semantic source preservation from visual Word rendering concerns.
- Extracted-text equality cannot prove every document-level semantic or OOXML property.
- Word fields/renderers are environment-dependent; no DOCX task or checker was executed.

## 6. `umairalipathan1980/Claude-Skill-for-Full-Stack-Application-Development`

### Identity and content evidence

- Public repository, default branch `master`.
- Primary skill: `fullstack-template-generator` under `.claude/skills/fullstack-template-generator/`.
- Read `README.md` (`3a700732bc5717c31f926418d08c6030c34fb18f`), `SKILL.md` (`57a51476d80c33a4b13acb7c3a62e242b9fcb457`), backend `main.py.template` (`2f1696ca054c56f916bf70aa99ddd4c2a5707c82`), and `reference.md` (`c55945f564fbe672e8085f0723f97e7aea31d173`).

### Architecture and workflow

The skill copies a concrete FastAPI + React/Vite application template. The backend template configures localhost CORS, requires `OPENAI_API_KEY`, exposes health/test/chat endpoints, validates message length, and calls the OpenAI client. Supporting references describe stack versions, file structure, development commands, deployment considerations, and future scaling options.

The repository contains a test directory scaffold, but its own reference says pytest must be added and frontend tests “can” be added; therefore the presence of a `tests/` directory is not evidence of an implemented test suite.

### Strengths and limits

- Concrete template artifacts make generated output predictable.
- Skill, examples, technical reference, and templates are clearly separated.
- Useful as a starter skeleton with explicit setup instructions.
- “Production-ready” language is stronger than the inspected implementation: production guidance itself calls for authentication, rate limiting, deployment configuration, and other additions.
- No substantive eval/test suite was verified and no generated application was run.

## 7. `wuyoscar/GPT-Image2-Skill`

### Identity and content evidence

- Public repository, default branch `main`.
- Primary skill: `gpt-image` at `skills/gpt-image/SKILL.md`.
- Read `README.md` (`6421e8745290513ce41340902287b78c98ec9bb7`), `SKILL.md` (`0db0ea3e98961b5d53d2fd0a9912de0eee538bab`), `skills/gpt-image/scripts/generate.py` (`1cfc9d332fbb4b275a02636859a400e15061f80a`), `src/gpt_image_cli/cli.py` (`ae2dc26ef1f58647ccbeef4c4f3699d528d9668e`), and `skills/gpt-image/references/gallery.md` (`d80826cb48fb9433d9900fe7da806e4121e7d960`).

### Architecture and workflow

The skill classifies generation/edit/inpaint/multi-reference requests, routes through a 162-entry categorized prompt-gallery index, optionally loads prompt-craft guidance, performs no-side-effect preflight, and delegates to one canonical CLI implementation instead of generating ad-hoc API code. The gallery explicitly instructs the agent to load one category normally and only 2–3 for hybrid tasks, which is a concrete context-budget rule.

The launcher resolves repo-local implementation, installed Python package, PATH executable, then transient `uvx`/`uv`. The canonical CLI uses the official OpenAI SDK, validates reference/mask paths, selects generation versus edit endpoints, loads API keys without overriding existing environment variables, writes returned image bytes, and has defined exit codes.

### Strengths and limits

- Strong separation between agent policy, reference gallery, launcher, and canonical implementation.
- Explicit setup/key/cost guardrails reduce accidental installation and secret mutation.
- Context-aware reference routing avoids loading the entire large prompt library.
- Depends on a paid external API and model behavior; API calls can create external cost.
- No formal `evals/` or pytest suite was found in the inspected surface; no image API call was executed.

## 8. `xuezheng627/daily-literature-digest-skill`

### Identity and content evidence

- Public repository, default branch `main`.
- Primary skill: `daily-literature-digest`.
- Read `README.md` (`8eb722ba499db441c97c350fe9bfe331fa63ce66`), `daily-literature-digest/SKILL.md` (`2a923d8df756910d7e419a25f04e397362028d80`), `scripts/daily_literature_digest.py` (`e76e4617bcaa577f323d29ff2169dddddd732f4a`), and `references/default-config.md` (`54a7283398f4d569e0a812d1d94143ffcbd428c2`).

### Architecture and workflow

The design deliberately separates deterministic collection from AI interpretation. The Python script gathers open metadata/abstracts from Crossref, OpenAlex, and arXiv and writes JSON; the agent later creates the digest, persists Markdown, optionally sends through Gmail, and marks success. State files prevent “email sent” or “run completed” from being inferred before the archive exists.

The skill explicitly blocks unattended paywall access, password handling, and automatic publisher full-text downloads. No-abstract records must remain title-level candidates, with no inferred method/result. The script supports config overrides, publisher/member mappings, retries for transient HTTP errors, Crossref contact identification, and state updates.

### Strengths and limits

- Clean deterministic-fetch versus AI-summary boundary.
- Strong privacy/paywall and evidence limits for unattended automation.
- Persistent config/state makes recurring operation inspectable.
- Recall and freshness depend on public metadata APIs and maintained publisher mappings.
- No formal test/eval suite was found; network fetch, Gmail, and automation behavior were not executed.

## 9. `yaojingang/yao-meta-skill`

### Identity and content evidence

- Public repository, default branch `main`.
- Primary skill: `yao-meta-skill`.
- Read README, `SKILL.md` (`a2c7a6e8974d698fd8716daa642d3e0036727820`), `evals/README.md` (`e1e848e77ba175a2f7769ebfd644fdf066314393`), and `scripts/trigger_eval.py` (`ff610affedf32adf86c7025186986d1bdce1526b`).

### Architecture and workflow

The repository has the broadest lifecycle surface in this batch: intent modeling, platform-neutral Skill IR, target compilers/adapters, trigger/output evaluation, package/install/upgrade checks, Review Studio, evidence and release governance, and post-release SkillOps/adoption drift. The root `SKILL.md` remains comparatively lean and routes complex methods into references/scripts/reports.

`evals/README.md` documents train/dev/holdout/blind/adversarial/confusion trigger sets, output evals, packaging expectations, registry/package/install/upgrade checks, adoption drift, review waivers, and compiler tests. `trigger_eval.py` implements semantic concept matching, negative/exclusion penalties, threshold classification, family statistics, false-positive/false-negative reporting, and baseline comparison.

The README explicitly distinguishes project-produced engineering evidence from independent external validation: beta/external-testing readiness is stated separately from stronger “world-class” claims, and a reported single-reviewer blind comparison is labeled with its limitations.

### Strengths and limits

- Strongest explicit eval/governance/portability architecture among these ten repositories.
- Evidence boundaries and unsupported claims are represented as first-class release concerns.
- Trigger quality, package integrity, installability, upgrades, and drift have executable surfaces.
- Process and artifact complexity are high and may be excessive for small personal skills.
- Self-produced benchmarks/reviews are not independent validation; none of the documented eval/test commands were executed in this analysis.

## 10. `Zechang-Xiong/chinese-reference-formatter-skill`

### Identity and content evidence

- Public repository, default branch `main`.
- Primary skill: `chinese-reference-formatter-skill`.
- Read `README.md` (`bdad58b2da0354fa1f32ec588eb7c2edeedd95ee`), `SKILL.md` (`0174f8ce104947481b6b71582ec625e2f899791c`), `scripts/format_reference.py` (`7edad887cf598e49cb6b75cc8a2a4bb2378492fa`), and `references/chinese-reference-rules.md` (`20c306cdae2cc91df63394c24aead47e1ee60cb2`).

### Architecture and workflow

The skill separates bibliographic verification from deterministic formatting. The agent must first resolve title, authors, year, venue and DOI/URL from public metadata using a source hierarchy; unresolved items become `not_found` or `ambiguous` rather than invented citations. Only verified normalized metadata is handed to the Python formatter.

The formatter uses Python standard library only, accepts normalized JSON, supports multiple reference types, handles Chinese and Western author display rules, creates GB/T-7714-like numeric entries and BibTeX, and builds deterministic citation keys. The reference document defines default conventions while explicitly yielding to institution/journal-specific rules supplied by the user.

### Strengths and limits

- Strong truth-resolution versus formatting boundary.
- Deterministic renderer and explicit ambiguity/not-found states.
- General rules avoid silently imposing school-specific requirements.
- Metadata verification itself remains an agent/web-research responsibility rather than being implemented in the formatter.
- No formal tests/evals were found and the formatter was not executed.

# Individual skill reports

## `product-prototype-figma`

- Repository: `pmlaowangba-lab/laowangba-pmprototype-skill`
- Trigger/use: editable B/C-end Figma product prototypes.
- Contract: IA → design plan → Anti-Slop gate → schema-validated `page.ui.yaml` → region-based Figma generation → screenshot review → incremental patch.
- Resources: `DESIGN.md`, design-gate references, page templates, JSON Schema.
- Validation behavior: hard phase gates and schema constraints; runtime validation not executed.
- Reusable pattern: pair a human-readable design plan with a machine-readable page contract before mutating a visual tool.

## `ai-tutor`

- Repository: `ShawhinT/ai-tutor-skill`
- Trigger/use: explain technical/AI concepts accessibly.
- Contract: select narrative structure, calibrate audience, explain plainly, add concrete examples, research when uncertainty/recency requires it.
- Resources: research methodology and YouTube transcript helper.
- Validation behavior: source-quality and uncertainty rules are documented; no automated eval found.
- Reusable pattern: keep the default teaching loop small and lazily load research methodology only when needed.

## `ppt-image-to-editable-ppt`

- Repository: `soulmujoco/EditableImage2PPTSkill`
- Trigger/use: reconstruct slide images into editable PowerPoint.
- Contract: inventory → asset extraction → layout JSON → native PPT objects/assets → batch merge → package/visual QA.
- Resources: asset manifest, layout JSON, reconstruction SOP, four Python scripts.
- Validation behavior: PPTX inspector checks slide/media/text package failures; visual parity remains separate.
- Reusable pattern: use an intermediate layout contract and independent structural QA for document reconstruction.

## `confluence`

- Repository: `SpillwaveSolutions/confluence-skill`
- Trigger/use: Confluence read/write, conversion, sync, attachments and diagrams.
- Contract: select MCP/REST/mark path based on operation and payload; convert and validate formats explicitly.
- Resources: conversion/storage/image/mark/troubleshooting references and Python utilities.
- Validation behavior: download pipeline includes retries and validation-oriented debug artifacts; no runtime run here.
- Reusable pattern: make tool selection an explicit decision matrix when multiple transports have different limits.

## `word-format-from-content-template`

- Repository: `Tang1206cc/codex-skill-paper-formatting-skill`
- Trigger/use: Word formatting from source draft + formatting spec + template.
- Contract: preserve text, extract complete spec, build checklist, format, compare text, remove template residue, render/inspect.
- Resources: detailed workflow/QA references and `compare_text.py`.
- Validation behavior: deterministic normalized text comparison plus visual/spec checklists.
- Reusable pattern: define immutable source truth separately from presentation transformation.

## `fullstack-template-generator`

- Repository: `umairalipathan1980/Claude-Skill-for-Full-Stack-Application-Development`
- Trigger/use: bootstrap FastAPI + React/Vite applications with OpenAI integration.
- Contract: copy supplied backend/frontend templates and provide setup commands.
- Resources: templates, examples, diagram, technical reference.
- Validation behavior: documentation mentions testing but the inspected package contains only a test scaffold, not verified tests.
- Reusable pattern: template-backed generation is more deterministic than free-form project scaffolding, but readiness claims must match the actual gates.

## `gpt-image`

- Repository: `wuyoscar/GPT-Image2-Skill`
- Trigger/use: GPT Image 2 generation/editing/inpainting/multi-reference workflows.
- Contract: classify request → load minimal gallery/craft references → preflight → canonical CLI → report outputs.
- Resources: 162-entry categorized gallery, craft/API references, skill launcher, canonical Python CLI.
- Validation behavior: input/mask/key/endpoint checks and explicit exit codes; external API not executed.
- Reusable pattern: one canonical implementation plus a context-routed reference atlas prevents code duplication and context explosion.

## `daily-literature-digest`

- Repository: `xuezheng627/daily-literature-digest-skill`
- Trigger/use: recurring literature monitoring and digest delivery.
- Contract: config → deterministic metadata fetch → AI summary → local archive → optional Gmail → explicit success state.
- Resources: default config, fetch/state script, optional Markdown-to-DOCX helper.
- Validation behavior: archive existence precedes success marking; no-abstract records remain title-only.
- Reusable pattern: keep network collection deterministic and make the model consume a persisted evidence payload.

## `yao-meta-skill`

- Repository: `yaojingang/yao-meta-skill`
- Trigger/use: create, improve, evaluate, package, release and govern reusable agent skills.
- Contract: fit assessment → intent/output/boundary model → Skill IR/package → target compilation → eval/review → release evidence → operational feedback.
- Resources: extensive references, schemas, scripts, tests, eval splits, reports, registry and evidence artifacts.
- Validation behavior: explicit trigger/output/package/install/upgrade/drift/review gates exist in source; none were executed here.
- Reusable pattern: separate semantic Skill IR from target-specific packaging and make evidence a release artifact rather than a prose claim.

## `chinese-reference-formatter-skill`

- Repository: `Zechang-Xiong/chinese-reference-formatter-skill`
- Trigger/use: verify titles and output Chinese academic references plus BibTeX.
- Contract: public metadata verification → conflict resolution → normalized JSON → deterministic formatter.
- Resources: reference-style rules and standard-library formatter.
- Validation behavior: unresolved/conflicting metadata has explicit `not_found`/`ambiguous` paths; no runtime executed.
- Reusable pattern: separate uncertain entity resolution from deterministic rendering so formatting cannot hide fabricated facts.

# Verification boundary

This batch is `structure-reviewed`, not `runtime-verified`. Source files were actually read and repository identity/star observations were checked, but third-party dependencies, tests, renderers, external APIs, Gmail/Confluence/Figma operations, OpenAI image calls, and generated applications were not executed. No repository was marked complete from metadata alone.