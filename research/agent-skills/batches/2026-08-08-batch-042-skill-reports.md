# Agent Skills Deep Analysis — Batch 042 Skill Reports

- Batch: `2026-08-08-batch-042`
- Direct `SKILL.md` reads: **49**
- Unique skill bodies directly reviewed: **45**
- New batch-local individual reports: **43**
- Exact prior-content mappings: **2 content lineages** covering 6 repository identities
- Runtime/build/test/eval execution: **not executed**

These reports summarize behavior, structure, evidence, and risks without reproducing source text. Cybersecurity entries intentionally omit operational attack instructions and retain only architecture/safety/verification observations.

## `daonhan/Agentskills` — 10 individual reports

### company-values

- Purpose: turn company-culture intent into a small set of operational values with hiring/work examples.
- Structure: text-only advisory Skill with a fixed question sequence and output shape.
- Useful pattern: converts an abstract culture topic into explicit decision prompts and anti-patterns.
- Risk/evidence: strongly anchored to one business philosophy and example company; no scripts, references, or evals; outcome quality is unverified.
- Status: `source-read / new batch-local report / runtime not_executed`.

### find-community

- Purpose: identify communities a founder already belongs to and rank them as possible business starting points.
- Structure: guided questions → evaluation criteria → narrowed candidate set.
- Useful pattern: requires connection, pain, reachability, and long-term interest rather than starting from a product idea.
- Risk/evidence: community-size and willingness-to-pay guidance is heuristic, with no local research adapter or eval.
- Status: `source-read / new batch-local report / runtime not_executed`.

### first-customers

- Purpose: plan early customer acquisition through progressively less familiar audiences.
- Structure: staged sales guidance, pricing notes, metrics, and a concrete weekly outreach output.
- Useful pattern: keeps early sales tied to feedback rather than treating marketing as a substitute for customer discovery.
- Risk/evidence: several numerical/general business claims are presented as broadly applicable without repository-local evidence; no evals.
- Status: `source-read / new batch-local report / runtime not_executed`.

### grow-sustainably

- Purpose: evaluate hiring, spending, funding, and scaling decisions through profitability and reversibility.
- Structure: cost model → growth/funding heuristics → burnout/cofounder considerations → decision output.
- Useful pattern: explicitly adds reversibility and cash impact to strategic decisions.
- Risk/evidence: some policy defaults are ideological rather than context-sensitive; historical examples can stale; no behavioral validation.
- Status: `source-read / new batch-local report / runtime not_executed`.

### marketing-plan

- Purpose: create a content-led marketing plan after initial customer validation.
- Structure: funnel, content tiers, channel guidance, email strategy, schedule, and paid-spend gate.
- Useful pattern: separates sales learning from later scalable distribution.
- Risk/evidence: platform and funnel assumptions are generic; no current-data integration or eval harness verifies recommendation quality.
- Status: `source-read / new batch-local report / runtime not_executed`.

### minimalist-review

- Purpose: provide a consistent “minimalist entrepreneur” review of a business decision.
- Structure: principle checklist + decision table + recommendation/experiment output.
- Useful pattern: compact reusable review rubric with a final validation action.
- Risk/evidence: the rubric intentionally embeds one philosophy, so it should not be mistaken for neutral business analysis; no alternative-framework comparison or eval.
- Status: `source-read / new batch-local report / runtime not_executed`.

### mvp

- Purpose: reduce product scope and move from manual delivery to systematized delivery and only then automation.
- Structure: staged maturity model, build questions, exclusions, checklist, output contract.
- Useful pattern: strong anti-overbuilding constraint that maps well to AI-assisted product development.
- Risk/evidence: fixed time/scope heuristics are not universally valid; no test cases verify that the Skill correctly distinguishes situations where more engineering is required.
- Status: `source-read / new batch-local report / runtime not_executed`.

### pricing

- Purpose: choose an initial pricing model and estimate customer-count implications.
- Structure: cost-based/value-based models, questions, simple financial math, output.
- Useful pattern: forces explicit cost/value assumptions instead of choosing a number without rationale.
- Risk/evidence: margin/trial/general market claims are context-dependent; no live competitor data or evaluation mechanism.
- Status: `source-read / new batch-local report / runtime not_executed`.

