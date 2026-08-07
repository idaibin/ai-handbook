# GitHub Agent Skills Deep Analysis — Batch 011

## Run result

- Batch: `2026-08-07-batch-011`
- Repository completions: **10**
- Individual skill reports: **274**
- Completion basis: repository identity + displayed GitHub stars + actual repository content inspection. No repository was completed from metadata alone.
- Evidence model: current repository-maintained inventories were used to enumerate all current skills; representative `SKILL.md` or equivalent definitions were directly read in every repository, with scripts, references, evals, validators, or checks read when available.
- Runtime validation: **not_executed**. Third-party scripts, installers, browsers, external services, pricing calculators, compliance tooling, and test suites were inspected where available but were not executed.
- Queue snapshot: `sources/catalog/github-agent-skills-index-latest.json`, `2502` unique repositories, `2088` deep-analysis eligible, `414` held for review.

Large collections are not represented as if every skill body was directly read. Each individual row records whether its basis is direct body evidence or the repository's current maintained inventory. Repository-level completion requires actual content reading beyond metadata; inventory-only rows do not imply body-level validation.

## Repository summary

| Repository | GitHub repository ID | Default branch | Stars observed | Current individual reports | Direct content evidence |
| --- | ---: | --- | ---: | ---: | --- |
| `posit-dev/skills` | `1101373353` | `main` | 460 | 23 | README/current catalog; `posit-dev/critical-code-reviewer/SKILL.md`; `count-skill-tokens.py` |
| `proficientlyjobs/proficiently-claude-skills` | `1155688938` | `main` | 311 | 7 | README/current inventory; `skills/setup/SKILL.md`; shared priority reference |
| `RTFM-IT-Services-LLC/msp-claude-skills` | `1304996438` | `main` | 62 | 14 | README/current tree; `skills/msp-pricing/SKILL.md`; deterministic pricing script |
| `SimonTheSalesBooster/ClaudeSkills-SprintClub` | `1162408886` | `main` | 37 | 29 | Current root inventory; `01-linkedin-prospect-hunter/SKILL.md`; duplicate `sales-closer` definitions |
| `staruhub/ClaudeSkills` | `1087021837` | `main` | 661 | 13 | Current curated inventory; `deep-research/SKILL.md`; validator; routing evals |
| `Sushegaad/Claude-Skills-Governance-Risk-and-Compliance` | `1183297079` | `main` | 810 | 30 | Current framework inventory; ISO 27001 packaged-skill documentation; repository eval-result artifact |
| `honnibal/claude-skills` | `1157050867` | `main` | 267 | 9 | README/current command inventory; `tighten-types.md.txt`; AST stub helper |
| `iamzhihuix/happy-claude-skills` | `1123503916` | `main` | 303 | 11 | README/current inventory; browser `SKILL.md`; Chrome/CDP launcher implementation |
| `jianshuo/claude-skills` | `1235464336` | `main` | 112 | 35 | Current root inventory; VoiceDrop prompt-eval skill; blind-judge rubric |
| `rampstackco/claude-skills` | `1224033309` | `main` | 519 | 103 | README/current 103-skill catalog; `creative-direction/SKILL.md`; brief reference; `SKILLS.lock` checksum manifest |

Stars are mutable observations from public GitHub repository pages during this run, not immutable repository properties. The RTFM page used for the displayed star observation was a recent GitHub crawl rather than a same-minute API field because the repository metadata connector does not expose stars.

---

## 1. `posit-dev/skills`

### Repository analysis

**Identity and structure.** Public, non-archived repository on `main`. The current catalog is organized by Posit/R ecosystem domains and shared cross-domain skill packages. The current maintained inventory resolves to 23 unique skill identities after deduplicating shared entries such as `brand-yml` and `alt-text` that appear in more than one catalog section.

**Direct content evidence.** `posit-dev/critical-code-reviewer/SKILL.md` is a substantial review protocol rather than a short persona prompt. It requires repository/PR context, distinguishes established facts from inferences and verification questions, uses severity tiers, treats accessibility as a cross-cutting quality requirement, and separates internal findings from implementer-facing feedback. `count-skill-tokens.py` parses `SKILL.md` frontmatter plus references and deterministically reports token/line size, including explicit metadata/body limits.

**Quality / risk.** The repository demonstrates useful authoring discipline through reusable review protocol and deterministic size measurement. No central repository-wide eval suite was directly observed in this batch, so no model-behavior pass claim is made.

### Individual skill reports

| Skill | Evidence basis | Report |
| --- | --- | --- |
| `critical-code-reviewer` | **direct body** | Evidence-oriented PR/code review workflow with context gathering, uncertainty labels, severity, accessibility, and controlled publication boundaries. |
| `describe-design` | current catalog | Current Posit catalog skill; body not directly read in this batch. |
| `new-work` | current catalog | Current Posit catalog skill; body not directly read in this batch. |
| `review-testing` | current catalog | Current Posit catalog skill; body not directly read in this batch. |
| `working-on` | current catalog | Current Posit catalog skill; body not directly read in this batch. |
| `pr-create` | current catalog | Current GitHub/PR workflow skill; body not directly read in this batch. |
| `pr-threads-address` | current catalog | Current GitHub/PR workflow skill; body not directly read in this batch. |
| `pr-threads-resolve` | current catalog | Current GitHub/PR workflow skill; body not directly read in this batch. |
| `create-release-checklist` | current catalog | Current release workflow skill; body not directly read in this batch. |
| `release-post` | current catalog | Current release workflow skill; body not directly read in this batch. |
| `testing-r-packages` | current catalog | Current R-package testing skill; body not directly read in this batch. |
| `cli` | current catalog | Current R/CLI-oriented skill; body not directly read in this batch. |
| `cran-extrachecks` | current catalog | Current CRAN-check workflow skill; body not directly read in this batch. |
| `lifecycle` | current catalog | Current R lifecycle skill; body not directly read in this batch. |
| `r-package-development` | current catalog | Current R package development skill; body not directly read in this batch. |
| `mirai` | current catalog | Current catalog entry for Mirai-related work; body not directly read in this batch. |
| `alt-text` | current catalog | Shared accessibility/content skill appearing across catalog groupings; counted once. |
| `ggsql` | current catalog | Current ggsql-oriented skill; body not directly read in this batch. |
| `brand-yml` | current catalog | Shared brand configuration skill appearing across catalog groupings; counted once. |
| `shiny-bslib` | current catalog | Current Shiny/bslib skill; body not directly read in this batch. |
| `shiny-bslib-theming` | current catalog | Current Shiny/bslib theming skill; body not directly read in this batch. |
| `authoring` | current catalog | Current Quarto authoring skill; body not directly read in this batch. |
| `deploy-to-connect` | current catalog | Current Posit Connect deployment skill; body not directly read in this batch. |

