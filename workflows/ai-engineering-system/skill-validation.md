# Skill Validation Policy

## 1. 目标

Skill 验证必须证明候选能力在明确边界内能够被正确触发、执行和验证，而不只是 `SKILL.md` 可以被读取。

## 2. 固定基础

每次验证固定两部分：

```yaml
skill_basis:
  repository: idaibin/skills
  commit: <full-sha>
  path: <skill-path>

target_basis:
  repository: <owner/repo>
  commit: <full-sha>
```

分支名只用于说明，不作为不可变证据。

## 3. 环境选择

| 验证目标 | 优先环境 |
| --- | --- |
| 包结构、路由、普通构建和单测 | Codex Cloud 隔离环境 |
| 私有仓库或需要本地缓存的开发 | Codex Local |
| 长期服务、数据库、systemd、多服务集成 | 自有云服务器 |
| macOS 权限、窗口、Finder、签名、公证 | 本地 Mac |
| 生产行为 | 真实目标环境 |

云端 Linux 结果不得替代 macOS 或生产证据。

## 4. 安装方式

在隔离目标仓库中安装固定 SHA 的候选 Skill。优先使用仓库级、任务级安装，避免污染全局环境。安装记录必须包含来源 commit、目标目录和实际加载结果。

私有凭据只在必要阶段使用最小权限、短期、只读授权，不写入日志、Git remote、配置或提交。

## 5. 验证层级

### V1 — Package

- 必需文件存在；
- 元数据合法；
- reference、script 和 asset 可访问；
- 不含本地绝对路径和敏感信息。

### V2 — Routing

- 明确 Trigger；
- 明确 Non-Trigger；
- 相近任务边界；
- 多 Skill owner routing；
- 授权问题和状态询问不应被误判为执行授权。

### V3 — Behavior

验证 Skill 是否：

- 读取项目规则；
- 尊重现有架构和技术栈；
- 不扩大任务范围；
- 不擅自提交、推送或部署；
- 正确处理失败和未验证项；
- 输出与合同匹配。

### V4 — Project

执行目标仓库规定的真实命令，例如：

```text
format / lint / unit test / integration test
frontend build / cargo build / clippy / Java test
Playwright / git diff --check
```

命令以目标仓库文档、`AGENTS.md`、CI 和实际代码为准。

### V5 — Claim Floor

必须检查完成声明：

```text
静态检查通过 ≠ 集成验证通过
本地构建通过 ≠ 已部署
mock 通过 ≠ 真实 provider 通过
Linux 云端通过 ≠ macOS 原生通过
```

### V6 — Generalization

稳定发布前至少覆盖：

- 一个主要目标仓库正例；
- 一个不同结构的正例；
- 一个相近但不应触发的负例；
- 一个失败或不适用边界。

## 6. 产物与存储

`idaibin/skills` 保存：

- Skill 实现；
- 通用 Trigger/Non-Trigger；
- 行为测试；
- 发布状态。

目标项目保存：

- 真实代码变更；
- 项目测试；
- 项目级配置。

`ai-handbook` 保存：

- 固定候选和目标 SHA；
- 测试任务与环境；
- 运行命令；
- 结果、Review 和剩余缺口；
- 晋级或降级决策。

## 7. 晋级状态

```text
candidate → pilot → stable
                 ↘ revise / deprecated
```

- `candidate`：结构和初步行为可测；
- `pilot`：固定真实任务通过，但泛化证据仍有限；
- `stable`：多项目正例、负例和回归门禁通过；
- `deprecated`：边界失效、被替代或持续产生高风险错误。

禁止候选 Skill 自动批准自己，禁止仅因一次成功直接进入 `stable`。
