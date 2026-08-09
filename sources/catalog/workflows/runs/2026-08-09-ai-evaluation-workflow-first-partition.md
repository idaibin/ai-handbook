# Workflows Index Run — ai-evaluation-workflow first partition

- run_id: `workflows-index-20260809T063604Z`
- observed_at: `2026-08-09T06:36:04Z`
- query: `AI evaluation workflow stars:>=1000`
- authority_basis: `idaibin/ai-handbook@14be7b4481ae708ea35ec908fdf18bfac6f2b22c`
- quota_gate: `quota_not_observable` (no first-party usage percentage was exposed to this run)
- evidence_level: `metadata_verified`

## Pagination evidence

| Page | Per page | Returned |
| ---: | ---: | ---: |
| 1 | 100 | 9 |
| 2 | 100 | 0 |

The first empty page is the deterministic terminal condition. Pages 3–10 were not requested or fabricated.

## Reconciliation

| Result | Count |
| --- | ---: |
| Search hits | 9 |
| Normalized unique identities | 9 |
| Duplicates against canonical index | 0 |
| Eligible | 7 |
| Held | 1 |
| Rejected | 1 |

All nine repositories passed the query's `stars:>=1000` floor and were observed as public, non-fork, non-archived repositories. Default-branch HEAD commits were independently resolved.

### Eligible queue additions

- `rpamis/comet`: agent skill harness explicitly producing evaluated workflows.
- `juanjuandog/FinSight-AI`: executable research agent with resilient workflow orchestration and RAG evaluation.
- `Ricky-7-Yan/intelligent-audit-system`: governed workflow, evaluation harness, human review and remediation delivery.
- `dataelement/bisheng`: executable GenAI workflow platform with evaluation and observability.
- `trpc-group/trpc-agent-go`: agent runtime with graph workflows, evaluation and observability.
- `EmbeddedLLM/JamAIBase`: executable spreadsheet pipelines and real-time LLM evaluation.
- `ray-r-ren/agent-apprenticeship`: CLI-driven workflow loops with mentor/human evaluation.

### Held

- `onestardao/WFGY`: public protocol, evidence and troubleshooting materials are present, but the README says deeper runtime/engine layers are staged for later release; a current executable workflow surface is not established by this index pass.

### Rejected

- `VoltAgent/awesome-ai-agent-papers`: curated paper index; topic rules explicitly exclude awesome lists without an executable workflow.

## Published snapshot

`workflows-ai-evaluation-workflow-20260809T063604Z` contains the three still-pending candidates from the prior snapshot plus seven newly eligible identities. Analyzed identities are not requeued. Candidate commits are fixed, but no implementation, tests, build or runtime behavior was validated by this index batch.

## Next shard

`coding-agent-pipeline:first-partition`