### processize

- Purpose: express a product idea as a manual, repeatable service before automating it.
- Structure: product definition → target users → manual steps → SOP-like handoff → charging → automation gate.
- Useful pattern: creates a concrete pre-software process artifact that can later become a specification.
- Risk/evidence: fixed customer-count/readiness thresholds are heuristics; no evidence tests whether the process is actually repeatable by another operator.
- Status: `source-read / new batch-local report / runtime not_executed`.

### validate-idea

- Purpose: test a business idea through problem evidence, manual delivery, and willingness to pay.
- Structure: four-stage validation flow, red/green flags, and a three-way verdict.
- Useful pattern: produces an explicit decision instead of an open-ended brainstorm.
- Risk/evidence: relies on qualitative self-reported evidence and fixed thresholds; no data collection or validation scripts.
- Status: `source-read / new batch-local report / runtime not_executed`.

## `withcrux/agentHack-skills` — 20 individual reports

Repository-wide note: all 20 indexed bodies were read. The repository includes real CI, Python MCP/CLI code and some Docker labs, but the pinned tree contains only three lab directories while many Skills declare other lab IDs. No runtime tests were executed. Reports below therefore classify instructional scope and implementation evidence only.

### analyzing-cron-job-privesc-vectors

- Purpose: lab-scoped Linux privilege-escalation training around scheduled-task misconfiguration.
- Structure: instructional workflow with authorization/sandbox warning and declared lab dependency.
- Evidence/risk: direct body read; declared lab coverage is not proven by the repository tree; behavioral success unverified.
- Status: `source-read / new batch-local report / runtime not_executed`.

### analyzing-jwt-token-security

- Purpose: authorized analysis of token configuration and implementation weaknesses.
- Structure: security-training workflow with defensive context and lab assumptions.
- Evidence/risk: direct body read; repository safety lint is textual and does not itself enforce target authorization.
- Status: `source-read / new batch-local report / runtime not_executed`.

### analyzing-network-packet-captures

- Purpose: inspect captured network traffic for security-relevant patterns in a training context.
- Structure: analysis-oriented workflow with tooling prerequisites and expected observations.
- Evidence/risk: direct body read; no fixture/eval corpus demonstrates detection accuracy.
- Status: `source-read / new batch-local report / runtime not_executed`.

### analyzing-sudo-rules-for-privesc-vectors

- Purpose: authorized/lab-scoped review of privilege-policy misconfiguration.
- Structure: instructional enumeration-and-analysis workflow with declared isolated environment.
- Evidence/risk: direct body read; its declared lab path is not present in the pinned lab tree, so runnable status is not verified.
- Status: `source-read / new batch-local report / runtime not_executed`.

### analyzing-web-application-http-headers

- Purpose: defensive inspection of HTTP security headers and information disclosure.
- Structure: low-risk web-hardening checklist with tool examples and remediation intent.
- Evidence/risk: useful defensive scope, but no repository-local test corpus checks completeness or false positives.
- Status: `source-read / new batch-local report / runtime not_executed`.

### cracking-weak-hashes-in-lab-environment

- Purpose: controlled credential-strength training in an isolated environment.
- Structure: lab-oriented educational workflow with explicit authorization language.
- Evidence/risk: declared cryptography lab directory is absent from the pinned `labs/` root; therefore the described sandbox is not repository-verified.
- Status: `source-read / new batch-local report / runtime not_executed`.

### detecting-insecure-deserialization-vulnerabilities

- Purpose: authorized detection of unsafe object-deserialization patterns.
- Structure: advanced web-security training workflow mapped to a shared lab declaration.
- Evidence/risk: direct body read; shared-lab existence does not prove that the lab actually models all described language/framework variants.
- Status: `source-read / new batch-local report / runtime not_executed`.

### detecting-lfi-path-traversal-vulnerabilities

