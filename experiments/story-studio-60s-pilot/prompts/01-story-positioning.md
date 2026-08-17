# Prompt Template: Story Positioning & Hook

## Purpose
Generate a high-concept positioning, audience definition, genre classification, logline, and 3-second hook for a 60-second AI comic/short-drama pilot.

## Input Contract
- `raw_idea`: Core premise or theme
- `target_platform`: (e.g., TikTok, YouTube Shorts, Douyin, Bilibili)
- `target_duration_sec`: 60
- `genre_preferences`: (e.g., Sci-Fi, Suspense, Cyberpunk, Urban Fantasy)

## Prompt Template

```text
You are a senior micro-drama showrunner and narrative strategist specializing in 60-second vertical visual storytelling.

Analyze the following initial idea and generate a complete Story Positioning Package:

[INPUT DATA]
Idea: {{raw_idea}}
Platform: {{target_platform}}
Duration: 60 seconds
Preferred Genres: {{genre_preferences}}

[REQUIREMENTS]
1. Core Logline: One punchy sentence capturing protagonist, inciting incident, core obstacle, and immediate stakes.
2. Target Audience Profile: Primary demographics, media consumption habits, emotional payoff sought.
3. Genre & Tone: Primary genre, secondary genre blend and generic tonal attributes.
   Do not request imitation of a living artist or reuse protected characters/settings.
4. Hook Architecture:
   - 00:00 - 00:03 Hook: Immediate visual/auditory disruption to prevent swipe-away.
   - 00:03 - 00:15 Setup: Escalating situation and character motivation.
   - 00:15 - 00:45 Conflict Escalation: Rising tension, mid-point revelation/twist at ~00:30.
   - 00:45 - 00:55 Climax Beat: Peak dramatic confrontation or discovery.
   - 00:55 - 01:00 Cliffhanger / CTA: Unresolved tension forcing follow/next-episode anticipation.
5. Virality & Retention Hypothesis: Why will viewers stay past 3s, 30s, and complete the video?

[OUTPUT FORMAT]
Output structured YAML or Markdown with exact headings matching the requirements above.
```
