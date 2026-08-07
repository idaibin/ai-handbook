# GitHub Agent Skills deep analysis — batch 008

Observed: 2026-08-07 09:10 +08:00

## Summary

This batch completed content-based review of 10 indexed repositories. A repository is counted only after GitHub identity and displayed stars were checked and actual repository content was read. The review inspected README/equivalent documentation, current skill inventory, representative `SKILL.md` or equivalent definitions, and scripts/references/eval assets when available.

Status for every repository in this batch: `structure-reviewed`.

Runtime status: `not_executed`. No third-party script, browser automation, external API call, build, test suite, eval harness, deployment, cloud operation, or generated media workflow was executed in this batch. Therefore none of the repositories are recorded as runtime-validated.

For large multi-skill repositories, the individual reports below are inventory-level reports grounded in the repository-maintained catalog/current directory inventory plus direct inspection of representative primary skill bodies and supporting implementation/evaluation assets. This is not a claim that every line of every large `SKILL.md` was runtime-tested.

## Queue handling

- Source queue: `sources/catalog/github-agent-skills-index-latest.json`.
- Already-completed identities were skipped.
- `abubakarsiddik31/claude-skills-collection` was inspected during qualification but was not counted: current repository content is a README-only outbound catalog of external skills, with no local skill package inventory. It should be treated as an `awesome_index` / catalog candidate rather than a content-bearing skill collection.
- Ten content-bearing repositories were completed below.

## Repository accounting

| Repository | GitHub identity | Stars observed | Active/canonical skill reports | Evidence boundary |
| --- | --- | ---: | ---: | --- |
| `aakashg/pm-claude-skills` | id `1168031255`, `main`, public, not archived | 93 | 5 | README + all 5 skill definitions |
| `Abhinavbwj/Claude-skills-for-Computational-Designers` | id `1192326101`, `main`, public, not archived | 198 | 18 | README + foundation/calculator skill bodies + calculator script |
| `addyosmani/agent-skills` | id `1158722119`, `main`, public, not archived | 82,884 | 24 | README + representative skill + eval docs/scripts inventory |
| `ahmedasmar/devops-claude-skills` | id `1083527025`, `main`, public, not archived | 193 | 6 | README + Terraform/Kubernetes skill bodies + script/reference inventory |
| `ailabs-393/ai-labs-claude-skills` | id `1091022859`, `main`, public, not archived | 438 | 24 | `ReadMe.md` + SEO skill + installer/generator implementation |
| `aiwithremy/claude-skills-llm-council` | id `1221232109`, `main`, public, not archived | 1.4k (GitHub UI rounded) | 1 | root `SKILL.md` workflow |
| `AKCodez/higgsfield-claude-skills` | id `1209744211`, `master`, public, not archived | 296 | 19 | README/current inventory + representative browser-automation skill |
| `anthropics/skills` | id `1061953414`, `main`, public, not archived | 166.7k (GitHub UI rounded) | 17 | README + current skill tree + `skill-creator` + template + spec path |
| `cafe3310/public-agent-skills` | id `1161077105`, `main`, public, not archived | 248 | 27 active | README + active/parked/archived lifecycle + representative workflow skill |
| `artwist-polyakov/polyakov-claude-skills` | id `1091701368`, `main`, public, not archived | 177 | 19 | README/plugin inventory + `knowledge-compiler` skill |

Total individual skill reports in this batch: **160**.

---

## 1. aakashg/pm-claude-skills

### Evidence read

- `README.md`
- `skills/linkedin-post-writer/SKILL.md`
- `skills/idea-validator/SKILL.md`
- `skills/prompt-engineer/SKILL.md`
- `skills/product-designer/SKILL.md`
- `skills/status-update-writer/SKILL.md`
- repository structure including `templates/`

### Repository analysis

The repository is a small, prompt-first PM collection. Skills are deliberately self-contained rather than backed by a shared runtime. The README distinguishes always-loaded project context from trigger-loaded skills and gives a consistent authoring/testing pattern. Each reviewed skill contains explicit trigger language, an ordered workflow, concrete output formatting, examples, and anti-patterns/checklists.

