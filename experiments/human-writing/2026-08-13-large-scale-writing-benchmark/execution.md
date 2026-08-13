# Benchmark execution contract

## Audit result

The original scaffold was not an executable benchmark runner. It could build task
plans, validate output files, create blind packets, validate judgments, and aggregate
scores, but it had no component that called a generation worker or persisted a
recoverable execution history. A plan's `pending_task_ids` therefore did not cause
any model work.

The minimum generation and development-loop gap is now implemented:

| Concern | Enforced by |
| --- | --- |
| exact Skill bytes and revision sent to the worker | `harness/dispatch.py` `skill-snapshots/v1` |
| real worker invocation | JSON stdin/stdout adapter subprocess, without a shell |
| immutable requests, responses, outputs, and receipts | `harness/artifact_store.py` |
| failure attempts and safe retry | append-only attempt refs; success ref is created once |
| resume | hash-verified success receipts are skipped, incomplete tasks are retried |
| Token and cost evidence | each receipt records exact usage/cost or explicit `null`; unknown is never converted to zero |
| adapter failure privacy | receipt stores only category, exit code, and stderr SHA-256; optional raw log is restricted and gitignored |
| exported `output` rows for blind packaging | `dispatch.export_outputs` / `--export-output` |
| Review before the next development wave | `harness/execution_state.py` |
| accepted `human-writing` revision used by the next wave | hash-verified execution state transition |

This is provider-neutral infrastructure, not evidence that any benchmark generation
has run. No production adapter, 1,200-case corpus, or judge workers are bundled. This
run may use only the current ChatGPT/Codex entitlement: paid APIs and paid human
review are outside scope. Until the remaining inputs exist, the large-scale result
remains unavailable.

## Generation adapter contract

Create the wave plan with `plan.py`, then supply a `skill-snapshots/v1` bundle whose
four entries contain the exact `SKILL.md` bytes and revision named by the plan. Run:

```bash
python harness/dispatch.py \
  --plan evidence/D01/plan.json \
  --cases evidence/D01/cases.jsonl \
  --snapshots evidence/D01/skill-snapshots.json \
  --store evidence/artifacts \
  --run-id D01 \
  --restricted-log-dir evidence/restricted-logs \
  --export-output evidence/D01/outputs.jsonl \
  --adapter /absolute/path/to/generation-adapter
```

The adapter reads one `generation-request/v1` JSON object from stdin. It returns one
JSON object with exactly:

```json
{
  "schema_version": "generation-response/v1",
  "task_id": "<request task_id>",
  "text": "<generated output>",
  "provider_request_id": "<provider receipt id or explicit local id>",
  "model_provider": "<frozen contract value>",
  "model_family": "<frozen contract value>",
  "model_revision": "<frozen contract value>",
  "usage": null,
  "cost": null
}
```

When exposed by the provider, `usage` must contain nonnegative `input_tokens`,
`output_tokens`, and their exact `total_tokens`; `cost` must contain `currency` and
nonnegative `amount`. Re-run the same command after interruption. Existing valid
success receipts are reused; they are never overwritten.

Adapter stderr is never copied into a receipt or the content-addressed store. When
`--restricted-log-dir` is supplied, raw stderr is written mode `0600` below the
gitignored `evidence/restricted-logs/` tree; otherwise it is discarded after its
SHA-256 is recorded. Adapter commands must receive credentials from their normal
secret environment, not argv or benchmark artifacts.

## Development-wave transition

Initialize once:

```bash
python harness/execution_state.py init --output evidence/execution-state-00.json
```

After all 480 outputs, deterministic gates, blind judgments, aggregation, and the 12
family reviews plus one global review are complete, advance one wave:

```bash
python harness/execution_state.py complete-dev \
  --state evidence/execution-state-00.json \
  --wave 1 \
  --cases evidence/D01/cases.jsonl \
  --plan evidence/D01/plan.json \
  --outputs evidence/D01/outputs.jsonl \
  --gate-report evidence/D01/gates.json \
  --bundle evidence/D01/blind-base \
  --aggregate evidence/D01/aggregate.json \
  --review evidence/D01/reviews.jsonl \
  --output evidence/execution-state-01.json
```

The transition reloads the mapping, all three packets, all three judgments, and the
gate report from `--bundle`, reruns aggregation, and compares the exact result and
input-evidence digest. A self-consistent but forged score file therefore cannot
advance the state. It also commits the plan, raw output hashes, gate report, and
blind/judge evidence together. The transition fails if any case, output, gate,
aggregate, review slice, revision, or hash is missing or inconsistent. Repeat for
D02-D08. Wave 8 freezes the candidate;
the existing `holdout.py` state machine then binds corpus commitment, candidate
revision, unlock, completion evidence, and final aggregation.

## Remaining execution prerequisites

The following are external work, not implemented results:

1. materialize and license-review all 1,200 cases;
2. create and verify the four exact Skill snapshot bundles;
3. configure a generation adapter and freeze its model contract;
4. dispatch three fresh anonymous judge contexts in the current environment and
   preserve their judgment files;
5. obtain the required blinded agent Review and adjudication artifacts;
6. persist large raw evidence as GitHub release assets or another content-addressed
   object store while keeping hashes and retrieval metadata in GitHub.

Do not open D02 until D01's state transition succeeds. Do not inspect or dispatch the
holdout until D08 has frozen the candidate and the holdout unlock transition succeeds.
