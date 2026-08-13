# Qualifier-lock preflight failure

This isolated `human-writing` generation used the first qualifier-lock draft at local commit `8071096cad933e25f1c80032ce22e21cfaa54c08`. It was stopped before blind judging because C03 still omitted the source qualifier `主要`, the exact defect the revision was intended to prevent.

The output is preserved as `human-writing.md`. The draft was then strengthened with an explicit private qualifier ledger and item-by-item fidelity check. A fresh agent generated the final output from the amended revision; the failed output was not reused or silently corrected.

This is a preflight failure, not a four-skill score. The commit was amended before publication, so `draft.patch` preserves its complete three-file change relative to the published semantic-unit base `aeb4a29e4f3646806542a5eb3891a44b91138f82`. The failed output's SHA-256 is `3434bbc835a253e13cf5039ac4c3db9986af76baa3301d028739148ab52f2fa5`. The final fixed revision is identified separately in the root manifest.