The strongest reusable pattern is task specificity: a skill owns one narrow deliverable and defines what information to gather, how to reason, and how to format the result. The main validation weakness is that no automated eval harness or executable verification layer was identified; the repository relies primarily on manual prompt testing and the quality of the written workflow.

### Individual skill reports

| Skill | Report |
| --- | --- |
| `linkedin-post-writer` | Structured LinkedIn drafting workflow covering idea extraction, format selection, hook/body/CTA construction, formatting rules, examples, and a pre-publish checklist. |
| `idea-validator` | Evidence-led product idea validation across problem severity, market evidence, differentiation, feasibility, and business viability, followed by competitive scan, verdict, killer questions, and de-risking experiments. |
| `prompt-engineer` | Diagnoses prompts across role, context, instructions, format, examples, constraints, and evaluation criteria, then rewrites with explicit structure and explains the changes. |
| `product-designer` | UI/design review workflow across clarity, flow, information architecture, consistency, error handling, and accessibility, with prioritized actionable findings. |
| `status-update-writer` | Converts raw project notes into an audience-calibrated update with TL;DR, status, completed outcomes, next steps, risks/blockers, decisions, and metrics when supplied. |

Verification note: content inspected; no runtime/eval execution performed.

---

## 2. Abhinavbwj/Claude-skills-for-Computational-Designers

### Evidence read

- `README.md`
- `skills/cd-foundations/SKILL.md`
- `skills/cd-calculator/SKILL.md`
- `skills/cd-calculator/scripts/geometry_calculator.py`
- README-declared reference and calculator inventory

### Repository analysis

This is a domain-heavy AEC/computational-design knowledge system. Its clearest architectural contribution is explicit progressive disclosure: metadata is always available, a `SKILL.md` body loads when invoked, and large references/scripts load only when needed. `cd-foundations` acts as an auto-activated routing/foundation layer, while domain skills handle specialized work and `cd-calculator` provides deterministic computation.

The calculator is not merely described in prose: the inspected Python implementation performs input validation and actual section-property calculations. That raises the repository above a prompt-only collection. However structural/engineering, environmental, material, and other domain outputs were not numerically cross-validated in this batch, so the repository remains structure-reviewed rather than engineering-validated.

### Individual skill reports

| Skill | Report |
| --- | --- |
| `cd-foundations` | Auto-activated foundation and router: computational-design paradigms, tool landscape, core concepts, anti-pattern awareness, and routing to specialized skills. |
| `parametric-modeling` | Parametric dependency-graph thinking, data-tree manipulation, facade parameterization, and performance-feedback patterns. |
| `generative-design` | Generative/evolutionary algorithms, fitness-function design, design-space search, and genotype/phenotype strategies. |
| `computational-geometry` | Curve/surface mathematics, solid modeling, intersections, Voronoi/Delaunay, spatial indexing, and robustness concerns. |
| `algorithmic-patterns` | Tessellation, recursive/fractal systems, attractor fields, packing, and weaving/interlocking pattern generation. |
| `structural-computation` | Form finding, finite-element fundamentals, shell/tensile systems, structural optimization, and early-stage quick checks. |
| `environmental-simulation` | Solar/daylight, wind/thermal, acoustics, energy/carbon, and microclimate simulation guidance. |
| `facade-computation` | Facade panelization/rationalization, glazing/system choices, and fabrication-oriented outputs. |
| `digital-fabrication` | Subtractive/additive/robotic fabrication, digital joinery, and file-to-factory workflow guidance. |
| `bim-scripting` | Revit/Dynamo/IFC automation patterns and BIM-oriented scripting workflows. |
| `interoperability` | Geometry/BIM/GIS file-format capabilities, exchange workflows, API bridges, coordinates, and round-trip fidelity concerns. |
| `scripting-reference` | AEC programming reference spanning Rhino/Python/C++/JavaScript ecosystems and performance patterns. |
| `optimization-methods` | Single- and multi-objective optimization, topology/layout/shape optimization, and surrogate-model methods. |
| `data-driven-design` | Sensor/POE data, spatial analysis, design-space mapping, urban data, and visualization workflows. |
| `mesh-processing` | Mesh generation, quality metrics, subdivision, remeshing, repair, and half-edge topology concepts. |
| `design-automation` | Rule/template automation, DAG orchestration, drawing automation, and testing/versioning of design workflows. |
| `ml-for-aec` | AEC-oriented supervised learning, generative models, computer vision, RL/physics-informed ML, NLP, and MLOps framing. |
| `cd-calculator` | Seven CLI calculators for geometry, structural checks, solar analysis, panel rationalization, mesh analysis, materials, and fabrication costing; a real calculator implementation was inspected. |

