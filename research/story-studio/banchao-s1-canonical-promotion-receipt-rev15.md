# Banchao S1 Canonical Promotion Receipt — Revision 15

- receipt_id: `BANCHAO-S1-CANONICAL-PROMOTION-REV15`
- execution_unit: `PROMOTE_CANONICAL_STORYBOARD_REFERENCE_194`
- promoted_at_utc: `2026-08-26T09:08:26Z`
- result: **PASS_CANONICAL_STORYBOARD_REFERENCE_194**

## Preconditions Verified

```text
revision 14 Drive readback: 6/6 PASS_EXACT_SHA
revision 14 GitHub readback: 5/5 PASS_GIT_BLOB_SHA
revision 14 Registry readback: 2/2 PASS
Task EXEC-0001..EXEC-0019: unique
L1A: 194/194 PASS_SELECTION
L1B: 194/194 PASS
L2: PASS_SEMANTIC_AGGREGATE
L3: 23/23 PASS
L4: 5/5 PASS_WITH_BOUNDED_ADAPTATIONS
```

## Promotion

```text
candidate_not_canonical → canonical_storyboard_reference
canonical: 0 → 194
production_ready: 0 → 0
mapping revision: 9 → 10
manifest revision: 9 → 10
status revision: 14 → 15
```

No image bytes, Drive asset references, shot IDs, frame keys, row order, Character State, Location or boundary decision changed.

## Hashes

- mapping: `dc495dd7e1fb20f3f4861de4b7fd09e53270f89bd23fe87c89a93895ce687c49`
- manifest: `fb1de906ca74dd65eceb024b42cba7c603e6b2c94d68b91ee20d8a94fc0653cb`
- status JSON: `128985c4b060e9e447fe9117605ecce57d997587d671bb7bf5e05eee2a469144`
- status Markdown: `3c1853ab7e2ee54cf62a33c369c94b8fcde876d2f0a384c47a8cea50c2214546`
- consistency matrix: `ab78e2fde3790077fbba3b26e053c65b3446dc167e989f7f8e69c24b64992c20`
- Visual Canon Gate: `ded8f4f275dfd4d5f923c82fdc3f48309f5fafa9b2e08b6b0d5a55ea3cef4292`
- Final Gate JSON: `1d140f3e4499f062f2b54ad1628f331aed2a9ab895f8abf62055279a20663ec8`
- Final Gate Markdown: `1138261540b2d8be322c60ec1f85b69f96ee17c766b685efeb89d38c3da3b4e2`

## Next Action

`VIDEO_CHAIN_TEST_SLICE_10_SECONDS`
