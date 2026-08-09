# lucaswalter/n8n-ai-automations workflow assessment

- Fixed commit: `57e1527902b8447e6cd3374d00237a34d3193e0b`
- Tree/content: `git-tree:1dd43acf4ce9d2e7077782f3cb8b330057cae224`
- Observed: 1,582 Stars; `main`; not forked or archived
- License: no LICENSE/COPYING and no GitHub license declaration found
- Evidence: `source_validated` for static workflow definitions; runtime not validated
- Subtype/topic fit: `workflow-template-collection`; fit

## Verified

All 38 exported n8n JSON files parsed, containing 885 nodes; three carry `active=true`. Triggers include forms, schedules, subworkflow calls, RSS, webhooks, chat, Gmail, Slack, WhatsApp and manual entry. Connections express real branches and loops. The newsletter workflow has two Slack send-and-wait review loops, although an LLM converts free text into an approval boolean. The Meta deck workflow loops over remote generation status. The active Twitter reply workflow can post publicly without a human gate.

External-effect nodes include HTTP, Slack, S3, Drive, Sheets, Gmail, Airtop, Twitter, WhatsApp and Twilio. Twenty workflows configure some retries and eleven define `onError`, but no workflow-level idempotency key or exactly-once mechanism was found.

## Inference

These are executable definitions rather than a links-only list. Importability and safety are nevertheless per-template: credentials, community nodes, API drift and retry duplication remain deployment concerns.

## Not verified

No license grant, tests, CI or run artifacts were found. No template was imported or dry-run; n8n compatibility, credentials and external effects remain unverified.

Evidence: [repository](https://github.com/lucaswalter/n8n-ai-automations/tree/57e1527902b8447e6cd3374d00237a34d3193e0b), [newsletter](https://github.com/lucaswalter/n8n-ai-automations/blob/57e1527902b8447e6cd3374d00237a34d3193e0b/ai_newsletter_generator.json), [Twitter workflow](https://github.com/lucaswalter/n8n-ai-automations/blob/57e1527902b8447e6cd3374d00237a34d3193e0b/twitter_reply_guy_agent.json).
