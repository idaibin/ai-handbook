# Summary

固定四动作序列的结果：baseline 依赖“连接即允许”，两个未授权动作均执行，registry 中连接 grant 保持 active、残留权限为 1；treatment 仅完成合法读取和已批准的本账户转账，grant 在 registry 中 active→revoked，阻断跨账户转账与删除，readback 正确。跳过 revoke、复用 grant、篡改 receipt 的固定负测均被非零校验捕获。

receipt 完整性按 fixture 顺序独立重放 transfer 的 before/after state，将 receipt postcondition 的 expected、observed、ok 与重放余额绑定；即使同时把 expected/observed 改为 999 也会被捕获。registry 的 grant 集合必须严格等于 receipt 中所有非空 grant，因此幽灵的 revoked/used grant 也会失败。原有五项负测（skip revoke、reuse grant、postcondition、registry used、revoke before）均保留，并新增 joint postcondition tamper 与 ghost grant。

这只说明 fake server 上的本地策略契约可重复满足 oracle；没有真实 MCP 握手、身份提供方、并发会话、网络错误或生产审计链路证据。
