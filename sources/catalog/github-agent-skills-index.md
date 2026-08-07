# GitHub Agent Skills Repository Index

## Current verified catalog

- Raw GitHub search hits already composed into the canonical catalog: `2630`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across composed inputs: `2634`
- Unique repositories after case-insensitive `owner/repository` deduplication: `2502`
- Exact duplicates removed across composed inputs: `132`
- New unique repositories composed in this run: `0`
- Provisionally eligible for later deep analysis: `2088`
- Held as adjacent or unclear search hits: `414`

Composed machine-readable authority: [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

The canonical total remains `2502` because the current `agentskills in:name,description` search is staged but has not yet completed exhaustive historical identity reconciliation. This run persisted pages `2-3`, bringing staged coverage to pages `1-3`.

## Completed search coverage

- `"agent skills" in:name,description`, pages `1-10`
- `"codex skills" in:name,description`, pages `1-10`
- `"claude skills" in:name,description`, pages `1-10`
- `"mcp skills" in:name,description`, pages `1-10`
- `"skill catalog" in:name,description`, pages `1-10`
- `"skill registry" in:name,description`, pages `1-10`
- `"agent skill" in:name,description`, pages `1-10`
- `"agentskills cli" in:name,description`, page `1`
- `"skill marketplace" in:name,description`, pages `1-10`
- `"agent skills hub" in:name,description`, pages `1-2`
- `"skill hub" in:name,description`, pages `1-10`
- `"agent skills directory" in:name,description`, pages `1-2`
- `"openai skills" in:name,description`, pages `1-10`
- `"anthropic skills" in:name,description`, pages `1-10`
- `"agent skills marketplace" in:name,description`, pages `1-10`
- `"agentskills specification" in:name,description`, page `1`
- `"skill lint" in:name,description`, complete accessible page-1 result set with `100` requested results
- `"agent skills validator" in:name,description`, complete accessible page-1 result set with `100` requested results
- `"agent skills standard" in:name,description`, pages `1-10`, `20` results per page
- `"agent skills eval" in:name,description`, complete accessible pages `1-3`, `20` requested results per page; page `4` returned `0`
- `"agent skills benchmark" in:name,description`, complete accessible page `1`, `50` requested results; page `2` returned `0`
- `"agent skills test" in:name,description`, complete accessible page `1`, `50` requested results; page `2` returned `0`
- `"agentskills sdk" in:name,description`, complete accessible page `1`, `50` requested results; page `2` returned `0`
- `"agent skills template" in:name,description`, complete accessible pages `1-3`, `20` requested results per page; page `4` returned `0`
- `"agent skills examples" in:name,description`, complete accessible pages `1-2`, `50` requested results per page; page `3` returned `0`
- `"agent skills protocol" in:name,description`, complete accessible page `1`, `50` requested results; page `2` returned `0`
- `"agent skills registry" in:name,description`, complete accessible pages `1-41`, `20` requested results per page; page `42` returned `0`

## In-progress search coverage

Query:

```text
agentskills in:name,description
```

Persisted staging coverage now includes pages `1-3`, each with `20` GitHub repository identities. Existing verified state records that this query was probed through page `11`; pages `4-11` are not yet persisted as staging batches.

Staged totals:

| Metric | Value |
| --- | ---: |
| Raw identities | `60` |
| Batch/internal or cross-staging duplicates | `0` |
| Exact prior duplicates directly confirmed | `3` |
| Identities still requiring full historical reconciliation | `57` |
| Canonical delta asserted | `0` |

The three directly confirmed prior duplicates are:

- `agentskills/agentskills`
- `darkrishabh/agent-skills-eval`
- `pratikxpanda/agentskills-sdk`

Pages `2-3` add `40` verified repository identities with no duplicate against the persisted page-1 staging batch. Those 40 identities remain `unresolved_against_full_prior_catalog`; code-search absence is not treated as evidence that an identity is new.

Staging artifacts:

- [`batches/agentskills-page-1.json`](batches/agentskills-page-1.json)
- [`batches/agentskills-pages-2-3.json`](batches/agentskills-pages-2-3.json)

## Pages 2-3 provisional classification

| Classification | Raw pages 2-3 count |
| --- | ---: |
| `specification` | `0` |
| `skill_collection` | `24` |
| `single_skill_or_domain_package` | `4` |
| `awesome_index` | `1` |
| `skill_tooling` | `6` |
| `adjacent_search_hit` | `1` |
| `unclear_search_hit` | `4` |

These classifications are provisional from repository identity and query context only. They are not added to canonical classification totals until historical reconciliation is complete.

## Canonical classification totals

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

This remains an index-only catalog. GitHub repository search verified repository identity and accessibility. Classification is provisional from repository identity and search context only. No repository README, `SKILL.md`, scripts, references, eval contents, stars, quality, or implementation behavior was assessed.

The current run deliberately does not treat code-search emptiness or an aggregate prior count as proof that an identity is new.

## Validation

- Previous canonical state remains: `2502 unique / 2088 eligible / 414 held`.
- Newly persisted pages in this run: `2-3`.
- New staged identities in this run: `40`.
- Pages `2-3` internal duplicates: `0`.
- Pages `2-3` duplicates against staged page `1`: `0`.
- Total staged identities across pages `1-3`: `60`.
- Directly confirmed prior duplicates across staged pages: `3`.
- Unresolved staged identities requiring exhaustive historical reconciliation: `57`.
- Pages `2-3` staging commit: `976813fd22aae37b599579977cb171539d5c6abf`.
- Latest-manifest staging-state commit: `34f74f3960aa713cdf32072b9ad84eea60cbeb58`.
- `2088 + 414 = 2502`, matching the canonical eligible and held partitions.
- No README, `SKILL.md`, scripts, references, eval contents, stars, or implementation contents were read during this index-only run.
