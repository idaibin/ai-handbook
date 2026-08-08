# Agent Skills Repository Deep Analysis — Batch 041

- Batch ID: `2026-08-08-batch-041`
- Scope: next **10 qualified repository identities** from the deterministic indexed queue
- Repository completion rule: identity + observed Stars + pinned revision + actual repository content read; metadata-only completion is prohibited
- Repositories completed: **10**
- README files directly read: **10**
- `SKILL.md` files directly read: **11**
- Unique Git content trees represented: **5**
- Direct unique skill bodies reviewed: **5**
- New canonical individual skill reports: **2**
- Runtime/build/test/eval execution: **not_executed**

## Queue selection

The queue continued from Batch 040 with `francktienta-lgtm/Anthropic-Cybersecurity-Skills`. Five index-stage candidates encountered before the tenth qualified completion were inspected and rejected from the completion count: four are exact Agent Skills specification/reference-SDK forks and one is a Rust skill validator. `maxdraki/OpenPulseAI` remains held as an `adjacent_search_hit`. The batch continued through the queue until ten genuinely qualified skill repositories were content-gated.

| Repository | GitHub ID | Stars observed | Pinned revision | Queue class | Content gate |
|---|---:|---:|---|---|---|
| `francktienta-lgtm/Anthropic-Cybersecurity-Skills` | 1200162249 | 0 | `2c88b96cf758c8a742c5b683e02c01e84497034f` | skill_collection | README + representative SKILL + exact tree read |
| `AbuAli1393/Anthropic-Cybersecurity-Skills` | 1200099896 | 1 | `2c88b96cf758c8a742c5b683e02c01e84497034f` | skill_collection | README + representative SKILL read directly from identity |
| `sirameshg/Anthropic-Cybersecurity-Skills` | 1200121146 | 0 | `2c88b96cf758c8a742c5b683e02c01e84497034f` | skill_collection | README + representative SKILL read directly from identity |
| `CYPKNFT/Anthropic-Cybersecurity-Skills` | 1200554527 | 0 | `c15f73db46149587e31df83c2f9d92a3b578ef21` | skill_collection | README + representative SKILL read directly from identity |
| `young9471/Anthropic-Cybersecurity-Skills` | 1200022514 | 0 | `2c88b96cf758c8a742c5b683e02c01e84497034f` | skill_collection | README + representative SKILL read directly from identity |
| `ABe-er/dreamina-cli-skill` | 1201158561 | 0 | `75e0a69a99f21a9c706045a0f6227b1b0804f886` | single_skill_or_domain_package | README + SKILL + recursive tree + wrapper source + command reference read |
| `barrettsoron/civic-skills` | 1201029194 | 1 | `087758437fb95a73769823619c76a0a9f2206c9d` | skill_collection | README + both SKILL bodies + references + recursive tree read |
| `justanotherkevin/almost-social-skills` | 1201465628 | 0 | `955115316fdf18eaef1ba6e7a9860704215e172f` | skill_collection | README + representative SKILL + reference + recursive tree read |
| `welma-git/wondelai-skills` | 1201561279 | 0 | `955115316fdf18eaef1ba6e7a9860704215e172f` | skill_collection | README + representative SKILL read directly from identity |
| `bmersereau/skills` | 1200902957 | 0 | `955115316fdf18eaef1ba6e7a9860704215e172f` | skill_collection | README + representative SKILL read directly from identity |

Observed Stars are point-in-time GitHub repository observations made during this batch; they are not historical values.

## 1–5. `Anthropic-Cybersecurity-Skills` fork identities

Four identities pin the exact older revision `2c88b96cf758c8a742c5b683e02c01e84497034f`; `CYPKNFT` pins the newer `c15f73db46149587e31df83c2f9d92a3b578ef21`. Every identity had its own README and `skills/performing-memory-forensics-with-volatility3/SKILL.md` opened directly before completion.

