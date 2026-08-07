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

The canonical total remains `2502` because the current `agentskills in:name,description` search is staged but has not yet completed exhaustive historical identity reconciliation. This run persisted pages `7-10`, bringing staging coverage to pages `1-10`.

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

Persisted staging coverage now includes pages `1-10`, each observed with `20` GitHub repository identities. This run also probed pages `11-16`; those pages returned `20` results each but are not claimed as persisted staging coverage yet.

Staged totals:

| Metric | Value |
| --- | ---: |
| Raw identities | `200` |
| Batch/internal or cross-staging duplicates | `1` |
| Unique staged identities after cross-staging deduplication | `199` |
| Exact prior duplicates directly confirmed | `3` |
| Identities still requiring full historical reconciliation | `196` |
| Canonical delta asserted | `0` |

The three directly confirmed prior-catalog duplicates remain:

- `agentskills/agentskills`
- `darkrishabh/agent-skills-eval`
- `pratikxpanda/agentskills-sdk`

Across persisted pages `1-10`, the only currently observed cross-staging repeat is `0xsarawut/agentskills`, which appeared at page `3` rank `20` and page `4` rank `1`. Pages `7-10` added `80` raw identities and all `80` were distinct from persisted pages `1-6` under case-insensitive `owner/repository` comparison.

Staging artifacts:

- [`batches/agentskills-page-1.json`](batches/agentskills-page-1.json)
- [`batches/agentskills-pages-2-3.json`](batches/agentskills-pages-2-3.json)
- [`batches/agentskills-pages-4-6.json`](batches/agentskills-pages-4-6.json)
- [`batches/agentskills-pages-7-10.json`](batches/agentskills-pages-7-10.json)

## Pages 7-10 provisional classification

| Classification | Count |
| --- | ---: |
| `specification` | `0` |
| `skill_collection` | `79` |
| `single_skill_or_domain_package` | `0` |
| `awesome_index` | `0` |
| `skill_tooling` | `0` |
| `adjacent_search_hit` | `0` |
| `unclear_search_hit` | `1` |

`OpenTideHQ/AgentTide` is kept as `unclear_search_hit` because this index phase intentionally does not read repository content to infer more than the search result identity supports. These classifications are not added to canonical classification totals until historical reconciliation is complete.

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

The current run deliberately does not treat code-search emptiness, mutable page ordering, or an aggregate prior count as proof that an identity is new.

## Validation

- Previous canonical state remains: `2502 unique / 2088 eligible / 414 held`.
- Newly persisted pages in this run: `7-10`.
- Raw identities newly persisted in this run: `80`.
- Internal duplicates within pages `7-10`: `0`.
- Cross-staging duplicates against pages `1-6`: `0`.
- New staged-unique identities in this run: `80`.
- Total staged raw identities across pages `1-10`: `200`.
- Total staged unique identities after cross-staging deduplication: `199`.
- Directly confirmed prior-catalog duplicates across staged pages: `3`.
- Unresolved staged identities requiring exhaustive historical reconciliation: `196`.
- Pages `7-10` staging commit: `f2e7d25f2372dcb601363135e6879ba82aa26570`.
- Latest-manifest staging-state commit: `00b5b25b4c94e2127ee18f03a6b0782e887c2d80`.
- `2088 + 414 = 2502`, matching the canonical eligible and held partitions.
- No README, `SKILL.md`, scripts, references, eval contents, stars, or implementation contents were read during this index-only run.
