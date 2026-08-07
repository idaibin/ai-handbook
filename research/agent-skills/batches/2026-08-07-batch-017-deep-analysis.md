# Agent Skills deep analysis — Batch 017

- Observed at: 2026-08-07 16:00 +08:00
- Queue source: `sources/catalog/github-agent-skills-index-latest.json`
- Repositories completed: **10**
- Repository-scoped individual skill reports: **25**
- Completion state: `structure-reviewed`
- Runtime validation: `not_executed`
- Rule: no repository in this batch is counted complete from metadata alone.

## Batch summary

| Repository | Displayed stars | Index classification | Content classification | Local skill reports | Content evidence reviewed |
| --- | ---: | --- | --- | ---: | --- |
| `kambleakash0/agent-skills` | 7 | `skill_collection` | `skill_collection_with_mcp_tools` | 13 | GitHub repository page/README/root structure, maintained 13-skill inventory, `skills/grill-master/SKILL.md`, `skills/teach-me/SKILL.md`, teach-me reference surface |
| `jeremyeder/dgx-agentskills` | 0 | `skill_collection` | `skill_collection_plus_mcp_plugin` | 5 | README/root tree, complete five-skill inventory, `skills/spark-setup/SKILL.md`, MCP test tree, `tests/mcp-server/status.test.ts` |
| `gigantsc/agentskills-hermes` | 0 | `skill_collection` | `specification_reference_sdk` | 0 | README/root tree, `package.json`, repository search for local `SKILL.md` |
| `cesareth/hermes-turkce-skills` | 0 | `skill_collection` | `skill_collection` | 4 | README/root tree, all four current `SKILL.md` bodies, KVKK helper script |
| `suprunoff/skills-catalog` | 0 | `skill_tooling` | `awesome_index_research_catalog` | 0 | README/root tree, `index.html`, repository search for local `SKILL.md` |
| `YoavLax/AgentEval` | 1 | `skill_tooling` | `skill_tooling_validator` | 0 | README/root tree, validator core, rule/test structure, `tests/test_cli.py` |
| `nxl801/obsidian-official-cli-skill` | 2 | `single_skill_or_domain_package` | `single_skill_or_domain_package` | 1 | README/root tree, source `SKILL.md`, official CLI reference file |
| `kayaman/agentskills` | 1 | `skill_collection` | `skill_tooling_package_manager` | 0 | README/root tree, Rust installer implementation, unit tests, CLI integration test |
| `siddontang/tidb-x-skill` | 0 | `single_skill_or_domain_package` | `single_skill_or_domain_package` | 1 | README/root tree, root `SKILL.md` |
| `antgly/law-of-demeter-swift-skill` | 0 | `single_skill_or_domain_package` | `single_skill_or_domain_package` | 1 | README/root tree, root `SKILL.md` |

Displayed stars were read from the current GitHub repository pages during this run. Repository/internal catalog star fields were not substituted for GitHub repository stars.

## Repository findings

### 1. `kambleakash0/agent-skills`

The repository is a real mixed content/tool collection rather than a name-only search hit. Its maintained README currently inventories 13 Agent Skills and three separate MCP servers. The direct `grill-master` body is a clarification gate: it withholds planning/implementation until a shared, testable understanding is reached, asks one focused question at a time, and explicitly prefers repository facts over asking the user to reconstruct known code behavior. The direct `teach-me` body is stateful and uses workspace files (`MISSION.md`, learning records, resources, lessons, glossary/notes) to make learning progress persistent and auditable.

**Useful pattern:** separate reusable skill bodies from heavier MCP capabilities while exposing both through one discoverable repository. `teach-me` also demonstrates a durable state model in which progress is based on recorded evidence rather than conversation memory alone.

**Risk/limitation:** Batch 017 verified the maintained inventory plus representative bodies, not all 13 bodies line by line. No repository-level eval runner was executed.

### 2. `jeremyeder/dgx-agentskills`

