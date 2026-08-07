# Agent Skills Deep Analysis — Batch 014

- Observed at: `2026-08-07T13:52:12+08:00`
- Queue source: `sources/catalog/github-agent-skills-index-latest.json`
- Repositories completed: **10**
- Individual skill reports: **222**
- Repository status: `structure-reviewed`
- Runtime validation: `not_executed`

## Completion rule

A repository is counted in this batch only after its GitHub identity and current displayed star count were checked and actual repository content was read. Repository-level review covered README or equivalent documentation, current `SKILL.md` definitions or a repository-maintained skill inventory, and available scripts, references, validators, benchmarks, or eval assets when present. Metadata-only candidates were not counted.

Large collections were handled with an explicit evidence boundary: complete current repository-maintained inventories were used to enumerate individual skill identities, while representative `SKILL.md` bodies and supporting implementation/validation files were read directly. The report does not claim that every large-collection skill body was independently line-by-line reviewed.

No third-party scripts, installers, tests, cloud APIs, browser workflows, uploads, or external side-effecting commands were executed during this batch.

## Repository summary

| Repository | Stars observed | Skill reports | Evidence depth | Result |
|---|---:|---:|---|---|
| `firstrui/codex-reverse-skills` | 38 | 2 | README + both skill contracts + routing reference | structure-reviewed |
| `Infinite-Labs-AI/infinite-skills` | 44 | 26 | README inventory + representative skill contracts + validator source | structure-reviewed |
| `lixiaolin94/skills` | 730 | 1 | README/current package + skill contract + operating contract + helper script | structure-reviewed |
| `vipulgupta2048/codex-skills` | 35 | 1 | current skill contract + reference playbook | structure-reviewed |
| `provencher/codex-skills` | 158 | 1 | README + complete skill contract | structure-reviewed |
| `sherman/codex-skills` | 40 | 2 | README + both skill contracts + concurrency verification reference | structure-reviewed |
| `wlzh/skills` | 596 | 15 | README + complete filename inventory + representative skill contracts | structure-reviewed |
| `SynaLinks/synalinks-skills` | 896 | 1 | README + skill contract + runnable example source + API reference | structure-reviewed |
| `TheGoat395/Codex-Skills` | 116 | 70 | generated inventory + manifest + representative contracts + quality/benchmark/validator files | structure-reviewed |
| `google/skills` | 15.8k | 103 | official README inventory + current SKILL search + representative contracts + eval helper source | structure-reviewed |

Total: **10 repositories / 222 repository-scoped individual skill reports**.

## Repository analysis

### 1. `firstrui/codex-reverse-skills`

**Identity and inventory.** Current repository structure exposes two skills: `web-js-reverse-master-flow` and `1997-pro-web-reverse-casebook`.

**Structure.** The primary skill is an evidence-first staged workflow; the casebook is a router/reference layer that maps observed problem classes back into the main workflow rather than acting as an independent execution controller. The reviewed routing reference separates runtime, obfuscation, WebAssembly, protocol, and mobile investigation lanes.

**Quality signals.** The main contract emphasizes evidence gates and separates direct evidence from inference before moving between phases. The casebook explicitly keeps final stage control with the primary workflow.

**Risk / limitation.** This is a dual-use reverse-engineering surface. Some references cover anti-bot, CAPTCHA, protocol, and mobile reverse-engineering scenarios. That makes authorization and scope boundaries material even though this batch only inspected content and performed no target operations.

**Evidence read.** `README.md`; `skills/web-js-reverse-master-flow/SKILL.md`; `skills/1997-pro-web-reverse-casebook/SKILL.md`; `skills/1997-pro-web-reverse-casebook/references/routing-matrix.md`.

### 2. `Infinite-Labs-AI/infinite-skills`

**Identity and inventory.** Current README defines one `goal` skill plus a curated 25-skill marketing set, yielding **26** current skill identities.

**Structure.** Skills use a flat `skills/<skill>/SKILL.md` layout. The `goal` skill focuses on converting long-horizon work into observable exit criteria. Marketing skills are narrowly scoped by task, such as positioning, customer research, offer design, launch planning, CRO, outreach, analytics, and retention.

**Validation.** `scripts/validate_marketing_skills.py` enforces the exact 25-skill marketing set, required frontmatter, trigger-style descriptions, placeholder removal, denied source-style phrases/headings, and textual-overlap checks.

**Finding.** The validator's source-overlap checks depend on a hard-coded developer-local `SOURCE_ROOT` under `/Users/chaosalchemist/...`. `ALLOW_MISSING_SOURCE_CORPUS=1` allows validation without that corpus, but then the source-comparison portion is skipped. Structural validation is therefore portable; full provenance/overlap validation is not fully self-contained in the repository.

**Evidence read.** `README.md`; `skills/goal/SKILL.md`; `skills/marketing-brief/SKILL.md`; `scripts/validate_marketing_skills.py`.

