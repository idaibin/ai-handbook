# GitHub Agent Skills Repository Index

## Current verified catalog

- Raw GitHub search hits: `2089`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Raw identities across all inputs: `2093`
- Unique repositories after case-insensitive `owner/repository` deduplication: `1967`
- Exact duplicates removed across current inputs: `126`
- New unique repositories collected in this run: `10`
- Net catalog delta versus the previous verified manifest: `+10`
- Provisionally eligible for later deep analysis: `1553`
- Held as adjacent or unclear search hits: `414`

Composed machine-readable authority: [`github-agent-skills-index-latest.json`](github-agent-skills-index-latest.json).

The current manifest composes the previous verified `1957`-repository canonical manifest with page `13` of the `agent skills registry` discovery query.

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

- `"agent skills registry" in:name,description`, pages `1-13` processed at `20` results per page; page `14` was probed and returned `20` repositories, so the next merge boundary is page `14`.

## This run

Query:

```text
"agent skills registry" in:name,description
```

Processed page `13` at `per_page=20`.

- Raw repository identities: `20`
- Internal batch duplicates: `0`
- Confirmed duplicates against the prior verified catalog: `10`
- Added as new repositories: `10`
- Previous verified catalog: `1957`
- Updated composed catalog: `1967`
- Added to provisional deep-analysis queue: `10`
- Added to held-for-review: `0`

Direct comparison against persisted `agent-skills-registry` pages `1-12` confirmed ten repeats in the page-13 response: `BarryYin/skillhub` and `hack-feng/skillhub` already occur on page `11`, while `99DevOps892/STA-skillhub`, `crowscc/skillhub`, `DBdoctor-DAS/skillhub`, `zhangyuanann/skillhub`, `NealShieh/skillhub`, `DonnyQu7/skillhub`, `khoantd/skillhub`, and `ljx0305/skillhub` already occur on page `12`. This verifies that repository-search pagination shifted across observation times and cannot be treated as a stable partition by page number alone.

The ten remaining identities were also compared against the directly inspected `skill-hub` pages `1-10`, `agent-skills-hub` pages `1-2`, and `skill-registry` pages `1-10` persisted artifacts; no exact case-insensitive `owner/repository` match was found in those overlap sets. Exact AI-handbook code search returned no positive prior match for the candidate identities, but empty code-search results were not used as sole uniqueness proof because earlier runs demonstrated false negatives.

All 20 page-13 results were provisionally classified from repository identity and GitHub search context as `skill_tooling`; only the ten new identities changed canonical classification totals. Repository IDs, default branches, sizes, archived flags, result ordering, classifications, eligibility, and verification notes are stored in [`batches/agent-skills-registry-page-13.json`](batches/agent-skills-registry-page-13.json).

## Classification totals

| Classification | Count | Index-stage meaning |
| --- | ---: | --- |
| `specification` | 163 | Identity strongly indicates a Skill specification, standard, or normative guidance. |
| `skill_collection` | 611 | Identity indicates a collection or examples of Skills. |
| `single_skill_or_domain_package` | 104 | Identity indicates one Skill or a domain-focused package. |
| `awesome_index` | 38 | Identity indicates a curated Skill index. |
| `skill_tooling` | 637 | Identity indicates validation, linting, evaluation, testing, packaging, discovery, registry, marketplace, management, benchmark, SDK, template, fixture, or runtime tooling. |
| `adjacent_search_hit` | 152 | Related to agents or Skills, but not clearly a Skill repository from identity alone. |
| `unclear_search_hit` | 262 | Identity is insufficient for reliable classification. |

## Evidence boundary

This remains an index-only catalog. GitHub repository search verified repository identities and accessibility. Classifications are provisional from repository identity and search context only. No repository README, `SKILL.md`, scripts, references, eval contents, stars, quality, or implementation behavior was assessed.

## Validation

- Previous canonical manifest commit: `7bb31f0016954ba596e8c43fbc0d2895c8ed7747` (`1957` repositories).
- `agent skills registry` page-13 batch commit: `17c726f7d8d6faf559a6ca2a6f26993beee75b82`.
- Composed latest-manifest commit: `05e7d46c24842c9ed3cbcc621ec8d16dd2743bd6`.
- `1957 + 10 = 1967` current unique repositories.
- `2093 - 126 = 1967` raw-to-unique reconciliation.
- Classification totals resolve to `1967`.
- `1553 + 414 = 1967`, matching the eligible and held partitions.
- Next index boundary: `"agent skills registry" in:name,description`, page `14`, `per_page=20`.
- No README, `SKILL.md`, scripts, references, eval contents, stars, or implementation contents were read during this index-only run.