---

## 2. `proficientlyjobs/proficiently-claude-skills`

### Repository analysis

**Identity and structure.** Public repository on `main`. Seven skills live under `skills/`, with shared references/templates providing cross-skill policy, fit scoring, data-directory rules, prerequisites, browser setup, and ATS patterns. The workflow uses persistent local user data under a dedicated data directory rather than embedding state in each skill.

**Direct content evidence.** `skills/setup/SKILL.md` implements resumable onboarding: inspect existing state, collect/save resume, capture preferences, optionally import LinkedIn contacts, interview through work history, then summarize readiness. `shared/references/priority-hierarchy.md` gives a clear conflict-resolution order headed by accuracy and explicit user corrections before workflow/style concerns.

**Quality / risk.** Shared references reduce cross-skill drift and the setup flow checks what already exists before writing. The suite handles personal career data and optional contact exports, so filesystem and privacy boundaries matter. No explicit repository eval suite was observed in this batch.

### Individual skill reports

| Skill | Evidence basis | Report |
| --- | --- | --- |
| `setup` | **direct body + shared reference** | Resumable local onboarding for resume, preferences, optional contacts, and work-history profile, governed by shared accuracy/user-correction precedence. |
| `job-search` | current README/inventory | Job-search workflow in the current seven-skill suite; body not directly read in this batch. |
| `tailor-resume` | current README/inventory | Resume tailoring workflow; body not directly read in this batch. |
| `cover-letter` | current README/inventory | Cover-letter workflow; body not directly read in this batch. |
| `network-scan` | current README/inventory | Network/contact matching workflow; body not directly read in this batch. |
| `apply` | current README/inventory | Job-application workflow; body not directly read in this batch. |
| `jobsearch-telegram` | current README/inventory | Telegram-oriented job-search workflow; body not directly read in this batch. |

---

## 3. `RTFM-IT-Services-LLC/msp-claude-skills`

### Repository analysis

**Identity and structure.** Public repository on `main`, packaged as an MSP operations kit. Current `skills/` contains 14 skill directories. The README currently says “Fifteen skills” and still documents `msp-leadgen`, but `msp-leadgen` is absent from the current skill tree; this report uses the actual current tree and records the drift rather than inflating the count.

**Direct content evidence.** `msp-pricing/SKILL.md` explicitly treats bundled dollar figures, margins, floors, multipliers, and labor assumptions as example defaults that must be rebuilt for the operator's own business. It delegates arithmetic to `scripts/price_quote.py`, which implements deterministic loaded-cost, floor, anchor, contract-ladder, value-uplift, margin, and minimum-engagement checks. This is a useful pattern: judgment stays in the skill while repeated arithmetic moves to code.

**Quality / risk.** Cross-skill ownership rules are explicit: pricing owns client-visible numbers, brand owns voice/format, and legal-adjacent work has an attorney escalation path. The principal issue is README/tree inventory drift. The pricing implementation was inspected but not executed; no correctness claim about its output is made.

### Individual skill reports

| Skill | Evidence basis | Report |
| --- | --- | --- |
| `msp-brand` | current tree/README | Foundation skill for MSP identity, voice, naming, and formatting; body not directly read in this batch. |
| `msp-client-comms` | current tree/README | Operational client communication workflow; body not directly read in this batch. |
| `msp-helpdesk` | current tree/README | Helpdesk priority/escalation workflow; body not directly read in this batch. |
| `msp-legal` | current tree/README | Legal-document/negotiation workflow with attorney escalation boundary; body not directly read in this batch. |
| `msp-maintenance` | current tree/README | Maintenance, patching, backup, monitoring, and change-management workflow; body not directly read in this batch. |
| `msp-marketing` | current tree/README | MSP content/distribution workflow; body not directly read in this batch. |
| `msp-metrics` | current tree/README | MSP monthly business/operational metrics workflow; body not directly read in this batch. |
| `msp-offboarding` | current tree/README | Client exit/offboarding runbook; body not directly read in this batch. |
| `msp-onboarding` | current tree/README | Client onboarding runbook; body not directly read in this batch. |
| `msp-pricing` | **direct body + script** | Pricing configurator that separates assumptions/judgment from deterministic calculation and explicitly requires local re-costing before client use. |
| `msp-qbr` | current tree/README | Quarterly business review workflow; body not directly read in this batch. |
| `msp-sales` | current tree/README | Sales/discovery/objection/pipeline workflow; body not directly read in this batch. |
| `msp-setup` | current tree/README | Guided kit configuration/readiness workflow; body not directly read in this batch. |
| `msp-website-setup` | current tree/README | Client static-site setup/deployment workflow; body not directly read in this batch. |

`msp-leadgen` is not counted because it is documented in the README but absent from the current `skills/` tree.

---

## 4. `SimonTheSalesBooster/ClaudeSkills-SprintClub`

### Repository analysis

**Identity and structure.** Public repository on `main`. The current root contains numbered skill directories `01` through `28`, plus both `sales-closer/` and `sales.closer/`. The README still presents an 18-skill collection, so the live tree is materially ahead of its documentation.