The older revision's recursive tree confirms a large structured collection with `.claude-plugin` manifests, `index.json`, mapping files, GitHub validation workflows, and skill packages. Its exact revision was already canonicalized in Batch 039; the newer `c15f73db...` lineage was already reviewed in Batch 040. Therefore this batch adds repository-identity coverage but does **not** duplicate canonical skill reports.

### Findings retained after direct recheck

- The collection claims 753 skills, while README prose remains internally inconsistent about 26 versus 38 domains. Catalog-size claims are inventory claims, not quality evidence.
- The structural validation workflow is useful for frontmatter/naming/index consistency, but it is not a behavioral or cybersecurity-accuracy eval.
- The representative memory-forensics body is substantive and operational, but representative reads do not justify claiming all 753 bodies are behaviorally validated.
- The newer `c15f73db...` lineage contains helper/script changes already captured in Batch 040. No new runtime, false-positive/false-negative, authorization, or safety evidence was produced in this run.
- No cybersecurity procedure was executed in this batch.

### Verdict

Keep repository coverage separate from canonical content coverage. These mirrors are valuable as taxonomy/index material, but adoption still requires per-skill risk, authorization, freshness, and behavioral gates.

## 6. `ABe-er/dreamina-cli-skill`

### Actual structure

The pinned tree contains `SKILL.md`, `agents/openai.yaml`, two reference documents, and a Python wrapper implementation plus thin command entry points. The wrapper source performs parameter normalization, local-path validation, JSON extraction/normalization, command-specific validation, and async submit-status handling. The command reference documents `--dry-run`, stable JSON success/failure payloads, argument mapping, and the current validation boundary.

The exact revision/tree is the same Dreamina content already reviewed under another repository identity in Batch 040, so this identity maps to the existing canonical report rather than creating a duplicate.

### Strengths

- Real executable wrapper code exists; this is not a prompt-only skill.
- `--dry-run` exposes the exact external CLI argument vector before expensive/ambiguous operations.
- Structured JSON responses and explicit `submit_id` handling make orchestration more deterministic than raw shell parsing.
- Local path and range/combination checks reduce some preventable command failures.

### Risks / gaps

- Installation documentation uses a remote `curl | bash` command without pinning an artifact/version in this snapshot.
- The repository tree surfaced no dedicated test/eval suite; wrapper behavior was read, not executed.
- The skill still depends on the external Dreamina CLI, login state, remote model behavior, and server-side validation.
- Returning full `cli_args` is useful for debugging but should be reviewed if future commands introduce sensitive parameters.

### Verdict

Good reference for a thin, inspectable CLI-wrapper Skill with dry-run and structured output. Reuse the wrapper contract pattern, but add pinned installation, repository-local tests/fixtures, secret-aware output redaction, and runtime verification before production use.

## 7. `barrettsoron/civic-skills`

### Actual structure

This repository contains two real Agent Skills:

1. `canadian-civic-data`
2. `news-analysis`

Both bodies were read in full at the pinned revision. The tree contains reference-only source adapters rather than executable scripts: five civic reference files and three news reference files. No repository-local test/eval harness surfaced. The README explicitly labels the project early-stage and says most API endpoints have not yet been tested against real use cases.

### Design strengths

- Both skills use a narrow operation router and tell the agent to load only the relevant reference, which is a good context-budget pattern.
- Data-source boundaries, auth expectations, coverage caveats, pagination notes, and known limitations are written down close to the routing decision.
- The repository explicitly rejects surveillance, mass scraping, and access-control circumvention.
- References are substantive: for example, the openparliament reference documents endpoint patterns and pagination; the GDELT reference distinguishes DOC 2.0 article search from the event database and warns that tone is only a signal.

### Findings

- **Repository documentation drift:** the root README still offers a lobbying example, while the current `canadian-civic-data/SKILL.md` routes only four sources and no longer routes lobbying. A stale `references/lobbying.md` also remains in the tree.
- **No executable adapter layer:** endpoint construction, response parsing, schema changes, retries, rate handling, provenance, and error normalization are delegated to the LLM/user environment. That keeps the package simple but weakens determinism.
- **Freshness risk:** several reference facts are inherently time-sensitive (current parliamentary session, API limits, source behavior). Static Markdown needs explicit last-verified dates or live contract tests.
- **README itself disclaims endpoint validation:** the repository should not be treated as runtime-certified.
- **No fixtures/evals surfaced:** there is no evidence here for response-schema compatibility, endpoint availability, source deduplication quality, or longitudinal news-analysis correctness.