Verification note: scripts were read but not executed; engineering/numerical correctness remains unverified.

---

## 3. addyosmani/agent-skills

### Evidence read

- `README.md`
- `skills/spec-driven-development/SKILL.md`
- `evals/README.md`
- repository search confirming `scripts/run-evals.js`, `scripts/lib/skill-lint.js`, validation scripts, hooks, references, agents, and eval case assets

### Repository analysis

The repository models software delivery as a connected lifecycle rather than unrelated prompts. Twenty-four skills cover define → plan → build → verify → review → ship, with a meta-router and shared process conventions. The inspected spec skill uses explicit phase gates and human review before moving from specification to planning/tasks/implementation.

This batch's strongest evaluation architecture is here. The repository documents three separate tiers: deterministic structural validation, deterministic trigger/routing evaluation, and token-spending behavioral evaluation. Trigger tests include positive/negative ownership checks and description-collision detection; behavioral tests use expectations against actual execution/dialogue artifacts. The existence and implementation surface of this harness were inspected, but the harness was not run in this batch.

### Individual skill reports

| Skill | Report |
| --- | --- |
| `using-agent-skills` | Meta-skill that maps incoming work to the correct workflow and establishes shared operating rules. |
| `interview-me` | One-question-at-a-time requirements elicitation for underspecified work. |
| `idea-refine` | Divergent/convergent exploration that turns vague ideas into concrete proposals. |
| `spec-driven-development` | Gated SPECIFY → PLAN → TASKS → IMPLEMENT workflow with surfaced assumptions, success criteria, human review, and a living specification. |
| `planning-and-task-breakdown` | Decomposes specifications into small, dependency-ordered, verifiable tasks with acceptance criteria. |
| `incremental-implementation` | Thin vertical slices with implement/test/verify/commit checkpoints, safe defaults, and rollback-friendly changes. |
| `test-driven-development` | Red-Green-Refactor workflow and test-structure guidance for behavior changes and bug fixes. |
| `context-engineering` | Controls which rules, specifications, source files, and integrations enter context at each stage. |
| `source-driven-development` | Grounds framework/library decisions in authoritative documentation and explicitly marks unverified claims. |
| `doubt-driven-development` | Adversarial review loop that extracts claims, challenges them, reconciles evidence, and defines a stopping condition. |
| `frontend-ui-engineering` | Component architecture, design systems, state management, responsive UI, and accessibility guidance. |
| `api-and-interface-design` | Contract-first API/module-boundary design with compatibility and input-boundary validation. |
| `browser-testing-with-devtools` | Browser runtime inspection workflow using DOM, console, network, and performance evidence. |
| `debugging-and-error-recovery` | Systematic reproduce → localize → reduce → fix → guard workflow with failure handling. |
| `code-review-and-quality` | Multi-axis review, change sizing, severity labels, and actionable review standards. |
| `code-simplification` | Reduces complexity while preserving behavior and respecting existing design constraints. |
| `security-and-hardening` | Secure input/auth/secrets/dependency/boundary review workflow; not security-validated by this batch. |
| `performance-optimization` | Measure-first profiling and optimization workflow rather than speculative tuning. |
| `git-workflow-and-versioning` | Trunk/atomic-commit/version-control discipline and commit-as-save-point patterns. |
| `ci-cd-and-automation` | CI/CD quality gates, feedback loops, feature-flagging, and automation guidance. |
| `deprecation-and-migration` | Structured removal/migration workflows with compatibility and zombie-code cleanup concerns. |
| `documentation-and-adrs` | Architecture decisions and API/documentation practices focused on preserving rationale. |
| `observability-and-instrumentation` | Structured logs, metrics, tracing, and symptom-based alerts as part of shipping. |
| `shipping-and-launch` | Pre-launch checks, staged rollout, rollback, feature-flag lifecycle, and monitoring. |

