# Forgeway 验证结果与边界

本页是历史验证索引，不是 Forgeway 的运行时结果，也不把“源码存在”写成“完整
交付完成”。每条记录都保留基线、证据类型和未验证项。

## 固定源码基线

| 基线 | 可核验结论 | 证据等级 |
| --- | --- | --- |
| `project-delivery-system@6c5f234a8d3a7a3d46dca3a086bb8b3b6d55b348` | 五文件 Platform Spec 脚手架、目标 / 实现轴、状态词和验证说明存在。 | `Source-verified` |
| `project-delivery-system@7d4037bc8e5d89f86cf5fd7685292b363b6858d3` | PDS 变更记录、交付合同目录、Schema / fixture / tooling 结构和采用边界存在。 | `Source-verified` |
| `project-delivery-system@af35977d547c5708af45f25fe9795d25857e5bc3` | 多组件拓扑相关合同、模板和负向 fixture 存在。 | `Source-verified` |
| `project-delivery-system@8eaf9c1d2cca8706ac3fb126852a0431f97ec3bf` | Forgeway 命名空间、Plugin、coordinator、host-neutral runtime 文档和便携性验收标准存在。 | `Source-verified` |

## 按证据层级的登记

### Source / 文档

已核验：

- 初始 Platform Spec 的五文件树和状态语义；
- PDS 的变更记录、产品边界、拓扑演进和结果绑定规则；
- Forgeway 的统一产品名称、Plugin / Skill 入口、capability handoff、目标项目 authority
  和授权边界；
- `CHG-FORGEWAY-001` / `003` 对外部项目、runtime、发布和兼容性的明确限制。

### Automated / 本地静态验证

历史交付记录报告 Forgeway 基线曾通过 Schema、fixture、Plugin / Skill 结构、便携性
扫描、链接检查和 `git diff --check`。该摘要对应的是 `8eaf9c1` 的交付过程，而不是
本次写入 handbook 时重新执行的命令；因此本页只将它记为“历史报告”，不宣称当前
工作树仍有相同结果。任何新结论必须在固定新基线上重新执行并保存命令、环境和输出。

### Artifact / 包边界

历史交付记录还报告 npm dry-run 包按显式 allowlist 构建，未把 `.codex` 审查记录带入
包内容。这个事实只描述当时的包检查；没有 npm 发布、安装后行为或下游消费者证据。

### Independent review / 独立审查

历史交付记录中，固定基线上的两次独立审查被报告为无 material findings / Accept。
审查是否满足固定 basis、隔离目录、自然终态和 provider-owned attribution，决定它能否
作为有效证据；本页不把没有这些字段的模型回复计入验收。

### Runtime / 真实目标项目

2026-08-12 的首个真实 Canary 使用 `feeds-hub@fe680131ab6222fc4553595213f3cf205811ce9d`
作为固定源码基线，选择“分页请求失败后保留卡片并允许手动重试同一页”作为小范围交付：

- 复用目标仓库已有产品、UI、组件、分页 API 和测试资产，没有建立平行 authority；
- 产品与 UI 能力先固定失败、loading、重试、结束和无障碍合同，前端能力再实现；
- 两轮独立前端审查发现并关闭去重、无 `IntersectionObserver` 回退、焦点、
  `hasMore` 语义、payload 校验、测试覆盖和 retry-loading 状态问题；
- 目标仓库原生命令通过：单元测试 72/72、MCP 测试 13/13、Astro check
  0 errors / 0 warnings、TypeScript 与 diff check 通过；
- 本机 system Chrome 完成 9 个 Playwright 场景，数据库 parity 场景因没有
  `DATABASE_URL` 跳过；
- Forgeway 的 Requirement、Task、Source / Automated / Artifact / Runtime /
  Review Evidence 和 replay 均保存在运行期忽略目录，并通过当前 Schema 校验。
- 复核发现目标仓库原先缺少 Google `DESIGN.md` 共享视觉 authority；Canary 随后在
  `feeds-hub/DESIGN.md` 首次建立 colors、typography、spacing、rounded 和 component
  semantics，Feature Spec 改为引用而非复制。固定 `@google/design.md@0.3.0` lint
  为 0 errors / 0 warnings，重复 H2 检查通过，并完成桌面与 390px 错误态两轮
  system Chrome computed-token / focus / overflow 验证。

这个结果把“真实目标项目本地交付”从 `Not verified` 提升为固定基线上的本地
`Runtime-resolved`。它不证明远端同步、部署、Production、真实外部 API、非 Chromium
浏览器或辅助技术输出；这些边界继续保持 `Not verified`。

## Canary 的最小证据包

后续 Canary 复用同一闭环时，至少需要：

1. 目标仓库和固定 commit / worktree 状态；
2. 发现到的原生资产及其 owner，明确哪些是复用、创建、推断或待确认；
3. 至少两个专业能力的输入、输出、权限和结果 envelope；
4. 实现差异、目标项目原生命令、审查记录和可归因 Evidence；
5. 中断 / 恢复记录，以及未执行的浏览器、部署、外部服务和生产项保持
   `Not verified`。

不得把静态合同或合成 fixture 提升为真实交付成功；每次新 Canary 都必须以自己的
固定 basis 和 Evidence 重新验收，不能继承本次结果。

## 研究保留规则

- 保留旧基线和失败 / 未完成状态，不用后续名称重写历史；
- 新验证必须写明观察日期、仓库、commit、命令、环境、输出和限制；
- 不把本页变成 Forgeway runtime 依赖，不复制当前 standards、schemas 或 workflows；
- 外部模型或 Provider 的品牌不是证据等级，只有可复查的固定基线和结果才是证据。