**Direct content evidence.** `01-linkedin-prospect-hunter/SKILL.md` defines inputs, search construction, a qualification scoring rubric, trigger-event research, tabular prospect output, and prioritization; it is a self-contained procedural Markdown skill without frontmatter. `sales-closer/SKILL.md` and `sales.closer/SKILL.md` were both read and are byte-identical with the same frontmatter `name: sales-closer`. They are therefore one skill identity exposed at two paths, not two individual reports.

**Quality / risk.** The collection is easy to inspect because most behavior is embedded directly in Markdown. It has weaker packaging discipline than repositories with validators/evals, and the README/tree drift plus duplicated alias path are concrete maintainability signals. No repository-level scripts, references, or eval suite were observed for the numbered family in this batch.

### Individual skill reports

| Skill | Evidence basis | Report |
| --- | --- | --- |
| `linkedin-prospect-hunter` | **direct body** | Defines ICP inputs, search strategy, qualification score, trigger events, prospect table, and prioritization. |
| `apollo-lead-builder` | current tree | Current numbered sales skill; body not directly read in this batch. |
| `social-selling-daily-routine` | current tree | Current numbered sales skill; body not directly read in this batch. |
| `icp-builder` | current tree | Current numbered ICP-building skill; body not directly read in this batch. |
| `pipeline-health-analyzer` | current tree | Current numbered pipeline analysis skill; body not directly read in this batch. |
| `prospect-research-brief` | current tree | Current numbered prospect-research skill; body not directly read in this batch. |
| `linkedin-outreach-writer` | current tree | Current numbered outreach-writing skill; body not directly read in this batch. |
| `crm-data-enrichment` | current tree | Current numbered CRM enrichment skill; body not directly read in this batch. |
| `deal-progression-coach` | current tree | Current numbered deal-progression skill; body not directly read in this batch. |
| `content-to-pipeline-planner` | current tree | Current numbered content-to-pipeline skill; body not directly read in this batch. |
| `deal-closer-playbook` | current tree | Current numbered closing playbook; body not directly read in this batch. |
| `negotiation-conditions-builder` | current tree | Current numbered negotiation skill; body not directly read in this batch. |
| `strategic-partner-finder` | current tree | Current numbered partner-finding skill; body not directly read in this batch. |
| `licensing-deal-architect` | current tree | Current numbered licensing-deal skill; body not directly read in this batch. |
| `enterprise-b2b-deal-hunter` | current tree | Current numbered enterprise deal skill; body not directly read in this batch. |
| `closing-objection-crusher` | current tree | Current numbered objection-handling skill; body not directly read in this batch. |
| `partnership-proposal-writer` | current tree | Current numbered proposal-writing skill; body not directly read in this batch. |
| `multi-stakeholder-deal-navigator` | current tree | Current numbered multi-stakeholder deal skill; body not directly read in this batch. |
| `signal-based-outreach-trigger` | current tree | Current numbered signal-based outreach skill; body not directly read in this batch. |
| `cold-email-sequence-builder` | current tree | Current numbered email-sequence skill; body not directly read in this batch. |
| `referral-machine` | current tree | Current numbered referral workflow; body not directly read in this batch. |
| `champion-builder` | current tree | Current numbered internal-champion workflow; body not directly read in this batch. |
| `competitive-battle-cards` | current tree | Current numbered competitive-sales skill; body not directly read in this batch. |
| `account-expansion-playbook` | current tree | Current numbered expansion workflow; body not directly read in this batch. |
| `cold-call-script-builder` | current tree | Current numbered call-script skill; body not directly read in this batch. |
| `podcast-guest-outreach` | current tree | Current numbered podcast outreach skill; body not directly read in this batch. |
| `linkedin-connection-request` | current tree | Current numbered connection-request skill; body not directly read in this batch. |
| `outreach-message-skill` | current tree | Current numbered outreach-message skill; body not directly read in this batch. |
| `sales-closer` | **direct body at two alias paths** | Same frontmatter/content at `sales-closer/` and `sales.closer/`; counted once as a closing/objection/MAP workflow. |

---

## 5. `staruhub/ClaudeSkills`

### Repository analysis

**Identity and structure.** Public repository on `main`. The current curated inventory contains 13 skills under `skills/`; `lab/` and other supporting/upstream surfaces are not counted as curated installable skills. The repository also carries `scripts/`, `tests/`, `verification/`, site/docs assets, and workflow automation.

**Direct content evidence.** `Geek-skills-deep-research/SKILL.md` is a mature research workflow with brief/full/delta modes, explicit routing exclusions, a small active-context bundle, source registry, citation verification, evaluator gates, observability, degraded mode, and stop conditions. `scripts/validate.py` performs deterministic structural checks across curated skills: required frontmatter, description length, SKILL line caps, platform-hardcoded paths, orphaned support files, and quality warnings. The deep-research routing eval file contains 18 positive/negative/route-away examples, including expected brief/full/delta modes.

**Quality / risk.** This is the strongest explicit eval/verification surface in this batch. It separates structural validation, routing fixtures, and model-oriented evaluation artifacts rather than treating one check as proof of overall quality. These assets were inspected only; no validator or eval was executed here.

### Individual skill reports

