import { createHash } from "node:crypto";
import { readFileSync, readdirSync } from "node:fs";
import { join } from "node:path";
import { compilePrompt } from "../dist/prototype/compiler.js";

function readJson(path) {
  return JSON.parse(readFileSync(path, "utf8"));
}

function sha256(value) {
  return createHash("sha256").update(value).digest("hex");
}

export function buildPromptSet(definition, contract) {
  if (definition.contract_id !== contract.id) {
    throw new Error(`Case ${definition.id} references ${definition.contract_id}, got ${contract.id}`);
  }

  const variants = definition.variants.map((variant) => {
    if (variant.kind === "subject_only") {
      const prompt = definition.subject;
      return {
        id: variant.id,
        kind: variant.kind,
        label: variant.label,
        prompt,
        prompt_sha256: sha256(prompt),
      };
    }

    if (variant.kind === "manual_reference") {
      const prompt = variant.prompt.trim();
      return {
        id: variant.id,
        kind: variant.kind,
        label: variant.label,
        prompt,
        prompt_sha256: sha256(prompt),
      };
    }

    if (variant.kind === "contract_compiled") {
      const compiled = compilePrompt({
        target: definition.target,
        subject: definition.subject,
        contract,
      });
      const fingerprintInput = JSON.stringify({
        prompt: compiled.prompt,
        negative_prompt: compiled.negative_prompt ?? null,
        parameters: compiled.parameters,
      });
      return {
        id: variant.id,
        kind: variant.kind,
        label: variant.label,
        prompt: compiled.prompt,
        negative_prompt: compiled.negative_prompt ?? null,
        parameters: compiled.parameters,
        semantic_signature: compiled.semantic_signature,
        prompt_sha256: sha256(fingerprintInput),
      };
    }

    throw new Error(`Unsupported prompt variant kind: ${variant.kind}`);
  });

  return {
    case_id: definition.id,
    contract_id: definition.contract_id,
    consumer: definition.consumer,
    target: definition.target,
    subject: definition.subject,
    comparison_axis: definition.comparison_axis,
    controls: definition.controls,
    review: definition.review,
    status: "prompt_set_ready_image_generation_pending",
    variants,
  };
}

export function generateAllPromptSets(root) {
  const contracts = new Map();
  for (const file of readdirSync(join(root, "contracts")).filter((name) => name.endsWith(".json")).sort()) {
    const contract = readJson(join(root, "contracts", file));
    contracts.set(contract.id, contract);
  }

  const promptSets = [];
  for (const file of readdirSync(join(root, "image-cases")).filter((name) => name.endsWith(".json")).sort()) {
    const definition = readJson(join(root, "image-cases", file));
    const contract = contracts.get(definition.contract_id);
    if (!contract) throw new Error(`Missing contract ${definition.contract_id} for ${definition.id}`);
    promptSets.push(buildPromptSet(definition, contract));
  }

  return promptSets;
}