- Purpose: authorized detection of file-path handling vulnerabilities.
- Structure: intermediate web-security workflow with a dedicated lab declaration.
- Evidence/risk: the dedicated lab directory is absent from the pinned tree; content is source-verified but runtime capability is not.
- Status: `source-read / new batch-local report / runtime not_executed`.

### detecting-sql-injection-vulnerabilities

- Purpose: teach detection of database-query injection within an isolated web lab.
- Structure: beginner workflow tied to the repository's `sqli-basics` lab.
- Evidence/risk: one of the few declared lab IDs that does exist at the pinned revision; still no run was performed to verify lab behavior or learning objectives.
- Status: `source-read / new batch-local report / runtime not_executed`.

### detecting-ssrf-vulnerabilities

- Purpose: authorized detection of server-side request-forgery behavior in a sandbox.
- Structure: intermediate web-security workflow with a dedicated lab claim.
- Evidence/risk: declared dedicated lab is not present in the pinned tree; runtime claim is unsupported at this revision.
- Status: `source-read / new batch-local report / runtime not_executed`.

### detecting-suid-misconfigurations-for-privesc

- Purpose: authorized Linux permission-misconfiguration training.
- Structure: privilege-escalation learning workflow linked to `suid-lab`.
- Evidence/risk: `suid-lab` exists in the tree, which is stronger than prose-only evidence; no execution was performed.
- Status: `source-read / new batch-local report / runtime not_executed`.

### detecting-xss-vulnerabilities-in-web-apps

- Purpose: authorized detection of client-side injection vulnerabilities in a web training environment.
- Structure: beginner workflow with dedicated-lab declaration.
- Evidence/risk: the named dedicated lab is not present in the pinned tree; behavioral claims remain unverified.
- Status: `source-read / new batch-local report / runtime not_executed`.

### exploiting-command-injection-vulnerabilities

- Purpose: isolated security training around unsafe command execution boundaries.
- Structure: instructional lab workflow with explicit authorization statement.
- Evidence/risk: its named lab is absent at the pinned revision; source presence cannot be equated with runnable training capability.
- Status: `source-read / new batch-local report / runtime not_executed`.

### performing-arp-spoofing-in-lab

- Purpose: isolated network-security training around local-network trust weaknesses.
- Structure: lab-scoped workflow declaring a dedicated network sandbox.
- Evidence/risk: direct repository inspection found no matching lab directory; this is a concrete Skill-to-resource contract break.
- Status: `source-read / new batch-local report / runtime not_executed`.

### performing-dns-zone-transfer-attacks

- Purpose: authorized DNS configuration/reconnaissance training.
- Structure: beginner network-security workflow with a dedicated lab claim.
- Evidence/risk: the pinned network-labs directory contains only `port-scan-lab`, so the named dedicated environment is absent.
- Status: `source-read / new batch-local report / runtime not_executed`.

### performing-osint-recon-on-simulated-target

- Purpose: reconnaissance training using simulated rather than real personal/organizational targets.
- Structure: explicitly privacy-aware educational workflow sharing the network lab.
- Evidence/risk: `port-scan-lab` exists and includes simulated DNS material; no end-to-end exercise/eval was run.
- Status: `source-read / new batch-local report / runtime not_executed`.

### performing-password-spray-in-lab

- Purpose: controlled authentication-defense training inside an isolated lab.
- Structure: credential-access learning workflow with explicit authorization language.
- Evidence/risk: the declared cryptography lab is absent from the pinned tree; repository safety wording therefore exceeds verified sandbox coverage.
- Status: `source-read / new batch-local report / runtime not_executed`.

### performing-port-scanning-in-safe-lab

- Purpose: network-service discovery training against an isolated target.
- Structure: beginner workflow tied to the existing `port-scan-lab`.
- Evidence/risk: sampled Compose configuration uses an internal-only bridge and restrictive container settings, but its startup dependency-install step may conflict with the no-egress network; runtime unverified.
- Status: `source-read / new batch-local report / runtime not_executed`.

### performing-smb-enumeration-in-lab

- Purpose: authorized file-sharing/service-enumeration training.
- Structure: lab-scoped network workflow with a dedicated environment claim.
- Evidence/risk: no corresponding dedicated lab directory exists at this revision.
- Status: `source-read / new batch-local report / runtime not_executed`.

