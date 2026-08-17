# Prompt Template: World & Character Bible

## Purpose
Define the canonical world rules, environmental visual constraints, and multi-angle character anchors for AI visual generation consistency.

## Input Contract
- `story_positioning`: Output from Stage 01
- `character_roster`: List of key characters and roles

## Prompt Template

```text
You are a world-builder and character concept artist for an episodic AI micro-drama series.

Create the definitive World Bible and Character Bible based on the approved story positioning:

[INPUT POSITIONING]
{{story_positioning}}

[WORLD BIBLE REQUIREMENTS]
1. Setting & Atmosphere: Time period, technology level, architectural style, atmospheric conditions (lighting, weather, air quality).
2. Key World Rules: Three non-negotiable physical or societal rules governing the universe.
3. Visual Environment Anchors: Fixed aesthetic palette (primary color accents, ambient lighting hex codes, textural references).

[CHARACTER BIBLE REQUIREMENTS] (For each character: Protagonist, Antagonist, Key Supporting)
1. Identity: Name, age, role, social status, core desire, fatal flaw.
2. Visual Key Traits (AI Image Lock Tokens):
   - Face & Hair: Exact facial geometry, eye color, hairstyle, distinctive marks (scars, cyberware, tattoos).
   - Wardrobe & Silhouette: Primary outfit, signature jacket/garment, textures, distinctive silhouette.
   - Fixed Color Palette: 2-3 specific colors locked to this character across all scenes.
   - Signature Prop: One unique physical item always associated with the character.
3. Multi-Angle Consistency Anchor Prompt:
   - Provide a standardized base prompt describing the character in Neutral Front, 3/4 Angle, and Profile view against a neutral studio background.
4. Voice & Mannerism Profile: Speech cadence, pitch, typical emotional baseline, physical ticks.

[OUTPUT FORMAT]
Structured Markdown ready for indexing into the Story Studio IP Asset Directory.
```
