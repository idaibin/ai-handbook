# Forgeway 演进研究

## 结论（截至 2026-08-12）

在本研究使用的源码基线中，`Forgeway` 是唯一的现行产品概念。`Platform Spec`、
`Project Delivery System`（简称 `PDS`）和 `AEF` 只作为设计演进阶段或历史称谓保留；
它们不是 Forgeway 的运行时前置条件，也不是需要另行安装或检出的产品。

这组文档记录“为什么收口到 Forgeway”以及当时能证明到哪一步。它不复制 Forgeway
当前的 standards、schemas、workflows、templates 或 Skill 实现，也不为运行中的
Forgeway 提供执行输入。Forgeway 的当前产品事实仍由
`idaibin/forgeway` 仓库中的产品、标准、合同和 runtime 文档负责；本目录只
保存研究、历史、决策背景和验证边界。

## 研究范围与证据规则

本次范围是本地 Git 历史、当前 Forgeway 源码文档和 `ai-handbook` 的知识治理约定。
没有调用外部服务，没有执行 Git 写操作，也没有把任何目标项目状态写入本目录。

| 标签 | 含义 |
| --- | --- |
| `Source-verified` | 能在给出的仓库路径和固定 commit 中直接读取到的事实。 |
| `Synthesis` | 由多个 `Source-verified` 事实归纳出的演进判断；不等于运行时行为。 |
| `Not verified` | 本次没有直接执行、读取或复现，不能从文档存在推断完成。 |

时间、commit 和路径是结论的一部分。若没有独立的 Platform Spec 或 AEF 仓库、发布包、
目标项目运行记录或生产证据，本研究不补写这些对象，也不把同名概念当成独立产品。

## 文档导航

- [演进时间线](./evolution.md)：从初始 Platform Spec 脚手架到 PDS，再到 Forgeway 的
  源码级变化。
- [Platform Spec 历史](./platform-spec-history.md)：初始五文件脚手架的范围、保留点和
  被后续交付体系替代的部分。
- [Project Delivery System 历史](./project-delivery-history.md)：PDS 阶段引入的交付
  Artifact、机器合同、拓扑和评测边界。
- [设计决策](./design-decisions.md)：收口、权威、Skills、证据和失败关闭等决策及其
  证据等级。
- [验证结果](./validation-results/README.md)：源码、自动化、Artifact、运行时和独立
  Review 的分层记录。

## 固定来源

以下是本研究实际使用的主要来源。表中的 `project-delivery-system` 是这些 commit
产生时的仓库 slug；当前 canonical repository 是 `idaibin/forgeway`，本地目录为
`/Users/daibin/Codex/repos/forgeway`。历史标签保留旧 slug 以准确归属原始证据。

| 来源 | 时间 / 基线 | 用途 |
| --- | --- | --- |
| `project-delivery-system` `6c5f234a8d3a7a3d46dca3a086bb8b3b6d55b348` | 2026-08-09 08:53 +08:00 | 初始 Platform Spec 五文件脚手架。 |
| `project-delivery-system` `7d4037bc8e5d89f86cf5fd7685292b363b6858d3` | 2026-08-09 20:05 +08:00 | Platform Spec → PDS 的结构替换与机器合同引入。 |
| `project-delivery-system` `be41e04b742549fcdad21c1ca28ab5d0be1f31bc` | 2026-08-09 23:23 +08:00 | Portfolio 结果与输入 Campaign 的绑定修正。 |
| `project-delivery-system` `af35977d547c5708af45f25fe9795d25857e5bc3` | 2026-08-11 01:32 +08:00 | 多组件 / Monorepo / Polyrepo 拓扑合同。 |
| `project-delivery-system` `8eaf9c1d2cca8706ac3fb126852a0431f97ec3bf` | 2026-08-11 21:36 +08:00 | Forgeway 品牌、Plugin、Skill 和 host-neutral runtime 收口。 |
| `product/forgeway-unification-roadmap.md`（工作树来源） | 读取于 2026-08-12 | 当前收口路线与 WP0–WP6 的计划性边界；不是本目录的运行时输入。 |

初始脚手架、PDS 和 Forgeway 都出现在同一个本地 Git 历史中。本次没有发现能独立证明
存在的 `platform-spec` 仓库或 AEF 仓库，因此文档使用“阶段”而不是“仓库”表述。

## 使用边界

阅读本目录可以解释设计背景、比较历史证据和定位待验证问题；它不能：

- 选择 Forgeway 的下一阶段、Skill、模型、Provider 或 CLI；
- 覆盖目标项目的产品、源码、迁移、接口、UI、测试或运行时权威；
- 代替 Forgeway 当前的标准、Schema、workflow、Plugin 或验证器；
- 把源码检查、合成 fixture、远程审查或一次本地测试升级成真实项目或生产完成。

任何后续实现都必须回到 Forgeway 当前仓库、目标项目固定 basis 和可复查 Evidence；
若本历史与当前源码冲突，以当前源码和显式决策为准。
