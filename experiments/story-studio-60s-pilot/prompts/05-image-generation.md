# Prompt Template: Image Generation & Consistency Anchoring

## Purpose
Generate provider-neutral image production requests with negative constraints,
reference requirements and review fields for each storyboard shot.

## Input Contract
- `shot_entry`: Individual shot metadata from Stage 04
- `character_bible`: Fixed visual descriptors and color palette
- `world_bible`: Environmental lighting and rendering style
- `generation_adapter_contract`: selected tool/model capability, version, rights and reproducibility fields

## Prompt Template

```text
You are an image-production prompt engineer for character-consistent cinematic storytelling.

Generate the exact image generation prompts for the following shot:

[SHOT METADATA]
{{shot_entry}}

[CONSISTENCY ANCHORS]
{{character_bible}}
{{world_bible}}

[PROMPT GENERATION RULES]
1. Positive Prompt Construction:
   [Subject & Character Tokens] + [Pose, Action, Emotion] + [Wardrobe & Distinctive Props] + [Environment & Setting Detail] + [Camera Lens, Angle, Framing 9:16 vertical] + [Lighting Scheme & Color Palette] + [Cinematic Texture & Render Style Tokens]
2. Reproducibility & Reference Parameters:
   Specify only parameters supported by `{{generation_adapter_contract}}`, plus input
   reference hashes, rights status and 9:16 dimensions. Do not invent a seed or
   provider-specific flag before an adapter is selected.
3. Negative Prompt:
   List mandatory exclusions (e.g., distorted hands, extra limbs, cartoonish blur, inconsistent face, oversaturated HDR, bad text).
4. Frame Variant Strategy:
   Provide 2 prompt variants:
   - Variant A: Primary keyframe (Starting state of shot)
   - Variant B: Secondary keyframe (Ending state of shot for interpolation/control)

[OUTPUT FORMAT]
Structured production request per shot with positive/negative prompts, adapter fields,
attempt metadata, expected PNG outputs, hashes/probes and required review checks.
```
