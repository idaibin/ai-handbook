# GitHub Agent Skills Repository Index

## Current verified catalog

- Raw GitHub search hits already composed into the canonical catalog: `2630`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across composed inputs: `2634`
- Unique repositories after case-insensitive `owner/repository` deduplication: `2502`
- Exact duplicates removed across composed inputs: `132`
- Provisionally eligible for later deep analysis: `2088`
- Held as adjacent or unclear search hits: `414`

Canonical totals remain frozen while the newer `agentskills` staging and created-date partitions are reconciled against the complete historical ledger. Machine-readable authority: [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

## Completed search coverage

The earlier index already persisted the documented query families for `agent skills`, `codex skills`, `claude skills`, `mcp skills`, skill catalogs/registries/marketplaces, OpenAI/Anthropic skills, validators, standards, evals, benchmarks, tests, SDKs, templates, examples, protocols, and the complete accessible `agent skills registry` pagination.

### Unpartitioned `agentskills`

```text
agentskills in:name,description
```

- Persisted pages: `1-50`
- Requested results per page: `20`
- Raw staging records: `1000`
- Page `51`: GitHub first-1000-results limit
- Full historical reconciliation: still pending for the unreconciled staging tail

The unpartitioned query therefore covers its accessible first `1000` search results, not the complete query universe.

## January 2026 created-date partition — complete

Query:

```text
agentskills in:name,description created:2026-01-01..2026-01-31
```

Pages `1-19` are persisted. The complete partition contains `368` raw identities and `368` unique identities under case-insensitive `owner/repository`; page `20` returned `0` repositories.

| Metric | Value |
| --- | ---: |
| Persisted pages | `1-19` |
| Raw identities | `368` |
| Unique identities within partition | `368` |
| Duplicates removed within partition | `0` |
| Terminal probe | page `20` returned `0` |
| Canonical additions asserted | `0` |

### January provisional classification

| Classification | Count |
| --- | ---: |
| `specification` | `2` |
| `skill_collection` | `275` |
| `single_skill_or_domain_package` | `32` |
| `awesome_index` | `11` |
| `skill_tooling` | `21` |
| `adjacent_search_hit` | `12` |
| `unclear_search_hit` | `15` |
| **Total** | **`368`** |

### January artifacts

- [`batches/agentskills-created-2026-01-pages-1-9.json`](batches/agentskills-created-2026-01-pages-1-9.json)
- [`batches/agentskills-created-2026-01-page-10.json`](batches/agentskills-created-2026-01-page-10.json)
- [`batches/agentskills-created-2026-01-pages-11-13.json`](batches/agentskills-created-2026-01-pages-11-13.json)
- [`batches/agentskills-created-2026-01-pages-14-16.json`](batches/agentskills-created-2026-01-pages-14-16.json)
- [`batches/agentskills-created-2026-01-pages-17-19.json`](batches/agentskills-created-2026-01-pages-17-19.json)

## February 2026 created-date partition — in progress

Query:

```text
agentskills in:name,description created:2026-02-01..2026-02-28
```

This run persisted pages `1-2`, each with `20` live GitHub repository-search results. The `40` identities are all distinct under case-insensitive `owner/repository` comparison. January and February are disjoint `created:` ranges, so a repository identity cannot legitimately belong to both partitions; reconciliation against the unpartitioned staging set and complete historical catalog is still pending.

| Metric | Value |
| --- | ---: |
| Persisted pages | `1-2` |
| Raw identities | `40` |
| Unique identities within persisted pages | `40` |
| Duplicates removed within persisted pages | `0` |
| Partition complete | `no` |
| Canonical additions asserted | `0` |

### February provisional classification, pages 1-2

| Classification | Count |
| --- | ---: |
| `specification` | `0` |
| `skill_collection` | `30` |
| `single_skill_or_domain_package` | `0` |
| `awesome_index` | `0` |
| `skill_tooling` | `5` |
| `adjacent_search_hit` | `4` |
| `unclear_search_hit` | `1` |
| **Total** | **`40`** |

Classification is provisional and uses repository identity plus search-returned repository metadata only. It is not merged into canonical classification totals.

### February artifacts

- [`batches/agentskills-created-2026-02-pages-1-2.json`](batches/agentskills-created-2026-02-pages-1-2.json) — batch commit `2f74722f0b8b0da9322c1da7ca3dde1c95389b52`
- [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json) — manifest commit `91973c2823bfd07847f89a76c75def75ba573b0e`

## Canonical classification totals

These remain unchanged until deterministic historical reconciliation completes.

| Classification | Count |
| --- | ---: |
| `specification` | `163` |
| `skill_collection` | `611` |
| `single_skill_or_domain_package` | `104` |
| `awesome_index` | `38` |
| `skill_tooling` | `1172` |
| `adjacent_search_hit` | `152` |
| `unclear_search_hit` | `262` |

## Evidence boundary

This phase is index-only. No target repository README, `SKILL.md`, scripts, references, eval contents, stars, implementation code, or runtime behavior was inspected. Repository completion for deep-analysis purposes is not asserted from these records.

## Next index action

Continue the February 2026 `created:` partition from page `3`. Canonical `2502 / 2088 / 414` remains unchanged until partition identities are reconciled against unpartitioned staging and the complete historical ledger.
