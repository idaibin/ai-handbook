# Workflows deep analysis — workflows-deep-20260809T054129Z

Snapshot: `workflows-agent-workflow-20260809T053108Z` (`ready`, source commit `bbe085490398f64c0028f4352933038cfa47f41d`). Claim was written and re-read before repository access. This batch reviewed the first ten pending identities at their snapshot commits.

## Result

- Repositories reviewed: 10
- Unique contents reviewed: 10
- Analyses reused: 0
- New repository reports: 10
- Evidence: 9 `source_validated`; 1 `runtime_validated` for Hexabot core runner tests only
- Runtime boundary: no external service, production queue, browser, SCM mutation or third-party side effect was executed

| Repository | Subtype | Evidence | Topic decision | Central limitation |
| --- | --- | --- | --- | --- |
| activepieces/activepieces | durable workflow engine | source | strong fit | arbitrary piece effects are not universally exactly-once |
| HKUDS/nanobot | scheduled agent turn | source | fit | not a declarative multi-step DAG; delivery is at-least-once |
| patched-codes/patchwork | linear coding pipeline | source | fit | no durable checkpoint; partial Git/SCM effects may remain |
| triggerdotdev/trigger.dev | durable task runtime | source | strong fit | external task effects remain author-idempotent |
| lucaswalter/n8n-ai-automations | template collection | source | fit | no license, tests or runtime evidence |
| darrenhinde/OpenAgentsControl | prompt-orchestrated coding workflow | source | fit | approval text conflicts with evaluator bypass behavior |
| hexabot-ai/Hexabot | durable workflow engine | runtime, core tests | strong fit | real host persistence/effects not tested |
| nanobrowser/nanobrowser | in-memory agent loop | source | fit | no durable resume or code-enforced approval gate |
| enescingoz/awesome-n8n-templates | template collection | source | conditional fit | 8/334 JSON fail strict shape; per-template rights/safety vary |
| golutra/golutra | multi-agent dispatch orchestrator | source | partial fit | README custom-template/autonomous claims not found in fixed source |

## Cross-repository findings

1. **Durability and side-effect safety are separate properties.** Activepieces, Trigger.dev and Hexabot persist or reconstruct execution well, yet none can automatically make every external action exactly-once. The reusable design is to combine workflow state with action-specific idempotency keys, result recording and explicit compensation.
2. **Human-in-the-loop is often weaker than its label.** Activepieces and Trigger.dev expose explicit waitpoints. Several other candidates rely on prompt wording, free-text interpreted by an LLM, a debug pause or a user-operated pause button. Those mechanisms should not receive the same human-gate score.
3. **“Workflow” spans at least seven implementation subtypes.** Comparing a scheduler, prompt protocol, template pack and durable engine on one flat score hides their contracts. Reports therefore record a subtype without relaxing the shared evidence gate.
4. **Template collections need collection-level validation plus per-template risk review.** One collection had no license; the larger collection had five malformed and three multi-root JSON files, and included an unattended privileged SSH update path. Popularity and `active=true` are not safety evidence.
5. **README claims require fixed-source confirmation.** Golutra contains a durable dispatch outbox, but source search did not locate the advertised custom workflow import/export implementation; its month-long autonomous coordinator is explicitly future work.

## Reusable patterns

- Persisted outbox with lease, bounded backoff and dead state for dispatch.
- Explicit waitpoint token and authorized completion for human review.
- Replay drift detection plus recorded action results for deterministic resume.
- Stable idempotency keys carried from trigger through external APIs.
- Static collection gate: single-root parse, schema/shape lint, credential scan, active-state reset and high-impact side-effect review before import.

## Evidence boundary

Static source and checked-in tests were distinguished from executed behavior. Hexabot alone reached `runtime_validated`, narrowly scoped to 16 core runner suites / 144 passing tests under a slightly older-than-declared Node 24 runtime. Every report lists remaining runtime, credential, external-effect and license uncertainties.

Next queue candidate: `langgenius/dify@3f89a3c742e1ce64b2167f3fcf664947f2b7cf82`.