| Skill | Evidence basis | Report |
| --- | --- | --- |
| `deck-studio` | current curated inventory | Current curated deck/presentation skill; body not directly read in this batch. |
| `deep-research` | **direct body + validator + eval fixture** | Evidence-rich research workflow with routing boundaries, deterministic citation/source helpers, evaluator gates, observability, and explicit routing eval cases. |
| `product-manager` | current curated inventory | Current curated product-management skill; body not directly read in this batch. |
| `wechat-article-writer` | current curated inventory | Current curated WeChat writing skill; body not directly read in this batch. |
| `pair-programming` | current curated inventory | Current curated pair-programming skill; body not directly read in this batch. |
| `security-audit` | current curated inventory | Current curated security-audit skill; body not directly read in this batch. |
| `solution-architect` | current curated inventory | Current curated solution-architecture skill; body not directly read in this batch. |
| `threejs-performance` | current curated inventory | Current curated Three.js performance skill; body not directly read in this batch. |
| `mineru-pdf-parser` | current curated inventory | Current curated MinerU/PDF skill; body not directly read in this batch. |
| `ai-sales-champion` | current curated inventory | Current curated sales skill; body not directly read in this batch. |
| `keqian-method` | current curated inventory | Current curated methodology skill; body not directly read in this batch. |
| `xuefeng-method` | current curated inventory | Current curated methodology skill; body not directly read in this batch. |
| `c-drive-cleaner` | current curated inventory | Current curated storage-cleanup skill; body not directly read in this batch. |

---

## 6. `Sushegaad/Claude-Skills-Governance-Risk-and-Compliance`

### Repository analysis

**Identity and structure.** Public repository on `main`. The current root exposes 30 framework-oriented packages covering privacy, security, accessibility, AI governance, operational resilience, and related compliance domains. The repository uses packaged `.skill` artifacts plus framework documentation rather than exposing every inner `SKILL.md` as a normal text path.

**Direct equivalent evidence.** `ISO 27001 - Claude Skill/ISO27001-README.md` documents the packaged skill architecture: a core `iso27001/SKILL.md` plus references for the 2022/2013 Annex A sets and cross-version mapping, with on-demand reference loading, output-format selection, gap-analysis, policy/document, control-implementation, and risk-assessment workflows. Because the raw inner `SKILL.md` is packaged inside the `.skill` archive, this is recorded as equivalent packaged-skill-definition evidence, not as a direct raw body read.

**Eval evidence.** `grc-skills-eval-results.html` exists as a repository artifact. The README's detailed benchmark table reports a repository-authored evaluation of 150 tests / 752 assertions, with 705/752 (94%) for skills versus 612/752 (81%) baseline. Elsewhere the repository About/prose says 97%, so the repository contains an internal benchmark-summary inconsistency. This batch does not independently reproduce the benchmark and does not treat the HTML presence as proof of the claimed result.

**Safety / scope.** Export-control packages are recorded only as high-level inventory identities here; no operational guidance from them is reproduced.

### Individual skill reports

| Framework skill | Evidence basis | Report |
| --- | --- | --- |
| `CCPA` | current framework inventory | Privacy/compliance framework package; body not directly unpacked in this batch. |
| `CIS Controls` | current framework inventory | Security-controls framework package; body not directly unpacked in this batch. |
| `CMMC` | current framework inventory | Compliance framework package; body not directly unpacked in this batch. |
| `CSRD` | current framework inventory | Reporting/compliance framework package; body not directly unpacked in this batch. |
| `DORA` | current framework inventory | Digital operational-resilience framework package; body not directly unpacked in this batch. |
| `DPDPA` | current framework inventory | Privacy/compliance framework package; body not directly unpacked in this batch. |
| `EAR` | **high-level inventory only** | Export-control framework package; no operational content reproduced. |
| `EU AI Act` | current framework inventory | AI-governance framework package; body not directly unpacked in this batch. |
| `EU CRA` | current framework inventory | Cyber-resilience framework package; body not directly unpacked in this batch. |
| `FedRamp` | current framework inventory | Government cloud/compliance framework package; body not directly unpacked in this batch. |
| `GDPR` | current framework inventory | Privacy/compliance framework package; body not directly unpacked in this batch. |
| `HIPAA` | current framework inventory | Health-data compliance framework package; body not directly unpacked in this batch. |
| `ISM` | current framework inventory | Security/compliance framework package; body not directly unpacked in this batch. |
| `ISO 27001` | **equivalent packaged definition + references documentation** | Documented skill architecture for ISMS gap analysis, policy/document generation, implementation guidance, risk assessment, and versioned references. |
| `ISO 27701` | current framework inventory | Privacy information management framework package; body not directly unpacked in this batch. |
| `ISO 42001` | current framework inventory | AI management-system framework package; body not directly unpacked in this batch. |
| `ITAR` | **high-level inventory only** | Export-control framework package; no operational content reproduced. |
| `LGPD` | current framework inventory | Privacy/compliance framework package; body not directly unpacked in this batch. |
| `NIS2` | current framework inventory | Cybersecurity compliance framework package; body not directly unpacked in this batch. |
| `NIST 800-53` | current framework inventory | Security/privacy controls framework package; body not directly unpacked in this batch. |
| `NIST AI RMF` | current framework inventory | AI risk-management framework package; body not directly unpacked in this batch. |
| `NIST Cybersecurity framework` | current framework inventory | Cybersecurity framework package; body not directly unpacked in this batch. |
| `NZISM` | current framework inventory | Security/compliance framework package; body not directly unpacked in this batch. |
| `PCI Compliance` | current framework inventory | Payment-card compliance framework package; body not directly unpacked in this batch. |
| `SOC 2` | current framework inventory | Assurance/compliance framework package; body not directly unpacked in this batch. |
| `SWIFT CSP` | current framework inventory | Financial-security compliance framework package; body not directly unpacked in this batch. |
| `Section 508` | current framework inventory | Accessibility compliance framework package; body not directly unpacked in this batch. |
| `TSA Compliance` | current framework inventory | Transportation-security compliance framework package; body not directly unpacked in this batch. |
| `Vietnam PDPL` | current framework inventory | Privacy/compliance framework package; body not directly unpacked in this batch. |
| `WCAG` | current framework inventory | Web accessibility framework package; body not directly unpacked in this batch. |

---

## 7. `honnibal/claude-skills`

### Repository analysis

**Identity and structure.** Public repository on `main`. The repository contains nine `.md.txt` command/skill definitions plus `stub_package.py`. The README deliberately keeps command definitions as `.md.txt` so GitHub renders them as plain text; installation renames them to `.md`. The repository also defaults these commands to explicit invocation rather than automatic model invocation.

