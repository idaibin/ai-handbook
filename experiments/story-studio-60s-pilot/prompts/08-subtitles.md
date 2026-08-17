# Prompt Template: Subtitle Generation & Timing Constraints

## Purpose
Format dialogue and sound effect indicators into millisecond-accurate subtitle streams formatted for high-retention mobile short-form display.

## Input Contract
- `dialogue_manifest`: Timed audio from Stage 07
- `subtitle_style`: Highlight colors, max characters per line

## Prompt Template

```text
You are a Subtitle and Kinetic Typography Editor for mobile vertical video.

Convert the recorded dialogue and critical sound cues into a high-retention Subtitle Specification:

[DIALOGUE & TIMING MANIFEST]
{{dialogue_manifest}}

[SUBTITLE SPECIFICATION CONSTRAINTS]
1. Reading Speed: Maximum 20 characters per second (CPS) to ensure mobile legibility.
2. Line Constraints:
   - Maximum 12 Chinese characters or 6 English words per line.
   - 1 line maximum visible at any timestamp (no multi-line stacking).
3. Visual Styling Rules:
   - Position: Centered horizontally, lower-third (y=75% of screen height to clear UI icons).
   - Font & Weight: Bold Sans-Serif with 2px dark drop shadow/stroke for high contrast against any background.
   - Dynamic Word Highlight: Specify keyword highlight color (e.g., #FFE600 Yellow on dramatic nouns/verbs).
4. Timing & SRT / JSON Format:
   For every entry provide:
   - Subtitle Index
   - Start Timestamp (hh:mm:ss,ms)
   - End Timestamp (hh:mm:ss,ms)
   - Text Content
   - Highlight Keyword

[OUTPUT FORMAT]
Valid SRT text block accompanied by a JSON manifest for automated rendering.
```
