# GitHub Agent Skills Deep Analysis — Batch 009

## Run result

- Batch: `2026-08-07-batch-009`
- Repository completions: **10**
- Individual skill reports: **115**
- Completion basis: repository identity + displayed GitHub stars + actual repository content inspection; no repository was completed from metadata alone.
- Runtime validation: **not_executed**. Third-party scripts, installers, browser flows, scanners, downloads, and build/test commands were not executed in this run.
- Queue snapshot used for reconciliation: `sources/catalog/github-agent-skills-index-latest.json`, observed `2026-08-07T10:03:09+08:00`, `2181` unique, `1767` deep-analysis eligible, `414` held.

This batch uses the existing schema-1.3 rule: the immutable batch report is authoritative for repository-specific skill identities and evidence. For large collections, every current skill receives an individual inventory report, while detailed body-level conclusions are limited to skills whose `SKILL.md` or equivalent support files were directly read. Inventory-only rows are explicitly identified as such and are not represented as direct body reads.

## Repository summary

| Repository | GitHub repository ID | Default branch | Stars observed | Active/canonical skill reports | Direct content evidence |
| --- | ---: | --- | ---: | ---: | --- |
| `binggandata/bggg-skills` | `1227413039` | `main` | 555 | 12 | Root inventory; `bggg-skill-taotie/SKILL.md`; `bggg-creator-image2ppt/SKILL.md`; `scripts/image2pptx.py`; Image2PPT eval JSON; supporting reference/script inventory |
| `chenxiachan/xhs-claude-skills` | `1196377162` | `master` | 396 | 3 | README/current plugin structure; all three `SKILL.md` files |
| `chujianyun/skills` | `1119498800` | `main` | 715 | 26 | README capability map; `skill-optimizer/SKILL.md`; `paper-interpreter/SKILL.md`; repository validator; repository validation tests |
| `coleam00/second-brain-skills` | `1141291453` | `main` | 808 | 6 | README; current `.claude/skills` inventory; `mcp-client/SKILL.md`; MCP client Python implementation; skill-creator script/reference inventory |
| `DannyMac180/skills` | `1253525979` | `main` | 515 | 2 | README/current root inventory; both `SKILL.md` files; workflow risk-gate reference |
| `davidondrej/skills` | `1279159149` | `main` | 3.4k | 47 | README; all five category inventories; `effective-agent-skills/SKILL.md`; `browser-harness/SKILL.md`; browser-harness install reference; supporting file search |
| `Fokkyp/claude-skills` | `1118004768` | `main` | 196 | 2 | README/current root inventory; both `SKILL.md` files; competitive-analysis data-collection reference |
| `haowjy/creative-writing-skills` | `1083255207` | `main` | 388 | 13 | README current skill/agent architecture; `creative-writing-muse/SKILL.md`; `story-memory/SKILL.md`; packaging script |
| `Harishwarrior/flutter-claude-skills` | `1081820059` | `main` | 58 | 2 | README; both `SKILL.md` files; hardcoded-secret scanner implementation; documented references/scripts inventory |
| `lukasreese/powerbi-claude-skills` | `1181497603` | `main` | 106 | 2 | README/status table; both available `SKILL.md` files; PBIP/PBIR/TMDL structure reference |

Stars are observations from the public GitHub repository pages during this run, not immutable repository properties.

---

## 1. `binggandata/bggg-skills`

### Repository analysis

**Identity and structure.** GitHub identity resolved to repository ID `1227413039`, public, non-archived, default branch `main`. The current root contains 12 skill directories plus repository-level configuration. The README treats each top-level skill as independently installable. Mature packages use the conventional split `SKILL.md` + human README + `scripts/` + `references/` + `assets/` + `evals/` + ignored `projects/` runtime outputs.

**Directly read evidence.** `bggg-creator-image2ppt/SKILL.md` defines a structured intermediate manifest between image/HTML/SVG inputs and editable PowerPoint objects; native text and simple shapes are preferred, with images used as fallback. `bggg-creator-image2ppt/scripts/image2pptx.py` is a substantial deterministic renderer using `python-pptx` and PIL rather than a prose-only workflow. `bggg-creator-image2ppt/evals/evals.json` contains three concrete eval scenarios covering image, HTML, and SVG conversion. `bggg-skill-taotie/SKILL.md` defines a comparison-and-incremental-improvement workflow rather than a one-shot rewrite.