Verification note: eval architecture was inspected, not executed.

---

## 4. ahmedasmar/devops-claude-skills

### Evidence read

- `README.md`
- `iac-terraform/skills/SKILL.md`
- `k8s-troubleshooter/skills/SKILL.md`
- README-declared scripts, references, and production templates across the remaining plugins

### Repository analysis

The repository packages six DevOps domains as Claude Code marketplace plugins. The inspected skills are operational workflows rather than short tips: they define triage/decision trees, scripts, references, validation steps, and remediation/verification phases. Several plugins expose supporting Python analysis tools and templates, particularly cost optimization, GitOps, and observability.

This is a domain where instructions can have external side effects. No infrastructure/cloud/cluster command was executed in this review, and no claim is made that the operational procedures are safe for a specific production environment.

### Individual skill reports

| Skill | Report |
| --- | --- |
| `iac-terraform` | Terraform/Terragrunt module design, state/drift inspection, validation, troubleshooting, and reusable infrastructure workflows backed by scripts/references. |
| `k8s-troubleshooter` | Systematic Kubernetes incident workflow from context gathering through triage/root-cause/remediation/verification, with supporting diagnostics. |
| `aws-cost-optimization` | FinOps-oriented identification of waste, reservation/rightsizing opportunities, anomalies, and recurring reporting; supporting analysis scripts are declared. |
| `ci-cd` | Pipeline design, caching/performance, security, and troubleshooting across CI/CD systems. |
| `gitops-workflows` | GitOps design and troubleshooting across ArgoCD/Flux, multi-environment/multi-cluster patterns, secrets, and progressive delivery; scripts/references/templates are declared. |
| `monitoring-observability` | Metrics, alerting, tracing, SLO/error-budget, dashboard, health-check, and tool-selection workflows with scripts/references/templates. |

Verification note: operational commands and cloud integrations were not run.

---

## 5. ailabs-393/ai-labs-claude-skills

### Evidence read

- `ReadMe.md`
- current `packages/skills/` inventory
- `packages/skills/seo-optimizer/SKILL.md`
- `install-skills.mjs`
- `generate-index-files.js`

### Repository analysis

The repository is both a skill collection and an npm-oriented packaging/installation layer. Skills can include `SKILL.md`, scripts, assets, and generated JS entrypoints. The SEO skill demonstrates a real script-driven audit workflow.

Two implementation details materially affect trust in the package surface. First, `generate-index-files.js` creates default `index.js` files that only log a skill name and return a generic success object when an entrypoint is missing; therefore an `index.js` being present is not proof that a skill has real executable logic. Second, the inspected installer copies built skills into the host `.claude/skills` directory and contains cleanup behavior when running from `node_modules`. These behaviors should be reviewed before treating the npm package as a transparent installer. No installer/build was executed here.

### Individual skill reports

