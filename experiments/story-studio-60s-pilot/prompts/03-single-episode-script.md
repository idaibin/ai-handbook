# Prompt Template: 60-Second Single-Episode Script

## Purpose
Convert story positioning and bible assets into a timed, shot-ready 60-second micro-drama script.

## Input Contract
- `world_bible`: World rules and visual guidelines
- `character_bible`: Character traits and voice parameters
- `episode_premise`: Specific conflict for Episode 1 (Pilot)

## Prompt Template

```text
You are an expert scriptwriter specializing in rapid-fire 60-second vertical video scripts.

Write the full production script for Episode 1 (60 seconds total runtime) based on the world and character specifications:

[WORLD & CHARACTER BIBLE]
{{world_bible}}
{{character_bible}}

[EPISODE PREMISE]
{{episode_premise}}

[SCRIPT CONSTRAINTS]
1. Duration: Exactly 60 seconds (12-15 dramatic action/dialogue beats).
2. Pacing: Average 1-2 spoken lines per 5-second interval; max 130 words spoken dialogue/narration.
3. Timestamp Structure:
   - [00:00 - 00:05] Beat 1: The Disruption / Visual Hook
   - [00:05 - 00:15] Beat 2: Escalation & Stakes
   - [00:15 - 00:30] Beat 3: Active Struggle / Obstacle
   - [00:30 - 00:45] Beat 4: Midpoint Reversal / Shock Discovery
   - [00:45 - 00:55] Beat 5: High-Stakes Climax
   - [00:55 - 01:00] Beat 6: Cliffhanger / Final Visual Punchline
4. Formatting:
   For every beat, provide:
   - Timestamp range
   - Scene Location (Interior/Exterior, Day/Night)
   - Visual Action (Subject action, physical reaction)
   - Spoken Lines (Character Name + Emotion tag + Dialogue text)
   - SFX / Music Layer Notes (Ambient, Foley, Stinger, Beat drop)

[OUTPUT FORMAT]
Production-ready screenplay format with exact timestamps.
```