### Verdict

A useful example of small router-first knowledge skills with clear source-specific references and ethical boundaries. The strongest next improvement would be deterministic source adapters plus fixture/live-contract tests, not more prose.

## 8–10. Three Wondel-derived repository identities

`justanotherkevin/almost-social-skills`, `welma-git/wondelai-skills`, and `bmersereau/skills` all pin the exact commit `955115316fdf18eaef1ba6e7a9860704215e172f` and tree `ce033c08eb129f35b624e0e96aad883843babaca`. Their READMEs were opened directly from each identity, and `top-design/SKILL.md` was also opened directly from each identity before completion. A `top-design` typography reference was reread from one representative identity.

This exact Wondel-derived snapshot was already canonicalized in Batch 039/040, so the three repositories add identity coverage only.

### Findings

- The snapshot is a genuine multi-skill package with plugin marketplace/symlink topology and substantive references, not a metadata-only hit.
- `top-design` now makes custom cursors opt-in, which is a useful explicit user-authorization boundary.
- The skill still encodes subjective weighted 0–10 aesthetic scoring and several categorical visual rules. These are critique heuristics, not objectively validated quality measurements.
- Accessibility/performance constraints are present, but aesthetic absolutes can still conflict with project context, device limits, brand requirements, or user preferences.
- No dedicated behavioral eval result is asserted for this snapshot in this batch; no browser/runtime validation was executed.

### Verdict

Keep this versioned snapshot as a useful design/product-framework corpus, but preserve provenance and avoid converting subjective scores into hard acceptance gates without project-specific evals.

## Reclassified / not completed

The following indexed candidates were inspected but **not** counted toward the ten completed repositories:

- `davccavalcante/agentskills` — exact pinned content states that the repository contains the Agent Skills specification, documentation, and reference SDK; not a local skill collection.
- `bdweb771-art/agentskills` — same specification/reference-SDK lineage at the same pinned commit; README opened directly.
- `Aether-Saint/agentskills` — same specification/reference-SDK lineage at the same pinned commit; README opened directly.
- `DCS6578/agentskills` — same specification/reference-SDK lineage at the same pinned commit; README opened directly.
- `bjester/shinyskills` — actual Rust validator/tooling project. Its README, current commit, and integration-test fixture were inspected; fixture `SKILL.md` content exists to test the validator, not as a catalog skill package. Reclassified as `skill_tooling`.

`maxdraki/OpenPulseAI` remains an index-stage `adjacent_search_hit` and was not used to fill the batch quota.

## Validation boundary

### Verified in Batch 041

- 10 completed repository identities, observed Stars, and pinned revisions;
- direct README reads for all 10 completed identities;
- direct `SKILL.md` read for every completed repository identity, with both civic skill bodies read;
- five unique Git content trees and exact mirror relationships;
- executable Dreamina wrapper source and command reference;
- civic repository structure and representative source references;
- Wondel representative body/reference and exact-tree lineage;
- five rejected index candidates were not counted as completed after content inspection.

### Not verified / not executed

- no repository script execution;
- no Python/Rust build or test run;
- no live civic/news/Dreamina API calls;
- no browser/UI validation;
- no cybersecurity procedure execution;
- no claim that every body in the 753-skill cybersecurity or Wondel collections was reread line-by-line in this batch;
- no claim that README quality/performance/security statements are externally validated.

Repository-level completion remains a **content-gated deep structure review**, not runtime certification.

## Queue continuation

The next qualified queue identity after this batch boundary is `solophoenixdev/Anthropic-Cybersecurity-Skills`. Canonical reconciliation remains pending; queue continuation must still use actual content gates rather than metadata.