| Skill | Report |
| --- | --- |
| `brand-analyzer` | Brand/audience analysis automation package. |
| `business-analytics-reporter` | Business metrics and reporting-oriented skill. |
| `business-document-generator` | Structured business-document generation workflow. |
| `cicd-pipeline-generator` | CI/CD configuration and pipeline-generation workflow. |
| `codebase-documenter` | Codebase documentation and explanatory artifact generation. |
| `csv-data-visualizer` | CSV analysis and visualization workflow. |
| `data-analyst` | General data-analysis skill package. |
| `docker-containerization` | Container-packaging workflow; runtime container operations were not executed. |
| `document-skills` | Document unpacking/validation/tooling-oriented bundle. |
| `finance-manager` | Finance-oriented workflow; no professional/financial correctness validation was performed. |
| `frontend-enhancer` | Frontend improvement and enhancement workflow. |
| `nutritional-specialist` | Nutrition-oriented guidance package; no health/clinical correctness validation was performed. |
| `personal-assistant` | General personal-assistant automation workflow. |
| `pitch-deck` | Pitch-deck content/generation workflow. |
| `research-paper-writer` | Structured research-paper drafting workflow. |
| `resume-manager` | Résumé creation/management workflow. |
| `script-writer` | Script/content drafting workflow. |
| `seo-optimizer` | Concrete SEO audit and remediation workflow invoking a local analyzer script and supporting structured output. |
| `social-media-generator` | Social-content generation workflow. |
| `startup-validator` | Startup/product idea validation workflow. |
| `storyboard-manager` | Storyboard planning and management workflow. |
| `tech-debt-analyzer` | Technical-debt assessment workflow. |
| `test-specialist` | Software-testing support workflow. |
| `travel-planner` | Travel-planning workflow. |

Verification note: packaging/build/postinstall behavior was inspected but not executed.

---

## 6. aiwithremy/claude-skills-llm-council

### Evidence read

- root `SKILL.md` including trigger policy, advisor definitions, council stages, peer-review flow, and synthesis instructions

### Repository analysis

This is a single orchestration skill. It frames a decision, enriches context from the workspace, dispatches five role-conditioned advisors in parallel, anonymizes their responses for peer review, and synthesizes a final recommendation through a chairman stage.

Its useful design idea is not “ask five times” but deliberate disagreement plus anonymous cross-review. The main limitation is equally important: the diversity described by the skill comes from role-conditioned subagents, not necessarily independent underlying models. No benchmark/eval evidence or scripts were identified in the repository during this batch.

### Individual skill reports

| Skill | Report |
| --- | --- |
| `llm-council` | Multi-lens decision review using five intentionally conflicting reasoning roles, anonymous peer review, and chairman synthesis for higher-stakes tradeoffs. |

Verification note: orchestration instructions inspected; no subagent experiment executed.

---

## 7. AKCodez/higgsfield-claude-skills

### Evidence read

- current README/inventory on default branch `master`
- `higgsfield-image-auto/SKILL.md`
- repository-level distinction between automation skills and prompt-style skills

### Repository analysis

The repository combines four workflow/automation skills with fifteen media-prompt style skills. The inspected automation skill is concrete about browser state, model/settings selection, result verification, and—importantly—requires user confirmation immediately before an action that consumes generation credits. This is a useful side-effect gate pattern.

The implementation is tightly coupled to a third-party web UI and dynamic browser element structure, so UI drift is an obvious maintenance risk. No browser session or generation was executed in this batch.

### Individual skill reports

| Skill | Report |
| --- | --- |
| `ugc-hot-girl` | UGC character-prompt generation stage used by the repository's media pipeline. |
| `higgsfield-image-auto` | Browser-assisted image-generation workflow with explicit pre-generation confirmation for a credit-consuming action. |
| `seedance-auto-generate` | Browser-assisted image-to-video generation workflow. |
| `ugc-video-auto` | Higher-level orchestration for the repository's UGC image/video pipeline. |
| `01-cinematic` | Cinematic visual prompt/style guidance. |
| `02-3d-cgi` | 3D/CGI visual prompt/style guidance. |
| `03-cartoon` | Cartoon/animation-oriented prompt guidance. |
| `04-comic-to-video` | Comic/manga-to-video prompt workflow. |
| `05-fight-scenes` | Action-scene prompt/style guidance. |
| `06-motion-design-ad` | Motion-design advertising prompt guidance. |
| `07-ecommerce-ad` | E-commerce advertising visual prompt guidance. |
| `08-anime-action` | Anime action-oriented prompt guidance. |
| `09-product-360` | Product turntable/360-style visual prompt workflow. |
| `10-music-video` | Music-video visual prompt guidance. |
| `11-social-hook` | Short-form/social-hook visual prompt guidance. |
| `12-brand-story` | Brand-story visual prompt guidance. |
| `13-fashion-lookbook` | Fashion/lookbook visual prompt guidance. |
| `14-food-beverage` | Food/beverage visual prompt guidance. |
| `15-real-estate` | Real-estate visual prompt guidance. |

