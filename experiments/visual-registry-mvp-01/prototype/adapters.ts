import type {
  CompileResult,
  SemanticTraceEntry,
  Target,
  VisualContract,
} from "./types.js";

const LABELS: Record<string, string> = {
  eastern_han: "Eastern Han dynasty",
  "50mm": "50mm lens",
  eye_level: "eye-level camera",
  low_to_medium: "low-to-medium contrast",
  side_window_daylight: "soft daylight from a side window",
  left_to_right: "left-to-right light direction",
  direct_front_interface: "direct frontal interface view",
  high_contrast_text: "high-contrast interface typography",
  low_saturation_orange_red: "low-saturation orange-red accent",
  title_zone_then_symbol: "title reserve first, then one focal symbol",
  no_text: "no rendered text",
  desktop_ui_mockup: "desktop UI mockup",
  ui_spec_exploration: "UI spec exploration",
  minimal_data_ui: "minimal data UI",
  modern_saas: "modern SaaS",
  historically_plausible_eastern_han: "historically plausible Eastern Han details",
};

export function renderToken(value: string): string {
  return LABELS[value] ?? value.replaceAll("_", " ");
}

function sentenceList(values: string[]): string {
  if (values.length === 0) return "";
  if (values.length === 1) return values[0];
  if (values.length === 2) return `${values[0]} and ${values[1]}`;
  return `${values.slice(0, -1).join(", ")}, and ${values.at(-1)}`;
}

function renderedByPrefix(
  trace: SemanticTraceEntry[],
  prefix: string,
  polarity: SemanticTraceEntry["polarity"] = "positive",
): string[] {
  return trace
    .filter((entry) => entry.path.startsWith(prefix) && entry.polarity === polarity)
    .map((entry) => entry.rendered);
}

function unique(values: string[]): string[] {
  return [...new Set(values)];
}

function positiveTerms(trace: SemanticTraceEntry[]): string[] {
  return unique(
    trace
      .filter((entry) => entry.polarity === "positive")
      .map((entry) => entry.rendered),
  );
}

function negativeTerms(trace: SemanticTraceEntry[]): string[] {
  return unique(
    trace
      .filter((entry) => entry.polarity === "negative")
      .map((entry) => entry.rendered),
  );
}

function outputParameters(contract: VisualContract): Record<string, string> {
  return {
    aspect_ratio: contract.defaults.aspect_ratio,
    output_medium: renderToken(contract.defaults.output_medium),
  };
}

function baseResult(
  target: Target,
  contract: VisualContract,
  subject: string,
  semanticSignature: string,
  trace: SemanticTraceEntry[],
): Omit<CompileResult, "prompt"> {
  return {
    target,
    contract_id: contract.id,
    subject,
    parameters: outputParameters(contract),
    semantic_signature: semanticSignature,
    trace,
  };
}

export function compileGemini(
  contract: VisualContract,
  subject: string,
  semanticSignature: string,
  trace: SemanticTraceEntry[],
): CompileResult {
  const intent = renderedByPrefix(trace, "intent.");
  const language = renderedByPrefix(trace, "visual_language.");
  const camera = renderedByPrefix(trace, "camera.");
  const lighting = renderedByPrefix(trace, "lighting.");
  const composition = renderedByPrefix(trace, "composition.");
  const required = renderedByPrefix(trace, "constraints.require");
  const avoided = negativeTerms(trace);
  const textControl = renderedByPrefix(trace, "constraints.text_policy", "control");

  const sections = [
    `Produce a visual depiction of ${subject}.`,
    `Output medium: ${renderToken(contract.defaults.output_medium)}.`,
    `Visual intent: ${sentenceList(intent)}.`,
    `Visual language: ${sentenceList(language)}.`,
    camera.length > 0 ? `Camera: ${sentenceList(camera)}.` : "",
    lighting.length > 0 ? `Lighting: ${sentenceList(lighting)}.` : "",
    `Composition: ${sentenceList(composition)}.`,
    `Preserve: ${sentenceList(required)}.`,
    textControl.length > 0 ? `Text handling: ${sentenceList(textControl)}.` : "",
    `Avoid: ${sentenceList(avoided)}.`,
    `Use an aspect ratio of ${contract.defaults.aspect_ratio}.`,
  ].filter(Boolean);

  return {
    ...baseResult("gemini", contract, subject, semanticSignature, trace),
    prompt: sections.join(" "),
  };
}

export function compileFlux(
  contract: VisualContract,
  subject: string,
  semanticSignature: string,
  trace: SemanticTraceEntry[],
): CompileResult {
  const controls = renderedByPrefix(trace, "constraints.text_policy", "control");
  return {
    ...baseResult("flux", contract, subject, semanticSignature, trace),
    prompt: [subject, ...positiveTerms(trace), ...controls].join(", "),
    negative_prompt: negativeTerms(trace).join(", "),
  };
}

export function compileMidjourney(
  contract: VisualContract,
  subject: string,
  semanticSignature: string,
  trace: SemanticTraceEntry[],
): CompileResult {
  const controls = renderedByPrefix(trace, "constraints.text_policy", "control");
  const negative = negativeTerms(trace);
  const noClause = negative.length > 0 ? ` --no ${negative.join(", ")}` : "";
  const prompt = [subject, ...positiveTerms(trace), ...controls].join(", ");

  return {
    ...baseResult("midjourney", contract, subject, semanticSignature, trace),
    prompt: `${prompt} --ar ${contract.defaults.aspect_ratio} --style raw${noClause}`,
  };
}