**Quality signal.** This is one of the stronger script-backed collections in this batch: execution-critical transformations are pushed into code, runtime artifacts are separated from source, and at least one complex package carries explicit eval cases. The Image2PPT evals are scenario/expectation definitions; this run did not execute them, so no passing status is inferred.

**Risk/limitation.** Some skills wrap authenticated browser/media workflows or external services. Those operational dependencies and site-specific behavior were not run. `web-access` is explicitly described by the repository as a third-party skill, so provenance differs from the BGGG-authored packages and should remain visible when later comparing quality.

### Individual skill reports

| Skill | Evidence basis | Report |
| --- | --- | --- |
| `bggg-creator-image2psd` | current README/inventory | Converts flat images to editable layered PSD output; package structure advertises scripts/references/assets/evals. Body not directly read in this batch. |
| `bggg-creator-image2ppt` | **direct body + script + evals** | Strong intermediate-representation design: visual understanding produces a manifest, deterministic code emits PPTX, native text/shapes are prioritized, and complex content can fall back to image components. |
| `bggg-skill-taotie` | **direct body** | Meta-skill for comparing other skills and incrementally absorbing useful patterns while preserving the target skill's purpose. |
| `bggg-tiktok-search` | current README/inventory | Read-only TikTok research workflow using a real local browser session and evidence artifacts. Body not directly read in this batch. |
| `bggg-tiktok-downloader` | current README/inventory | Media-download workflow with a primary downloader and fallback path. Body not directly read in this batch. |
| `bggg-tiktok-readvideo` | current README/inventory | Decomposes video into metadata, transcript, scenes, keyframes, contact sheet, and timeline for later agent reasoning. |
| `bggg-tiktok-cut` | current README/inventory | JSON edit-plan + FFmpeg-oriented vertical-video editing workflow. |
| `bggg-tiktok-capcut` | current README/inventory | Generates new CapCut drafts from template drafts and validates draft structure. |
| `tiktok-gemini-video-workflow` | current README/inventory | Multi-stage product/video production workflow with tracking and rework boundaries. |
| `sif-keyword-scout` | current README/inventory | Processes Sif keyword exports into tiers, competitor/ad-gap analysis, and downstream reports. |
| `sif-keyword-tracker` | current README/inventory | Compares historical keyword snapshots for the same ASIN and produces update/recommendation deltas. |
| `web-access` | current README/inventory | Third-party browser/CDP access package reused by the collection; provenance should be tracked separately from first-party skills. |

---

## 2. `chenxiachan/xhs-claude-skills`

### Repository analysis

**Identity and structure.** Repository ID `1196377162`, public, non-archived, default branch `master`. The current plugin has exactly three skill definitions: `xhs`, `xhs-batch`, and `xhs-analyze`; logic is mostly embedded in `SKILL.md` rather than separated into repository scripts.

**Directly read evidence.** All three current `SKILL.md` files were read. `xhs` performs cookie-backed HTTP extraction, optional video/audio processing, local transcription, and Markdown/Obsidian persistence. `xhs-batch` composes the single-item flow across multiple links and adds pacing plus result aggregation. `xhs-analyze` operates on the locally persisted Markdown corpus.

**Architecture.** The repository forms a clear three-stage pipeline: capture → batch capture → local analysis. It is small and easy to understand, but duplication exists because the batch skill refers to the single-item workflow semantically rather than delegating through a deterministic shared implementation.

**Risk/limitation.** The current `xhs` body stores authenticated session cookies in a fixed local file and its inline Python example disables TLS certificate verification. That is a concrete security weakness in the documented implementation path. It also relies on page-internal data structure and local model/tool availability, making it more brittle than an API-backed integration. No separate eval suite was observed.

### Individual skill reports

| Skill | Evidence basis | Report |
| --- | --- | --- |
| `xhs` | **direct body** | End-to-end Xiaohongshu extraction to local Markdown, with image/video handling and optional local transcription. Useful local-first pipeline, but session-cookie handling and disabled TLS verification need hardening. |
| `xhs-batch` | **direct body** | Batch coordinator over the single-post extraction workflow with pacing and success/failure summary. Simpler than duplicating the extraction internals, but still coupled to `xhs`'s assumptions. |
| `xhs-analyze` | **direct body** | Read-only analysis over previously persisted Markdown notes, supporting keyword-scoped or corpus-wide synthesis. Lowest side-effect surface of the three. |

