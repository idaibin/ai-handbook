import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const path = join(root, "prompt-cases", "anthropomorphic-watercolor-cat-librarian-v01.json");
const promptCase = JSON.parse(readFileSync(path, "utf8"));

const promptSha = createHash("sha256").update(promptCase.prompt_text, "utf8").digest("hex");
assert.equal(promptSha, promptCase.prompt_sha256);
assert.equal(promptCase.metadata.status, "generation_blocked");
assert.equal(promptCase.generation_batches.length, 1);

const batch = promptCase.generation_batches[0];
assert.equal(batch.status, "blocked");
assert.equal(batch.requested_count, 4);
assert.equal(batch.results.length, 4);
assert.equal(batch.prompt_sha256, promptCase.prompt_sha256);
assert.equal(batch.parameters.independent_files_required, true);
assert.equal(batch.parameters.contact_sheet_is_result, false);
assert.equal(batch.failure.type, "output_shape_violation");
assert.equal(batch.failure.attempt_evidence.filter((item) => item.outcome === "combined_output").length, 3);
assert.equal(batch.failure.attempt_evidence.filter((item) => item.outcome === "http_error").length, 1);

for (const [index, result] of batch.results.entries()) {
  const sequence = index + 1;
  assert.equal(result.sequence, sequence);
  assert.equal(result.result_id, `${promptCase.prompt_id}__r${String(sequence).padStart(2, "0")}`);
  assert.equal(result.status, "pending");
  assert.equal(result.source_kind, "none");
  assert.equal(result.provider_receipt, null);
  assert.equal(result.drive_file_id, null);
  assert.equal(result.image_sha256, null);
  assert.equal(result.width, null);
  assert.equal(result.height, null);
}

process.stdout.write(`${JSON.stringify({
  status: "passed",
  prompt_id: promptCase.prompt_id,
  prompt_sha256: promptCase.prompt_sha256,
  batch_id: batch.batch_id,
  batch_status: batch.status,
  requested_count: batch.requested_count,
  saved_provider_native_images: 0,
  pending_result_identities: batch.results.map((result) => result.result_id),
  invalid_generation_attempts: batch.failure.attempt_evidence.length,
  checks: [
    "prompt_hash_matches",
    "generation_batch_present",
    "one_prompt_to_four_result_identities",
    "combined_outputs_not_counted",
    "provider_native_evidence_absent",
    "blocked_failure_evidence_recorded"
  ]
}, null, 2)}\n`);
