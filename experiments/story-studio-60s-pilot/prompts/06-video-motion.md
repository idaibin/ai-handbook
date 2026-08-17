# Prompt Template: Image-to-Video Motion Generation

## Purpose
Generate provider-neutral motion prompts, camera trajectories and dynamics for a
selected image-to-video adapter.

## Input Contract
- `shot_entry`: Shot timing and camera movement
- `start_frame`: Reference to approved keyframe image from Stage 05
- `end_frame`: Optional ending keyframe reference
- `video_adapter_contract`: selected engine capability/version, input/output and probe fields

## Prompt Template

```text
You are an AI Video Cinematographer and Image-to-Video Motion Director.

Generate the exact motion prompt and parameter configuration to animate the keyframe image into a coherent video shot:

[SHOT METADATA]
{{shot_entry}}

[KEYFRAME ASSET]
Start Frame Description: {{start_frame}}
Duration: {{shot_entry.duration}} seconds

[MOTION PROMPT RULES]
1. Camera Motion Descriptor:
   Specify exact camera movement direction, speed curve, and focal shift (e.g., "Slow steady camera dolly-in toward protagonist's eyes, background parallax motion subtle").
2. Subject Physical Dynamics:
   Specify micro-movements of the subject (e.g., "Character blinks once, chest heaves with heavy breathing, hair rustles slightly from ambient wind, pupils dilate").
3. Environmental Dynamics:
   Specify background physics (e.g., "Neon rain streaks down window pane in background, flickering neon sign reflections on wet pavement, steam slowly rising from street vent").
4. Adapter Controls:
   - Use only controls declared by `{{video_adapter_contract}}`.
   - Record approved input-image hash, duration, camera controls and negative motion constraints.
   - Require output clip hash, codec/duration/dimension probe and continuity review.

[OUTPUT FORMAT]
Structured video attempt request and evidence requirements per shot.
```
