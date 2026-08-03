# 来源覆盖合同

本目录定义 AI 知识工程 v1.0 的固定提交阅读证据。`manifest.yaml` 固定 12 个主来源与六个能力簇；每个逻辑来源必须恰好覆盖：`readme`、`core`、`security_or_boundary`、`evaluation_or_testing`、`code_or_test`。

运行：

```sh
python3 ai-handbook/sources/coverage/validate_coverage.py
python3 -m unittest ai-handbook/sources/coverage/test_validate_coverage.py
# Requires a working authenticated `gh` session and only performs read-only API calls.
python3 ai-handbook/sources/coverage/validate_coverage.py --verify-remote
```

验证器会区分 `schema_valid`（结构/条件字段）与 `coverage_complete`（每个 manifest required role 均已读到）。完成模式下任一 required role 为 `not_found` 会非零退出；摘要固定输出 `read/not_found/incomplete`。验证器会交叉检查 batch 的 repository/commit 是否与 `github-ai-repositories.yaml` 和本 manifest 一致。`read_at_fixed_commit` 记录要求路径、40 位 Git blob SHA、定位器、覆盖范围、原子主张、边界/反例及未验证项。

`not_found` 不是资料不存在，必须提供 `search_evidence`：固定 `commit`、具体 `method_or_query`、实际搜索的 `searched_paths_or_tree`、`result` 和剩余 `gap`。`x`、`TBD` 等占位值不能通过。

当前三个既有 batch 是 manifest `legacy_batch_allowlist` 中明确允许的 `legacy-v1`；历史 `read` 会在验证时标准化为 `read_at_fixed_commit`。只有该 allowlist 可由父 identity 展开。新 batch 必须为 `canonical-v2`，使用嵌套结构并在每条 record 重复 `source_id/repo/commit_sha`，以便移动单条记录仍可审计。

`coverage.schema.yaml` 使用 Draft 2020-12 条件字段和闭合对象。CLI 在安装 `jsonschema` 时执行该 schema；本机没有该依赖时会使用等价的内置结构校验（包含 status 条件字段、unknown-field、canonical identity 和 legacy allowlist），因此 CLI 不会把第三方 schema 当作已执行。

`--verify-remote` 通过已认证的 `gh api` 固定读取 commit、递归 tree 和 blob：校验 path/tree blob SHA，下载 blob 后重新计算 Git blob SHA，并在内容中检查 locator。分号复合 locator 的每个片段都必须匹配；Markdown `# heading` 或 `path.md#heading` 只匹配 Markdown heading（emoji/空白可归一），代码 symbol 按完整标识符匹配，自由文本按明确的大小写/空白归一短语匹配。因此 `SECURITY.md#security` 不会因正文中出现普通 security 一词通过。认证、网络或 GitHub 配额不可用时，会以 `Not verified` 非零失败，绝不静默跳过，也不输出 token。

本地完成模式只证明记录结构、自声明身份和五角色覆盖完整；只有 `--verify-remote` 成功，或另有逐条固定提交复核记录时，才能把对应记录计为 path/blob/locator 已远端核验。即使远端核验通过，也只支持“读取了指定文件与定位器，并把主张限制在该证据内”，不证明代码已经运行、测试已经通过、仓库已被完整阅读，也不证明生产安全性、运行时行为或外部服务效果；这些必须由独立实验/运行记录验证。
