# Agent Skills Individual Reports — Batch 044

- Batch ID: `2026-08-08-batch-044`
- Completed repository identities: **10**
- Direct `SKILL.md` reads: **16**
- Direct unique Skill bodies reviewed: **12**
- New canonical Skill-body reports: **2**
- Existing canonical bodies directly reverified/mapped: **10**
- Runtime/build/test/eval execution: **not_executed**

Only bodies directly read in this batch are eligible for mapping. Collection inventories are not converted into individual reports. Historical cross-repository canonical reconciliation remains pending.

## 1. `chainlink-cre-skill` — new canonical report

- Repository: `chethanuk/chainlink-agent-skills`
- Revision: `8d6f777a3e3c4a28449f98dbbfb29e108cd75ff5`
- Body: `chainlink-cre-skill/SKILL.md`
- Version: `0.2`
- Supporting content read: repository README; reference map embedded in Skill
- Execution: **not_executed**

**Purpose.** Help an agent onboard to and develop against Chainlink Runtime Environment (CRE), including workflow generation, CLI/SDK questions and runtime operations.

**Structure.** The body is deliberately thin relative to its reference set. It routes questions to topic-specific references and distinguishes conceptual knowledge from exact current implementation details. For CLI syntax it prioritizes local `cre <command> --help`; for code/docs it prioritizes targeted official pages, then repository references, then large text dumps only as a last resort.

**Strong patterns.** The most reusable design is “fetch as resolution, not preparation”: write or scaffold from the local contract, identify an exact missing fact, fetch only that fact, then continue. This reduces speculative browsing and context growth. The workflow-generation checklist also defaults to simulation and withholds deployment steps unless explicitly requested.

**Risks / gaps.** Correctness still depends on live external documentation and the host’s WebFetch/Bash behavior. The Skill contains procedural guidance for assessing fetched-content quality, but this is not a deterministic parser or source-verification implementation. No repository-local CRE behavioral eval was surfaced and no CLI/API execution was performed in this review.

**Verdict.** **High-value reference architecture for freshness-sensitive developer Skills; pair it with executable source/version checks and task fixtures before treating the behavior as verified.**

## 2. `chainlink-ccip-skill` — new canonical report

- Repository: `chethanuk/chainlink-agent-skills`
- Revision: `8d6f777a3e3c4a28449f98dbbfb29e108cd75ff5`
- Body: `chainlink-ccip-skill/SKILL.md`
- Version: `0.0.1`
- Supporting content read: `references/official-sources.md`, `evals/chainlink-ccip-skill/README.md`, `eval-rubric.md`, eval directory structure
- Execution: **not_executed**

**Purpose.** Route Chainlink CCIP requests across discovery, tool-first sends, contract work, simulation, monitoring and CCT workflows while constraining external side effects.

**Structure.** Progressive disclosure is explicit: references are loaded only for the active workflow. A separate freshness/source map assigns conceptual documentation, CLI/API/SDK documentation, live route/token directory data and explorer/message status to different official sources.

**Strong patterns.** The authorization contract is unusually concrete. Read-only work may proceed, while state-changing operations require a preflight summary and explicit approval; selected testnet effects require a second confirmation immediately before execution; mainnet writes are refused in the reviewed version. These rules are mirrored in a real Promptfoo eval surface whose must-pass rubric includes mainnet-write refusal, approval preservation, correct workflow routing and live-source discipline.

**Risks / gaps.** The presence of Promptfoo cases and rubrics is evidence of an executable evaluation design, not evidence that it passes. This batch did not run Promptfoo or any Chainlink operation. LLM-as-judge portions also need stable provider/version pinning and deterministic assertions for the safety-critical gates where possible.

**Verdict.** **One of the stronger observed Skill designs for combining progressive disclosure, freshness routing, explicit side-effect authorization and an executable eval contract. Runtime/eval results remain unverified until run.**

## Existing canonical body mappings directly reverified

### Dreamina

`JimmyZhangJW/dreamina-cli-skill` directly reverified `dreamina-cli` plus its Python wrapper and integration reference. The body maps to the Dreamina wrapper report already established in Batch 040; this repository identity does not create a second canonical report.

### Fernandez/Omaclaren collection

`fernandezbaptiste/agent-skills-public` directly reread all four bodies: `guide-mode`, `critique-skill`, `annotated-reply-skill`, and `preview-browser-skill`. The catalog already contains these bodies from earlier analysis (including Batch 018 lineage), so this batch records repository coverage and current-body verification only.

### Wondel lineage

Four repository identities (`gregvanhorn/skills`, `navneet10sep/skills`, `yamisoto/skills`, `leviathannexusprime-bot/skills`) independently reread the same `clean-architecture` body and resolve to the same complete Git tree. `clean-architecture` is already represented in prior Wondel analysis; no duplicate report is created.

### Zephyr lineage

`bunjunwang/zephyr-agent-skills` directly reread the umbrella router, `zephyr-index`, and `devicetree`, and inspected the repository validator plus devicetree helper/reference. The `devicetree`/Zephyr body lineage is already represented in Batch 027; this is repository/tree reverification rather than a new canonical report.

### Anthropic-Cybersecurity-Skills lineage

`rwe137/Anthropic-Cybersecurity-Skills` and `chillux/Anthropic-Cybersecurity-Skills` independently reread the v1.2.0 README and `analyzing-api-gateway-access-logs`. Both are exact tree duplicates of the `5dd2ce82...` lineage already covered in Batch 043, so the sampled body is mapped rather than duplicated.

## Cross-batch evidence discipline

- A repository identity is counted only after direct content inspection in this batch.
- An exact duplicate tree may reuse prior canonical Skill reports, but the repository identity still receives its own coverage record.
- A README count such as 41 Wondel Skills or 754 Cybersecurity Skills is inventory evidence only.
- Scripts/evals inspected but not run remain `not_executed`; no pass result is inferred from their existence or documentation.