**Direct equivalent evidence.** `tighten-types.md.txt` is a complete command definition with frontmatter and a structured workflow: survey scoped Python files, analyze cross-cutting type patterns, edit in grouped passes, and verify using the project's configured type checker. It distinguishes Pydantic versus `TypedDict`, overloads, upstream type tightening, and runtime/public-API safety. `stub_package.py` is real deterministic AST tooling that emits condensed signatures/classes/functions with source locations, decorators, annotations, and optional docstrings.

**Quality / risk.** Keeping untrusted command bodies visibly plain on GitHub is a useful inspection-oriented choice. The repository states that commands are semi-automatically generated and should be reviewed carefully. No explicit eval suite was observed.

### Individual skill reports

| Skill | Evidence basis | Report |
| --- | --- | --- |
| `alignment-chart` | current command inventory | Current command-style skill; body not directly read in this batch. |
| `concept-analysis` | current command inventory | Current command-style skill; body not directly read in this batch. |
| `contract-docstrings` | current command inventory | Current command-style skill; body not directly read in this batch. |
| `hypothesis-tests` | current command inventory | Current command-style skill; body not directly read in this batch. |
| `mutation-testing` | current command inventory | Current command-style skill; body not directly read in this batch. |
| `pre-mortem` | current command inventory | Current command-style skill; body not directly read in this batch. |
| `stub-package` | **helper implementation directly read** | Command identity backed by an AST helper that can generate condensed package stubs; command body itself not directly read in this batch. |
| `tighten-types` | **direct equivalent body** | Python type-tightening workflow with read-before-edit, structured data-model decisions, overload guidance, and type-check verification. |
| `try-except` | current command inventory | Current command-style skill; body not directly read in this batch. |

---

## 8. `iamzhihuix/happy-claude-skills`

### Repository analysis

**Identity and structure.** Public repository on `main`. The current README exposes 11 skills spanning document replication, media processing/generation, web research, browser tooling, credential-oriented integration, and open-source preparation. Skills are organized under `skills/` with support scripts/references where needed.

**Direct content evidence.** `skills/browser/SKILL.md` defines a small Chrome DevTools Protocol toolkit: start Chrome, navigate, evaluate page JavaScript, capture screenshots, and interactively pick DOM elements. `skills/browser/scripts/start.js` kills the existing Chrome process, starts a separate CDP-enabled instance, and optionally uses `rsync` to copy the user's Chrome profile into a cache before launch.

**Quality / risk.** The fresh-profile mode is relatively contained. The optional profile-copy mode intentionally carries cookies/logins into an automation-controlled browser and therefore materially expands the skill's authority; it should be treated as a high-trust mode rather than a routine default. No explicit eval suite was observed in this batch.

### Individual skill reports

| Skill | Evidence basis | Report |
| --- | --- | --- |
| `docx-format-replicator` | current README/inventory | Current document-format replication skill; body not directly read in this batch. |
| `video-processor` | current README/inventory | Current video-processing skill; body not directly read in this batch. |
| `wechat-article-writer` | current README/inventory | Current WeChat writing skill; body not directly read in this batch. |
| `trends-bulletin` | current README/inventory | Current trend/bulletin skill; body not directly read in this batch. |
| `browser` | **direct body + script** | CDP browser workflow with deterministic launch/navigation helpers; profile-copy mode can inherit authenticated browser authority. |
| `1password` | current README/inventory | Current 1Password-oriented skill; body not directly read in this batch. |
| `happy-image-gen` | current README/inventory | Current image-generation skill; body not directly read in this batch. |
| `happy-video-gen` | current README/inventory | Current video-generation skill; body not directly read in this batch. |
| `happy-audio-gen` | current README/inventory | Current audio-generation skill; body not directly read in this batch. |
| `happy-dreamina` | current README/inventory | Current Dreamina-oriented generation skill; body not directly read in this batch. |
| `open-source-prep` | current README/inventory | Current open-source preparation skill; body not directly read in this batch. |

---

## 9. `jianshuo/claude-skills`

### Repository analysis

**Identity and structure.** Public repository on `main`. The current root contains 35 skill directories, substantially more than the README/About text that still says 13. The tree is therefore the authority for current inventory in this report. Naming is predominantly `wjs-` plus gerund-oriented action names, reflecting a personal workflow catalog.

**Direct content evidence.** `wjs-evaling-voicedrop-prompts/SKILL.md` is an explicit prompt-evaluation protocol rather than a generic reviewer. It compares champion and candidate prompts on golden fixtures, randomizes A/B order for blind pairwise judging, aggregates normalized verdicts, requires a promotion threshold and no deterministic fallback, and reserves final style approval for the user. `references/judge-rubric.md` defines the single judging schema and dimensions including fidelity/no fabrication. The executable harness and fixture data live in the separate/local `jianshuo.dev/agent/eval/` workspace, so this repository contains the protocol/rubric, not the whole runnable evaluation system.

**Quality / risk.** The evaluation skill shows strong separation of candidate generation, blinded judging, aggregation, and human release approval. The major maintenance issue is documentation drift: current tree 35 vs README/About 13. No external harness was run in this batch.

### Individual skill reports

