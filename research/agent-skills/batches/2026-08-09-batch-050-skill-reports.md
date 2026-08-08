# Agent Skills Individual Reports — Batch 050

These are repository-scoped reports for Skill bodies newly materialized in Batch 050. Scores are analysis ratings, not executed benchmark results. No repository runtime/test/eval was executed in this batch.

## 1. `stjordanis/Anthropic-Cybersecurity-Skills::achieving-cmmc-level-2-compliance`

- Repository revision: `673da1f3b0b7be34ffc9624ef3858fe45f1c3bed`
- Path: `skills/achieving-cmmc-level-2-compliance/SKILL.md`
- Analysis rating: **3.0/5**

**Purpose / scope.** A defensive compliance Skill that organizes evidence-oriented assessment work around CMMC Level 2. It uses a conventional `SKILL.md + references + scripts + assets` layout.

**Workflow model.** The Skill defines a staged assessment/reporting flow and routes supporting automation through its local script directory. The surrounding repository provides generated indexes and CI-level structural checks.

**Evidence inspected.** `SKILL.md`, the Skill directory contents, `scripts/process.py`, root README and `.github/workflows/validate-skills.yml`.

**Strengths.** Clear defensive scope, structured evidence/report expectations, and a repository-wide validator that checks frontmatter/index/syntax/link consistency.

**Gaps / risks.** Frontmatter identifies version `2.0` while the body identifies `1.0.0`; repository README inventory is also internally inconsistent. The representative Python processor is generic and shallow relative to the domain claims. Structural CI does not establish behavioral Skill quality.

**Reusable abstraction.** Separate the domain operating contract, long-form references, deterministic conformance validation, and optional automation scripts—but require behavioral evals before claiming end-to-end reliability.

## 2. `Scoheart/agentskills::git-commit`

- Repository revision: `82fe3f694b9f46af043292def6b769654f0b2a05`
- Path: `skills/tool/git-commit/SKILL.md`
- Analysis rating: **4.0/5**

**Purpose / scope.** A Git commit workflow Skill inside a broader lockfile/catalog-managed Skill collection.

**Workflow model.** Inspect repository and branch state, confirm intended files, stage only the approved scope, prepare/perform the commit flow, and apply explicit Git safety restrictions.

**Evidence inspected.** Root tree, `CLAUDE.md`, `skills-lock.json`, and the complete representative `SKILL.md`. The pinned root does not expose a conventional `README.md`, which is recorded rather than inferred away.

**Strengths.** The Skill makes side effects explicit and prohibits several destructive or policy-bypassing operations. Scope confirmation before staging is a strong reusable boundary for coding agents.

**Gaps / risks.** It still participates in a real repository-changing workflow, so host-level authorization should remain authoritative. No behavioral eval was executed to verify that an agent consistently honors the stated gates.

**Reusable abstraction.** Treat Git writes as a separately governed capability: inspect → scope-confirm → stage only approved files → validate → side effect, with destructive operations denied by policy.

## 3. `desaiuditd/skills::git-commit-message`

- Repository revision: `47109e81a74fe1b5675cfe1239246ecd59b41335`
- Path: `skills/git-commit-message/SKILL.md`
- Analysis rating: **4.0/5**

**Purpose / scope.** Generate a Conventional Commit-style message from the staged change set without performing the commit itself.

**Workflow model.** Read staged facts, infer only what the diff supports, request missing motivation when WHY is not observable, optionally use issue context, then write the proposed message to `.git/COMMIT_EDITMSG`.

**Evidence inspected.** Root README and complete `SKILL.md`.

**Strengths.** Strong fact/intent separation: observable WHAT can come from the diff, while missing WHY is not fabricated. Artifact generation is explicitly separated from the external `git commit` side effect.

**Gaps / risks.** No repository-local behavioral eval was found/executed in this review, so message-quality consistency remains unverified.

**Reusable abstraction.** Separate `derive facts → resolve missing intent → generate artifact` from `execute external side effect`.

## 4. `juicyjusung/juicy-skills::kr-daytrade`

- Repository revision: `4be83edc06f1ecad686eb883257269440120c196`
- Path: `skills/kr-daytrade/SKILL.md`
- Analysis rating: **3.5/5**

**Purpose / scope.** A Korean-market research/planning Skill. This report intentionally evaluates engineering boundaries rather than reproducing trading tactics.

**Workflow model.** Gather market data, organize analysis and present a research/planning output. The Skill explicitly excludes account access, order placement and automated trading.

**Evidence inspected.** Root README, complete `SKILL.md`, repository tree and related script inventory.

**Strengths.** Clear read-only boundary between analysis and financial side effects.

**Gaps / risks.** Market conclusions are externally time-sensitive and the Skill is not an executed, audited financial model. No runtime or accuracy eval was executed.

**Reusable abstraction.** For financially sensitive Skills, encode a hard capability boundary so research/data access cannot silently become transaction authority.

## 5. `juicyjusung/juicy-skills::kr-market`

- Repository revision: `4be83edc06f1ecad686eb883257269440120c196`
- Path: `skills/kr-market/SKILL.md`
- Analysis rating: **4.0/5**

**Purpose / scope.** Read-only Korean market-data access and presentation.

