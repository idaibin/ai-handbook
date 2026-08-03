# AI capability clusters — completion audit (2026-08-03)

This is an evidence ledger, not a promotion decision.  It distinguishes fixed-source coverage, deterministic fixture results, and unverified runtime claims.  The three application-case runners and all six cluster fixture runners were re-executed twice during final verification; their regenerated `runs/*.json`, adjudications where applicable, and recorded hashes are described below.

## 1. Fixed primary-source coverage

The coverage contract is [README](../../sources/coverage/README.md), [manifest](../../sources/coverage/manifest.yaml), and [validator](../../sources/coverage/validate_coverage.py).  It declares 12 pinned primary-source IDs and three allowlisted `legacy-v1` batches:

| Source ID | Repository | pinned commit |
| --- | --- | --- |
| `openai-agents-python` | `openai/openai-agents-python` | `000a96b602889b00f7cfaa210c41e1a74be65272` |
| `langgraph` | `langchain-ai/langgraph` | `b2926a0ff9589c28c7e01fe7cdbb337b86d5a4b4` |
| `llama-index` | `run-llama/llama_index` | `c864fcfa2c1d1f987ccdbcdab7b18e395c01ba86` |
| `graphrag` | `microsoft/graphrag` | `14a00ad88fc33cf2b52f4f113f25807556f8e25e` |
| `mem0` | `mem0ai/mem0` | `760dca6f391277d79c3c7d2096c1bf1d037526c3` |
| `mcp-servers` | `modelcontextprotocol/servers` | `76d64c822f5125032f89eb71dbdb94e42b434821` |
| `composio` | `ComposioHQ/composio` | `f1c1aa5613c2464aa8a53420d2357617a4d8bf2f` |
| `deepeval` | `confident-ai/deepeval` | `0d100e37d4263f208488f3c13e15561bce3b694f` |
| `langfuse-langfuse` | `langfuse/langfuse` | `314804b5c68d42bc742505c7b2552298bfe0ca88` |
| `promptfoo-promptfoo` | `promptfoo/promptfoo` | `82ca3c24ec445cf1734face46042c187b659b954` |
| `openhands-openhands` | `OpenHands/OpenHands` | `2feab551c4c12130c126159e1a0bd56753e2968f` |
| `browser-use-browser-use` | `browser-use/browser-use` | `f0aa3a8bb03779c71a5aa262d389e3bfe6b77cdc` |

Batches: [`batch-agent-rag.yaml`](../../sources/coverage/batch-agent-rag.yaml), [`batch-memory-mcp-eval.yaml`](../../sources/coverage/batch-memory-mcp-eval.yaml), and [`batch-observe-coding.yaml`](../../sources/coverage/batch-observe-coding.yaml).

Local command executed during this audit:

```sh
python3 sources/coverage/validate_coverage.py \
  sources/coverage/batch-agent-rag.yaml \
  sources/coverage/batch-memory-mcp-eval.yaml \
  sources/coverage/batch-observe-coding.yaml
# coverage: batches=3 sources=12 records=60 read=60 not_found=0 incomplete=0
# coverage: schema_valid=yes coverage_complete=yes errors=0
```

Status: **locally verified** as 60/60 `read_at_fixed_commit` role records (five required roles per source), schema-valid and coverage-complete.  Current remote verification is **Not verified**: `validate_coverage.py --verify-remote` cannot connect to `api.github.com`.  Local coverage validates record structure and self-declared fixed identities, not GitHub path/blob/locator retrieval, upstream runtime, provider, or production behavior.

## 2. Level 3 knowledge IR ledger

All six are draft, selected `level_3`, and render `model` plus `framework`; none is a Skill.  Evidence counts are individual `evidence` entries in `principles`, `frameworks`, and `anti_patterns`.

