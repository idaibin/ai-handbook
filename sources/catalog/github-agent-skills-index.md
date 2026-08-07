# GitHub Agent Skills Repository Index

## Current verified catalog

- Raw GitHub search hits: `2109`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across all inputs: `2113`
- Unique repositories after case-insensitive `owner/repository` deduplication: `1987`
- Exact duplicates removed across current inputs: `126`
- New unique repositories collected in this run: `20`
- Net catalog delta versus the previous verified manifest: `+20`
- Provisionally eligible for later deep analysis: `1573`
- Held as adjacent or unclear search hits: `414`

Composed machine-readable authority: [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

The current manifest composes the previous verified `1967`-repository canonical manifest with page `14` of the `agent skills registry` discovery query.

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

- `"agent skills registry" in:name,description`, pages `1-14` processed at `20` results per page; page `15` was probed and returned `20` repositories, so the next merge boundary is page `15`.

## This run

Query:

```text
"agent skills registry" in:name,description
```

Processed page `14` at `per_page=20`.

- Raw repository identities: `20`
- Internal batch duplicates: `0`
- Confirmed duplicates against the prior verified catalog: `0`
- Added as new repositories: `20`
- Previous verified catalog: `1967`
- Updated composed catalog: `1987`
- Added to provisional deep-analysis queue: `20`
- Added to held-for-review: `0`

All 20 page-14 identities were compared directly against persisted `agent-skills-registry` pages `1-13`. They were also compared against the directly inspected `skill-hub` pages `1-10`, `agent-skills-hub` pages `1-2`, and `skill-registry` pages `1-10` persisted artifacts. No exact case-insensitive `owner/repository` duplicate was found in those overlap sets. Empty GitHub code-search results were not used as sole uniqueness evidence because earlier runs demonstrated false negatives.

All 20 page-14 results were provisionally classified from repository identity and GitHub search context as `skill_tooling`; all 20 are provisionally eligible for later deep analysis. Repository IDs, default branches, sizes, archived flags, result ordering, classifications, eligibility, and verification notes are stored in [`batches/agent-skills-registry-page-14.json`](batches/agent-skills-registry-page-14.json).

## Classification totals

| Classification | Count | Index-stage meaning |
| --- | ---: | --- |
| `specification` | 163 | Identity strongly indicates a Skill specification, standard, or normative guidance. |
| `skill_collection` | 611 | Identity indicates a collection or examples of Skills. |
| `single_skill_or_domain_package` | 104 | Identity indicates one Skill or a domain-focused package. |
| `awesome_index` | 38 | Identity indicates a curated Skill index. |
| `skill_tooling` | 657 | Identity indicates validation, linting, evaluation, testing, packaging, discovery, registry, marketplace, management, benchmark, SDK, template, fixture, or runtime tooling. |
| `adjacent_search_hit` | 152 | Related to agents or Skills, but not clearly a Skill repository from identity alone. |
| `unclear_search_hit` | 262 | Identity is insufficient for reliable classification. |

## Evidence boundary

This remains an index-only catalog. GitHub repository search verified repository identities and accessibility. Classifications are provisional from repository identity and search context only. No repository README, `SKILL.md`, scripts, references, eval contents, stars, quality, or implementation behavior was assessed.

## Validation

- Previous canonical manifest commit: `05e7d46c24842c9ed3cbcc621ec8d16dd2743bd6` (`1967` repositories).
- `agent skills registry` page-14 batch commit: `4e3db2c9c5312c293d153831fbf1188a117c1704`.
- Composed latest-manifest commit: `6266229646ba8d702038e5455e13afdfdb44fd0b`.
- `1967 + 20 = 1987` current unique repositories.
- `2113 - 126 = 1987` raw-to-unique reconciliation.
- Classification totals resolve to `1987`.
- `1573 + 414 = 1987`, matching the eligible and held partitions.
- Next index boundary: `"agent skills registry" in:name,description`, page `15`, `per_page=20`.
- No README, `SKILL.md`, scripts, references, eval contents, stars, or implementation contents were read during this index-only run.