This repository combines five Agent Skills with a DGX Spark MCP/plugin implementation. `spark-setup/SKILL.md` is operationally structured: it defines prerequisites and ordered provisioning phases, treats phases as re-runnable, includes deployment and explicit validation checkpoints, and specifies a final setup report. The repository also contains a nontrivial MCP test suite; `tests/mcp-server/status.test.ts` tests normal system/GPU metric parsing and a failure path for the GPU command.

**Useful pattern:** pair operational skills with implementation-level tests for the tooling they invoke, while keeping the human/agent workflow readable in `SKILL.md`.

**Validation boundary:** the test sources and operational commands were inspected but no SSH, GPU, Docker, network, build, or test command was executed in this batch.

### 3. `gigantsc/agentskills-hermes`

The index-stage name classification overstated this repository as a skill collection. Content inspection shows a forked Agent Skills specification/documentation/reference repository: root structure includes documentation and reference surfaces, and `package.json` only exposes a docs development command. Repository search did not surface a local `SKILL.md` package. Example skills referenced by documentation are external and are not reassigned to this repository.

**Classification correction:** `skill_collection` → `specification_reference_sdk`.

**Useful pattern:** keep specifications/reference SDKs in the catalog as first-class ecosystem artifacts, but do not inflate skill counts from linked examples.

### 4. `cesareth/hermes-turkce-skills`

The repository contains four current Turkish-language skills, and all four bodies were directly read: `turkce-asistan`, `kvkk-denetim`, `resmi-yazi`, and `turkce-kod`. The collection is region/language-specific rather than a generic translation layer. It includes linked references and, for `kvkk-denetim`, a Python helper script.

The KVKK helper is concrete code but intentionally simple: it performs regex-based checks for expected phrases and risk indicators, calculates a weighted score, and prints a report. The skill itself contains an explicit legal-information disclaimer. Batch 017 therefore treats the script as a quick heuristic aid, not as proof of legal compliance.

**Useful pattern:** domain/language skills can keep the main workflow concise while pushing vocabulary or legal/technical detail into references and bounded helper scripts.

**Risk/limitation:** several legal/administrative statements are authored guidance and were not independently revalidated against current law in this repository-analysis batch.

### 5. `suprunoff/skills-catalog`

This candidate is a static research/catalog site rather than skill runtime tooling. Root content is primarily `index.html`, README/deployment material, and a research directory. The catalog page contains large marketplace/index statistics and curated platform sections; those numbers are repository-authored research claims, not independently verified counts in this batch. Repository search did not surface a local `SKILL.md` package.

**Classification correction:** `skill_tooling` → `awesome_index_research_catalog`.

**Useful pattern:** index/catalog repositories are valuable discovery inputs but should remain separate from installable skill identity counts.

### 6. `YoavLax/AgentEval`

This is a Python quality-gate/validator for `SKILL.md` and agent markdown, not a bundled skill collection. The reviewed `src/agenteval/core.py` parses a target, detects skill-versus-agent type, selects rule sets, applies ignore/skip options, and returns structured diagnostics/check runs. `tests/test_cli.py` verifies exit-code semantics, JSON output shape, directory discovery, threshold overrides, ignore rules, and CLI behavior. The README explicitly documents heuristic/tokenizer and compatibility limitations.

**Useful pattern:** validation tooling states where its signals are heuristic and exposes deterministic machine-readable results/exit codes instead of presenting lint success as semantic correctness.

**Validation boundary:** tests were read but not run; no local bundled skill package was surfaced, so the repository contributes zero individual skill reports.

### 7. `nxl801/obsidian-official-cli-skill`

The repository contains one source skill plus packaging/release material. `obsidian-official-cli/SKILL.md` is retrieval-first: it searches/context-filters before reading notes, uses Obsidian-specific graph/metadata commands to expand only when useful, prefers structured output for downstream parsing, and explicitly separates read-only defaults from mutating commands. Its reference file provides the concrete command families used by the workflow.

**Useful pattern:** knowledge-retrieval skills can reduce model context and accidental side effects by making narrow retrieval the default and enumerating write-risk boundaries separately.

**Validation boundary:** repository documentation states the skill has been tested with a real vault, but Batch 017 did not independently execute Obsidian or a vault workflow.

### 8. `kayaman/agentskills`