### performing-web-directory-enumeration

- Purpose: authorized web content-discovery training.
- Structure: beginner reconnaissance workflow sharing `sqli-basics`.
- Evidence/risk: the shared lab exists, but no runtime evidence proves the expected tools/content are present and aligned with the Skill.
- Status: `source-read / new batch-local report / runtime not_executed`.

## `thunderstormwang/AgentSkills` — 12 individual reports

### coding-style

- Purpose: enforce repository-level coding conventions and reduce stylistic drift.
- Structure: concise policy Skill applied during code changes/reviews.
- Useful pattern: keeps implementation conventions separate from feature logic.
- Risk/evidence: no repository-local eval directly proves adherence or conflict resolution with project-local instructions.
- Status: `source-read / new batch-local report / runtime not_executed`.

### doc-coauthoring

- Purpose: guide structured collaborative document creation through staged context, drafting, and reader validation.
- Structure: progressive authoring workflow; appears upstream-derived/adapted.
- Useful pattern: explicit phases and reader-oriented validation rather than one-pass generation.
- Risk/evidence: exact historical cross-repository canonical equivalence has not been reconciled; no local execution performed.
- Status: `source-read / new observed revision / runtime not_executed`.

### file-translator

- Purpose: translate file content while preserving usable output artifacts.
- Structure: file-oriented translation workflow with target-file behavior rules.
- Finding: existing target output may be overwritten by default; general reuse should prefer collision-safe output or explicit overwrite authorization.
- Status: `source-read / new batch-local report / runtime not_executed`.

### garmin-running-export

- Purpose: export personal running/activity data through a browser-authenticated flow.
- Structure: operational workflow with credential/state-file handling and CSV-oriented output.
- Strong point: explicitly treats saved browser state as sensitive and limits intended mutation.
- Risk: health/fitness and authentication data require clearer destination, retention, overwrite, and minimization policies; no runtime test executed.
- Status: `source-read / new batch-local report / runtime not_executed`.

### gen-task-in-plan

- Purpose: append compatible follow-up work to an existing plan while detecting conflicts with the plan's requirement boundary.
- Structure: compatibility classification + separate follow-up artifact + progress table.
- Eval surface: three concrete fixture-style cases cover compatible, violating, and ambiguous requests with file-level expectations.
- Evidence: eval definitions are stronger than prose-only guidance but were not executed in this batch.
- Status: `source-read + eval_defined / new batch-local report / eval not_executed`.

### git-commit

- Purpose: inspect changes and prepare a meaningful commit while requiring explicit approval before the external side effect.
- Structure: diff-based analysis, commit-message preparation, approval gate, then commit.
- Eval surface: three synthetic change cases specify expected interpretation, but no run result is stored in the inspected file.
- Critical interaction: conflicts with `implementation`, which treats the commit as pre-authorized.
- Status: `source-read + eval_defined / new batch-local report / eval not_executed`.

### implementation

- Purpose: execute tasks from an approved implementation plan and keep task progress synchronized.
- Structure: plan-driven implementation loop with verification and commit behavior.
- Useful pattern: ties code changes back to explicit task artifacts instead of free-form coding.
- Critical risk: its “pre-authorized commit” assumption conflicts with the explicit confirmation gate in `git-commit`; authorization must move to higher-precedence policy.
- Status: `source-read / new batch-local report / runtime not_executed`.

### mcp-builder

- Purpose: guide MCP server design and implementation.
- Structure: staged design/build workflow with reference material; appears upstream-derived/adapted.
- Useful pattern: separates protocol/tool design questions from implementation.
- Risk/evidence: repository presence does not prove built MCP servers pass protocol/behavior tests; exact cross-repository canonical equivalence pending.
- Status: `source-read / new observed revision / runtime not_executed`.

### my-code-review

