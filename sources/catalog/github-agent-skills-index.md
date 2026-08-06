# GitHub Agent Skills Repository Index

## Current verified batch

- Search query: `"agent skills" in:name,description`
- GitHub result pages covered: `1-10`
- Results per page: `10`
- Raw search hits: `100`
- Existing discovery-inbox candidates merged and re-verified: `4`
- Unique repositories after case-insensitive `owner/repository` deduplication: `104`
- Exact duplicates removed in this batch: `0`
- Provisionally eligible for later deep analysis: `79`
- Held as adjacent or unclear search hits: `25`

Machine-readable authority: [`github-agent-skills-index.json`](github-agent-skills-index.json).

## Classification counts

| Classification | Count | Meaning at index stage |
| --- | ---: | --- |
| `specification` | 1 | Repository identity strongly indicates a Skill specification. |
| `skill_collection` | 44 | Repository identity indicates a collection of Skills. |
| `single_skill_or_domain_package` | 18 | Repository identity indicates one Skill or a domain-focused package. |
| `awesome_index` | 10 | Repository identity indicates an index or curated collection. |
| `skill_tooling` | 6 | Repository identity indicates Skill discovery, validation, scanning, packaging, or runtime tooling. |
| `adjacent_search_hit` | 16 | Search hit is related to agents or tooling but is not clearly a Skill repository from identity alone. |
| `unclear_search_hit` | 9 | Repository identity is insufficient for reliable classification. |

## Evidence boundary

This was an index-only run. GitHub connector results verified that the repositories existed and were accessible during collection. No repository README, `SKILL.md`, scripts, references, evaluations, stars, quality, or implementation behavior was assessed. Classifications are therefore provisional and must not be treated as deep-analysis results.

## Validation

- The machine-readable catalog was written in commit `5513d718f323d284034805baf4bbd6fe7c42fbbf`.
- The committed file was fetched back from `main` after the write.
- Stored progress totals and category counts both resolve to `104` repositories.
- The next index run should merge by case-insensitive `owner/repository`, preserve all origins, and only add genuinely new repositories.