---

## 3. `chujianyun/skills`

### Repository analysis

**Identity and structure.** Repository ID `1119498800`, public, non-archived, default branch `main`. Current README defines a three-level physical taxonomy `skills/<category>/<skill-name>/` with eight categories, backed by `config/skill-categories.json`. The repository also contains `.claude-plugin`, scripts, tests, and project instructions.

**Directly read evidence.** `skills/review/skill-optimizer/SKILL.md` uses an explicit review → plan → confirmation → implement → verify gate and checks sensitive information, high-impact actions, dependency installability, progressive disclosure, and scope control. `skills/content/paper-interpreter/SKILL.md` is a file-oriented research pipeline with explicit evidence boundaries and a user-confirmed secondary review stage. `scripts/validate_skill.py` delegates repository validation to `skill_repository.validate_skill` and optionally runs an official quick validator. `tests/test_skill_repository.py` directly tests duplicate taxonomy membership, duplicate skill names, category membership, frontmatter constraints, directory/name agreement, broken local references, marketplace path consistency, and likely-secret detection.

**Architecture.** This is the strongest repository-governance design in this batch: taxonomy is machine-readable, README and marketplace paths are validated, repeatable checks exist as code, and tests exercise failure cases rather than only happy paths. The skill bodies explicitly distinguish human-facing README material from AI execution instructions and emphasize progressive loading.

**Runtime boundary.** The validators and tests were inspected but not executed. Therefore the report verifies the presence and intent of quality gates, not their current passing status.

### Individual skill reports

The README-maintained capability map is the inventory authority for the 26 rows below. `skill-optimizer` and `paper-interpreter` received direct body reads; the remaining rows are inventory-level reports grounded in the repository's current capability map and taxonomy.

| Skill | Category / mode signal | Report |
| --- | --- | --- |
| `qoder-wiki` | knowledge / tool wrapper | Product-documentation context wrapper for Qoder questions. |
| `prompt-optimizer` | review / reviewer-generator | Reviews and improves prompts and instruction framing. |
| `agent-md-advisor` | review / advisor-reviewer-generator | Guidance and review for `AGENTS.md` / `CLAUDE.md` style agent instructions. |
| `claude-config-advisor` | review / reviewer-inversion | Reviews/designs Claude Code project configuration with diagnosis before change. |
| `skill-optimizer` | review / **direct body** | Mature gated skill-review workflow with scope, security, dependency, structure, confirmation, and verification checks. |
| `agent-optimizer` | review / reviewer-consultant | Agent/Skill/workflow design review based on a stated AgentOps framework. |
| `p7-advisor` | career / advisor-reviewer | Career evidence/readiness assessment against a P7-level model. |
| `p8-advisor` | career / advisor-reviewer | Career/leadership assessment against a P8-level model. |
| `p9-advisor` | career / advisor-reviewer | Organization/business-level leadership assessment against a P9-level model. |
| `mermaid` | visual / generator-reviewer | Mermaid diagram generation/review across common diagram families. |
| `remove-ai-flavor` | content / pipeline-generator-reviewer | Rewrites existing text to reduce templated/AI-like phrasing while preserving intent. |
| `article-interpreter` | content / pipeline-generator | Converts article/PDF/text inputs into structured interpretation reports. |
| `github-code-interpreter` | content / pipeline-generator | Repository/source interpretation and learning-report workflow. |
| `paper-interpreter` | content / **direct body** | Local artifact-oriented arXiv pipeline with PDF/source capture, structured report generation, explicit uncertainty, and opt-in review. |
| `opendataloader-pdf` | media / tool-wrapper-pipeline | PDF extraction/conversion for Markdown/JSON/HTML and downstream data preparation. |
| `local-audio-transcriber` | media / tool-wrapper-pipeline | Local audio/video transcription to reusable text/subtitle artifacts. |
| `alltuu-downloader` | media / tool-wrapper-pipeline | Site-specific photo-album download workflow. |
| `photoplus-downloader` | media / tool-wrapper-pipeline | Site-specific PhotoPlus album download workflow. |
| `wechat-official-account-qr` | visual / tool-wrapper-generator | Generates official-account follow QR assets from account identifiers. |
| `openclaw-ops` | operations / runbook | State-first OpenClaw operational troubleshooting. |
| `openclaw-session-cleaner` | operations / runbook | Session-file cleanup/rebuild workflow with potentially destructive operations requiring guardrails. |
| `will-codex-quota-reset` | operations / tool wrapper | Queries quota-reset timing/probability information. |
| `copaw-ops` | operations / runbook | CoPaw service/config/model/cron/channel troubleshooting. |
| `hermes-ops` | operations / runbook | Hermes Agent service/gateway/platform/cron/profile troubleshooting. |
| `hermes-qq` | operations / pipeline | Workflow for adding/maintaining QQ platform integration in Hermes. |
| `claudian-installer` | distribution / pipeline | Installs/integrates the Claudian Obsidian plugin. |

