# Knowledge & Intelligence System Map

- Stable route id: `knowledge-intelligence-system`
- Status: active Feed owner; research-report and insights runtime not verified
- Product: feeds-hub
- Lifecycle: `Sources → Feeds → Research → Insights`

## Outcome

Turn external sources and events into deduplicated, source-grounded and time-bounded
intelligence records, research reports, insights and knowledge candidates.

```text
Sources → Feeds → Research → Insights
(Collect → Normalize → Analyze → Verify → Publish Intelligence → Handoff Candidate)
```

## Owned artifacts

- source and event identity;
- feed records and deduplication state;
- evidence-linked analysis, research reports and insights;
- freshness/correction state;
- knowledge-candidate handoffs.

## Boundary

feeds-hub answers what happened and what current source evidence supports. It does not
own final content publishing, courses or video production. Authored audience content
routes to Createway. Durable Knowledge IR, courses and knowledge cards remain with
`knowledge-distillation` until an explicit migration. feeds-hub source-code, schema,
adapter or UI changes are separate `product-delivery-system` Tasks.

Current runtime evidence covers the existing Feed role only. Research-report and
insights storage, generation, review and publication in feeds-hub are architecture
targets and remain `Not verified` until the target repository implements and exercises
them.

## Gates

- stable source/event identity and observation time;
- primary source and corroboration boundary;
- fact, inference, conflict and correction separated;
- freshness and duplicate handling explicit;
- research report and insights tied to fixed source evidence;
- knowledge promotion performed only through an explicit handoff and downstream gate.
