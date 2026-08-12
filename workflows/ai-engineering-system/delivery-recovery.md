# Git Delivery And Recovery

本文件定义代码与版本化文档的阶段交付，以及 GitHub push 失败后的持久化恢复流程。

## 1. Normal Delivery

每个任务使用独立分支，不直接修改默认分支。每完成一个可独立验证的阶段：

```text
检查 scope 和 diff → 执行匹配风险的验证 → commit
→ push 当前分支 → 核验远端分支和完整 commit SHA
```

大型任务不得等到全部完成后才首次 push。未经用户授权，不合并默认分支、不创建 PR、不修改无关仓库。

## 2. Push Failure

push 失败不等于代码交付完成。先进行有界诊断与重试；仍失败时：

1. 保留已验证的本地 commit；
2. 检查未跟踪文件，排除密钥、Token、`.env` 和隐私数据；
3. 从该 commit 导出可恢复的 Git bundle；
4. 生成 manifest 和 SHA-256；
5. 将 bundle、manifest 及不适合 Git 的验证资产上传至私有 Google Drive；
6. 读取 Drive metadata，确认文件存在；
7. 标记 `remote_status: not_persisted` 和 `sync_status: write_failed`。

Drive 只提供灾难恢复副本，不能替代 GitHub，也不能据此声称已远端交付。

## 3. Recovery Layout

```text
AI Engineering Lab/
└── Recovery/
    └── <repository>/
        └── <task-or-branch>/
            ├── <repository>__<branch>__<short-sha>__<date>.bundle
            ├── manifest.yaml
            ├── evidence/
            └── assets/
```

`manifest.yaml` 至少记录：

```yaml
repository: owner/name
branch: feat/example
commit: full_commit_sha
basis_commit: full_basis_sha
backup_type: git_bundle
bundle_sha256: sha256
created_at: RFC3339_timestamp
validation:
  status: passed_or_partial
  commands: []
remote_status: not_persisted
sync_status: write_failed
failure_reason: push_error_summary
```

## 4. Restore And Close

后续 AI 必须先读取 manifest、校验 bundle SHA-256、恢复分支并重新核对验证状态；必要时重新运行受环境或时间影响的检查。GitHub 恢复可写后 push 同一 commit，并核验远端完整 SHA。

恢复成功后更新 manifest 为 `remote_status: persisted`、记录远端 SHA 和恢复时间。Drive 副本可以归档，但不得在远端核验前删除。