---

## 4. `coleam00/second-brain-skills`

### Repository analysis

**Identity and structure.** Repository ID `1141291453`, public, non-archived, default branch `main`. The current `.claude/skills` tree contains six skills. README positions them as a knowledge-work/second-brain set sharing progressive-disclosure principles.

**Directly read evidence.** `mcp-client/SKILL.md` and its `scripts/mcp_client.py` were read. The script is a real async MCP client with configuration resolution and separate stdio, SSE, streamable-HTTP, and FastMCP transports; it lists tool schemas on demand rather than exposing every MCP tool definition up front. Search of `skill-creator` showed `SKILL.md`, references, and deterministic scripts including initialization, packaging, and quick validation.

**Architecture.** The MCP client is a useful example of pushing protocol complexity into deterministic code and keeping the skill body focused on routing/configuration. The collection also demonstrates cross-skill artifact reuse: brand files are produced once and consumed by presentation/content workflows.

**Risk/limitation.** MCP configuration may contain API keys in local JSON. The inspected implementation supports environment/config-file resolution but no repository-level secret-management abstraction was observed. No eval suite was observed in the current repository, and the scripts were not executed.

### Individual skill reports

| Skill | Evidence basis | Report |
| --- | --- | --- |
| `brand-voice-generator` | current README/inventory | Produces reusable brand/tone artifacts consumed by other content/presentation skills. |
| `mcp-client` | **direct body + script** | Strong progressive-disclosure wrapper over real MCP transports; deterministic client code keeps tool schemas out of context until requested. |
| `pptx-generator` | current README/inventory | Presentation generation driven by reusable brand configuration and Python presentation tooling. |
| `remotion` | current README/inventory | Remotion/React video domain guidance organized as modular rules. |
| `skill-creator` | inventory + script/reference search | Skill-authoring package with progressive disclosure plus initialization, packaging, and quick-validation helpers. |
| `sop-creator` | current README/inventory | Converts process knowledge into actionable SOP/runbook-style documentation. |

---

## 5. `DannyMac180/skills`

### Repository analysis

**Identity and structure.** Repository ID `1253525979`, public, non-archived, default branch `main`. The repository currently contains two top-level skills.

**Directly read evidence.** Both `codex-dynamic-workflows/SKILL.md` and `explain-this/SKILL.md` were read. The workflow skill separates planning, approval gates, bounded work packets, integration, and verification, and explicitly says not to claim subagent execution when no runner exists. Its `references/risk-gates.md` distinguishes read-only/local actions from destructive, external, expensive, credential, and production actions. `explain-this` uses persistent learner state, artifact-specific adapters, quiz-based comprehension checks, and spaced-repetition state.

**Architecture.** Both skills have unusually explicit state and completion contracts. One is orchestration-oriented; the other is learning-state oriented. The workflow skill's refusal to fake unavailable runner capabilities is a valuable reliability pattern.

**Runtime boundary.** Supporting scripts/references are named by the skill bodies, but no workflow scaffold, verifier, or spaced-repetition script was executed.

### Individual skill reports

