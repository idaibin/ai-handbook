# Forgeway 演进时间线

本时间线按本地 Git 的可读 commit 编排。它描述源码和文档如何变化，不声称每个阶段
都已经在真实项目中运行成功。

## 1. Platform Spec 脚手架

**基线：** `project-delivery-system@6c5f234a8d3a7a3d46dca3a086bb8b3b6d55b348`，
2026-08-09 08:53（Asia/Shanghai）。

**Source-verified：** 根目录当时只有 `README.md` 和 `docs/` 下的架构、治理、领域模板、
验证说明等五个 Markdown 文件。README 将其描述为脱敏、Markdown-first 的规格与验证
起点，并明确区分目标轴（应该怎样工作）和实现轴（现在怎样工作），同时定义
`Declared`、`Source-resolved`、`Automated`、`Runtime-resolved`、`Gap` 和
`Not verified` 等证据状态。

**保留价值：** 固定 basis、owner、目标 / 实现分离、证据分级和“不能证明就保持
`Not verified`”成为后续体系的核心语义。

**边界：** 该 commit 是当前仓库历史中的一个阶段；本次没有证据证明另有一个独立的
`platform-spec` 仓库、发布包或运行服务。README 的 `{{...}}` 占位符也不是某个真实
项目的交付记录。

## 2. Platform Spec → Project Delivery System

**基线：** `project-delivery-system@7d4037bc8e5d89f86cf5fd7685292b363b6858d3`，
2026-08-09 20:05。

**Source-verified：** 变更记录 `CHG-PDS-001` 说明：五文件静态布局被替换；为命名的
消费者扩大为产品、UI、需求变更、机器元数据、Prompt、tooling、fixtures 和受控证据；
引入 YAML / JSON Schema 仅承载交付元数据，并保留目标项目的 API、数据库和 UI 权威在
项目自身。PDS README 将主线扩展为产品定义、需求、领域 / 数据、接口、UI、Task、
Change、实现、验证和证据。

**为什么需要变化：** 初始 Markdown 脚手架适合验证概念和阅读路径，但无法单独承载
跨阶段的可执行交接、机器校验和正负向 fixture。变化的目标是增加可检查的交付合同，
不是复制目标项目的业务模型。

**未验证项：** `CHG-PDS-001` 明确外部项目交付在固定 SHAs 上执行 Work 之前保持
`Not verified`。因此“引入 11 个项目评测”是当时的采用目标 / 评测设计，不是 11 个
项目已经完成的证据。

## 3. PDS 阶段的合同加固

### 3.1 输入绑定

**基线：** `be41e04b742549fcdad21c1ca28ab5d0be1f31bc`，2026-08-09 23:23。

Portfolio 结果被绑定到输入 Campaign 的哈希、项目、Requirement、Gate 和 system
basis。这一步把“有一份结果”收紧为“结果对应这次固定输入”，并增加了负向 fixture
来拒绝错绑结果。它强化了可追溯性，但本身不证明目标项目执行。

### 3.2 项目拓扑

**基线：** `af35977d547c5708af45f25fe9795d25857e5bc3`，2026-08-11 01:32。

PDS 增加多组件、Monorepo 和 Polyrepo 的 repository / component basis、manifest
placement、gate aggregation、部分结果和证据隔离。设计目的不是强制所有项目使用
同一目录，而是让元数据能指向真实 owner。该 commit 的 56 个文件变更和 fixture 扩展
证明了合同已被实现为源码；不等于所有拓扑已经在外部项目运行验证。

### 3.3 受控 Pilot 记录随后被撤回出可移植源

`6dfb220`（2026-08-11 02:34）和 `4c79651`（2026-08-11 02:39）曾把一个
`rustzen-admin` analytics pilot 的 foundation 和结果写入评测目录。后续 Forgeway
收口 commit `8eaf9c1` 将该具体项目记录从可移植源删除，避免把项目、审查者或执行状态
带进通用产品包。这里能证明“曾有一个受控 pilot 记录”，不能证明真实生产交付已完成。

## 4. PDS → Forgeway

**基线：** `project-delivery-system@8eaf9c1d2cca8706ac3fb126852a0431f97ec3bf`，
2026-08-11 21:36。

**Source-verified：** `CHG-FORGEWAY-001`、`CHG-FORGEWAY-003`、README、Plugin manifest、
coordinator / workflow 文档和 `REQ-FORGEWAY-001` 已统一使用 Forgeway 名称与命名空间；
增加显式 Plugin / coordinator Skill 和 host-neutral capability handoff；删除已提交的
具体项目、模型、CLI 和外部审查执行状态；保留 target / implementation authority、
fixed basis、Evidence、Gap 和 `Not verified`。

**收口理由：** 产品、Plugin、Skill、命令、合同 URN、Artifact ID、文档和本地安装若
各用一套名称，会产生重复入口和双重事实源。`CHG-FORGEWAY-003` 的决定是采用一个
持久身份 `Forgeway` / `forgeway`，不在没有真实外部消费者时增加旧命名兼容别名。

**边界：** 该 commit 证明的是源代码和可移植合同的收口。它没有证明 npm 发布、GitHub
远端改名、目标项目采用、部署或生产运行；runtime 和外部项目仍明确为 `Not verified`。

## 5. 当前产品方向（计划性来源）

`product/forgeway-unification-roadmap.md` 在 2026-08-12 的工作树中把 Forgeway 的
目标进一步描述为：从新想法、空目录或现有仓库开始，发现项目资产，协调专业能力，
一直推进到实现、验证、审查、证据和交付。路线将 WP0（现有 handoff 收口）排在 WP1
产品边界、WP2 资产、WP3 workflow、WP4 历史迁移、WP5 Canary 和 WP6 仓库更名前；
WP2 与 WP4 可以并行，其余按依赖串行。

这段内容是当前计划的 `Source-verified` 记录，但由于读取时仍是工作树文件，不能把
它当成已合并的交付结果。是否执行、通过或进入 runtime，必须以之后的 commit 和
独立 Evidence 为准。

## 6. AEF 的证据边界

当前可核验范围内，`AEF` 只出现在 Forgeway 统一路线图列举历史设计阶段的语句中；
没有找到对应的独立 Git 仓库、commit、可执行包、消费者或运行证据。因此本研究只记
“路线图中的历史标签”，不推断 AEF 的具体功能、版本、时间或仓库边界。
