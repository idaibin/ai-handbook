# Forgeway + Skills TypeScript — Local Runtime Validation Handoff

Status: `paused_for_local_runtime_validation`  
Task identifier: `TASK — Forgeway + Skills — TypeScript 能力建设`  
Task key: `ai-engineering-lab/forgeway-skills/typescript-capability`  
Recorded date: `2026-08-20`

## Conclusion

The implementation and delivery are complete. Repository gates, dependency security,
cross-repository capability alignment, the TypeScript task Oracle, Harness contracts,
and synthetic isolation fixtures have passed.

The remaining evidence requires a runtime with Docker, Harbor, Codex, and an already
approved authentication route. The current remote execution container has no `docker`,
`harbor`, or `codex` executable. The user declined creation of a new OpenAI API key, so
remaining runtime validation is handed off to the local environment.

No authenticated Harbor + Codex Trial and no real-task A/B/C effectiveness Trial have
run. Do not claim that Skills or Forgeway improve real-repository resolution rates.

## Fixed delivered basis

| Source | Ref | Status |
| --- | --- | --- |
| `idaibin/skills` | `main@0d6039345d646c4d4795da7de22aa9b257930a59` | delivered and read back |
| `idaibin/skills` delivery branch | `codex/dev-typescript@463b8000afed61650fe242aa59758ca7f7460430` | retained |
| Skills index | blob `92b493268110117f7beaa6e80765f403bd37eab1` | aligned |
| `idaibin/forgeway` | `main@6dcd835f6fe4fe5e5b4e1dca30975b841c1ccd75` | delivered and read back |
| `idaibin/forgeway` delivery branch | `codex/typed-stage-registry@6dcd835f6fe4fe5e5b4e1dca30975b841c1ccd75` | retained |
| Approved protocol | `idaibin/ai-handbook@772139f2f7fe45289163765ff1d2418ef967f8ab` | approved basis |
| Harbor | `harbor-framework/harbor@c3ce0c60bbd2fd1888b327efcc880dbd86d8b7cf` | candidate runtime basis |
| Harbor version | `0.21.0` | fixed |
| Codex CLI contract | `0.147.0` | contract validated, live auth not validated |

## Verified evidence

### Skills

- Full gate: `pass`.
- Packages: `17`.
- Routing: `56/56`.
- Final integrated tests: `337`.
- Evidence branch: `validation/dev-typescript-full-gate-20260820`.
- Result: `.validation/results/dev-typescript-full-gate.json`.
- Log SHA-256: `e65c79c229e667cb1b92a7e591e6af9617c5ec2ca2b272d4ab0c6f64d73c4f46`.

### Forgeway

- `npm ci`, `npm audit`, `npm test`, strict typecheck, typed Stage Registry,
  workflow-stage, brownfield canary and Skills alignment: `pass`.
- Schemas: `17`; validation cases: `79`; workflow-stage cases: `27`.
- Dependency versions: `ajv=8.20.0`, `yaml=2.9.0`.
- Recorded audit vulnerabilities: `0`.
- Full-gate branch: `validation/typed-stage-registry-full-gate-20260820`.
- Delivery receipt branch: `validation/typed-stage-registry-final-integration-20260820`.
- Delivery receipt: `.validation/delivery-receipts/forgeway-skills-typescript-delivery-20260820.json`.

### TypeScript Oracle

- Task: `phase0-ts-darkreader-7238`.
- Repository: `darkreader/darkreader`.
- Issue: `#7238`; reference PR: `#7241`.
- Base: `991883df4d5910851130e3dc0e21fcbce604ea7d`.
- Base full suite: `3/3`; reference full suite: `3/3`.
- Role: Phase 0 infrastructure smoke only.
- Phase 1 effectiveness candidate: `false`.
- Evidence branch: `validation/paired-eval-phase0-typescript-preflight-20260820`.

### Harness contract

- Candidate branch: `agent/paired-eval-phase0-harness-contract-20260820`.
- Source commit: `f7fe2e774b6486106abd9b589bacc3d06e8b3432`.
- Frozen Skill Bundle: `dev-typescript + repo-map`, 22 files, 80333 bytes.
- Bundle SHA-256: `bd733fed7ac51148f5b10c9ba5584a30b5635d348866bf162a2568457053f686`.
- A/B/C parity, accounting rejection rules, Patch sealing/replay, Agent capsule,
  and Verifier isolation passed at contract or synthetic-fixture level.

## Not verified

- Authenticated provider model identity.
- Live Harbor Trial receipts.
- Live Codex Skill reading or use.
- Live Forgeway decomposition, validation, retry and recovery.
- End-to-end Group C Token/cost conservation.
- Docker-level network/future-history isolation and separate Verifier non-disclosure.
- A→B or B→C real-task effectiveness.
- Rust and Java Phase 0 Smoke tasks.

## Local validation order

1. Re-run the Skills canonical gate at the delivered `main` commit.
2. Re-run the Forgeway canonical gate and align it with the delivered Skills index.
3. Re-run the Harness contract preflight from
   `agent/paired-eval-phase0-harness-contract-20260820`.
4. Adapt and execute the sealed synthetic live-runtime probe from
   `agent/paired-eval-phase0-live-runtime-20260820` using the locally approved Codex
   authentication route.
5. Only after all live-runtime gates pass, decide whether to freeze Rust/Java Smoke
   tasks and authorize Phase 0.

The live-runtime candidate is a GitHub Actions-oriented script and currently checks
`OPENAI_API_KEY`. A local `auth.json` or `CODEX_AUTH_JSON_PATH` route requires a minimal
local adaptation. That adaptation creates a new unverified tree and must rerun all
applicable gates before its evidence is accepted.

## Stable execution record

Repository: `idaibin/forgeway`  
Branch: `validation/paired-eval-phase0-typescript-preflight-20260820`  
Path: `.validation/benchmark-preflight/phase-0/execution-record.json`  
Recording commit: `40bce6008d8fbe2bf6b0c580e29bdab95c6f58e4`

## Drive copies

- Local checkpoint: https://docs.google.com/document/d/1yvW1N1zPzAhThi1EwjHh6WIZ0_lEf7S8pnKbJ7GjghM/edit
- Final status and evidence index: https://docs.google.com/document/d/18mDBUuOIzWqrP7J9amVWsaCJdaDPQkFxKayDTBzI9Xo/edit
- Drive folder: `05_Forgeway/Delivery-Evidence`

## Stop boundary

Until live-runtime validation passes:

- do not claim real-repository effectiveness;
- do not promote `darkreader#7238` to Phase 1;
- do not expand to the 15-task Pilot;
- do not merge candidate Harness infrastructure to Forgeway `main`;
- do not delete delivery, Oracle, Harness or live-runtime evidence branches.
