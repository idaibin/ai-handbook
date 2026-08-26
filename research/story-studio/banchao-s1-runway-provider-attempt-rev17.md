# Banchao S1 — Runway Generative Provider Attempt — Revision 17

- `attempt_id`: `BANCHAO-S1-RUNWAY-PROVIDER-ATTEMPT-REV17`
- `execution_unit`: `VIDEO_CHAIN_TEST_GENERATIVE_PROVIDER_RESOLUTION`
- `attempted_at_utc`: `2026-08-26T11:41:41Z`
- `provider`: `Runway`
- `result`: **BLOCKED_ACCOUNT_LIMITATION_PAID_PLAN_REQUIRED**
- `classification`: `FAIL_RIGHTS_OR_PROVIDER`
- `canonical`: `194`
- `production_ready`: `0`

## Conclusion

The connected Runway workspace was authenticated and a minimal 5-second `EP01-F01` image-to-video request was submitted to test real actor-motion generation.

The provider rejected the request before generation with:

```text
kind: account_limitation
reason: paid_plan_required
model: Gen-4 Turbo
```

No generation job or video output was created.

## Verified provider state

```text
authenticated: true
team_id: 64820834
team_name: Bruce
personal_workspace: true
multiple_workspaces_available: false
availableVideoModels: []
requested_model: gen-4-turbo
```

The connector does not expose a numeric credit balance. Therefore this result proves **no usable paid video capability in the current workspace**, but it does not prove a specific remaining-credit number.

## Scope boundary

This is a Provider/account limitation, not a failure of:

- the 194 canonical storyboard references;
- the 10 production derivatives;
- the Motion Contract proxy;
- Foley/audio muxing;
- MP4 assembly or decoding.

No canonical source, Drive asset reference, mapping, manifest, derivative, audio, or prior test output was modified.

## State decision

```text
video_chain_test: PARTIAL_PASS
generative_actor_motion: BLOCKED_PAID_PLAN_REQUIRED
canonical: 194
production_ready: 0
full-season video production: not authorized
next_action: GENERATIVE_VIDEO_PROVIDER_ENABLEMENT_OR_ALTERNATE_PROVIDER
```
