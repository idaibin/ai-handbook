# Case 01 result

- Fixed target scope: `['/manage/log', '/manage/dict', '/system/module']`; classified negative routes: `{'missing_mapping_decoy': '/system/status', 'scope_external': '/manage/task'}`.
- Treatment never loads oracle or expected answers while deriving candidates; it parses route groups and exact capability-map rows from frozen source.
- Baseline metrics: `{"F1": 0.0, "FN": 3, "FP": 0, "TP": 0, "precision": 0.0, "recall": 0.0}`.
- Treatment metrics: `{"F1": 1.0, "FN": 0, "FP": 0, "TP": 3, "precision": 1.0, "recall": 1.0}`; frozen-oracle pass: `True`.
- Frozen oracle SHA-256 unchanged: `True` (`4522c7fce0a3ceb9be97eeadd88403795563becfd6d328e7f69de9b299601685`).
- Missing-mapping decoy and scope-external routes both have no finding; injected decoy mapping and removed external mapping each fail their synthetic parser check.
- Not verified: browser/visual behavior, permission service runtime, provider/agent behavior, and production deployment safety.