| Skill | Evidence basis | Report |
| --- | --- | --- |
| `wangjianshuo-perspective` | current tree | Current perspective/persona workflow; body not directly read in this batch. |
| `wjs-auditing-project` | current tree | Current project-audit workflow; body not directly read in this batch. |
| `wjs-burning-subtitles` | current tree | Current subtitle-burn workflow; body not directly read in this batch. |
| `wjs-cleaning-spam` | current tree | Current spam-cleaning workflow; body not directly read in this batch. |
| `wjs-converting-text-to-video` | current tree | Current text-to-video workflow; body not directly read in this batch. |
| `wjs-converting-wp-to-hugo` | current tree | Current WordPress-to-Hugo workflow; body not directly read in this batch. |
| `wjs-distilling-style` | current tree | Current style-distillation workflow; body not directly read in this batch. |
| `wjs-dubbing-video` | current tree | Current video-dubbing workflow; body not directly read in this batch. |
| `wjs-eating-and-growing` | current tree | Current personal workflow skill; body not directly read in this batch. |
| `wjs-editing-multicam` | current tree | Current multicam editing workflow; body not directly read in this batch. |
| `wjs-evaling-voicedrop-prompts` | **direct body + rubric** | Champion-vs-candidate prompt evaluation protocol with blinded randomized pairwise judging, aggregation threshold, and human promotion gate. |
| `wjs-localizing-video` | current tree | Current video-localization workflow; body not directly read in this batch. |
| `wjs-looping-feedback` | current tree | Current feedback-loop workflow; body not directly read in this batch. |
| `wjs-mining-articles` | current tree | Current article-mining workflow; body not directly read in this batch. |
| `wjs-mining-voicedrop` | current tree | Current VoiceDrop mining workflow; body not directly read in this batch. |
| `wjs-overlaying-video` | current tree | Current video-overlay workflow; body not directly read in this batch. |
| `wjs-polishing-x-engagement` | current tree | Current X engagement-polishing workflow; body not directly read in this batch. |
| `wjs-promoting-skills` | current tree | Current skill-promotion workflow; body not directly read in this batch. |
| `wjs-publishing-appstore` | current tree | Current App Store publishing workflow; body not directly read in this batch. |
| `wjs-publishing-hugo` | current tree | Current Hugo publishing workflow; body not directly read in this batch. |
| `wjs-publishing-testflight` | current tree | Current TestFlight publishing workflow; body not directly read in this batch. |
| `wjs-publishing-wechat` | current tree | Current WeChat publishing workflow; body not directly read in this batch. |
| `wjs-reframing-video` | current tree | Current video-reframing workflow; body not directly read in this batch. |
| `wjs-segmenting-video` | current tree | Current video-segmentation workflow; body not directly read in this batch. |
| `wjs-syncing-multicam` | current tree | Current multicam-sync workflow; body not directly read in this batch. |
| `wjs-syndicating-articles` | current tree | Current article-syndication workflow; body not directly read in this batch. |
| `wjs-teaching-english` | current tree | Current English-teaching workflow; body not directly read in this batch. |
| `wjs-transcribing-audio` | current tree | Current audio-transcription workflow; body not directly read in this batch. |
| `wjs-translating-subtitles` | current tree | Current subtitle-translation workflow; body not directly read in this batch. |
| `wjs-tweeting-from-articles` | current tree | Current article-to-X workflow; body not directly read in this batch. |
| `wjs-uploading-video` | current tree | Current video-upload workflow; body not directly read in this batch. |
| `wjs-voicedrop-choosing-cover` | current tree | Current VoiceDrop cover-selection workflow; body not directly read in this batch. |
| `wjs-voicedrop` | current tree | Current VoiceDrop workflow; body not directly read in this batch. |
| `wjs-x-improving-content` | current tree | Current X content-improvement workflow; body not directly read in this batch. |
| `wjs-x-increasing-follower` | current tree | Current X audience-growth workflow; body not directly read in this batch. |

---

## 10. `rampstackco/claude-skills`

### Repository analysis

**Identity and structure.** Public, non-archived repository on `main`. The current README/catalog states 103 stack-agnostic skills across 16 categories, supported by hundreds of reference files. Root governance surfaces include `SKILL_AUTHORING.md`, `SECURITY.md`, CI/scripts, `SKILLS.lock`, and workflow manifests.

**Direct content evidence.** `skills/creative-direction/SKILL.md` shows the repository's standard shape: frontmatter metadata, explicit when-to-use and when-not-to-use sections, required inputs, a domain framework, ordered workflow, failure patterns, output contract, and references. `references/brief-template.md` gives a concrete project artifact schema including directional axes, synthesis, inspiration references, rejection list, and open questions. `SKILLS.lock` is a machine-readable checksum manifest mapping each skill/support file to hashes; the root README also documents lint/schema checks in CI.

**Quality / risk.** The strongest pattern is collection-scale governance: uniform packaging, support-file limits, checksum inventory, security guidance, and automated lint/schema checks. These are strong structural signals but not proof of behavior quality; no CI, lint, or model evaluation was executed here.

### Individual skill reports

Each row below is a current catalog identity. `creative-direction` is the directly read body; the remaining rows are inventory-level reports unless otherwise stated.