| Skill | Evidence basis | Report |
| --- | --- | --- |
| `codex-dynamic-workflows` | **direct body + risk reference** | Supervised orchestration pattern with success criteria, packet isolation, approval gates, explicit integration, and verification. Strong anti-fabrication rule around unavailable subagent runners. |
| `explain-this` | **direct body** | Personalized explanation system with persistent learner profile, artifact adapters, quiz evidence, and spaced repetition. Explicitly separates durable evidence from one-off learner mistakes. |

---

## 6. `davidondrej/skills`

### Repository analysis

**Identity and structure.** Repository ID `1279159149`, public, non-archived, default branch `main`. The repository currently groups 47 skill directories under five categories: agent orchestration (13), skill authoring (4), research/web (8), ops/setup (11), and thinking/docs (11). A separate root `hooks/` directory provides repository-level integration support.

**Directly read evidence.** `effective-agent-skills/SKILL.md` is a substantial authoring guide covering progressive disclosure, description-as-routing-contract, deterministic scripts, validation loops, client-specific invocation controls, failure modes, and security review. `browser-harness/SKILL.md` defines real-browser/CDP operation with explicit routing away from browser automation when static scraping is sufficient, screenshot-first verification, and domain-specific reference loading. `browser-harness/references/install.md` documents install/connection architecture and current-browser vs isolated-browser modes.

**Architecture.** The collection is broad but taxonomy keeps capability discovery tractable. Two recurring design patterns are visible in the direct reads: route to the smallest adequate capability, and move fragile/repetitive behavior to deterministic tools. The authoring skill is especially explicit that trigger descriptions are routing contracts rather than workflow summaries.

**Risk/limitation.** The 47 individual rows below are current directory-inventory reports. Only representative bodies were opened in this batch; therefore body-specific quality claims are restricted to `effective-agent-skills` and `browser-harness`. Browser control and agent orchestration can have high external side effects; this run only inspected their instructions and did not invoke them.

### Individual skill reports

#### Agent orchestration (13)

| Skill | Inventory-level report |
| --- | --- |
| `agent-self-scheduling` | Scheduling/continuation primitive for agent work. |
| `cmux` | Agent/workflow coordination primitive associated with cmux. |
| `codex-subagent` | Codex-oriented subagent delegation workflow. |
| `corral-launch-agents` | Multi-agent launch/coordinator workflow. |
| `fable-review` | Review-oriented orchestration for Fable workflows. |
| `fable-safe-prompt` | Prompt/safety wrapper for Fable-oriented agent work. |
| `git-worktree` | Worktree-based isolation primitive for parallel agent/code tasks. |
| `goal-loop` | Goal-oriented iterative execution loop. |
| `gpt-review` | GPT-based independent/review pass workflow. |
| `handoff` | Structured transfer of context/work between agents or sessions. |
| `herdr` | Multi-agent coordination capability; body not directly read in this batch. |
| `launch-subagent` | Focused subagent launch primitive. |
| `run-deep-swe` | Long/deep software-engineering agent execution workflow. |

#### Skill authoring (4)

| Skill | Inventory-level report |
| --- | --- |
| `distribute-skill-to-all-agents` | Skill distribution/synchronization across agent environments. |
| `effective-agent-skills` | **Directly read.** Comprehensive authoring guide emphasizing routing descriptions, progressive disclosure, deterministic code, validation loops, failure handling, and cross-client differences. |
| `folder-specific-claude-and-agents-md` | Scopes agent instruction files to directory/folder context. |
| `push-skill-to-github` | Publishing/distribution workflow for pushing a skill to GitHub. |

#### Research and web (8)

| Skill | Inventory-level report |
| --- | --- |
| `browser-harness` | **Directly read with install reference.** CDP browser-control capability with static-scrape routing, screenshot verification, real-session support, and explicit setup paths. |
| `deep-research` | Structured deep-research workflow. |
| `deepapi` | DeepAPI-backed web/research capability wrapper. |
| `fireflies-transcript` | Retrieval/processing workflow for Fireflies transcripts. |
| `online-shopping` | Web research workflow specialized for shopping information. |
| `pi-web-search` | Web-search capability for Pi/agent workflows. |
| `research-prompt` | Research prompt/process primitive. |
| `youtube-transcript` | YouTube transcript retrieval/processing workflow. |

#### Ops and setup (11)