**Workflow model.** Route data requests to local TypeScript scripts that call the external market-data API and return structured observations. Account/order operations are outside the Skill's declared scope.

**Evidence inspected.** `SKILL.md`, Skill directory/script inventory and `scripts/_client.ts`.

**Strengths.** The client separates credential loading, token caching, request handling and bounded retries. Cached credentials/tokens are written with restrictive file permissions where supported. The Skill contract keeps data retrieval distinct from trading authority.

**Gaps / risks.** Live API behavior, rate limits, credentials and returned data were not executed or validated. The client still depends on external credentials/network availability.

**Reusable abstraction.** `read-only capability contract + credential boundary + bounded retry + explicit API error surface` is a useful pattern for external-data Skills.

## 6. `juicyjusung/juicy-skills::persuade`

- Repository revision: `4be83edc06f1ecad686eb883257269440120c196`
- Path: `skills/persuade/SKILL.md`
- Analysis rating: **3.5/5**

**Purpose / scope.** A structured persuasive-writing Skill using established rhetorical/persuasion frameworks.

**Workflow model.** Identify audience/goal, choose an appropriate persuasion structure, develop claims/support, then revise the message for clarity and credibility.

**Evidence inspected.** Root README, actual repository tree and complete `SKILL.md`.

**Strengths.** Clear composition workflow and reusable framing concepts.

**Gaps / risks.** Persuasion quality is contextual and no repository-local eval was executed. A host application should preserve higher-level safety and truthfulness policy rather than treating the Skill as independent authorization to manipulate users.

**Reusable abstraction.** Keep rhetorical technique in a subordinate content Skill while truthfulness/safety constraints remain host-level policy.

## 7. `juicyjusung/juicy-skills::stock-research`

- Repository revision: `4be83edc06f1ecad686eb883257269440120c196`
- Path: `skills/stock-research/SKILL.md`
- Analysis rating: **4.0/5**

**Purpose / scope.** Evidence-oriented company/stock research. This report evaluates provenance design, not investment recommendations.

**Workflow model.** Gather company and financial evidence, prioritize primary regulatory filings, attach source/time context to numerical claims, and synthesize research with explicit sourcing.

**Evidence inspected.** Root README and complete `SKILL.md`.

**Strengths.** The provenance contract is the strongest part: numerical facts should carry source and observation time, and official filings are preferred over secondary summaries.

**Gaps / risks.** Financial data is time-sensitive; there is no executed accuracy benchmark in this batch. Research output must not be conflated with transaction authorization or guaranteed investment outcomes.

**Reusable abstraction.** Require `claim → source → timestamp` for time-sensitive numerical research, with primary-source preference encoded in the Skill contract.

## 8. `juicyjusung/juicy-skills::us-market`

- Repository revision: `4be83edc06f1ecad686eb883257269440120c196`
- Path: `skills/us-market/SKILL.md`
- Analysis rating: **3.5/5**

**Purpose / scope.** Read-only U.S. market-data research/presentation.

**Workflow model.** Retrieve market observations through data tooling and summarize them, while keeping account access/order execution outside scope.

**Evidence inspected.** Root README, repository tree and complete `SKILL.md`.

**Strengths.** Explicit separation between market information and financial side effects; fallback/source guidance is present for data retrieval.

**Gaps / risks.** External data freshness/availability and behavioral correctness were not runtime validated.

**Reusable abstraction.** Use capability-level separation (`market-data-read` vs `transaction-write`) rather than relying on prompt wording alone.

## 9. `mihado/wondelai-skills::clean-architecture`

- Repository revision: `66de348733ec508b3b8c81717333dbc2ca9f4cf0`
- Path: `clean-architecture/SKILL.md`
- Analysis rating: **4.0/5**

**Purpose / scope.** A Clean Architecture design/review Skill focused on dependency direction, boundary placement, SOLID principles and framework isolation.

**Workflow model.** Keep the top-level Skill as the operating/routing layer, then progressively load long-form architecture references when deeper boundary or SOLID reasoning is needed.

**Evidence inspected.** Root README, complete `SKILL.md`, `references/boundaries.md`, the reference inventory and `references/solid-principles.md`.

**Strengths.** Strong progressive-disclosure structure. The boundary reference makes interface/dependency inversion and boundary-crossing data explicit; the SOLID reference supplies concrete violation/remediation examples without overloading the main Skill.

**Gaps / risks.** It is methodology-heavy rather than execution/eval-heavy. No behavioral harness was executed to show consistent application to real repositories or to measure false-positive architectural findings.

**Reusable abstraction.** `SKILL.md = decision/routing contract`, `references/ = deep doctrine/examples`, with deterministic repository-specific validation added separately when the Skill is used for real code changes.

## Batch-level conclusion

The most reusable patterns from these nine new reports are:

1. **Host-level side-effect governance** rather than assuming Skill activation grants write authority.
2. **Artifact generation separated from execution** for Git and other consequential operations.
3. **Read-only vs write capability separation** for external financial/data systems.
4. **Claim/source/time provenance** for time-sensitive numerical research.
5. **Progressive disclosure** from concise Skill routing rules into deeper references.
6. **Structural CI distinguished from behavioral evals**; no pass result is recorded unless the behavior was actually executed and observed.