- Purpose: review code changes by tracing intent, completeness, callers, contracts, and runtime impact beyond the textual diff.
- Structure: evidence-first review checklist with explicit impact-surface reasoning.
- Useful pattern: aligns well with “actual call chain before change” engineering discipline.
- Risk/evidence: no repository-local calibration/eval suite measures false positives or missed issues.
- Status: `source-read / new batch-local report / runtime not_executed`.

### playwright-cli

- Purpose: browser automation/testing through a CLI-oriented Playwright interface.
- Structure: command reference plus browser/session/network/storage capabilities.
- Useful pattern: exposes a compact operational surface for UI verification.
- Risk: broad browser and state-manipulation capability needs host-level authorization, test-target boundaries, and secret-handling policy; no browser run executed.
- Status: `source-read / new batch-local report / runtime not_executed`.

### sd-design

- Purpose: convert requirements into a gated design document and hand off confirmed design to task generation.
- Structure: Req → Pre Design Sync → Design, with progress tables and backward impact propagation.
- Useful pattern: re-reads actual code before design, separates stakeholder AC from technical test cases, and keeps implementation code out of design contracts.
- Risk/evidence: workflow is detailed but repository-local tests for phase gates/recursive updates were not found/executed.
- Status: `source-read / new batch-local report / runtime not_executed`.

### skill-creator

- Purpose: create/improve Skills and iteratively evaluate their behavior/triggering.
- Structure: intent capture → draft → test prompts → with/without-skill comparison → metrics/review → iteration.
- Useful pattern: explicitly asks for baseline comparisons and artifactized eval workspaces instead of “looks good” review.
- Risk/evidence: the Skill describes substantial evaluation infrastructure, but this batch did not execute it and exact upstream lineage reconciliation remains pending.
- Status: `source-read / new observed revision / runtime not_executed`.

## `shengxuan-create/interview-skill` — 1 individual report

### interview-skill

- Purpose: candidate-side interview preparation, research, mock interviewing, evidence-aware question generation, and post-interview learning.
- Structure: compact root router → mode-specific bilingual references → helper tools/examples/eval definitions.
- Strong pattern: progressive disclosure plus explicit “unknown/gap” handling for company-specific research reduces hallucination pressure.
- Eval surface: 13 current cases define prompts and pass expectations across research, mock, debrief, story-bank and other modes.
- Verification finding: current eval file says assertions are added during runs; no run artifacts supporting the README's historical `100%` trigger-accuracy headline were verified.
- Drift finding: `company_intel.py` references `result_evaluator.md`, but repository search at the pinned revision found no such artifact. The root Skill also labels four core disciplines but enumerates three.
- Tooling finding: at least one “research” helper builds search-query plans rather than performing source retrieval/validation itself, so evidence quality still depends on the host search/model layer.
- Status: `source-read + eval_defined / new batch-local report / eval not_executed`.

## Exact prior-content mappings — no duplicate reports

### Anthropic Cybersecurity Skills `c15f73db...` lineage

The following five repository identities were independently content-gated, then mapped to the already-reviewed exact lineage rather than creating new skill reports:

- `solophoenixdev/Anthropic-Cybersecurity-Skills`
- `Bendjou18/anthropic-cybersecurity-skills`
- `themaulanas/Anthropic-Cybersecurity-Skills`
- `APhuongKMA/Anthropic-Cybersecurity-Skills`
- `inessaGit/Anthropic-Cybersecurity-Skills`

Pinned commit for all five: `c15f73db46149587e31df83c2f9d92a3b578ef21`.

### Dreamina wrapper lineage

`VastFuture/dreamina-cli-skill` at `75e0a69a99f21a9c706045a0f6227b1b0804f886` was directly gated with README and root Skill reads, then mapped to the already-reviewed Dreamina wrapper content. No duplicate report was created.

## Count note

The **43** additions in this file are batch-local observed content reports: 10 `daonhan` + 20 `withcrux` + 12 `thunderstormwang` + 1 `shengxuan-create`. Historical cross-repository canonical reconciliation is still pending, especially for upstream-derived general Skills such as `doc-coauthoring`, `mcp-builder`, and `skill-creator`. Future reconciliation may merge identical historical content identities; it must not retroactively pretend those bodies were not directly read in Batch 042.