Despite its index-stage `skill_collection` label, this is a Rust package manager for skills hosted elsewhere. The README documents add/list/remove/update/init/find workflows, project/global installation locations, lockfile tracking, and support for both root-level and `skills/` layouts. Direct review of `src/core/installer.rs` confirms single/multiple skill installation, recursive copying, content hashing, and lockfile updates; unit tests cover install/update/empty/lockfile cases. `tests/integration.rs` builds a temporary local repository with two root-level `SKILL.md` packages and asserts the CLI installs both.

**Classification correction:** `skill_collection` → `skill_tooling_package_manager`.

**Useful pattern:** package-manager identity and installed skill identities remain separate; the lockfile provides provenance/change tracking rather than copying remote skills into the manager's own catalog count.

**Validation boundary:** Rust tests and CLI were inspected, not executed.

### 9. `siddontang/tidb-x-skill`

This is a single root skill. The body teaches TiDB X concepts and patterns for durable/queryable agent state, including memory/context and auditable decisions. It is much closer to a product/domain knowledge package than to executable tooling.

**Useful pattern:** a domain skill can combine a mental model, applicability boundaries, reusable schema patterns, and source links in one self-contained package.

**Risk/limitation:** architecture, performance, pricing/billing, and product capability statements inside the repository are publisher-authored claims. Batch 017 did not independently benchmark or product-verify them.

### 10. `antgly/law-of-demeter-swift-skill`

This repository contains one strict Swift review skill. The body defines aggressive detection triggers for deep reach-through chains while also listing false-positive guardrails for standard-library pipelines, fluent APIs, and boundary mapping. It gives Swift-specific replacement naming, a smallest-safe-refactor ordering, severity labels, a review response structure, and anti-regression follow-up checks.

**Useful pattern:** a review skill is stronger when it pairs detection heuristics with explicit exceptions and a constrained repair strategy; this reduces both missed findings and indiscriminate over-flagging.

**Validation boundary:** no scripts/tests/evals are present in the reviewed root structure, and no behavioral evaluation was run.

## Classification corrections from content evidence

| Repository | Index-stage label | Content-grounded label | Reason |
| --- | --- | --- | --- |
| `gigantsc/agentskills-hermes` | `skill_collection` | `specification_reference_sdk` | Spec/docs/reference repository; no local skill package surfaced. |
| `suprunoff/skills-catalog` | `skill_tooling` | `awesome_index_research_catalog` | Static research/catalog site; no local skill package surfaced. |
| `kayaman/agentskills` | `skill_collection` | `skill_tooling_package_manager` | Rust installer/manager for externally hosted skills; no local bundled corpus counted. |

These corrections are deep-analysis findings. They do not rewrite the canonical index classification in this batch; index reconciliation remains a separate catalog task.

## Individual report artifact

The 25 repository-scoped identities are recorded once each in:

- `research/agent-skills/batches/2026-08-07-batch-017-skill-reports-01.md`

Six repositories contribute local skill identities; four ecosystem/tooling/index repositories deliberately contribute zero. Remote marketplace entries, linked examples, dependency-provided content, and externally installed skills are not reassigned to the repository that references or manages them.

## Count reconciliation

```text
kambleakash0/agent-skills                 13
jeremyeder/dgx-agentskills                 5
gigantsc/agentskills-hermes                0
cesareth/hermes-turkce-skills              4
suprunoff/skills-catalog                    0
YoavLax/AgentEval                           0
nxl801/obsidian-official-cli-skill          1
kayaman/agentskills                         0
siddontang/tidb-x-skill                     1
antgly/law-of-demeter-swift-skill           1
---------------------------------------------
total                                      25
```

## Validation boundary

This batch performed source/content review only. Identity and current displayed GitHub stars were checked, repository structure and maintained documentation were inspected, representative/all-small-corpus skill bodies were read as described above, and available implementation/test/reference surfaces were inspected where relevant.

No third-party installer, CLI, test suite, evaluation runner, cloud API, browser automation, GPU/SSH/Docker command, database service, or repository script was executed. The correct state is therefore `structure-reviewed` with `runtime_validation: not_executed`. A repository is counted complete here only for the defined source-review gate; this status is not runtime verification.