### 3. `lixiaolin94/skills`

**Identity and inventory.** Current repository exposes one formal skill: `web-shader-extractor`.

**Structure.** `SKILL.md` acts as an index/router and delegates detailed operating rules to focused references. The contract uses explicit `SOURCE`, `PARTIAL`, and `GUESS` labels, requires target attribution before deeper analysis, and separates baseline replay from later projectization.

**Safety / evidence boundary.** The operating contract explicitly limits work to public or authorized content and says not to persist cookies, authorization headers, tokens, or secrets. The reviewed bundle scanner labels its output as hypotheses rather than target-bound conclusions.

**Evidence read.** `web-shader-extractor/SKILL.md`; `web-shader-extractor/references/operating-contract.md`; `web-shader-extractor/scripts/scan-bundle.sh`.

### 4. `vipulgupta2048/codex-skills`

**Identity and inventory.** Current repository contains one formal skill, `frontend-design`.

**Structure.** The skill separates the main workflow from reusable references and starter assets. The reviewed aesthetic playbook provides selectable visual directions rather than one fixed design style, while the main skill covers intent, tokens, layout, motion, responsive behavior, accessibility, and performance checks.

**Evidence gap.** No repository-level eval or validation harness was observed in the reviewed surface; quality guidance is primarily procedural/reference driven.

**Evidence read.** `skills/frontend-design/SKILL.md`; `skills/frontend-design/references/aesthetic-playbook.md`.

### 5. `provencher/codex-skills`

**Identity and inventory.** Current repository contains a single `orchestrate` skill.

**Structure.** The contract is intentionally small: it delegates substantial work to narrow agents, keeps ownership non-overlapping, prevents leaf delegation, and preserves user approvals in the parent thread.

**Evidence gap.** No scripts, references, or eval harnesses were observed in the reviewed surface. The value is the compact coordination contract rather than a packaged validation system.

**Evidence read.** `README.md`; `orchestrate/SKILL.md`.

### 6. `sherman/codex-skills`

**Identity and inventory.** Two current skills: `effective-java-core` and `effective-java-concurrency`.

**Structure.** The core skill turns Effective Java guidance into an operational checklist with selectively loadable references. The concurrency skill is a separate workflow for concrete concurrent code paths and focuses on invariants, ownership, lifecycle, cancellation, saturation, and workload-specific execution choices.

**Verification discipline.** The reviewed concurrency reference explicitly requires tracing real concurrent paths, deterministic synchronization-based tests instead of timing sleeps, bounded test timeouts, stress/JMM tooling where appropriate, overload analysis, and honest reporting of untested claims.

**Evidence read.** `README.md`; both current `SKILL.md` files; `skills/effective-java-concurrency/references/review-and-testing.md`.

### 7. `wlzh/skills`

**Identity and inventory.** A current filename-level inventory identified **15** formal `SKILL.md` packages. The repository is heterogeneous: media conversion, publishing/fetching, invoice processing, content automation, VPS hardening, and other utilities coexist in one collection.

**Structure.** Representative skills combine narrative contracts with operational scripts/configuration. `x-fetcher` documents a preference layer and third-party API dependency. `youtube-publisher` has OAuth/upload behavior and a dry-run option. `voice-changer` packages RVC-oriented processing guidance.

**High-impact finding.** `wlzh-invoice-scanner` instructs preprocessing that can delete `.xml`/`.ofd` files, delete original ZIP files after extraction, and move extracted files into another directory. Those are destructive filesystem side effects before the final report stage. A safer reusable contract would require an explicit non-destructive default or a user-confirmed backup/destructive gate.

**External-side-effect finding.** `youtube-publisher` is intentionally side-effecting: authentication and upload operations target YouTube. The skill documents a dry-run path, but actual publishing must be treated as an explicit external action boundary.

**Evidence read.** `README.md`; current `SKILL.md` filename inventory; representative `voice-changer/SKILL.md`, `x-fetcher-skill/SKILL.md`, `youtube-publisher/SKILL.md`, and `wlzh-invoice-scanner/SKILL.md`.

### 8. `SynaLinks/synalinks-skills`

**Identity and inventory.** One repository-level skill: `synalinks`.

**Structure.** The skill is a broad framework guide backed by focused `references/`, runnable `scripts/`, and captured run-log paths. It covers core data/model abstractions, program composition, control flow, agent/tool patterns, RAG, training, rewards, optimization, and providers while routing deeper topics to separate reference documents.

**Evidence packaging.** The reviewed `simple_qa.py` is an actual runnable example, and the API reference mirrors the main concepts with concrete signatures. The repository's use of scripts plus captured logs is stronger evidence packaging than prose-only skills, though this batch did not execute the scripts or verify the recorded logs against a fresh runtime.

