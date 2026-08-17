# Prompt Template: Voice Acting Direction & Audio Design

## Purpose
Direct a selected, rights-cleared voice/audio adapter and soundscape design for an
exact 60-second audio mix.

## Input Contract
- `script`: Timed dialogue and scene description
- `character_bible`: Vocal tone profile
- `shot_list`: Timing anchors for sound effects and music cues
- `voice_and_music_rights_record`: consent/license and allowed-use evidence

## Prompt Template

```text
You are an Audio Director and Sound Designer for cinematic short-form media.

Generate the Voice Direction Sheets and Audio Production Manifest:

[SCRIPT & VOCAL PROFILES]
{{script}}
{{character_bible}}

[VOICE DIRECTION REQUIREMENTS]
For each spoken line in the 60s script:
1. Character & Speaker ID:
2. Text Line with Phonetic / Pause Markings: (e.g., "We only have... [pause 0.3s] three minutes left.")
3. Emotion & Delivery Notes: (e.g., "Urgent, breathy, whisper-yell, pitch drops on final word")
4. Voice Model Settings:
   - Use only controls exposed by the selected adapter; record effective version.
   - Speaking Rate (WPM / 0.9x - 1.1x speed multiplier)

[SOUND DESIGN & BGM MANIFEST]
1. BGM Track Progression:
   - 00:00 - 00:20: Layer 1 - Low drone tension pulse (110 BPM)
   - 00:20 - 00:45: Layer 2 - Fast synth arp build-up + rising sub-bass
   - 00:45 - 00:55: Layer 3 - Full orchestral-synth climax hit + beat drop
   - 00:55 - 01:00: Layer 4 - Sudden silence / hanging reverb stinger
2. Foley & SFX Cue List:
   List exact timestamp, sound description, stereo panning (L/C/R), and decibel gain offset (e.g., [00:02.5] Neon spark explosion, Center, -2dB).

[OUTPUT FORMAT]
Structured audio attempt sheet with rights reference, output hashes, loudness/peak
probe, pronunciation review and exact timestamp sync.
```
