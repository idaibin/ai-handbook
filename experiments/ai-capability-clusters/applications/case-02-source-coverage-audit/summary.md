# Case 02 result

- Validator: `python3 sources/coverage/validate_coverage.py sources/coverage/batch-agent-rag.yaml sources/coverage/batch-memory-mcp-eval.yaml sources/coverage/batch-observe-coding.yaml` exit `0`; errors `0`.
- Counts: `{"batches": 3, "incomplete": 0, "not_found": 0, "read": 60, "records": 60, "sources": 12}`; treatment frozen-oracle pass `True`.
- Baseline metrics: `{"F1": 0.0, "FN": 60, "FP": 12, "TP": 0, "precision": 0.0, "recall": 0.0}`; treatment metrics: `{"F1": 1.0, "FN": 0, "FP": 0, "TP": 60, "precision": 1.0, "recall": 1.0}`.
- Frozen oracle SHA-256 unchanged: `True` (`44535d5ad633a4cdd1b15673d71ee1c4c2c1a2ff49fc187233b5ede21d23f125`).
- Fixed-commit structure/coverage is verified locally; remote GitHub path/blob and upstream runtime/provider effects remain `Not verified`.