| Skill | Inventory-level report |
| --- | --- |
| `anti-sleep` | Prevents or manages host sleep for long-running agent tasks. |
| `create-readonly-db-role` | Database setup workflow for read-only access. |
| `cyber-audit` | Defensive audit workflow; body not directly read in this batch. |
| `global-agent-guardrails` | Cross-environment agent guardrail setup. |
| `google-safe-browsing` | Safe Browsing integration/check workflow. |
| `macbook-metrics-setup` | macOS metrics/observability setup. |
| `nuke-cursor-app` | Destructive-reset style Cursor setup workflow; should be treated as high-impact until body-level gates are verified. |
| `pi-custom-model` | Custom model configuration for Pi. |
| `prod-push` | Production-push workflow; high external side-effect surface by category/name and should require explicit gates. |
| `read-prod-database` | Production database read workflow; sensitive-data boundaries require body-level verification before reuse. |
| `setup-help` | General setup/troubleshooting helper. |

#### Thinking and docs (11)

| Skill | Inventory-level report |
| --- | --- |
| `before-building` | Pre-implementation thinking/requirements discipline. |
| `brain-to-docs` | Converts rough thinking into structured documentation. |
| `decisions` | Decision capture/decision-making workflow. |
| `level-up` | Improvement/refinement workflow. |
| `next-decision` | Chooses or frames the next decision in an ongoing effort. |
| `prompt-me` | Interactive prompting/interviewing workflow. |
| `read-all-adrs` | Loads architecture decision records as project context. |
| `remind` | Reminder/context retention workflow. |
| `save-idea` | Persists an idea into a durable artifact. |
| `short` | Concision/short-output mode. |
| `teach` | Teaching/explanation workflow with supporting resource format. |

---

## 7. `Fokkyp/claude-skills`

### Repository analysis

**Identity and structure.** Repository ID `1118004768`, public, non-archived, default branch `main`. Current repository root contains two skills: `prd-generator` and `competitive-analysis`. The latter has a `references/` subtree.

**Directly read evidence.** Both skill bodies were read, along with `competitive-analysis/references/data-collection.md`. `prd-generator` is primarily a conversational document-generation process with module-by-module clarification/review. `competitive-analysis` is more mature: it has a hard scope-confirmation gate before collection, separates single-product vs multi-product modes, persists raw/summary/merged research artifacts, and loads frameworks/diagram guidance from references.

**Architecture.** `competitive-analysis` demonstrates a useful research pattern: collect → persist raw evidence → summarize per source → merge by analysis dimension → write report. This reduces reliance on transient context. The split reference design is more scalable than the monolithic `prd-generator` body.

**Risk/limitation.** The competitive-analysis workflow assumes a capable web-search/scrape MCP or equivalent and may consume large context; the README itself warns about context pressure. No automated eval/test suite was observed, so the claimed commercial use has not been independently reproduced here.

### Individual skill reports

| Skill | Evidence basis | Report |
| --- | --- | --- |
| `prd-generator` | **direct body** | Conversational PRD authoring workflow covering clarification, competitive input, requirements, Mermaid flows, module review, and structured final document. Mostly prompt-driven; limited deterministic validation. |
| `competitive-analysis` | **direct body + reference** | Evidence-oriented competitive research pipeline with scope gate, phased collection, persisted raw/summary/merged artifacts, framework-driven report modes, and explicit source-confidence handling. |

---

## 8. `haowjy/creative-writing-skills`

### Repository analysis

**Identity and structure.** Repository ID `1083255207`, public, non-archived, default branch `main`. The repository combines 13 skills, a multi-agent writing system, plugin/config files, bootstrap material, docs, scripts, and packaging/release configuration. README describes specialized agents for muse, drafting, critique, editing, reader simulation, character simulation, continuity, brainstorming, outlining, and style capture.

**Directly read evidence.** `creative-writing-muse/SKILL.md` provides a single-agent fallback that deliberately switches stances while keeping author intent visible. `story-memory/SKILL.md` is a reference-oriented durable-state package pointing to context, fact extraction, reference writing, artifact layout, and persistent issue resources. `scripts/create_skill_zips.py` builds `.skill` ZIPs from `cw/skills/*` and includes `SKILL.md` plus resources.

