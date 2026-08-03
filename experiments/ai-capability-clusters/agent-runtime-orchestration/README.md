# Runtime orchestration fixed experiment

本机行为实验：用 Python 标准库模拟 guardrail、blocking gate、checkpoint interrupt 和重执行；不是上游运行时或生产 E2E 证明。输入冻结在 `fixtures.json`，独立 oracle 在 `oracle.json`。

运行：`python3 run_experiment.py`。脚本确定性生成 `runs/baseline.json` 与 `runs/treatment.json`，并打印同样的 JSON；treatment 不满足 oracle 时返回非零。

验收：treatment 按 `max_turns` 执行，真实 interrupt/recovery case 的 recovery state 为 1/1；预算耗尽 case 必须显式 `blocked`，不得超预算。冻结 oracle 逐项按列表精确顺序校验事件，重复、反转及 checkpoint/interrupt/recovered 交换均失败。另报全部 case 的 `final_state_accuracy`、重复副作用和 guardrail 泄漏；baseline 应展示重试副作用和 gate 泄漏。
