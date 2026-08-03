# Case 02 — Source coverage audit

真实 basis 是 `ai-handbook/sources/coverage/manifest.yaml`、`batch-agent-rag.yaml`、`batch-memory-mcp-eval.yaml`、`batch-observe-coding.yaml` 与 `validate_coverage.py` 的当前固定文件；manifest SHA-256=`e0a6acdd90c173782898fb704a513c5073c1973370211e7d3446479d393fd52e`，脚本记录每个文件 SHA-256、validator 命令/版本和实际返回值。oracle 预注册为 12 sources、60 records、每 source 五个 roles（`readme`、`core`、`security_or_boundary`、`evaluation_or_testing`、`code_or_test`）、所有状态 `read_at_fixed_commit`、`errors=0`。`oracle.json` 是只读冻结输入（SHA-256=`44535d5ad633a4cdd1b15673d71ee1c4c2c1a2ff49fc187233b5ede21d23f125`）：脚本不创建或覆盖它，仅用它独立比对 source/record count、roles、status、errors 和 record keys，并记录运行前后 hash 必须不变。

baseline 只读取 README/manifest 摘要，故只声称 12 个 source summary，不声称具体 role records，故意漏掉 60 条 record。treatment 实际运行 `validate_coverage.py` 并通过其 `normalize_batch` 解析三批记录；覆盖指标按 `source_id|role` 计算 TP/FP/FN/precision/recall/F1。该实验应用 RAG/evaluation IR 的固定 basis、独立 oracle 与 unknown 传播；结构校验不等同于上游运行效果或远端 GitHub 证明。

运行：`python3 run_experiment.py`。产物：`basis.json`、`oracle.json`、`runs/baseline.json`、`runs/treatment.json`、`adjudication.json`、`summary.md`。treatment 通过独立 oracle 才 exit 0。`--verify-remote` 未调用，远端 path/blob/locator 保持 Not verified。
