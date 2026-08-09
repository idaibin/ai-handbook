# Workflows Index Run — agent-workflow first partition

- run_id: `workflows-index-20260809T053108Z`
- observed_at: `2026-08-09T05:31:08Z`
- query: `agent workflow automation stars:>=1000`
- authority_basis: `idaibin/ai-handbook@bbe085490398f64c0028f4352933038cfa47f41d`
- evidence_level: `metadata_verified`

## Pagination evidence

| Page | Per page | Returned |
| ---: | ---: | ---: |
| 1 | 100 | 26 |
| 2 | 100 | 0 |

GitHub Search reported `total_count=26` and `incomplete_results=false`. The first empty page is the deterministic terminal condition, so pages 3–10 were not fabricated or requested.

## Reconciliation

| Result | Count |
| --- | ---: |
| Search hits | 26 |
| Normalized unique identities | 26 |
| Case-insensitive duplicates | 0 |
| Eligible | 13 |
| Held | 7 |
| Rejected | 6 |

All 26 identities are public, non-fork and non-archived according to the observed Search metadata. Each record also has an independently resolved default-branch HEAD commit.

### Eligible queue

- `activepieces/activepieces`
- `HKUDS/nanobot`
- `patched-codes/patchwork`
- `triggerdotdev/trigger.dev`
- `lucaswalter/n8n-ai-automations`
- `darrenhinde/OpenAgentsControl`
- `hexabot-ai/Hexabot`
- `nanobrowser/nanobrowser`
- `enescingoz/awesome-n8n-templates`
- `golutra/golutra`
- `langgenius/dify`
- `moazbuilds/CodeMachine-CLI`
- `skalesapp/skales`

### Held for content qualification

- `muesli/beehive`: generic event automation; current AI-workflow fit is not established.
- `Forward-Future/loopy`: agent-loop library and Skill; end-to-end workflow needs content review.
- `keinsaasforever/better-chatbot`: product claim without an identified workflow definition.
- `waooAI/waoowaoo`: vertical product; reusable workflow assets are not established.
- `LING71671/open-reverselab`: workflow inputs, outputs and entry are unclear.
- `ghostwright/ghost-os`: recipes/workflows need executable and state evidence.
- `cloudposse/atmos`: infrastructure runtime; AI workflow boundary needs content review.

### Rejected from Workflow topic

- `martinrusev/imbox`: IMAP library used by workflows.
- `softaworks/agent-toolkit`: Skills-first repository.
- `ATH-MaaS/ComfyUI-Copilot`: single workflow-enhancing node.
- `pipeshub-ai/pipeshub-ai`: context/RAG layer used by workflows.
- `firerpa/lamda`: device-control and automation API platform.
- `refly-ai/refly`: Agent Skills builder.

## Published snapshot

`workflows-agent-workflow-20260809T053108Z` contains only the 13 eligible identities. Every candidate is fixed to the observed default-branch HEAD, but no README, workflow definition, source tree, test, build, or runtime behavior was inspected. The snapshot is therefore eligible for deep-analysis claiming, not evidence that any repository implements its advertised behavior.

## Next shard

`ai-evaluation-workflow:first-partition`
