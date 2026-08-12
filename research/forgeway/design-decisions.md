# Forgeway 设计决策历史

以下决策按当前可核验来源整理。`状态`描述证据强度，不表示 handbook 拥有 Forgeway
运行时决策权。

| 决策 | 依据 | 状态 |
| --- | --- | --- |
| Forgeway 是唯一现行产品身份；Platform Spec、PDS、AEF 只保留为历史阶段。 | `CHG-FORGEWAY-003` @ `8eaf9c1`；`product/forgeway-unification-roadmap.md`（2026-08-12 工作树） | `Source-verified`，AEF 的具体历史功能 `Not verified` |
| 不维护 Platform Spec / PDS 双轨兼容树，除非发现真实外部消费者。 | `CHG-PDS-001`、`CHG-FORGEWAY-001`、`CHG-FORGEWAY-003` | `Source-verified` 的源代码决策 |
| 目标项目的产品、源码、迁移、原生接口、UI、测试和运行环境拥有事实权威。 | PDS / Forgeway product foundation、README 和 authority 文档 | `Source-verified` |
| Forgeway 只索引交付 metadata 和证据，不复制目标业务 schema。 | `CHG-PDS-001`、Forgeway README | `Source-verified` |
| Skills 是独立、可复用的专业能力 owner；Forgeway 负责阶段匹配和 handoff，不把 Skill 包名、模型、Provider、CLI 或版本写死。 | `CHG-FORGEWAY-003`、runtime coordinator / handoff 文档 | `Source-verified`（宿主运行时选择仍需运行证据） |
| 缺失或歧义能力 fail closed，不隐式换模型、fallback 或扩大权限。 | Forgeway runtime workflow / capability handoff 文档 | `Source-verified` 的合同；真实宿主行为 `Not verified` |
| 固定 basis、Artifact、Evidence、Gap 和 `Not verified` 不能被一次文档检查互相替代。 | 初始 Platform Spec README、PDS standards、Forgeway evidence 文档 | `Source-verified` 的语义；完整项目闭环 `Not verified` |
| 多仓 / Monorepo 支持通过 owner、component 和 basis metadata 表达，不强制目标项目复制 Forgeway 目录。 | `CHG-FORGEWAY-002`、topology 文档、统一路线图 | `Source-verified` 的设计；跨项目采用 `Not verified` |
| 当前工作流从项目发现、资产建立、Gap、能力调用、实现、测试、审查、证据到交付；新项目和现有项目都可作为入口。 | `product/forgeway-unification-roadmap.md`（2026-08-12 工作树） | 计划性 `Source-verified`；完整 workflow 尚待 WP3 / Canary 证据 |
| GitHub 仓库更名、发布、部署、目标项目 mutation 和生产验证是独立授权动作。 | Forgeway README、`CHG-FORGEWAY-003`、统一路线图 | `Source-verified` 的授权边界；执行状态 `Not verified` |

## 决策解释

### 一个产品入口，多个专业能力

历史上名称逐步从 Platform Spec 到 PDS，再到 Forgeway，反映的是能力范围扩大和执行
入口明确化，而不是要保留三套并行产品。收口把用户-facing 入口、交付合同和能力匹配
放到 Forgeway，把领域专业实现留给 Skills，把项目事实留给目标仓库。

### 历史与运行时分离

研究记录必须保留演进理由，否则未来容易重新引入已经否决的双重事实源；但 runtime
读取历史会把过去的设计选择变成隐式依赖。因此本目录只记录历史、决策和验证边界，
不发布可被 Forgeway 执行器读取的 Schema、workflow 或 Skill 复制品。

### 证据等级不升级

源码读取只证明源码中有某个结构；Schema / fixture 检查只证明该基线的自动化规则；
本地 Plugin / Skill 检查只证明包结构；目标运行、外部服务、部署和生产各有独立门禁。
任何缺失记录都写成 `Not verified`，而不是“推测完成”。

## 尚未决策或不能从历史推出的事项

- 不存在可核验的 AEF 独立仓库或具体产品边界；
- 没有固定的 Skill catalog、模型路由表或 Provider 绑定；
- 尚不能据此选择一个 Canary 目标项目、声明其生产状态或授权远端改名；
- 是否需要旧名称兼容，取决于将来是否发现真实消费者，不能由历史名称本身推出。
