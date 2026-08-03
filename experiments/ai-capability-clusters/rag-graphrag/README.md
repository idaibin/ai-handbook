# RAG / GraphRAG fixed experiment

本机行为实验：冻结 5 条小语料、直接问题与多跳问题，比较词项 top-k baseline 与“先分类、再沿图路径” treatment；不是上游检索器、模型或生产 RAG 证明。输入和独立 oracle 分别见 `fixtures.json`、`oracle.json`。

运行：`python3 run_experiment.py`。脚本只用 Python 标准库，确定性写入 `runs/baseline.json`、`runs/treatment.json` 并打印 JSON；treatment 不通过 oracle 时返回非零。

验收指标拆分为 lexical Recall@k、graph/path recall、图扩展步数预算和仅针对 direct cases 的 direct accuracy；运行结果同时比较 baseline/treatment 的 direct regression。oracle 的 budget key 必须与问题 ID 完全一致，并逐题校验 expansion steps，不能以总和抵消超支。路由必须从 question text 推断，`kind` 标签含扰动负测，不能作为路由输入。baseline 的 top-1 多跳检索故意只能命中 founder 文档，treatment 必须补齐图路径。