**Architecture.** The repo cleanly separates orchestration/agent roles from shared craft/state skills. `story-memory` is especially relevant as a durable project-memory pattern: settled facts and decisions are written into project artifacts rather than assumed to persist in model context. README also exposes a validation command (`meridian mars check`), but it was not executed.

**Observed packaging nuance.** The packaging script reads `cw/skills/*`, while the repository also exposes a root `skills/` tree. That may be an intentional source/published split, but the relationship was not runtime-validated in this batch and should not be assumed equivalent without the package check.

### Individual skill reports

| Skill | Evidence basis | Report |
| --- | --- | --- |
| `creative-writing-modes` | README inventory | Prose execution modes for drafting, revision, bridges, alternate takes, and line polish. |
| `creative-writing-craft` | README inventory | Craft references for prose, scene construction, style, voice, and genre/page technique. |
| `writing-principles` | README inventory | Reader-reward, quality, and LLM-default discipline for fiction. |
| `story-planning` | README inventory | Direction, brainstorming, outlining, and story architecture before drafting. |
| `story-review` | README inventory | Multi-level editorial review and reader-signal synthesis. |
| `story-memory` | **direct body** | Durable project-state/reference skill for context handoff, fact extraction, reference artifacts, and issue tracking. |
| `reader-sim` | README inventory | First-time reader simulation from a specified persona. |
| `character-sim` | README inventory | In-character simulation for voice and relationship discovery. |
| `creative-writing-muse` | **direct body** | Single-agent fallback coordinator that explicitly changes writing stances while preserving author intent and separating exploration, drafting, critique, and memory. |
| `writing-staffing` | README inventory | Chooses/organizes agent composition for writing workflows. |
| `llm-writing` | README inventory | Language-discipline skill intended to suppress unchosen model defaults while preserving deliberate style decisions. |
| `shared-dao` | README inventory | Shared canonical vocabulary, aliases, and ambiguity-resolution rules. |
| `project-setup` | README inventory | One-time setup of project instruction and knowledge-base structure. |

---

## 9. `Harishwarrior/flutter-claude-skills`

### Repository analysis

**Identity and structure.** Repository ID `1081820059`, public, non-archived, default branch `main`. It contains two domain skills: Flutter testing and defensive mobile-security review. `flutter-tester` is reference-heavy; `owasp-mobile-security-checker` combines a skill body, a mobile-security reference, and four Python scanners.

**Directly read evidence.** Both `SKILL.md` files were read. `flutter-tester` organizes unit/widget/integration/Riverpod testing around layer isolation, Given-When-Then, deterministic async handling, and explicit cleanup. `owasp-mobile-security-checker` separates four automatable checks from manual review categories. `scripts/scan_hardcoded_secrets.py` was inspected: it searches expected project file classes with regex patterns, filters common placeholders, returns structured findings, and exits non-zero for higher-severity results.

**Quality signal.** The security skill correctly warns that scanner findings need contextual verification and that it is not a substitute for a professional assessment. The testing skill is narrowly scoped and gives explicit setup/cleanup/verification patterns instead of generic testing advice.

**Security finding.** The inspected secret scanner includes the matched source line in console/JSON finding output. If a real secret is detected, that behavior can duplicate sensitive material into logs/artifacts. A safer implementation would redact matched values while preserving location/type/severity. This is a report finding only; the scanner was not executed.

### Individual skill reports

| Skill | Evidence basis | Report |
| --- | --- | --- |
| `flutter-tester` | **direct body** | Focused Flutter testing discipline spanning isolated layers, Riverpod/Mockito/GetIt setup, widget-test stability, success/error paths, and cleanup. |
| `owasp-mobile-security-checker` | **direct body + scanner** | Defensive mobile audit workflow combining scripted checks with manual review guidance. Useful automation split, but current secret-finding output should redact sensitive matched content. |

---

## 10. `lukasreese/powerbi-claude-skills`

### Repository analysis

**Identity and structure.** Repository ID `1181497603`, public, non-archived, default branch `main`. README currently marks two skills **Available** and `pbip-dependency-analyzer` **Coming soon**. Only the two available skills are counted as individual skill reports in this batch.

