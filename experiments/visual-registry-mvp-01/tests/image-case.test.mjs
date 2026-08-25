import assert from "node:assert/strict";
import { readFileSync, readdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { compilePrompt } from "../dist/prototype/compiler.js";
import { generateAllPromptSets } from "../prototype/image-case-demo.mjs";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const first = generateAllPromptSets(root);
const second = generateAllPromptSets(root);
assert.deepEqual(first, second, "image prompt sets are not deterministic");
assert.equal(first.length, 2);

const cases = new Map();
for (const file of readdirSync(join(root, "image-cases")).filter((name) => name.endsWith(".json"))) {
  const definition = JSON.parse(readFileSync(join(root, "image-cases", file), "utf8"));
  cases.set(definition.id, definition);
}

for (const promptSet of first) {
  const definition = cases.get(promptSet.case_id);
  assert.ok(definition);
  assert.equal(promptSet.status, "prompt_set_ready_image_generation_pending");
  assert.equal(promptSet.variants.length, 3);
  assert.deepEqual(
    promptSet.variants.map((variant) => variant.kind).sort(),
    ["contract_compiled", "manual_reference", "subject_only"],
  );
  assert.equal(new Set(promptSet.variants.map((variant) => variant.id)).size, 3);
  assert.equal(new Set(promptSet.variants.map((variant) => variant.prompt_sha256)).size, 3);
  assert.ok(promptSet.variants.every((variant) => variant.prompt.length > 0));
  assert.equal(promptSet.controls.same_provider_model, true);
  assert.equal(promptSet.controls.same_aspect_ratio, true);
  assert.equal(promptSet.controls.post_processing, "none");

  const contract = JSON.parse(
    readFileSync(join(root, "contracts", `${definition.contract_id.replaceAll("_", "-")}.json`), "utf8"),
  );
  const expected = compilePrompt({
    target: definition.target,
    subject: definition.subject,
    contract,
  });
  const compiled = promptSet.variants.find((variant) => variant.kind === "contract_compiled");
  assert.equal(compiled.prompt, expected.prompt);
  assert.equal(compiled.semantic_signature, expected.semantic_signature);
}

process.stdout.write(`${JSON.stringify({
  status: "passed",
  image_cases: first.length,
  prompt_variants: first.reduce((count, item) => count + item.variants.length, 0),
  planned_images: first.reduce((count, item) => count + item.variants.length * item.controls.images_per_variant, 0),
  checks: [
    "deterministic_prompt_sets",
    "abc_variant_contract",
    "distinct_prompt_hashes",
    "fixed_trial_controls",
    "compiler_variant_matches_compiler",
    "image_generation_status_not_overstated"
  ]
}, null, 2)}\n`);
