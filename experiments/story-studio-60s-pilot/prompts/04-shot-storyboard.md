# Prompt Template: Shot List & Storyboard Breakdown

## Purpose
Decompose the 60-second script into a granular, executable 10-12 shot storyboard list with camera movements, durations, and compositional blocking.

## Input Contract
- `script`: Timed 60s script from Stage 03
- `aspect_ratio`: 9:16 (Vertical)

## Prompt Template

```text
You are a cinematographer and storyboard director for high-octane AI vertical short-form productions.

Translate the following 60-second script into a structured Shot List & Storyboard specification:

[SCRIPT]
{{script}}

[REQUIREMENTS]
Breakdown the script into 10 to 12 precise visual shots. For each shot specify:

1. Shot ID: (e.g., SHOT_01 to SHOT_12)
2. Time Range & Duration: (e.g., 00:00 - 00:04, 4.0s)
3. Shot Size: (Extreme Close-Up [ECU], Close-Up [CU], Medium Close-Up [MCU], Medium Shot [MS], Wide Shot [WS])
4. Camera Angle & Lens: (Low Angle 24mm, Eye Level 50mm, High Angle Dutch Tilt 35mm, Macro 85mm)
5. Camera Movement: (Static, Slow Dolly-In, Whip Pan Right, Rapid Tracking Shot, Pedestal Up)
6. Subject & Action: Precise character blocking and movement in the 9:16 vertical frame
7. Lighting & Color Mood: Key light direction, fill, backlight, rim light color, background atmospheric depth
8. Continuity Anchor: Characters/props present and their required visual consistency anchors
9. Audio / Dialogue Sync: Corresponding dialogue line or SFX cue occurring during this shot

[OUTPUT FORMAT]
A markdown table followed by granular shot blocks suitable for image prompt generation.
```
