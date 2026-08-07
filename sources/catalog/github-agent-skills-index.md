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

This run backfilled pages `1-9`, each with `20` live GitHub repository-search results. The `180` identities are all distinct under case-insensitive `owner/repository` comparison. They were then merged with the already-persisted January pages `10-19` (`188` identities); the cross-set overlap count is `0`.

The complete January partition is therefore:

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

Classification remains provisional and is based only on repository identity, GitHub search context, and search-returned size metadata where applicable. It is not merged into canonical classification totals yet.

### January artifacts

- [`batches/agentskills-created-2026-01-pages-1-9.json`](batches/agentskills-created-2026-01-pages-1-9.json) — batch commit `07dcd90a08fb9fb988e8631b971a6d94e4c031b0`
- [`batches/agentskills-created-2026-01-page-10.json`](batches/agentskills-created-2026-01-page-10.json)
- [`batches/agentskills-created-2026-01-pages-11-13.json`](batches/agentskills-created-2026-01-pages-11-13.json)
- [`batches/agentskills-created-2026-01-pages-14-16.json`](batches/agentskills-created-2026-01-pages-14-16.json)
- [`batches/agentskills-created-2026-01-pages-17-19.json`](batches/agentskills-created-2026-01-pages-17-19.json)
- [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json) — January-completion manifest commit `0242d579844f6a46d7008dfabb60c61fa1b6e4ff`

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

Begin the next deterministic `created:` partition while separately reconciling partition identities against the unpartitioned staging set and the historical canonical ledger. Canonical `2502 / 2088 / 414` remains unchanged until that reconciliation produces verified deltas.
