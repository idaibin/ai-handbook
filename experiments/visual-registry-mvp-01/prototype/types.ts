export type Target = "gemini" | "flux" | "midjourney";
export type Polarity = "positive" | "negative" | "control";

export interface VisualContract {
  schema_version: "0.1";
  id: string;
  name: string;
  description: string;
  category: "narrative" | "interface" | "editorial";
  intent: {
    domain: string;
    period?: string;
    mood: string[];
    usage: string[];
  };
  visual_language: {
    realism: string;
    styles: string[];
    palette: string[];
    materials: string[];
    textures: string[];
    atmosphere: string[];
  };
  camera?: {
    shot?: string;
    lens?: string;
    angle?: string;
    depth_of_field?: string;
  };
  lighting?: {
    source?: string;
    direction?: string;
    quality?: string;
    contrast?: string;
  };
  composition: {
    layout: string;
    framing: string;
    hierarchy: string;
    negative_space: string;
  };
  constraints: {
    require: string[];
    avoid: string[];
    text_policy: "none" | "reserved_space" | "placeholder" | "exact";
  };
  defaults: {
    aspect_ratio: string;
    output_medium: string;
  };
  metadata: {
    status: "draft" | "golden_candidate" | "validated" | "deprecated";
    consumers: string[];
    provenance: "original_contract" | "adapted_contract";
  };
}

export interface SemanticTraceEntry {
  path: string;
  value: string;
  rendered: string;
  polarity: Polarity;
}

export interface CompileInput {
  target: Target;
  subject: string;
  contract: VisualContract;
}

export interface CompileResult {
  target: Target;
  contract_id: string;
  subject: string;
  prompt: string;
  negative_prompt?: string;
  parameters: Record<string, string | number | boolean>;
  semantic_signature: string;
  trace: SemanticTraceEntry[];
}
