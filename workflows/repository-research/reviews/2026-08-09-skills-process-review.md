# Skills Research Process Review — 2026-08-09

## Verified basis

- Active scheduled tasks were `Skills Index 50` at minute 50 and `Skills Catalog Research` at minute 00.
- The index has a frozen canonical count of 2502 and is staging the May 2026 created-date partition.
- Deep-analysis Batch 058 reports 580 repository identities, but ten identities collapse to three previously reviewed content trees and create zero new Skill reports.
- At the inspected main revision, `deep-analysis-latest.json` still pointed to Batch 057 while Batch 058 was already committed.
- Batch 058 counted ten zero-Star repository identities as completed structure reviews; this is valid identity coverage but not ten independent high-value Skill analyses.

## Findings and changes

| Problem | Impact | Applied change |
| --- | --- | --- |
| Long automation prompts duplicate mutable process rules | Prompt and repository method drift over time | Tasks now read one main-branch process and topic config |
| Repository count and unique content count are easy to conflate | Fork-heavy batches appear deeper than they are | Separate repository, content, reuse and new-report metrics |
| Latest pointer was not verified after write | Future runs can resume from stale state | Require post-commit main re-read and fail closed |
| A quota of ten can reward repeated low-value forks | Throughput can replace research value | Make ten an upper target; quality and evidence override quota |
| Retrospective did not require testing the prior change | “Self-improvement” can become unbounded prose | One change per batch with hypothesis, metric and rollback |
| Shared-state writes were not explicitly serialized | Parallel workers may overwrite queue/progress | Subagents return evidence only; main writer owns shared state |

## Method version decision

Adopt `repository-research v1.0`. Do not migrate historical artifacts. Existing Skills paths remain authoritative through the `skills.toml` topic adapter; Agents and Workflows start in separate roots to prevent scope contamination.
