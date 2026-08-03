# MCP 工具授权边界固定实验

这是本机契约实验：用 stdlib 的 fake server/actions 验证连接级授权与逐次、可撤销授权的差异。它不调用真实 MCP、网络、模型或付费服务，因此不能证明 OpenHands、真实 MCP server 或生产部署行为。

运行：`python3 run_experiment.py`。脚本固定读取 `fixtures.json` 与独立 `oracle.json`，生成 `runs/baseline.json`、`runs/treatment.json`；oracle 不通过被测实现生成，校验失败返回非零。

Treatment 合同包含 principal/session/account/target allowlist、逐次审批、registry 中一次性 grant 的 active→revoked 状态转换、postcondition readback 和显式 revoke receipt。receipt integrity 按 fixtures 的 action 顺序独立重放每笔 transfer 的 before/after state，且将 receipt 的 `expected`、`observed`、`ok=true` 绑定到该重放结果；即使把 expected 与 observed 同时改成 999 也会失败。它还要求 registry grant 集合严格等于 receipts 中所有非空 grant 的集合，因此任何幽灵 revoked/used grant 都会失败。残留权限直接由 registry 的 active 状态计算。固定负测保留跳过 revoke、复用 grant、篡改 postcondition、篡改 registry used、篡改 revoke before，并新增 joint postcondition tamper 和 ghost grant。