Verification note: no media-generation or browser automation was executed.

---

## 8. anthropics/skills

### Evidence read

- `README.md`
- current `skills/` tree
- `skills/skill-creator/SKILL.md`
- `template/SKILL.md`
- `spec/agent-skills-spec.md` path/current presence

### Repository analysis

This repository is an authoritative reference point for Anthropic's implementation of skills. It combines examples, a specification, a minimal template, and complex production-used/source-available document skills. The README explicitly distinguishes Apache-2.0 open-source examples from the source-available document skills (`docx`, `pdf`, `pptx`, `xlsx`); that license distinction must be preserved when reusing ideas or code.

`skill-creator` is particularly valuable because it treats skill authoring as an empirical loop: capture intent, write the skill, create realistic test prompts, run with-skill and baseline variants, evaluate qualitatively/quantitatively, iterate, and optimize triggering. It also codifies progressive disclosure and a “lack of surprise” safety principle. The testing workflow was read, not executed.

### Individual skill reports

| Skill | Report |
| --- | --- |
| `algorithmic-art` | Generative/algorithmic art workflow and creative coding guidance. |
| `brand-guidelines` | Applies supplied brand rules/assets to produced artifacts. |
| `canvas-design` | Static visual/canvas design workflow. |
| `claude-api` | Claude API implementation/migration guidance. |
| `doc-coauthoring` | Collaborative document-writing workflow. |
| `docx` | Complex Word document creation/editing skill; source-available rather than Apache-2.0 according to the repository README. |
| `frontend-design` | Frontend/UI design workflow. |
| `internal-comms` | Internal communication artifact workflow. |
| `mcp-builder` | MCP server authoring guidance. |
| `pdf` | Complex PDF workflow; source-available rather than Apache-2.0 according to the repository README. |
| `pptx` | Complex presentation generation/editing workflow; source-available rather than Apache-2.0 according to the repository README. |
| `skill-creator` | Full skill authoring/evaluation/iteration workflow with baseline comparison, eval artifacts, progressive disclosure, and description optimization. |
| `slack-gif-creator` | GIF creation workflow targeted at Slack usage. |
| `theme-factory` | Reusable visual-theme generation/application workflow. |
| `web-artifacts-builder` | Builds interactive web artifacts. |
| `webapp-testing` | Web-application testing workflow. |
| `xlsx` | Complex spreadsheet workflow; source-available rather than Apache-2.0 according to the repository README. |

The template and Agent Skills specification were inspected as repository-level standards assets and are not counted as additional skills.

Verification note: no skill evals or production document workflows were executed.

---

## 9. cafe3310/public-agent-skills

### Evidence read

- current `README.md`
- active/`skills_parked`/`skills_archived` catalog separation
- frontmatter convention documenting `depends_on_skill` and `depends_on_binary`
- `skills/doc-todo-log-loop/SKILL.md`
- repository search confirming multiple active and parked skill paths

### Repository analysis

The repository is intentionally personal and says so. Its notable catalog design is lifecycle-aware: active skills are separated from parked and archived skills instead of every historical package being presented as equally current. This batch counts only the 27 active skills; parked and archived entries are retained by the repository but excluded from the active skill count.

The repository extends skill frontmatter with explicit skill and binary dependencies, which is useful for machine-readable dependency checks. The inspected `doc-todo-log-loop` also has clear human-control boundaries: documentation/TODO planning precede execution, verification must be reported, user confirmation precedes completion logging, and the human owns the final git-commit step. The README warns users to audit skill documents/code before local installation.

### Individual active skill reports