**Evidence read.** `README.md`; `skills/synalinks/SKILL.md`; `skills/synalinks/scripts/simple_qa.py`; `skills/synalinks/references/api-reference.md`.

### 9. `TheGoat395/Codex-Skills`

**Identity and inventory.** `SKILL_INVENTORY.md` and `manifest.json` both report **70** current skills generated from `skills/*/SKILL.md`.

**Structure.** The collection is strongly focused on frontend design, React/Next.js implementation, motion, accessibility, responsive behavior, performance, browser QA, content quality, and delivery gates. Representative contracts split pre-build gating (`premium-web-build-gate`) from post-build audit (`frontend-quality-auditor`) and specialist follow-ups.

**Governance / validation.** `SKILL_QUALITY_STANDARD.md` defines trigger clarity, operational behavior, verification, dependency, privacy, and destructive-action criteria. `scripts/validate_skills.py` checks folder/frontmatter identity, minimum description length, and curated-collection references. `BENCHMARKS.md` explicitly distinguishes estimated workflow impact from measured benchmark evidence.

**Evidence boundary.** The repository says measured benchmark artifacts exist, but this batch did not execute or independently reproduce those benchmarks. They are therefore recorded as repository-provided evidence, not revalidated performance claims.

**Evidence read.** `SKILL_INVENTORY.md`; `manifest.json`; representative `frontend-quality-auditor/SKILL.md` and `premium-web-build-gate/SKILL.md`; `SKILL_QUALITY_STANDARD.md`; `BENCHMARKS.md`; `scripts/validate_skills.py`.

### 10. `google/skills`

**Identity and inventory.** The official Google repository's current README lists **103 local skills** across getting started, multi-product solutions, AI/ML, infrastructure, databases/analytics, developer tools, management, Well-Architected, security, hosting, advertising, and analytics. Six separate repositories listed under “Additional Google skills” were excluded from this repository's local count.

**Structure.** The repository is a broad official skill catalog under active development. Current local `SKILL.md` search confirms concrete package paths under areas such as `skills/cloud/` and `skills/ads/`.

**Representative contracts.** `google-cloud-recipe-auth` distinguishes authentication from authorization and recommends ADC, impersonation, attached service identities, short-lived credentials, and workload identity federation rather than static service-account keys. `agent-platform-eval-flywheel` defines data preparation → inference → grading → failure analysis → iteration, with separate confirmation tiers for read-only local inspection versus cost-incurring remote evaluation.

**Implementation / eval support.** The reviewed `inspect_results.py` helper reads persisted evaluation result JSON, renders summary/per-case metrics, returns non-zero for malformed/empty result data, and optionally renders an HTML report when the SDK is available.

**Evidence boundary.** The repository is actively changing; the 103 count is the current README-listed local inventory observed in this batch, not a permanent repository invariant. No Google Cloud evaluation, deployment, or paid operation was executed.

**Evidence read.** Current official `README.md`; current `SKILL.md` repository search; `skills/cloud/google-cloud-recipe-auth/SKILL.md`; `skills/cloud/agent-platform-eval-flywheel/SKILL.md`; its `scripts/inspect_results.py`.

## Individual report artifacts

- `research/agent-skills/batches/2026-08-07-batch-014-skill-reports-01.md` — 119 reports for the first nine repositories.
- `research/agent-skills/batches/2026-08-07-batch-014-skill-reports-02.md` — 103 reports for `google/skills`.

## Batch findings

1. **Reproducibility boundary:** `Infinite-Labs-AI/infinite-skills` has a substantive validator, but full source-overlap validation depends on a hard-coded external local corpus path.
2. **Destructive-action boundary:** `wlzh/skills` includes an invoice workflow that deletes and moves source files during preprocessing; this deserves a stronger non-destructive default or explicit confirmation gate.
3. **External side effects:** publishing/authentication skills in `wlzh/skills` and cost-incurring evaluation paths in `google/skills` have materially different side-effect profiles from read-only advisory skills; their contracts should be judged with those boundaries intact.
4. **Evidence maturity:** `TheGoat395/Codex-Skills`, `SynaLinks/synalinks-skills`, and `google/skills` expose stronger supporting evidence surfaces than prose-only packs through validators, scripts, reference material, logs/benchmarks, or result-inspection utilities. This batch inspected those surfaces but did not execute them.
5. **Dual-use boundary:** the two reverse-engineering repositories in this batch are technically structured and evidence-oriented, but authorization and target scope remain essential because the workflows can apply to protective mechanisms as well as benign debugging/reproduction.

## Verification status

- Repository identities: verified through live GitHub repository metadata.
- Displayed stars: verified from live GitHub repository pages during this batch.
- Actual repository content: read for all 10 completed repositories.
- Individual skill identities: direct skill bodies for small repositories; current maintained inventory plus representative direct bodies for large collections.
- Runtime validation: **not executed**.
- Third-party side effects: **none executed**.