| Skill | Category | Evidence basis | Report |
| --- | --- | --- | --- |
| `brand-discovery` | Strategy and discovery | current catalog | Current catalog skill; body not directly read in this batch. |
| `creative-brief` | Strategy and discovery | current catalog | Current catalog skill; body not directly read in this batch. |
| `creative-direction` | Strategy and discovery | **direct body + reference** | Four-axis aesthetic-direction workflow with explicit routing exclusions, tension checks, failure patterns, and a concrete reusable `BRIEF.md` contract. |
| `information-architecture` | Strategy and discovery | current catalog | Current catalog skill; body not directly read in this batch. |
| `content-strategy` | Strategy and discovery | current catalog | Current catalog skill; body not directly read in this batch. |
| `brand-ideation` | Brand | current catalog | Current catalog skill; body not directly read in this batch. |
| `brand-identity` | Brand | current catalog | Current catalog skill; body not directly read in this batch. |
| `brand-style-guide` | Brand | current catalog | Current catalog skill; body not directly read in this batch. |
| `brand-voice` | Brand | current catalog | Current catalog skill; body not directly read in this batch. |
| `brand-archetype-system` | Brand | current catalog | Current catalog skill; body not directly read in this batch. |
| `logo-design` | Brand | current catalog | Current catalog skill; body not directly read in this batch. |
| `creative-brief-selector` | Brand | current catalog | Current catalog skill; body not directly read in this batch. |
| `design-system` | Design | current catalog | Current catalog skill; body not directly read in this batch. |
| `design-standards` | Design | current catalog | Current catalog skill; body not directly read in this batch. |
| `art-direction` | Design | current catalog | Current catalog skill; body not directly read in this batch. |
| `vertical-site-conventions` | Design | current catalog | Current catalog skill; body not directly read in this batch. |
| `pillar-content-architecture` | Content | current catalog | Current catalog skill; body not directly read in this batch. |
| `content-brief-authoring` | Content | current catalog | Current catalog skill; body not directly read in this batch. |
| `content-and-copy` | Content | current catalog | Current catalog skill; body not directly read in this batch. |
| `landing-page-copy` | Content | current catalog | Current catalog skill; body not directly read in this batch. |
| `email-sequences` | Content | current catalog | Current catalog skill; body not directly read in this batch. |
| `programmatic-seo` | Content | current catalog | Current catalog skill; body not directly read in this batch. |
| `editorial-qa` | Content | current catalog | Current catalog skill; body not directly read in this batch. |
| `ai-content-collaboration` | Content | current catalog | Current catalog skill; body not directly read in this batch. |
| `long-form-content-frameworks` | Content | current catalog | Current catalog skill; body not directly read in this batch. |
| `content-refresh-system` | Content | current catalog | Current catalog skill; body not directly read in this batch. |
| `content-repurposing` | Content | current catalog | Current catalog skill; body not directly read in this batch. |
| `content-distribution` | Content | current catalog | Current catalog skill; body not directly read in this batch. |
| `evidence-based-reviews` | Content | current catalog | Current catalog skill; body not directly read in this batch. |
| `seo-onpage` | SEO foundation | current catalog | Current catalog skill; body not directly read in this batch. |
| `seo-technical` | SEO foundation | current catalog | Current catalog skill; body not directly read in this batch. |
| `seo-keyword` | SEO foundation | current catalog | Current catalog skill; body not directly read in this batch. |
| `seo-competitor` | SEO foundation | current catalog | Current catalog skill; body not directly read in this batch. |
| `seo-offpage` | SEO foundation | current catalog | Current catalog skill; body not directly read in this batch. |
| `seo-content-audit` | SEO foundation | current catalog | Current catalog skill; body not directly read in this batch. |
| `seo-aeo-geo` | SEO foundation | current catalog | Current catalog skill; body not directly read in this batch. |
| `seo-audit-orchestration` | SEO audit suite | current catalog | Current catalog skill; body not directly read in this batch. |
| `seo-backlink-audit` | SEO audit suite | current catalog | Current catalog skill; body not directly read in this batch. |
| `seo-keyword-gap-audit` | SEO audit suite | current catalog | Current catalog skill; body not directly read in this batch. |
| `seo-content-gap-audit` | SEO audit suite | current catalog | Current catalog skill; body not directly read in this batch. |
| `seo-traffic-diagnosis` | SEO audit suite | current catalog | Current catalog skill; body not directly read in this batch. |
| `seo-site-health-audit` | SEO audit suite | current catalog | Current catalog skill; body not directly read in this batch. |
| `seo-rank-tracking` | SEO audit suite | current catalog | Current catalog skill; body not directly read in this batch. |
| `pm-spec-writing` | Product | current catalog | Current catalog skill; body not directly read in this batch. |
| `roadmap-planning` | Product | current catalog | Current catalog skill; body not directly read in this batch. |
| `integration-orchestrator` | Product | current catalog | Current catalog skill; body not directly read in this batch. |
| `experiment-design` | Product | current catalog | Current catalog skill; body not directly read in this batch. |
| `feature-flagging` | Product | current catalog | Current catalog skill; body not directly read in this batch. |
| `experimentation-analytics` | Product | current catalog | Current catalog skill; body not directly read in this batch. |
| `experimentation-platform-orchestrator` | Product | current catalog | Current catalog skill; body not directly read in this batch. |
| `product-analytics-setup` | Product | current catalog | Current catalog skill; body not directly read in this batch. |
| `data-warehouse-experimentation` | Product | current catalog | Current catalog skill; body not directly read in this batch. |
| `feature-launch-playbook` | Product | current catalog | Current catalog skill; body not directly read in this batch. |
| `jtbd-framing` | Product | current catalog | Current catalog skill; body not directly read in this batch. |
| `okr-design` | Product | current catalog | Current catalog skill; body not directly read in this batch. |
| `beta-program-management` | Product | current catalog | Current catalog skill; body not directly read in this batch. |
| `code-review-web` | Development | current catalog | Current catalog skill; body not directly read in this batch. |
| `frontend-component-build` | Development | current catalog | Current catalog skill; body not directly read in this batch. |
| `accessibility-audit` | Development | current catalog | Current catalog skill; body not directly read in this batch. |
| `performance-optimization` | Development | current catalog | Current catalog skill; body not directly read in this batch. |
| `qa-testing` | Quality assurance | current catalog | Current catalog skill; body not directly read in this batch. |
| `launch-runbook` | Operations | current catalog | Current catalog skill; body not directly read in this batch. |
| `incident-response` | Operations | current catalog | Current catalog skill; body not directly read in this batch. |
| `after-action-report` | Operations | current catalog | Current catalog skill; body not directly read in this batch. |
| `domain-strategy` | Operations | current catalog | Current catalog skill; body not directly read in this batch. |
| `monitoring-and-alerting` | Operations | current catalog | Current catalog skill; body not directly read in this batch. |
| `backup-and-disaster-recovery` | Operations | current catalog | Current catalog skill; body not directly read in this batch. |
| `security-baseline` | Operations | current catalog | Current catalog skill; body not directly read in this batch. |
| `email-deliverability` | Operations | current catalog | Current catalog skill; body not directly read in this batch. |
| `media-asset-management` | Operations | current catalog | Current catalog skill; body not directly read in this batch. |
| `analytics-strategy` | Growth | current catalog | Current catalog skill; body not directly read in this batch. |
| `cro-optimization` | Growth | current catalog | Current catalog skill; body not directly read in this batch. |
| `lead-magnet-design` | Growth tooling | current catalog | Current catalog skill; body not directly read in this batch. |
| `calculator-design` | Growth tooling | current catalog | Current catalog skill; body not directly read in this batch. |
| `quiz-and-assessment-design` | Growth tooling | current catalog | Current catalog skill; body not directly read in this batch. |
| `multi-step-form-design` | Growth tooling | current catalog | Current catalog skill; body not directly read in this batch. |
| `chatbot-flow-design` | Growth tooling | current catalog | Current catalog skill; body not directly read in this batch. |
| `funnel-flow-architecture` | Growth tooling | current catalog | Current catalog skill; body not directly read in this batch. |
| `onboarding-wizard-design` | Growth tooling | current catalog | Current catalog skill; body not directly read in this batch. |
| `interactive-product-tour` | Growth tooling | current catalog | Current catalog skill; body not directly read in this batch. |
| `upgrade-flow-design` | Growth tooling | current catalog | Current catalog skill; body not directly read in this batch. |
| `scheduler-and-booking-design` | Growth tooling | current catalog | Current catalog skill; body not directly read in this batch. |
| `comparison-tool-design` | Growth tooling | current catalog | Current catalog skill; body not directly read in this batch. |
| `product-configurator-design` | Growth tooling | current catalog | Current catalog skill; body not directly read in this batch. |
| `paid-media-strategy` | Marketing | current catalog | Current catalog skill; body not directly read in this batch. |
| `ads-creative-development` | Marketing | current catalog | Current catalog skill; body not directly read in this batch. |
| `ads-performance-analytics` | Marketing | current catalog | Current catalog skill; body not directly read in this batch. |
| `ux-research` | Research | current catalog | Current catalog skill; body not directly read in this batch. |
| `usability-testing` | Research | current catalog | Current catalog skill; body not directly read in this batch. |
| `journey-mapping` | Research | current catalog | Current catalog skill; body not directly read in this batch. |
| `discovery-research-synthesis` | Research | current catalog | Current catalog skill; body not directly read in this batch. |
| `user-feedback-aggregation` | Research | current catalog | Current catalog skill; body not directly read in this batch. |
| `competitor-experience-audit` | Research | current catalog | Current catalog skill; body not directly read in this batch. |
| `form-strategy` | Cross-cutting workflows | current catalog | Current catalog skill; body not directly read in this batch. |
| `content-migration` | Cross-cutting workflows | current catalog | Current catalog skill; body not directly read in this batch. |
| `internationalization` | Cross-cutting workflows | current catalog | Current catalog skill; body not directly read in this batch. |
| `dependency-management` | Cross-cutting workflows | current catalog | Current catalog skill; body not directly read in this batch. |
| `cost-optimization` | Cross-cutting workflows | current catalog | Current catalog skill; body not directly read in this batch. |
| `stakeholder-communication` | Process and team | current catalog | Current catalog skill; body not directly read in this batch. |
| `documentation-strategy` | Process and team | current catalog | Current catalog skill; body not directly read in this batch. |
| `vendor-evaluation` | Process and team | current catalog | Current catalog skill; body not directly read in this batch. |
| `team-onboarding-playbook` | Process and team | current catalog | Current catalog skill; body not directly read in this batch. |
| `skill-creation-walkthrough` | Process and team | current catalog | Current catalog skill; body not directly read in this batch. |

