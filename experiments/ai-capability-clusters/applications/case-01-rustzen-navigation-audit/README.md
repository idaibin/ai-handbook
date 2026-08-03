# Case 01 — RustZen navigation audit

真实 basis 固定在由 `RUSTZEN_ADMIN_REPO` 指定的 RustZen Admin Git repository 的 Git object `4e0189b52b5b6904a4b4082361a893a6f66e6797`。脚本只用 `git show <commit>:<path>` 读取，不读取当前工作树内容。

这是固定 target-scope 审计：只读冻结 `fixtures.json` 中的 audit targets 与分类负路径。`missing_mapping_decoy=/system/status` 必须在 routes 中、却没有 exact capability-map row；`scope_external=/manage/task` 必须同时存在于 routes/capability map、却不在 fixed target scope。treatment 从 `routes.tsx` 通用解析 route groups，并从 capability-map Markdown 表通用解析 exact frontend route 到 capability/backend owner；它只据这些来源为每个冻结 target 枚举 candidate finding，不读取 oracle 或 expected answers。两个负路径都不得产生 finding；给 decoy 注入 exact mapping 或删除 external mapping 的 synthetic parser test 必须失败。

`oracle.json` 是只读冻结输入：只在 treatment 输出之后按 routes、candidate IDs、finding data 和 metrics 评分。运行前后 SHA-256 必须不变；篡改 oracle 会非零退出。浏览器/视觉、权限服务运行时、provider/agent 行为与生产部署安全均为 Not verified。

从本 case 目录运行：`RUSTZEN_ADMIN_REPO=/path/to/rustzen-admin python3 run_experiment.py`。未设置该环境变量或路径不存在时，脚本会清晰失败。固定 commit、目标 paths 与 Not verified 边界保持不变。产物：`basis.json`、`fixtures.json`、`oracle.json`、`runs/`、`adjudication.json`、`summary.md`。