**Directly read evidence.** `pbi-requirements-gathering/SKILL.md` implements a 10-phase adaptive stakeholder interview with per-phase summaries, risk flags, resumable Markdown state, and final HTML/Markdown output. `pbir-report-builder/SKILL.md` writes PBIR JSON into an existing PBIP project rather than trying to recreate Power BI Desktop boilerplate. It instructs the agent to detect the schema version from existing project files and bundles extensive templates/references. `pbir-report-builder/references/folder-structure.md` documents report and semantic-model folder dependencies.

**Architecture.** The report-builder's hybrid strategy is a good response to version-sensitive generated files: let Desktop create authoritative scaffolding, then modify the narrower PBIR surface. The requirements skill's explicit session state makes long interviews resumable and auditable.

**Verified naming issue.** The directory is `pbir-report-builder`, but the current `SKILL.md` frontmatter says `name: pbi-report-builder`. Agent Skills implementations that enforce directory/frontmatter agreement may reject or misroute this package. This should be validated/fixed upstream before treating cross-client portability as verified.

**Not counted.** `pbip-dependency-analyzer` is present as a directory but README status is `Coming soon`; it is not counted as an active/canonical skill report.

### Individual skill reports

| Skill | Evidence basis | Report |
| --- | --- | --- |
| `pbi-requirements-gathering` | **direct body** | Adaptive 10-phase Power BI discovery interview with risk surfacing, question-level status, resumable session state, and shareable outputs. |
| `pbir-report-builder` | **direct body + reference** | PBIR JSON generation against Desktop-created PBIP scaffolding, with local schemas/templates and schema-version detection. Strong version-boundary strategy; current folder/frontmatter name mismatch is a portability defect candidate. |

---

## Cross-repository findings

1. **Deterministic code is the clearest reliability multiplier.** BGGG's Image2PPT renderer, Coleam's MCP client, Chujianyun's validator/tests, Harishwarrior's scanners, and Haowjy's packager all move fragile repeated behavior out of prose. This is stronger evidence of implementability than instructions alone.
2. **Repository-level validation is still uncommon.** `chujianyun/skills` stands out because taxonomy, naming, references, marketplace paths, and likely-secret checks are backed by tests. Other repositories often document validation behavior but do not expose an equally obvious test harness.
3. **Progressive disclosure appears in multiple mature designs.** Coleam's MCP client, Chujianyun's skill/reference split, David Ondrej's authoring guidance, and Haowjy's story-memory resources all avoid loading every detail into the primary skill body.
4. **Persistent artifacts reduce context-loss risk.** Fokkyp's raw/summary/merged research directories, DannyMac180's learner/review state, Haowjy's story knowledge base, and Lukas Reese's resumable requirements Markdown all treat files as durable state rather than assuming conversation memory is authoritative.
5. **Security and portability need explicit validation, not intent.** This batch found concrete candidates: TLS verification disabled in the Xiaohongshu extraction snippet, sensitive matched lines emitted by the Flutter secret scanner, and a folder/frontmatter name mismatch in `pbir-report-builder`. These are direct content findings, not inferred from repository popularity.
6. **Stars are discovery context, not quality evidence.** The most-starred repository in this batch is not automatically the best-governed one; the strongest machine-checkable repository governance observed here is in `chujianyun/skills`.

## Validation boundaries

- Repository identity: verified through GitHub repository metadata.
- Stars: verified from current public GitHub repository pages during this run.
- README/structure: current repository pages and/or repository files were read for every completed repository.
- Skill content: actual `SKILL.md` bodies were read in every completed repository; all skills in the small repositories were read, while large collections use complete current inventory reports plus representative direct body reads as explicitly marked above.
- Scripts/references/evals/tests: inspected when exposed and relevant to the selected direct-read skills; examples include BGGG evals/renderer, Chujianyun validator/tests, Coleam MCP implementation, DannyMac risk reference, David browser reference, Fokkyp collection reference, Haowjy packager, Harish scanner, and Lukas PBIR structure reference.
- Runtime: **not executed**. No third-party command was treated as passing merely because code/tests/evals exist.

## Queue reconciliation

Using the latest index snapshot observed before commit:

```text
indexed unique:              2181
deep-analysis eligible:      1767
held for review:              414
completed before batch 009:    80
completed in batch 009:        10
completed total:               90
eligible remaining estimate: 1677
```

Cumulative individual skill reports after this batch: `463 + 115 = 578`.