---

## Cross-repository findings

1. **Inventory drift is common enough to require tree-level verification.** RTFM says 15 skills but current tree has 14 and no `msp-leadgen`; Simon documents 18 while the current tree yields 29 unique identities after alias deduplication; Jianshuo documents 13 while current tree has 35. These repositories would be miscounted if completion relied on README metadata alone.
2. **Strong deterministic support code is a recurring quality pattern.** Posit's token/line counter, RTFM's pricing calculator, Honnibal's AST stub generator, Happy's browser launch helpers, and Staruhub's validator move repeatable mechanics out of prose.
3. **Staruhub has the strongest explicit evaluation surface in this batch.** It combines structural validation with routing fixtures and documented evaluation/verification artifacts. This is still only static evidence here because the checks were not executed.
4. **Rampstack emphasizes collection governance at scale.** Its 103-skill catalog is paired with uniform authoring contracts, references, lint/schema checks, security documentation, and a concrete `SKILLS.lock` checksum manifest.
5. **Privilege expansion should be visible in skill reviews.** Happy's browser profile-copy mode intentionally transfers cookies/logins into an automation-controlled Chrome profile; fresh-profile use is a materially narrower authority boundary.
6. **Repository-authored benchmark claims must remain source-qualified.** The GRC repository's detailed evaluation table says 94% (705/752) while another summary says 97%. This batch records the inconsistency and does not treat either as independently reproduced evidence.

## Validation and completion decision

- Ten repositories were selected from the existing indexed, deep-analysis-eligible queue and were not present in the prior completed-repository manifest.
- All ten GitHub identities/default branches were resolved through GitHub repository metadata.
- Displayed GitHub star counts were observed for all ten repositories.
- Actual repository content was read for every completion. Each repository has at least one directly read `SKILL.md` or equivalent packaged/command definition, and supporting scripts/references/evals were inspected where available.
- Current repository-maintained inventories were used for complete individual-skill enumeration; large collections explicitly distinguish inventory-level rows from direct-body rows.
- Current individual report counts reconcile: `23 + 7 + 14 + 29 + 13 + 30 + 9 + 11 + 35 + 103 = 274`.
- No third-party runtime command, test suite, browser automation, installer, external service call, compliance workflow, or pricing calculation was executed.
- Result: **10 repository completions / 274 individual skill reports / structure-reviewed / runtime not executed**.
