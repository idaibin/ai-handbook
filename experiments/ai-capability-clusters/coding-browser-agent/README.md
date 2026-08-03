# Coding / browser-agent 固定实验

这是本机契约实验：用 mock workspace、静态 HTTP/DOM fixture 和 Python stdlib 验证边界策略；不是 OpenHands、真实浏览器、网络、模型或生产 coding-agent 运行证明。

运行 `python3 run_experiment.py`。baseline 是宽目录、无动作预算、无 mutation approval/postcondition；treatment 对 navigate/click_save/read_dom 统一校验 domain、path、current page，并区分 attempted 与 executed budget（blocked 也计 attempt）。`click_save` 会变更独立 DOM fixture state，随后 `read_dom` 报告实际 observed state。完成必须同时有 `passed=true`、approval、before/after、DOM observed postcondition、diff 与完整 receipt；approval 篡改、错误状态、缺失按钮、evil domain 的 mutation/DOM、错误路径和预算耗尽均 fail closed。workspace 读取先规范化 POSIX mock path，拒绝绝对路径、NUL 与任何 `..` 组件，并以路径边界而非字符串前缀匹配 allowlist；mock IO 仅使用规范化结果。负测覆盖 `workspace/app/../secret.txt`、绝对路径、同前缀 sibling、NUL、evil domain、错误 DOM/path 与预算；所有 blocked receipt 都必须没有 evidence。独立 `oracle.json` 校验允许 diff、禁止路径、状态和动作序列，失败返回非零。symlink 解析未验证：此 mock 没有真实文件系统或 symlink。
