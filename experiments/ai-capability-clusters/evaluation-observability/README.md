# Evaluation / observability 固定实验

这是本机契约实验，不是 OpenHands、真实 evaluator、模型或生产 telemetry 的运行证明。`fixtures.json` 冻结成功、错误、安全违规、缺 telemetry，以及“其他轴正常但 trace 不完整”的 trace；只使用 Python stdlib/JSON。

运行 `python3 run_experiment.py` 生成两个确定性结果。baseline 只信 outcome（完整 trace 的成功才是其设计目标，但会暴露 false-pass）；treatment 先处理 security fail，再将 `trace_complete` 非 `true` 判为 unknown，确保安全失败优先于未知。`validate(result, fixtures, oracle)` 从 fixtures 独立重建完整 axis 集合，严格校验 experiment ID、trace ID 集合和每个 outcome/process/security/trace_complete；指标也只从 fixtures truth 加 result predictions 重算后再比对 oracle。负测覆盖删除或篡改任意轴/complete 值、仅 trace incomplete 的正常表象，以及 security fail + incomplete 必须仍为 fail。