| IR draft ID | Knowledge / artifact | Source-supported citations | Unverified inferences | Independently verified local observations |
| --- | --- | ---: | ---: | ---: |
| `agent-runtime-orchestration` | [knowledge](https://github.com/idaibin/knowledge-distillation/blob/main/examples/engineering/agent-runtime-orchestration/knowledge.yaml) / [framework](https://github.com/idaibin/knowledge-distillation/blob/main/examples/engineering/agent-runtime-orchestration/artifact/framework.md) | 8 | 2 | 1 |
| `rag-graphrag-decision` | [knowledge](https://github.com/idaibin/knowledge-distillation/blob/main/examples/engineering/rag-graphrag-decision/knowledge.yaml) / [framework](https://github.com/idaibin/knowledge-distillation/blob/main/examples/engineering/rag-graphrag-decision/artifact/framework.md) | 10 | 2 | 1 |
| `agent-memory-scope-lifecycle` | [knowledge](https://github.com/idaibin/knowledge-distillation/blob/main/examples/engineering/agent-memory-scope-lifecycle/knowledge.yaml) / [framework](https://github.com/idaibin/knowledge-distillation/blob/main/examples/engineering/agent-memory-scope-lifecycle/artifact/framework.md) | 11 | 2 | 1 |
| `mcp-tool-authorization-boundaries` | [knowledge](https://github.com/idaibin/knowledge-distillation/blob/main/examples/engineering/mcp-tool-authorization-boundaries/knowledge.yaml) / [framework](https://github.com/idaibin/knowledge-distillation/blob/main/examples/engineering/mcp-tool-authorization-boundaries/artifact/framework.md) | 3 | 12 | 1 |
| `evaluation-observability-contract` | [knowledge](https://github.com/idaibin/knowledge-distillation/blob/main/examples/engineering/evaluation-observability-contract/knowledge.yaml) / [framework](https://github.com/idaibin/knowledge-distillation/blob/main/examples/engineering/evaluation-observability-contract/artifact/framework.md) | 5 | 13 | 1 |
| `coding-browser-agent-boundaries` | [knowledge](https://github.com/idaibin/knowledge-distillation/blob/main/examples/engineering/coding-browser-agent-boundaries/knowledge.yaml) / [framework](https://github.com/idaibin/knowledge-distillation/blob/main/examples/engineering/coding-browser-agent-boundaries/artifact/framework.md) | 8 | 7 | 1 |
| **Total** | six Level 3 drafts | **45** | **38** | **6** |

The previously recorded locally executed IR checks all exited 0:

```sh
KNOWLEDGE_DISTILLATION_ROOT=/path/to/knowledge-distillation
for ir in agent-runtime-orchestration rag-graphrag-decision agent-memory-scope-lifecycle mcp-tool-authorization-boundaries evaluation-observability-contract coding-browser-agent-boundaries; do
  python3 "$KNOWLEDGE_DISTILLATION_ROOT/scripts/validate_ir.py" "$KNOWLEDGE_DISTILLATION_ROOT/examples/engineering/$ir/knowledge.yaml" || exit 1
done
# VALID: each file | level=level_3 | maturity=draft
```

`validate_ir.py` is a contract validator, not remote citation retrieval.  Therefore `source_supported` means the IR records a pinned source citation; it does not elevate any cited repository capability to a locally reproduced runtime fact.

## 3. Six fixed fixture experiments

Every command below is executable from the ai-handbook root.  All six cluster runners were re-executed twice during this audit; their SHA-256 values are from the regenerated stored runs.  “Oracle result” means the recorded treatment result satisfies that experiment's fixed JSON oracle and its documented negative checks, not a real service E2E.

| Cluster | Command / stored results | Oracle and negative checks | Current SHA-256 and key metrics |
| --- | --- | --- | --- |
| [runtime](agent-runtime-orchestration/README.md) | `cd experiments/ai-capability-clusters/agent-runtime-orchestration && python3 run_experiment.py` | `passed_oracle=true`; two fixed adverse paths: blocking gate and interrupt budget exhaustion (there is no separate numeric `negative_checks()` counter). | baseline `b222ad858f0d4f9521423475d270584ec41cb9090b921f31a709041819d1e0a9`; treatment `e69292f90a5810b5a19e2f66edfa56e07900fd040558621a67b5c205e50ee94d`. Treatment: final-state accuracy 1.0, duplicate effects 0, guardrail leaks 0, budget violations 0; baseline: 0.667, 1, 1, 0. |
| [RAG / GraphRAG](rag-graphrag/README.md) | `cd experiments/ai-capability-clusters/rag-graphrag && python3 run_experiment.py` | `passed_oracle=true`; one label-perturbation negative (`q-direct-acme`), and per-question expansion-budget closure. | baseline `47527ac8de3bbf9d93b99df590ed195ffdb8a218e960affb389896f2067f6888`; treatment `8965588dee0335c28e39729969490199cd76f9b3af98ec2789f0124850f5d505`. Treatment: graph/path recall 1.0 vs 0.0, direct accuracy 1.0 unchanged, expansion 1, cost 20 vs 19. |
| [memory](memory/README.md) | `cd experiments/ai-capability-clusters/memory && python3 run_experiment.py` | `passed_oracle=true`; 5 negative checks: orphan fact, unclassified secret, cross-user source, queried-fact tamper, oracle sensitive-key tamper. | baseline `5e95e63482a181efe20009cc0d5f6bf9dff35137c0fb8b62c897c4d42f63f13f`; treatment `274041d7d308c82f9d5c32551a2e632f8894625bc69f25d78dac4bbfed0f778f`. Treatment P/R 1.0/1.0, query-scope leaks 0/6, secret retention 0, 28 token units; baseline P/R 0.167/0.167, leaks 2/6, secret retention 2, 65 token units. |
| [MCP tools](mcp-tools/README.md) | `cd experiments/ai-capability-clusters/mcp-tools && python3 run_experiment.py` | Script validates treatment oracle and 7 negative receipt checks (skip revoke, reuse grant, receipt, registry-used, revoke-before, joint-postcondition, ghost grant); stored run has no `passed_oracle` field. | baseline `1fc1868772343d2e27788e7cf611fa17dd0a13cf9364c5e61cf70741a33ec52f`; treatment `38874556525b09a4faf68e2d441c4c8e3cb62b4385890ec684efaf384a57b3df`. Unauthorized blocked 0→2, postcondition accuracy 0→1, residual permission 1→0, false reject 0 in both. |
| [evaluation / observability](evaluation-observability/README.md) | `cd experiments/ai-capability-clusters/evaluation-observability && python3 run_experiment.py` | Script validates oracle plus 26 fail-closed axis/completeness tamper checks; stored run has no `passed_oracle` field. | baseline `61f013c7589899cc22dcf2a4f2010c3161e3c79518ea31967222c4a9d60491aa`; treatment `80b185220eb3bd57ed66db55fd4048c56b1db44eb1fdfcb79c648f5f48ffc2be`. Macro-F1 0.277777778→1.0; false pass 4→0; security masking 2→0; unknown recall 0→1. |
| [coding / browser agent](coding-browser-agent/README.md) | `cd experiments/ai-capability-clusters/coding-browser-agent && python3 run_experiment.py` | Script validates oracle plus 11 boundary/receipt checks.  Symlink/TOCTOU is explicitly outside this mock. | baseline `c1219ecbfb673bb5ea495b7f6d53bb44bdd703a07a7f5565fdaa51118bf23bdc`; treatment `e0cccaf14627f6b9676ce6a73330d6f3fe10b5d1f5eaff5138fe70ee64eed2a9`. Out-of-bounds 2→0; no-evidence completion 1→0; attempted/executed 8/8→8/5; recovery 0→1. |

All six experiments are limited to their stated Python-stdlib mock or JSON/fixture bases; none proves a real provider, runtime, RAG index, memory store, MCP connection, evaluator/telemetry backend, browser, filesystem, or production deployment.

## 4. Three application-case ledger

| Case | Command and basis / oracle check | Baseline TP/FP/FN; P/R/F1 | Treatment TP/FP/FN; P/R/F1 |
| --- | --- | --- | --- |
| [01 RustZen navigation audit](applications/case-01-rustzen-navigation-audit/README.md) | Re-executed twice: `cd experiments/ai-capability-clusters/applications/case-01-rustzen-navigation-audit && RUSTZEN_ADMIN_REPO=/path/to/rustzen-admin python3 run_experiment.py`; `oracle_pass=true`, frozen commit and all target paths read. Treatment enumerates fixed-scope candidates by parsing route groups and exact capability-map frontend-route ownership. `missing_mapping_decoy=/system/status` is in routes but absent from the map; `scope_external=/manage/task` is in both but outside target scope; neither produces an FP. Synthetic injection of the decoy mapping and removal of the external mapping each fail their parser check. Oracle `4522c7...01685`; browser/visual `not_verified`. | 0/0/3; 0/0/0 | 3/0/0; 1/1/1 |
| [02 source coverage audit](applications/case-02-source-coverage-audit/README.md) | Re-executed twice: `cd experiments/ai-capability-clusters/applications/case-02-source-coverage-audit && python3 run_experiment.py`; stored adjudication: `oracle_pass=true`, validator exit 0, errors 0, counts match; remote `Not verified`. | 0/12/60; 0/0/0 | 60/0/0; 1/1/1 |
| [03 isolated knowledge patch](applications/case-03-isolated-knowledge-patch/README.md) | Re-executed twice: `cd experiments/ai-capability-clusters/applications/case-03-isolated-knowledge-patch && KNOWLEDGE_DISTILLATION_ROOT=/path/to/knowledge-distillation python3 run_experiment.py`; `oracle_pass=true`, source unchanged, target-only diff, validator exit 0, no residual permissions. Fail-closed canonical containment requires `workspace/input/knowledge.yaml`; sibling, absolute, `..`, and symlink targets return nonzero before write/delete. Oracle `887799...26634`. | 0/0/5; 0/0/0 | 5/0/0; 1/1/1 |

Current stored run hashes, in the same order (baseline; treatment):

1. Case 01: `ace3fcead3a34e37ec99eec587cf0dd98099b57228892ff038aeb141a0965657`; `76da205325c91967b297977373cdf4c01cfb042adfc9700ce50dfb83396fcdf4`.
2. Case 02: `abb517d2879c27459850003ba76982649e8dc94b0e417f60126c0c14fc688083`; `1d2176eda38b0f002ba4b870f49e5ba11d6a0d89d01aa16f47e17a36aebf223c`.
3. Case 03: `7840d889d2eb6795b7113ed83561dd7bdfc94d6ec35f2979e69a08769464f014`; `7973bc226ec8d2164b389bea7c623d2177c2dbdfee00f681b54eee616c8f5fca`.

## 5. Skill gate and final-review ledger

The authoritative gate record is [the 2026-08-03 assessment](https://github.com/idaibin/knowledge-distillation/blob/main/skill-feedback/2026-08-03-ai-knowledge-engineering-v1-skill-gate-assessment.md).  Status: **no-promotion**.  The three positive paired lifts are recorded above, but the required independent frozen negative-boundary case is absent.  Consequently no Skill is installed or published; the Level 3 drafts remain framework/experiment material.

| Review priority | Status | Evidence-bounded disposition |
| --- | --- | --- |
| P0 — local evidence integrity | **verified** | Coverage validator passed (12 sources, 3 batches, 60/60 records); all six IR validators were previously recorded as passing; the three application adjudications were regenerated once and identify their oracle checks. |
| P1 — deterministic fixed-basis treatment evidence | **verified** | The three application runners were freshly executed twice against their fixed bases; resulting runs, summaries, oracles, adjudications, and SHA-256 values are mutually described by their case documentation. |
| P2 — promotion/generalization/runtime acceptance | **pending** | Independent treatment negative boundary, cross-repository reproduction, and live-environment evidence are absent; no promotion may be inferred. |

Explicit **Not verified**: real provider/model behavior; real agent/runtime orchestration; remote fixed-commit path/blob/locator validation; real RAG/GraphRAG retrieval; real memory isolation/classification; real MCP protocol, identity, concurrency, or audit chain; evaluator/telemetry backend; browser/DOM/network/filesystem behavior; symlink and TOCTOU resistance; production deployment; browser visual/permission behavior; cross-application and cross-repository generalization.

## 6. Workspace boundary

This audit is scoped to the ai-handbook repository.  knowledge-distillation is an external dependency: its tracked state and assets are not modified by these runners, and its published links are used for cross-repository references.  This update re-executed all six cluster runners plus the three scoped application runners and synchronized this audit; no destructive action, commit, publication, or installation was performed.

## Audit validation

After writing this file, validate its relative links/path tokens and whitespace with:

```sh
python3 -c 'from pathlib import Path; import re; p=Path("experiments/ai-capability-clusters/completion-audit-2026-08-03.md"); missing=[x for x in re.findall(r"\]\(([^)#]+)", p.read_text()) if "://" not in x and not (p.parent / x).exists()]; print("missing links:", missing); raise SystemExit(bool(missing))'
git diff --no-index --check /dev/null experiments/ai-capability-clusters/completion-audit-2026-08-03.md
```
