# Summary

baseline 完成了全部八个动作，但读取了 secret、访问 evil.local，且状态没有证据链（`completed_without_evidence`）。treatment 对所有浏览器动作执行 domain/path/current-page 检查，八次 attempted 中仅五次 executed；保存 mutation 变更独立 DOM fixture，随后读取实际 observed state，并以 approval、before/after、DOM postcondition、diff、receipt 形成完整证据链，阻断两个越界动作并继续收敛，额外动作因 executed budget 耗尽被阻断。approval 篡改、错误状态、缺失保存按钮、evil mutation/DOM、错误路径和预算均有 fail-closed 负测。

workspace 读取还对 traversal、绝对路径、NUL 和 sibling-prefix fail closed，且 mock 读取只接受规范化路径；所有 blocked action 都无 evidence。symlink 解析仍为 Not verified，因为实验不接触真实文件系统。本实验只证明冻结 mock 环境中的策略和结果可重放；不覆盖真实文件权限、浏览器沙箱、DOM 漂移、恢复失败或生产审计。
