# Project Delivery System（PDS）历史

## 阶段定义

PDS 是 Platform Spec 脚手架之后、Forgeway 品牌收口之前的产品阶段。主要固定来源：

```text
CHG-PDS-001: project-delivery-system@7d4037bc8e5d89f86cf5fd7685292b363b6858d3
date: 2026-08-09 20:05 +08:00
```

PDS 不是当前产品名。它在 Git 历史中表达“把静态规格扩展成可执行交付体系”的阶段；
`8eaf9c1` 后的当前产品身份是 Forgeway。

## PDS 引入的能力边界

`CHG-PDS-001` 和同 commit 的 README / product foundation 直接记录了以下变化：

1. 从五文件 Markdown 脚手架转为包含标准、workflow、交付元数据合同、Prompt、模板、
   fixtures、tooling、evidence 和 evaluation 的体系。
2. YAML 和 JSON Schema 仅承载交付元数据（例如 owner、basis、状态、引用和结果），
   不复制目标项目的业务 API、数据库或 UI schema。
3. 从产品定义到 Requirement、Domain/Data、Interface、UI、Task、Implementation、
   Automated / Artifact / Runtime Evidence、Review 和 Gap / Change 形成可追踪主线。
4. 目标项目仍拥有自己的源码、迁移、接口合同、设计文件、CI/CD 和运行平台。

这些条目是源文件中的产品设计事实；它们本身不构成任何目标项目的运行结果。

## 关键修正

### 结果必须绑定输入

`be41e04b742549fcdad21c1ca28ab5d0be1f31bc`（2026-08-09 23:23）将 Portfolio result
绑定到输入 Campaign 的 hash、project、Requirement、Gate 和 system basis，并增加
相应负向 fixture。历史意义是把“结果文件存在”提升为“结果和固定输入对应”；不应
推断因此已经执行目标项目。

### 支持多组件拓扑

`af35977d547c5708af45f25fe9795d25857e5bc3`（2026-08-11 01:32）增加 Monolith、
Monorepo、Polyrepo 和多组件的 metadata、manifest placement、component gate 和
证据约束。此变化解决了多仓 owner 放置和结果聚合问题，但不强制项目复制 PDS 的
目录，也没有证明所有拓扑在外部系统成功运行。

### Pilot 的历史位置

`6dfb220` 与 `4c79651` 曾记录 `rustzen-admin` analytics pilot 的 foundation 和
result。Forgeway 收口时这些具体项目材料从可移植评测源中删除，说明 PDS 的实验性
采用记录不应成为通用产品包的一部分。它们可以作为历史线索，但不是本 handbook 的
生产成功证明。

## 为什么继续收口为 Forgeway

PDS 阶段同时承载了产品名、Plugin / Skill 入口、合同命名空间和 runtime 适配方向，
容易把“交付体系”“用户入口”和“能力实现”理解成多个产品。`CHG-FORGEWAY-003`
在 `8eaf9c1` 中明确：

- 当前显示名统一为 `Forgeway`，机器命名空间统一为 `forgeway`；
- Forgeway 是用户侧入口，Professional Skills 是可复用的内部能力 owner；
- capability discovery 在宿主运行时发生，不维护固定 Skill catalog、模型、Provider、
  CLI 或版本清单；
- 没有已验证外部消费者时不提供旧 PDS 别名或兼容树；
- 远端仓库改名、发布、目标项目迁移、部署和生产验证仍是独立授权动作。

## 证据和未决项

**已由源码证明：** PDS 的合同、Schema、fixtures、topology 规则以及向 Forgeway 的
命名空间替换都在本地 Git 历史中可读。

**仍为 `Not verified`：** PDS 或 Forgeway 是否已经让一个目标项目完成完整的真实交付、
是否完成部署 / 生产运行、是否有外部发布包或外部消费者，以及是否发生 GitHub 远端
仓库改名。后续研究若获得这些证据，应新建时间有界的验证记录，不回写为无条件成功。

## 与当前 Forgeway 的关系

PDS 的历史资产只用于解释当前设计选择。Forgeway runtime 不依赖本文件；当前标准、
contracts、workflows、Plugin 和 validators 仍只在 Forgeway 仓库维护。本目录不复制
这些实现文件。