| Skill | Report |
| --- | --- |
| `doc-todo-log-loop` | Lightweight document → TODO → human assignment → implementation/verification → development-log loop with explicit completion gates. |
| `project-design-concept-organizer` | Extracts implicit design decisions from code/project changes into reusable design concepts/protocol documentation. |
| `learning-assistant` | Interactive learning workflow with structured topic decomposition and persistent local learning-state/knowledge tracking. |
| `wx-emoji-maker` | Batch image-processing workflow for preparing WeChat-style emoji assets. |
| `showcase-video-processor` | Release/showcase video post-processing and storyboard-planning workflow using media tooling. |
| `agent-browser` | Browser automation skill based on a compact accessibility-tree/element-reference workflow; sourced from another project per README. |
| `impeccable` | Frontend design/iteration workflow sourced from an upstream project and kept as an active local skill. |
| `handoff` | Produces/updates `HANDOFF.md` so a fresh-context agent can continue a task with goals, progress, attempts, recommended skills, and next steps. |
| `claude-code-handoff` | Parses local Claude Code session history into a handoff artifact for continuation in a fresh session. |
| `git-snapshot-rollback` | Creates a safety snapshot before destructive git rollback and records traceability links. |
| `interactive-human-review` | Guided human review/checklist workflow for large changes, emphasizing understanding and explicit checkpoints. |
| `release-showcase-manager` | Repository-scale management workflow for model-release demonstrations, from research/scenarios through implementation/recording/evaluation. |
| `model-cookbook-writer` | Source-referenced workflow for designing and compiling model cookbooks into browsable artifacts. |
| `im-local-kb` | Large IM/chat knowledge-ingestion and local Markdown knowledge-base workflow with incremental processing. |
| `media-organizer` | Media-asset naming/classification/indexing workflow using metadata/content-aware organization. |
| `doc-template-provider` | Standardized project/product/defect/TODO/document templates for consistent project documentation. |
| `tech-to-marketing-brief` | Converts technical capabilities into marketing briefs, channel-specific content examples, and related implementation tickets. |
| `weekly-report-writer` | Builds weekly reports from dated logs/project documents while carrying unfinished items and surfacing risks. |
| `cafe3310-obsidian-writer` | Writes notes using the repository owner's Obsidian metadata/tag/style conventions. |
| `content-tone-adjuster` | Rewrites content toward more natural/practical tone profiles defined by the repository. |
| `long-audio-transcript-processor` | Incremental long-transcript cleanup/structuring with resumable state and shared terminology corrections. |
| `long-audio-to-obsidian` | Converts complex transcript-project files into consolidated Obsidian-ready Markdown. |
| `interview-processor` | Structures interview preparation and post-interview records from transcripts, notes, role information, and résumé context. |
| `deep-research` | Multi-stage research workflow with evaluation framing, parallel source collection, cross-comparison, and saturation checks. |
| `online-content-collector` | Localizes marked online/file content into a structured local knowledge workflow. |
| `twitter-watch` | Collects interaction data for a configured set of posts; external retrieval behavior was not executed. |
| `markdown-new` | Converts web/file content to Markdown using an external conversion service workflow. |

Verification note: parked/archived skills were not counted as active; external tools/services were not executed.

---

## 10. artwist-polyakov/polyakov-claude-skills

### Evidence read

- `README.md`
- marketplace/plugin-oriented structure under `plugins/<plugin>/skills/<skill>/`
- `plugins/knowledge-compiler/skills/knowledge-compiler/SKILL.md`
- README-declared script/cache/quality-gate behavior

### Repository analysis

The repository packages nineteen domain plugins around concrete external tools and repeatable workflows. Its strongest inspected design is `knowledge-compiler`: it converts legally accessible long-form material into a source-mapped reusable skill rather than merely summarizing it. The workflow separates source extraction, outline scouting, segmentation, skeleton creation, structured knowledge compilation, source pointers/manifest, and a quality gate. It explicitly rejects DRM/paywall/access-protection bypass and requires source mapping for substantive claims.

