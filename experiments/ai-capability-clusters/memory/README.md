# Scoped memory fixed experiment

本机行为实验：冻结多用户、多 run、矛盾更新、删除和 secret 输入，比较 append-only 无 scope baseline 与 scope filter + upsert/tombstone + secret rejection treatment；不是任何上游记忆运行时的证明。输入和独立 oracle 分别在 `fixtures.json`、`oracle.json`。

运行：`python3 run_experiment.py`。脚本用 Python 标准库确定性写入 `runs/baseline.json`、`runs/treatment.json` 并打印 JSON；treatment 不通过 oracle 时返回非零。

预注册的 `fixtures.json.policy` 是执行期唯一读取的 policy：其中固定 `sensitive_keys`、`forbidden_returns` 和查询期望值；`execute(mode, fixtures)` 不接收也不读取 oracle。因此修改 `oracle.json` 的 sensitive keys 不会改变 treatment 原始输出，只会使 validation 失败。`oracle.json` 仅用于校验其与预注册 policy 的一致性，以及 event disposition、完整 store（含 tombstone/provenance）、facts/queries/store key 闭合与 secret rejection。

验收指标：precision、recall、stale fact rate、`query_scope_leak_count/rate`、`store_provenance_mismatch_count/rate`、secret retention、token units。两类泄漏分开计算：前者从每个 query 实际 selected source user/scope 的 receipt 计算（当前 baseline 为 2/6，treatment 为 0），后者从完整 store 的 scope user 与 source user 计算。answer receipt 始终保留 `selected_source_user` 和 `selected_source_scope`，不会因 store provenance 为零而把发生过的跨用户 query 报成零；`api_token` 即使没有旧式 `secret` 标记也会按 sensitive key 拒绝。

固定负测会分别注入 orphan fact、未分类 secret 的错误 retain、跨用户来源、queried fact 篡改，以及 validation-only oracle sensitive-key 篡改；每一项都必须使 oracle 校验非零。结果仍只证明冻结本机 JSON 契约，不证明上游记忆运行时、真实分类器或生产数据隔离。
