# Workflows Index Run — coding-agent-pipeline first partition

- run_id: `workflows-index-20260809T155200Z`
- observed_at: `2026-08-09T15:52:00Z`
- query: `coding agent pipeline stars:>=1000`
- authority_basis: `idaibin/ai-handbook@4f8e9c2208a4a4a0d0140f41e3c3a7cb57171022`
- evidence_level: `metadata_verified`

## Pagination evidence

| Page | Per page | Returned |
| ---: | ---: | ---: |
| 1 | 100 | 6 |
| 2 | 100 | 0 |

The first empty page is the deterministic terminal condition. Pages 3–10 were not requested or fabricated.

## Reconciliation

| Result | Count |
| --- | ---: |
| Search hits | 6 |
| Normalized unique identities | 6 |
| Duplicates against canonical index | 0 |
| Eligible | 5 |
| Held | 0 |
| Rejected | 1 |

The search query establishes the configured `stars:>=1000` floor. The connector projection did not expose exact star/fork/open-issue counts or all fork/disabled/license fields; unsupported values remain null. Descriptions are explicitly synthesized from bounded root README evidence.

### Eligible queue additions

- `calesthio/OpenMontage`: coding-agent-driven production pipeline with persisted stages and approval gates.
- `alibaba/open-code-review`: AI code-review CLI with diff/file inputs and structured findings.
- `rocketride-org/rocketride-server`: portable AI pipeline builder and runtime.
- `slothflowlabs/duckle`: AI-assisted executable data pipeline DAG with headless validation.
- `open-mercato/open-mercato`: architecture-aware AI coding harness with specs and tests.

### Rejected

- `zubair-trabzada/ai-sales-team-claude`: executable sales workflow, but its primary artifact is sales intelligence rather than AI engineering/coding/research-evaluation/delivery.

## Published snapshot

`workflows-coding-agent-pipeline-20260809T155200Z` contains five pending candidates fixed to default-branch HEAD commits. No implementation, test, build or runtime behavior was validated by this index batch.

## Next shard

`agent-workflow:second-partition`
