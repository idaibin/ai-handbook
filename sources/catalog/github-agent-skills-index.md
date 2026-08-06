# GitHub Agent Skills Repository Index

## Current verified catalog

- Raw GitHub search hits: `1829`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across all inputs: `1833`
- Unique repositories after case-insensitive `owner/repository` deduplication: `1731`
- Exact duplicates removed across current inputs: `102`
- New unique repositories collected in this run: `12`
- Net catalog delta versus the previous verified manifest: `+12`
- Provisionally eligible for later deep analysis: `1325`
- Held as adjacent or unclear search hits: `406`

Composed machine-readable authority: [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

The current manifest composes the previous verified `1719`-repository canonical manifest with the verified `agent skills protocol` discovery batch.

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

## This run

Query:

```text
"agent skills protocol" in:name,description
```

GitHub returned `12` repositories on page `1` and `0` on page `2`, so this query is complete at `per_page=50`.

- Raw repository identities: `12`
- Internal batch duplicates: `0`
- Duplicates against the prior verified catalog: `0`
- Added as new repositories: `12`
- Previous verified catalog: `1719`
- Updated composed catalog: `1731`
- Added to provisional deep-analysis queue: `11`
- Added to held-for-review: `1`

Provisional classification for the new identities is `10 single_skill_or_domain_package`, `1 awesome_index`, and `1 adjacent_search_hit`. Repository IDs, default branches, sizes, archived flags, result ordering, classifications, eligibility, and verification notes are stored in [`batches/agent-skills-protocol-search.json`](batches/agent-skills-protocol-search.json).

AI-handbook code search was run for the four repository-name clusters represented by the result set: `personal-finance-skill`, `liuxiaoyan-skill`, `Claude-pjm-risk-analyzer`, and `awesome-payment-agent-skills`. None returned a prior indexed match, so all 12 identities are new relative to the verified `1719` catalog base.

## Classification totals

| Classification | Count | Index-stage meaning |
| --- | ---: | --- |
| `specification` | 163 | Identity strongly indicates a Skill specification, standard, or normative guidance. |
| `skill_collection` | 531 | Identity indicates a collection or examples of Skills. |
| `single_skill_or_domain_package` | 102 | Identity indicates one Skill or a domain-focused package. |
| `awesome_index` | 38 | Identity indicates a curated Skill index. |
| `skill_tooling` | 491 | Identity indicates validation, linting, evaluation, testing, packaging, discovery, registry, marketplace, management, benchmark, SDK, template, fixture, or runtime tooling. |
| `adjacent_search_hit` | 150 | Related to agents or Skills, but not clearly a Skill repository from identity alone. |
| `unclear_search_hit` | 256 | Identity is insufficient for reliable classification. |

## Evidence boundary

This remains an index-only catalog. GitHub repository search verified repository identities and accessibility. Classifications are provisional from repository identity and search context only. No repository README, `SKILL.md`, scripts, references, eval contents, stars, quality, or implementation behavior was assessed.

## Validation

- Previous canonical manifest commit: `43c5def72f278eef4c44487d66e31edc254c81d1` (`1719` repositories).
- `agent skills protocol` batch commit: `e28265401b72503a2ed87c9222266282423f15fd`.
- Composed latest-manifest commit: `20e825ef419507127da9e303885f8cdc4621ad16`.
- `1719 + 12 = 1731` current unique repositories.
- `1833 - 102 = 1731` raw-to-unique reconciliation.
- Classification totals resolve to `1731`.
- `1325 + 406 = 1731`, matching the eligible and held partitions.
- Page `2` returned zero results; `"agent skills protocol"` is complete at `per_page=50`.
- No README, `SKILL.md`, scripts, references, eval contents, stars, or implementation contents were read during this index-only run.
