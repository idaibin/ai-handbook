# GitHub Agent Skills deep analysis — Batch 018

- Observed at: `2026-08-07T17:09:25+08:00`
- Queue source: `sources/catalog/github-agent-skills-index-latest.json`
- Repository count: **10**
- Repository-scoped skill reports: **53**
- Validation state: `structure-reviewed`
- Runtime validation: `not_executed`
- Individual reports: `research/agent-skills/batches/2026-08-07-batch-018-skill-reports-01.md`

## Scope and method

This batch used the existing indexed queue and excluded repositories already listed in `research/agent-skills/deep-analysis-progress.json`. For each selected repository, identity was verified through GitHub repository metadata, displayed/current stars were checked from current GitHub surfaces where available, and actual repository content was read. The review covered repository-maintained inventory/README surfaces, `SKILL.md` or equivalent definitions, and available scripts/references relevant to the repository's core mechanism.

Large collections are not represented as if every body were read line-by-line. A repository-maintained complete inventory plus representative direct skill-body reads is recorded as `inventory-verified`; direct file reads are recorded as `direct-body-reviewed` in the individual report artifact.

## Repository results

| Repository | Stars observed | Local skill reports | Content reviewed | Result |
| --- | ---: | ---: | --- | --- |
| `wtsi-hgi/agentskills` | 1 | 27 | `docs/skills.md`; `agent-conduct`; `implementation-principles`; `testing-principles`; `subagents`; `orchestrator` | Strong layered engineering workflow with explicit safety, evidence, verification, and subagent boundaries. |
| `omaclaren/agent-skills-public` | 3 | 5 | README plus all five current skill bodies | Small, explicit-invocation collection with unusually clear mutation and prompt/data boundaries. |
| `ok406lhq/skills-guardian` | 0 | 1 | `SKILL.md`, static scanner, install wrapper | Useful defensive signal generator, but regex/additive scoring is heuristic and cannot prove skill safety. |
| `timeplus-io/AgentSkills` | 1 | 6 | README inventory; `timeplus-sql-guide`; `searxng-web-search`; search implementation | Well-structured product/domain collection with progressive references and concrete operational error handling. |
| `avoidthekitchen/agent-agnostic-skills` | 1 | 4 | all four current skill bodies plus candidate-extraction implementation | High research value: evidence-first RPI workflow and review-rule bootstrapping with calibration instead of raw-frequency promotion. |
| `yashasvigirdhar/skills` | 2 | 4 | README inventory; `feature-inventory` body | Strong product-knowledge pattern around a structured YAML inventory, drift detection, and a human bootstrap gate. |
| `postnitro/postnitro-carousel-skill` | 1 | 1 | `SKILL.md`, API reference | Clear external-service adapter with asynchronous lifecycle and schema constraints; runtime remains service/account dependent. |
| `maxamillion/agentskill-rhoai-cve-analysis` | 0 | 1 | README, skill body, CVE methodology | Defensive analysis pipeline is well decomposed, but automatic fallback classification introduces a material false-negative risk if treated as authoritative security truth. |
| `Digidai/website2markdown-skills` | 2 | 1 | root `SKILL.md`, repository structure/reference map | Broad external web-conversion wrapper with progressive reference loading; service/platform behavior was not reproduced. |
| `zht043/AgentSkills` | 10 | 3 | deprecated README, root governance skill, three current local skill bodies | Repository is a deprecated migration source, not an active canonical collection; only three not-yet-migrated local skills are counted. |

### Star evidence note

Nine repositories had stars observed from current GitHub repository surfaces in this run. `ok406lhq/skills-guardian` identity was verified directly through GitHub, while the current star value `0` was cross-checked from synchronized repository metadata because the public GitHub HTML surface repeatedly failed to resolve in the web cache. This is recorded as a lower-strength star observation than the other nine and is not used for any quality conclusion.

## Key findings

### 1. `wtsi-hgi/agentskills`: layered skill architecture is directly reusable

Verified facts:

- The complete repository inventory contains 27 skills arranged as universal conduct, shared implementation/testing principles, workflow skills, and four stack triplets.
- `agent-conduct` explicitly prohibits fabricated results and requires blockers to be reported rather than hidden.
- `implementation-principles` requires the smallest coherent change, semantic reuse, TDD, and explicit reporting when quality gates cannot run.
- `subagents` defines cross-harness adapters and requires writable workers for orchestrated work.
- `orchestrator` does not mark plan items complete until implementation/review success is returned.

Evidence-based inference: the strongest reusable concept is not an individual prompt but the dependency layering: stable cross-project policy -> stack convention -> implementor/reviewer -> orchestration. This is compatible with a Skills Catalog that wants fewer stable entry points and explicit supporting contracts.

Limit: these orchestration contracts were source-reviewed only; no harness was launched to validate enforcement.

### 2. `avoidthekitchen/agent-agnostic-skills`: evidence-first RPI aligns with AI Engineering workflow goals

Verified facts:

