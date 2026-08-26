# Banchao S1 — 10-second Video Chain Test v1

- result: `PARTIAL_PASS_PROVIDER_BLOCKED`
- canonical input: `194` approved storyboard references
- test slice: `EP01-F01 → EP01-F10`
- output: `1920×1080 / 24fps / 10.000s / H.264 + AAC`
- production_ready: `0`

## Verified passes

- 10/10 current canonical source refs resolved from mapping revision 10.
- 10/10 production derivatives embed sRGB without crop, resize, or pixel change.
- Motion Contract rendered as a deterministic low-amplitude camera proxy.
- Restrained room tone, brush texture, stop cue, and cloth rustle were generated and muxed.
- MP4 assembly completed; full ffmpeg decode returned no error.
- Output SHA-256: `398046257ceaec0b61c2497bda9daaf5ef5b1581a9d8c65c7ef33172f97fdaab`.

## Provider blocker

The connected Runway workspace is authenticated but reports `availableVideoModels=[]`. Therefore true image-to-video actor motion was not executed. The generated MP4 is a deterministic chain-validation proxy, not a production video shot.

## State decision

```text
canonical: 194 (unchanged)
production_ready: 0 (unchanged)
full-season video production: not authorized
next_action: VIDEO_CHAIN_TEST_GENERATIVE_PROVIDER_RESOLUTION
```

## Stable evidence

- Video Drive ID: `1UPEXwogEdIV6szZypFd8i4nnYRk_sRLS`
- Package Drive ID: `1Yy61_rkQs0AI5g35wCib1q-FftkSr6-P`
- Verification Drive ID: `1tewtIhK9BBEdfbbJz-ZV5ntkXaicaMws`
- Motion Contract Drive ID: `1WfwNDarKk1yIUMSL7n2fsAL82kAr7A9Q`
