# GitHub Agent Skills Repository Index

## Current verified catalog

- Raw GitHub search hits: `1869`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across all inputs: `1873`
- Unique repositories after case-insensitive `owner/repository` deduplication: `1758`
- Exact duplicates removed across current inputs: `115`
- New unique repositories collected in this run: `19`
- Net catalog delta versus the previous verified manifest: `+19`
- Provisionally eligible for later deep analysis: `1351`
- Held as adjacent or unclear search hits: `407`

Composed machine-readable authority: [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

The current manifest composes the previous verified `1739`-repository canonical manifest with page `2` of the `agent skills registry` discovery query.

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

## In-progress search coverage

- `"agent skills registry" in:name,description`, pages `1-2` complete at `20` results per page; page `3` was probed and returned `20` repositories, so the next merge boundary is page `3`.

## This run

Query:

```text
"agent skills registry" in:name,description
```

Processed page `2` at `per_page=20`.

- Raw repository identities: `20`
- Internal batch duplicates: `0`
- Duplicates against the prior verified catalog: `1`
- Added as new repositories: `19`
- Previous verified catalog: `1739`
- Updated composed catalog: `1758`
- Added to provisional deep-analysis queue: `18`
- Added to held-for-review: `1`

`wm4n/skill-registry` was already persisted in [`batches/skill-registry-pages-1-10.json`](batches/skill-registry-pages-1-10.json). Exact AI-handbook code search was executed for all 20 page-2 identities; the other 19 returned no prior indexed match.

Provisional classification for the 19 new identities is `14 skill_collection`, `4 skill_tooling`, and `1 unclear_search_hit`. Repository IDs, default branches, sizes, archived flags, result ordering, classifications, eligibility, and verification notes are stored in [`batches/agent-skills-registry-page-2.json`](batches/agent-skills-registry-page-2.json).

## Classification totals

| Classification | Count | Index-stage meaning |
| --- | ---: | --- |
| `specification` | 163 | Identity strongly indicates a Skill specification, standard, or normative guidance. |
| `skill_collection` | 551 | Identity indicates a collection or examples of Skills. |
| `single_skill_or_domain_package` | 102 | Identity indicates one Skill or a domain-focused package. |
| `awesome_index` | 38 | Identity indicates a curated Skill index. |
| `skill_tooling` | 497 | Identity indicates validation, linting, evaluation, testing, packaging, discovery, registry, marketplace, management, benchmark, SDK, template, fixture, or runtime tooling. |
| `adjacent_search_hit` | 150 | Related to agents or Skills, but not clearly a Skill repository from identity alone. |
| `unclear_search_hit` | 257 | Identity is insufficient for reliable classification. |

## Evidence boundary

This remains an index-only catalog. GitHub repository search verified repository identities and accessibility. Classifications are provisional from repository identity and search context only. No repository README, `SKILL.md`, scripts, references, eval contents, stars, quality, or implementation behavior was assessed.

## Validation

- Previous canonical manifest commit: `678e9598812028246bdeaed117f9fe21d1511ced` (`1739` repositories).
- `agent skills registry` page-2 batch commit: `f32fdf0bc81823b9ecc48d98a229d4dfc7833a77`.
- Composed latest-manifest commit: `18847678305be3500c2fa4ee4fe1aa0c040d035d`.
- `1739 + 19 = 1758` current unique repositories.
- `1873 - 115 = 1758` raw-to-unique reconciliation.
- Classification totals resolve to `1758`.
- `1351 + 407 = 1758`, matching the eligible and held partitions.
- Next index boundary: `"agent skills registry" in:name,description`, page `3`, `per_page=20`.
- No README, `SKILL.md`, scripts, references, eval contents, stars, or implementation contents were read during this index-only run.