The broader catalog includes scraping, remote-server operations, analytics, publishing, image generation, social/research APIs, and genome interpretation. Those domains carry materially different safety/correctness requirements; this batch only reviewed structure/content and did not execute them or validate professional/clinical correctness.

### Individual skill reports

| Skill | Report |
| --- | --- |
| `docx-contracts` | Fills structured Word templates from context/placeholders and gathers missing fields. |
| `scrapedo-web-scraper` | External-service web extraction workflow; not executed in this review. |
| `agent-deck` | AI-agent session creation/status/result orchestration through an external CLI. |
| `genome-analizer` | Genetic-data interpretation workflow; no clinical/medical correctness validation was performed. |
| `ssh-remote-connection` | Remote-server connection/operation workflow; no remote operation was executed. |
| `yandex-wordstat` | Search-demand/keyword analysis workflow using Yandex data. |
| `codex-review` | Cross-agent implementation/review workflow with review-state logging and recursion guard. |
| `fal-ai-image` | Image-generation/editing workflow through an external image API. |
| `yandex-search-api` | Yandex search-result API collection/parsing workflow. |
| `yandex-metrika` | Yandex Metrika analytics/reporting workflow with cache-oriented data handling. |
| `yandex-webmaster` | Yandex Webmaster site/search/indexing management workflow. |
| `telegraph-publisher` | Telegraph page publication and asset-management workflow. |
| `crawl4ai-seo` | Website crawling and SEO-analysis workflow. |
| `telegram-channel-parser` | Telegram-channel content collection/parsing workflow. |
| `x-research` | X/Twitter research workflow using an external API. |
| `github-pages-publisher` | GitHub Pages publication workflow. |
| `sourcecraft-publisher` | SourceCraft site publication workflow. |
| `reddit-skill` | Reddit research/API workflow. |
| `knowledge-compiler` | Source-to-skill compilation pipeline with outline/segment stages, structured references, source map/manifest, and a quality gate. |

Verification note: external APIs, remote operations, publishing, scraping, and domain-sensitive workflows were not executed.

---

## Cross-repository findings

1. **Evaluation maturity varies substantially.** `addyosmani/agent-skills` has the strongest explicit multi-tier repository-wide eval design in this batch; `anthropics/skills` embeds with-skill/baseline iteration and eval methodology in `skill-creator`. Most other repositories rely on structural conventions, examples, scripts, and manual testing rather than a repeatable behavioral eval layer.

2. **Progressive disclosure is a reusable architecture, not just a formatting preference.** The computational-design repository explicitly separates metadata, skill body, and on-demand references/scripts; Anthropic's authoring guidance describes the same three-level model. `addyosmani/agent-skills` similarly pushes shared material into references and task-specific workflows into skills.

3. **Human approval gates are a strong side-effect control.** The Higgsfield automation requires confirmation before a credit-consuming action; `doc-todo-log-loop` retains human task selection and final git ownership; `spec-driven-development` uses human phase reviews. This is preferable to relying only on a generic warning in prose.

4. **Artifact presence is not implementation proof.** `ailabs-393/ai-labs-claude-skills` can generate missing JS entrypoints from a placeholder template. Future catalog scoring should distinguish substantive executable code from generated stubs.

5. **Catalog lifecycle state matters.** `cafe3310/public-agent-skills` distinguishes active, parked, and archived skills. The catalog should preserve this state so historical packages are not accidentally treated as current/available.

6. **Licensing belongs in the evidence model.** `anthropics/skills` explicitly states that several production document skills are source-available rather than open source. Reference value does not imply permission to copy code wholesale.

7. **Domain-sensitive repositories require stronger validation than structural review.** AEC engineering calculations, infrastructure operations, finance/nutrition/genome-oriented workflows, and external-account automations cannot be considered trustworthy merely because the instructions and scripts are coherent. Runtime tests and, where relevant, domain review remain separate gates.

## Batch result

- Repositories completed this batch: **10**
- Individual active/canonical skill reports: **160**
- Repository status: **structure-reviewed**
- Runtime validation: **not executed**
- README-only catalog triaged but not counted: `abubakarsiddik31/claude-skills-collection`