- `rpi-research` requires evidence-backed research, parallel tracks, conflict reconciliation, file/line references, and explicit inference labeling.
- `rpi-plan` turns that research into phased, file-level checklists with measurable success criteria and explicit non-goals.
- `rpi-implement-plan` updates progress only after implementation and verification, while surfacing stale-plan/code mismatches.
- `bootstrap-checks-from-prs` stores PR evidence and candidate-rule artifacts, then recommends holdout calibration before checks are broadly adopted.
- Its rule extractor uses frequency plus risk, detectability, scope and retained evidence rather than treating event counts as proof.

Evidence-based inference: the RPI split is a useful comparison basis for existing `repo-map` / `product-spec` / development / review boundaries, but should be borrowed as a workflow principle rather than automatically copied into additional Skills.

### 3. `yashasvigirdhar/skills`: structured feature inventory is a useful product/engineering bridge

Verified facts:

- `feature-inventory` maintains a YAML feature inventory connecting user-facing features to API routes, frontend routes, tests, docs, flags, personas and lifecycle status.
- Bootstrap requires an interactive human confirmation gate and explicitly refuses initial bootstrap in scheduled/non-interactive execution.
- Drift-sync compares declared feature surfaces to code and records each run.
- The skill itself states static route discovery has blind spots and recommends runtime introspection where possible.

Evidence-based inference: the strongest reusable idea is a structured cross-layer product capability ledger, especially for keeping product specification, API, frontend, tests and documentation traceable without forcing all information into Markdown prose.

### 4. `maxamillion/agentskill-rhoai-cve-analysis`: strong pipeline decomposition, but fallback semantics need caution

Verified facts:

- The skill separates container/CVE collection, deterministic pre-triage, second-pass review, remediation generation and reporting.
- The methodology prioritizes more authoritative product/VEX signals before generic heuristics.
- Later fallback tiers intentionally guarantee that no `DEFERRED` result remains, including generic classifications based on severity/context categories.

Risk: eliminating all `DEFERRED` states trades uncertainty visibility for completion. In a security review workflow, forcing ambiguous findings into `NOT_AFFECTED`/`MITIGATED` can create false confidence. This is a methodology risk, not evidence that the project has produced an incorrect real-world CVE decision.

Minimum improvement if adapting the pattern: preserve an explicit unresolved state unless a classification is supported by authoritative product evidence or a separately validated rule.

### 5. `zht043/AgentSkills`: index classification needs correction

Verified facts:

- Current README says `AgentSkills (Deprecated)` and states maintenance has stopped.
- Former `skill-creator`, SSH suite and Ascend suite have moved to independent repositories.
- Only `markdown-mermaid-illustrator`, legacy `doc-illustrator`, and `export-history` remain listed as not-yet-migrated local skills.

Classification correction:

```text
previous index-stage classification: skill_collection
content-reviewed classification: deprecated_migration_source / historical_skill_collection
current local skill count: 3
```

The moved repositories must be indexed and analyzed under their own identities; their skills are not counted again here.

## Cross-repository reusable patterns

| Pattern | Evidence | Reuse direction |
| --- | --- | --- |
| Layer policy, conventions, implementor/reviewer, orchestration | `wtsi-hgi/agentskills` | Keep entry Skills small while putting stable shared contracts underneath. |
| Research -> plan -> implementation with durable evidence | `avoidthekitchen/agent-agnostic-skills` | Compare with existing research/review workflow; reuse semantics before adding new Skill names. |
| Structured capability inventory tied to code surfaces | `yashasvigirdhar/skills` | Candidate input for product-spec/repo-map data contracts and drift validation. |
| Explicit invocation for potentially intrusive interaction modes | `omaclaren/agent-skills-public` | Useful for skills that alter collaboration style or mutate user artifacts. |
| Separate deterministic analysis from uncertainty | `skills-guardian` and RHOAI CVE skill | Preserve signal strength and unresolved states; do not convert heuristic output into verified facts. |
| Progressive disclosure via references | `timeplus-io/AgentSkills`, `website2markdown`, others | Keep `SKILL.md` navigational/core and load large domain references only when needed. |

## Risks and limitations

- Runtime behavior was **not** executed. No source-reviewed script, test suite, build, installer, cloud API, external browser/search service, CVE analysis, database, or product endpoint was run.
- Star counts are point-in-time metadata and are not used as a proxy for engineering quality.
- Large collections use complete repository-maintained inventories plus representative direct body reads; this is not equivalent to line-by-line review of every skill body.
- External-service skills may drift independently of their repository documentation.
- `zht043/AgentSkills` is deprecated; any future analysis should follow the migrated repositories instead of treating this monorepo as canonical.

## Count reconciliation

```text
repositories completed this batch: 10
repository-scoped skill reports:   53
previous repositories completed:  170
cumulative repositories completed:180
previous skill reports:            2256
cumulative skill reports:          2309
canonical eligible snapshot:       2088
remaining estimate after batch:    1908
```

## Validation boundary

Status is `structure-reviewed`, not `runtime-verified`. A repository is counted here because current identity/stars were checked and actual source content was read, not because search metadata described it as a Skill repository. No build/test/runtime success is asserted.