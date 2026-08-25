import {
  compileFlux,
  compileGemini,
  compileMidjourney,
  renderToken,
} from "./adapters.js";
import type {
  CompileInput,
  CompileResult,
  Polarity,
  SemanticTraceEntry,
  VisualContract,
} from "./types.js";

function add(
  trace: SemanticTraceEntry[],
  path: string,
  value: string | undefined,
  polarity: Polarity = "positive",
): void {
  if (!value) return;
  trace.push({ path, value, rendered: renderToken(value), polarity });
}

function addMany(
  trace: SemanticTraceEntry[],
  path: string,
  values: string[] | undefined,
  polarity: Polarity = "positive",
): void {
  for (const value of values ?? []) add(trace, path, value, polarity);
}

function textPolicyControl(contract: VisualContract): string {
  switch (contract.constraints.text_policy) {
    case "none":
      return "no_text";
    case "reserved_space":
      return "clear_text_reserve_without_rendered_lettering";
    case "placeholder":
      return "placeholder_labels_without_brand_copy";
    case "exact":
      return "exact_text_only_when_explicitly_supplied";
  }
}

function policyNegatives(contract: VisualContract): string[] {
  switch (contract.constraints.text_policy) {
    case "none":
      return ["readable_text", "logos", "watermarks"];
    case "reserved_space":
      return ["garbled_text", "rendered_headline", "watermarks"];
    case "placeholder":
      return ["garbled_typography", "brand_logos", "watermarks"];
    case "exact":
      return ["misspelled_text", "extra_text", "watermarks"];
  }
}

export function buildSemanticTrace(contract: VisualContract): SemanticTraceEntry[] {
  const trace: SemanticTraceEntry[] = [];

  add(trace, "intent.domain", contract.intent.domain);
  add(trace, "intent.period", contract.intent.period);
  addMany(trace, "intent.mood", contract.intent.mood);
  addMany(trace, "intent.usage", contract.intent.usage);

  add(trace, "visual_language.realism", contract.visual_language.realism);
  addMany(trace, "visual_language.styles", contract.visual_language.styles);
  addMany(trace, "visual_language.palette", contract.visual_language.palette);
  addMany(trace, "visual_language.materials", contract.visual_language.materials);
  addMany(trace, "visual_language.textures", contract.visual_language.textures);
  addMany(trace, "visual_language.atmosphere", contract.visual_language.atmosphere);

  add(trace, "camera.shot", contract.camera?.shot);
  add(trace, "camera.lens", contract.camera?.lens);
  add(trace, "camera.angle", contract.camera?.angle);
  add(trace, "camera.depth_of_field", contract.camera?.depth_of_field);

  add(trace, "lighting.source", contract.lighting?.source);
  add(trace, "lighting.direction", contract.lighting?.direction);
  add(trace, "lighting.quality", contract.lighting?.quality);
  add(trace, "lighting.contrast", contract.lighting?.contrast);

  add(trace, "composition.layout", contract.composition.layout);
  add(trace, "composition.framing", contract.composition.framing);
  add(trace, "composition.hierarchy", contract.composition.hierarchy);
  add(trace, "composition.negative_space", contract.composition.negative_space);

  addMany(trace, "constraints.require", contract.constraints.require);
  addMany(trace, "constraints.avoid", contract.constraints.avoid, "negative");
  addMany(trace, "constraints.text_policy.avoid", policyNegatives(contract), "negative");
  add(
    trace,
    "constraints.text_policy.control",
    textPolicyControl(contract),
    "control",
  );

  add(trace, "defaults.output_medium", contract.defaults.output_medium);
  add(trace, "defaults.aspect_ratio", contract.defaults.aspect_ratio, "control");

  return trace;
}

function stableSignature(trace: SemanticTraceEntry[]): string {
  const canonical = trace
    .map((entry) => `${entry.polarity}:${entry.path}:${entry.value}`)
    .join("|");

  let hash = 0x811c9dc5;
  for (let index = 0; index < canonical.length; index += 1) {
    hash ^= canonical.charCodeAt(index);
    hash = Math.imul(hash, 0x01000193) >>> 0;
  }
  return `vlc-${hash.toString(16).padStart(8, "0")}`;
}

function assertCompileInput(input: CompileInput): void {
  if (!(["gemini", "flux", "midjourney"] as string[]).includes(input.target)) {
    throw new Error(`Unsupported target: ${String(input.target)}`);
  }
  if (input.contract.schema_version !== "0.1") {
    throw new Error(`Unsupported schema version: ${input.contract.schema_version}`);
  }
  if (input.subject.trim().length === 0) {
    throw new Error("Subject must not be empty");
  }
}

export function compilePrompt(input: CompileInput): CompileResult {
  assertCompileInput(input);
  const trace = buildSemanticTrace(input.contract);
  const signature = stableSignature(trace);
  const subject = input.subject.trim();

  switch (input.target) {
    case "gemini":
      return compileGemini(input.contract, subject, signature, trace);
    case "flux":
      return compileFlux(input.contract, subject, signature, trace);
    case "midjourney":
      return compileMidjourney(input.contract, subject, signature, trace);
  }
}
