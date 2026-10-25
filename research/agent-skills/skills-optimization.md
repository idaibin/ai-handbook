# Skills 优化记录

## 当前建议与状态

目标：缩短研发总时间、减少 token，同时保持交付质量、完整验收和权限边界。模型已可靠具备的能力不重复包装为 Skill；保留能补足具体缺口、提供项目约束或可执行资源的内容。

| 优先级 | 当前建议 | 状态 |
| --- | --- | --- |
| P0 | 区分执行阶段与质量失败，落实已有提交/反馈规则 | 10/22 既有实现已交付，统一门禁 471 测试、102 路由；晚间研究仅引用，未复跑 |
| P1 | 补跨篇语义重复和 ops 失败反例；运行规则只作最小修订 | 测试候选已实现，生产写作规则保持不变 |
| P1 | 比较无技能、当前和候选的真实端到端增量 | 严格对照与收益仍未验证；现有合成决定不能替代 |
| P1 | 核 compaction/resume 后既有授权、在途状态和完成门禁的恢复资格 | 新增研究候选；先核已有覆盖，无本仓缺陷或收益结论，未启动实现/实测 |
| P2 | 对照官方/上游资料，拒绝重复或无证据规则 | 10 月 21–22 日材料已去重；Graphify/OTel 不扩展，晚间仅新增恢复资格核验候选 |
| P2 | 重复 YAML 键校验链及宿主差异 | 历史待核项，本轮不扩展为无关实现 |

本文件及[目录入口](README.md)是 2026-10-16 新批准的维护范围。旧研究的 [paused 状态与阶段关闭边界](../stage-reviews/2026-08-11-repository-research-stage-closure.md)继续有效；不恢复批量扫描、顺序深研或其它项目。建议不等于执行，也不等于已证实收益。

此处保存研究依据、建议及结果摘要；实现、测试和可执行验收归 [idaibin/skills](https://github.com/idaibin/skills)。后续以固定提交、测试路径及结果链接关联，不在此复制实现或私密会话、邮件、凭据。

## 验证与记录口径

- 三组为 A 无额外技能、B 当前技能、C 精简技能；这与既有 [Skills / Forgeway 配对评测](../../experiments/skills-forgeway-paired-evaluation-v1/README.md)的 A/B/C 分组不同，不混用结论，也不启动该实验。
- 运行前固定任务输入、验收标准、代码基线 SHA、Skills 提交与内容摘要、模型版本/快照（不可得时注明别名及日期）、reasoning/provider/预算、执行器和工具版本、系统环境、网络及权限配置。各组只改变 Skills 条件，使用独立干净环境并记录实际加载内容。
- 对同一固定任务交错运行三组并重复；预先确定任务范围、重复数及质量门槛，避免事后挑最好的一次。将简单路由任务与完整研发任务分开报告；局部工具减少不能替代研发总时间改善。
- 每次记录端到端耗时（含读取、重试、验收）、可得 input/output/cached/总 token、工具调用数、返工次数、人工介入次数及耗时、功能与回归质量、验收完整性、权限越界或额外授权。缺失项写“未知/未采集”，不能填 0；token 不完整时不能宣称 token 节省或等预算优势。
- 验收由独立结果判据决定，保留失败、跳过与基础设施异常；先确认实际运行了哪些断言及覆盖，再判断通过。只有质量和完整验收达标、权限边界保持，且重复对照支持成本改善，才考虑采纳；退化或证据不足则保留原方案或继续验证。

每条记录使用北京时间（Asia/Shanghai）日期，区分来源发生日、记录日与复测日。至少包含：变化与固定来源、具体删改建议、依据、预期收益、验证方案、真实结果及实现/测试链接。预期收益是待验证假设；结果分别标记历史证据、今日静态核验或真实运行。

## 2026-10-26（北京时间）｜宿主资格与验收覆盖增量

### 当前建议与状态

- **不新增运行规则或框架。** Forgeway 既有证据契约已覆盖真实宿主注册、实际事件、加载的 handler bytes、可信 CODE owner 和独立目标读回；本日仅核官方变化的适用边界，不更新 adapter 版本、不启用 hooks。
- **保留 JSX 覆盖披露。** tooling typecheck 成功不能声称检查了未包含的 UI JSX；复用已修 Primer 38 的范围证据，不重复增加同类 canary、不安装依赖。
- **未来资格核验清单候选：** 如果以后明确获准验证 Codex 0.164 的实际 plugin hook，记录实际宿主版本、bundle/content identity 与当前 trust 状态；插件变更或回滚后，未经重新确认的资格不能沿用。该候选不是新 trust 实现或当前执行批准。
- **收益与状态：** 仅只读研究、源代码对照及独立适用性审查；未运行行为评测，无端到端耗时/token/cache 节省结论。Handbook 按需参考设计仍只是已交付设计，未实施。

### 基线、日期与缺口

研究窗口为 2026-10-25 UTC 16:01–16:04，即北京时间 10 月 26 日 00:01–00:04。开始前核对当前任务树及共享研究记录，未发现本日已完成研究；用户明确说明 10 月 25 日份已完成，不重复该日研究。

固定文档读取基线为维护分支 `docs/skills-ops-validation-2026-10-22@917bcf5f32e0daae9d5a21a36b6e549701848460`，blob `ef89e2f700bb40b3e4b0c937985b76b9feedbd1c`，不是仍停在初始化版本的 main。共享记录有 10 月 23–24 日研究交付；10 月 25 日完成采用本次明确交接。未取得 10 月 25 日原始 20 项快照，不伪造逐日差异，也不把归档缺口写成当日未研究；本次不代为补齐 23–25 日正文。

### 可得 20 项采样与限制

GitHub connector 搜索 `skills sort:stars-desc`、page=1、per_page=20，UTC 16:01:20–16:01:27。保留返回原序；[直接搜索入口](https://github.com/search?q=skills&type=repositories&s=stars&o=desc) 返回 HTTP 429，公共 API 搜索的网页读取不可得，未继续重试。connector 不给出明确排序认证、total_count 或 incomplete_results，故**不能认证全站严格前 20 或搜索完整性**。随后 UTC 16:02:31–16:02:41 分别读取这 20 库 metadata/default branch，取得下列 stars/SHA；非原子采样，不重新排序或过滤普通项目。

| 返回原序 | 仓库 | Stars | 固定 HEAD |
| ---: | --- | ---: | --- |
| 1 | [obra/superpowers](https://github.com/obra/superpowers) | 304,900 | [`2ce8aa15d05bd57213e6f746f953aafb7ded7a8b`](https://github.com/obra/superpowers/tree/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b) |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | 303,017 | [`5beb35b040e3de97e54fa9e386d7e42d15c295c2`](https://github.com/mattpocock/skills/tree/5beb35b040e3de97e54fa9e386d7e42d15c295c2) |
| 3 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | 288,568 | [`90606c8315ee09cafc303515c5f33024db6b9882`](https://github.com/affaan-m/ECC/tree/90606c8315ee09cafc303515c5f33024db6b9882) |
| 4 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | 223,654 | [`2c606141936f1eeef17fa3043a72095b4765b9c2`](https://github.com/multica-ai/andrej-karpathy-skills/tree/2c606141936f1eeef17fa3043a72095b4765b9c2) |
| 5 | [anthropics/skills](https://github.com/anthropics/skills) | 183,685 | [`dbd4588f9e1033efb41dad4bef2f7947c8993d44`](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44) |
| 6 | [langgenius/dify](https://github.com/langgenius/dify) | 159,499 | [`f64b57d6565adbabb40f5b95ea9780f381dc0f97`](https://github.com/langgenius/dify/tree/f64b57d6565adbabb40f5b95ea9780f381dc0f97) |
| 7 | [Snailclimb/JavaGuide](https://github.com/Snailclimb/JavaGuide) | 159,248 | [`992dae31eade2a34ba8dbbbcf5ed9de5511325ec`](https://github.com/Snailclimb/JavaGuide/tree/992dae31eade2a34ba8dbbbcf5ed9de5511325ec) |
| 8 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | 148,554 | [`de0a235ad6389ce4afa333b472cdee615a3f3987`](https://github.com/farion1231/cc-switch/tree/de0a235ad6389ce4afa333b472cdee615a3f3987) |
| 9 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 143,009 | [`6c16b23f1bacd0fdf240bb5141ef45e59e82c306`](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/6c16b23f1bacd0fdf240bb5141ef45e59e82c306) |
| 10 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 140,249 | [`d14efff8ed1faa4187f004f79926f428c8074ec7`](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/d14efff8ed1faa4187f004f79926f428c8074ec7) |
| 11 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | 134,899 | [`92741d162b2094ffc2fed58cfbd8ee823e9da62c`](https://github.com/Graphify-Labs/graphify/tree/92741d162b2094ffc2fed58cfbd8ee823e9da62c) |
| 12 | [Chalarangelo/30-seconds-of-code](https://github.com/Chalarangelo/30-seconds-of-code) | 129,324 | [`bd756f8b2283a38560efe83cb30af38324d4e9e9`](https://github.com/Chalarangelo/30-seconds-of-code/tree/bd756f8b2283a38560efe83cb30af38324d4e9e9) |
| 13 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | 114,966 | [`9b68f7ed12b05e7efaff18e65c5a3fc2849fd0a4`](https://github.com/JuliusBrussee/caveman/tree/9b68f7ed12b05e7efaff18e65c5a3fc2849fd0a4) |
| 14 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 110,396 | [`aeac41d4d005999432bb7312f7ff06383a91d59d`](https://github.com/addyosmani/agent-skills/tree/aeac41d4d005999432bb7312f7ff06383a91d59d) |
| 15 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 102,321 | [`12af471f627f866411b4bd785b19646d3672784c`](https://github.com/Leonxlnx/taste-skill/tree/12af471f627f866411b4bd785b19646d3672784c) |
| 16 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | 99,514 | [`fefb0f918eefa7db6daef8cc83787fc7d6f74187`](https://github.com/ruvnet/RuView/tree/fefb0f918eefa7db6daef8cc83787fc7d6f74187) |
| 17 | [florinpop17/app-ideas](https://github.com/florinpop17/app-ideas) | 98,322 | [`9e8dd00f10b881babc273d66949b7ffa0e310097`](https://github.com/florinpop17/app-ideas/tree/9e8dd00f10b881babc273d66949b7ffa0e310097) |
| 18 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | 89,044 | [`81c6be8d87090670c45d08a8f97f9d29c5af0bec`](https://github.com/tt-a1i/archify/tree/81c6be8d87090670c45d08a8f97f9d29c5af0bec) |
| 19 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | 84,410 | [`ce0fa4c114226213e5e5799cc2fea43687dc4aba`](https://github.com/bytedance/deer-flow/tree/ce0fa4c114226213e5e5799cc2fea43687dc4aba) |
| 20 | [lobehub/lobehub](https://github.com/lobehub/lobehub) | 83,481 | [`2c759f545c1382cafa2d81b6b299502c797e5dc9`](https://github.com/lobehub/lobehub/tree/2c759f545c1382cafa2d81b6b299502c797e5dc9) |

仅与既有 10 月 22 日可读完整表比较：集合、返回顺序相同，11 个 HEAD 不同、9 个相同；**这不是 10 月 25→26 日变化统计**。未变来源不重复深读，变化仓库亦未全量逐行审计。Stars 不作为采纳依据。

### 固定来源、反证与具体取舍

| 来源与核验 | 建议 / 风险 / 验收 / 状态 |
| --- | --- |
| [Codex 0.164.0](https://github.com/openai/codex/releases/tag/rust-v0.164.0)，10 月 23 日 04:48:10 UTC 发布，固定 `6aaac694803004a63c6f393d153c96d22521a6b9`；Forgeway 原适配器固定 0.163.0 / `83086188ae0614bd882818ff1aa23f3194962012`。直接读取两个版本的 [PostToolUse input schema](https://github.com/openai/codex/blob/6aaac694803004a63c6f393d153c96d22521a6b9/codex-rs/hooks/schema/generated/post-tool-use.command.input.schema.json)，均为 blob `f92af1dd3249ddf3511ef707c4310329e5b85c80`、1,386 字符，正文相同。 | **不改 envelope、不因版本新而升级。** 仅证明 schema 未变，不证明 0.164 整体运行或真实宿主链已经验证；无运行实测。 |
| [plugin_trust.rs](https://github.com/openai/codex/blob/6aaac694803004a63c6f393d153c96d22521a6b9/codex-rs/hooks/src/engine/plugin_trust.rs)，blob `8fe88effa1c4e447d15af402d637afff69322354`：执行前核 fresh content hash；[hooks_list integration tests](https://github.com/openai/codex/blob/6aaac694803004a63c6f393d153c96d22521a6b9/codex-rs/app-server/tests/suite/v2/hooks_list.rs)覆盖升级和回滚后 Modified/重新批准。对应 [PR #54619](https://github.com/openai/codex/pull/54619) 于 10 月 16 日合入，不能称 10 月 26 日新实现。 | 仅进入未来 **F06 / ops-client 宿主资格清单**：实际版本、bundle identity、当前 trust 必须匹配；变更/回滚后的未确认资格保持阻塞。既有 Forgeway 契约已经要求加载字节和可信宿主绑定，本日独立适用性审查认为无需改运行代码。风险是重复宿主安全实现或将旧 declaration approval 当作当前代码信任；不启用 hooks、不写配置、不迁移 legacy trust。 |
| 实际 Forgeway Primer 修复固定本地 `5e4018d2efbbe86ecab1b37fdb726ac899a47a4e` 的证据与配置直接核读：`tsconfig.tooling.json` 只 include `tooling/stage-registry-contract.ts`，不覆盖 `product-ui/src/main.jsx`。生成 JS/CSS 检查是静态产物证据，非浏览器/AT。 | 对 **dev-tests / UI 验收** 保留检查入口、配置和范围披露，不把 tooling check 计作 JSX 类型安全。若后续获准补覆盖，应由原入口证明 JSX 真正纳入检查且具备所需类型，而非加一条同义提示或重复 sx canary。本日未改依赖、源码或测试。 |
| [Claude Code 2.1.310](https://github.com/anthropics/claude-code/releases/tag/v2.1.310) 有压缩、符号链接提示、无人回应 elicitation 的错误处理修复；[Gemini 10/25 nightly](https://github.com/google-gemini/gemini-cli/releases/tag/v0.67.0-nightly.20261025.gcd1b45c2d) 无详细新增变更说明。 | 仅官方来源旁证，不推定 Codex/Forgeway 已具备同等行为，不安装、不以模型“已经会”为由删具体约束。 |

Codex 两 release 的 compare 返回 330 commits / 300 files，达到文件列表上限；本轮只对上述固定关键文件继续核读，不能宣称完整代码审计。插件内容指纹本身也不是完整运行环境证明，不复制上游实现或其安全配置。

近期已完成的 malformed-gate 分类、loading status、Primer 38 和 canonical pkg/obs CLI 修复，分别保持原发布/本地冻结/独审状态，不借本日研究重新执行或扩大验收。发布版本 `8e26dac37392fc845fc7ca1ebf691f4a1a7a282f` 不代表所有候选已发布；原 browser/reader/host trust 阻塞不因研究解除。无新 runner、无 Tokyo 复跑、无模型调用。

### 结果与停止点

今天的可复核增量是 schema 不变的反证、宿主内容信任的未来资格要点，以及真实 UI typecheck 覆盖边界。**不新增 Forgeway 运行实现**；独立适用性审查支持这一判断。严格全站排序认证和 10 月 25 日原始快照比较仍为未完成证据项，不用重复检索或历史统计伪装补齐。没有 A/B/C 运行、完整 token、耗时、返工或质量配对；不宣称稳定收益。

## 2026-10-22（北京时间，晚间）｜来源增量与压缩恢复资格核验

研究交接记录于 23:07；仓库搜索约为 UTC 14:59，逐库 metadata/默认 HEAD 核验窗口为 UTC 14:59:45–15:01:40（北京时间 22:59:45–23:01:40）。这是研究增量，不是新研发包；今日统一实施的 20 包、471 测试、102 路由沿用前节对应回执，不在本轮重放或重新宣派。

### 本地基线、范围及交接限制

- 固定文档编辑前为本地 `c369a3b01a2855471531bef81b193ea7e71931e8`，299 行、49,987 字节、SHA-256 `5f425288ce6abf669c130f4b86211189c434e8b817f58ace1a08850dc707609d`；编辑端已读全文，交接研究端获得关键原文和覆盖摘要，两者不混称。真实远端 main 仍为 `1859577953ae342dadf265a7e1172d4e62574c5f`，固定文档 blob 为 `23cd78183793b9fe11d897846bac9a4811d8bdc6`；远端初始化正文不替代今日本地终版。
- Skills 公开研究基线仍为 `27f8aa1e1028ec20e1b59d63b167d4b1c48fbca6`；今日已交付本地版本为 `0d34a1d45bd3436afd0cc7f9caf5a56251bb859c`。本地已拆分 `ops-device`，不以远端旧模拟器归属覆盖现有实现；本轮不修改 Skills。
- 复用研究交接的公开来源采样和 compare 元数据；编辑端另核关键固定文件、故障报告和官方发布说明，没有独立重放搜索及 11 个完整 compare，更没有逐行审计全部变更。20 库集合与 10/19 相同，11 库 HEAD 变化、9 库相同；10/21 三个定向提交不是完整新快照。
- 比较中 Dify、Deer-flow、Lobehub 的返回列表均为 300 文件，按达到 API 文件列表上限处理，不能称完整；其它库取得列表也不等于完成代码审计。没有执行上游脚本或模型评测，未取得全站搜索完整性证明。
- 本轮未新增读取私人邮件或 Reddit；X 选题没有在本轮独立核读原帖，不写作新鲜已验证来源或运行证据。公开记录不收录私人任务、运行原文，亦不转载公开 issue 中附带的会话标识或私人上下文。研究交接提及的机器可读采样附件不等于已在仓库归档，本节表格保留实际取得的字段。

### 可得搜索前 20 原序快照

交接采用 GitHub `search_repositories`，查询 `skills sort:stars-desc`、page=1、per_page=20；[查询入口](https://github.com/search?q=skills&type=repositories&s=stars&o=desc)。搜索与逐库核验非原子采样；以下保留返回原序，不剔除 Dify、JavaGuide、RuView 等来制造“20 个 AI 技能库”。Stars 只作采样字段，不作采纳依据；下列时间是固定 HEAD 提交时间，不是 pushed_at。

| 原序 | 仓库 | Stars | 默认分支 | 固定 SHA | HEAD 提交时间 UTC |
| ---: | --- | ---: | --- | --- | --- |
| 1 | [obra/superpowers](https://github.com/obra/superpowers) | 303,514 | main | `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b` | 2026-10-21T21:00:49Z |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | 300,575 | main | `5beb35b040e3de97e54fa9e386d7e42d15c295c2` | 2026-10-19T15:51:40Z |
| 3 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | 286,199 | main | `90606c8315ee09cafc303515c5f33024db6b9882` | 2026-10-20T21:28:23Z |
| 4 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | 222,315 | main | `2c606141936f1eeef17fa3043a72095b4765b9c2` | 2026-04-20T10:05:04Z |
| 5 | [anthropics/skills](https://github.com/anthropics/skills) | 182,947 | main | `dbd4588f9e1033efb41dad4bef2f7947c8993d44` | 2026-10-09T18:45:49Z |
| 6 | [langgenius/dify](https://github.com/langgenius/dify) | 159,251 | main | `0d06488de5dfc0ae49b28be5ffb19c8b819ef364` | 2026-10-22T08:51:52Z |
| 7 | [Snailclimb/JavaGuide](https://github.com/Snailclimb/JavaGuide) | 159,207 | main | `50f02a5984c062fe7221629d0a6a40ec15c26fd7` | 2026-10-16T06:30:59Z |
| 8 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | 147,623 | main | `e4873bc8aa2555225d4867ec2f04b1290f1d21d9` | 2026-10-22T08:50:37Z |
| 9 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 142,653 | main | `6c16b23f1bacd0fdf240bb5141ef45e59e82c306` | 2026-10-21T23:23:38Z |
| 10 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 138,838 | main | `623a9a9037d006ea727f8213f084d02a6b6f11b5` | 2026-10-21T22:06:38Z |
| 11 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | 132,486 | v8 | `847a93f3cab5e2c82ea9170014b21cd2c52a4417` | 2026-10-21T15:22:06Z |
| 12 | [Chalarangelo/30-seconds-of-code](https://github.com/Chalarangelo/30-seconds-of-code) | 129,293 | master | `bd756f8b2283a38560efe83cb30af38324d4e9e9` | 2026-09-09T11:56:56Z |
| 13 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | 114,311 | main | `bad48a0e1df55e05e3f52249afa35ecc1909ee76` | 2026-10-17T21:08:52Z |
| 14 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 109,541 | main | `aeac41d4d005999432bb7312f7ff06383a91d59d` | 2026-10-13T20:21:06Z |
| 15 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 100,951 | main | `6010f91a9935f1c167dfc500fb1a475681892e6b` | 2026-10-20T18:38:06Z |
| 16 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | 99,147 | main | `a1ca023ee872683d160250d47ae3d4d228af55a0` | 2026-10-13T04:04:27Z |
| 17 | [florinpop17/app-ideas](https://github.com/florinpop17/app-ideas) | 98,293 | master | `9e8dd00f10b881babc273d66949b7ffa0e310097` | 2025-10-11T14:51:21Z |
| 18 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | 87,444 | main | `25cf37080fc8b1dbe758a4efc3935b55f3327083` | 2026-10-19T13:54:27Z |
| 19 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | 84,281 | main | `66508d7522015ab6582105130da691e2803eba0d` | 2026-10-22T11:35:43Z |
| 20 | [lobehub/lobehub](https://github.com/lobehub/lobehub) | 83,417 | canary | `9cc0cfbba4b8244b62e4272f584fe266b21c12e6` | 2026-10-22T13:29:56Z |

相对 10/19：Dify/JavaGuide 互换 6/7，Graphify/30-seconds-of-code 互换 11/12，其余顺序不变。旧表已有 stars，本轮不据非原子采样报告精确全站排名或采纳收益，也不把 pushed_at 当 HEAD 时间。

### 11 库变化的比较范围

下表是研究交接返回的 compare 元数据与文件列表计数；链接固定旧表和本表端点。ahead 是提交数，文件数不是审计通过数。

| 仓库 / 固定比较 | Ahead commits | 返回文件 | 覆盖限制 |
| --- | ---: | ---: | --- |
| [obra/superpowers](https://github.com/obra/superpowers/compare/bb92a77741419a4ab5f06e711a283343f1ada0c3...2ce8aa15d05bd57213e6f746f953aafb7ded7a8b) | 2 | 64 | 列表筛选，非逐行审计 |
| [mattpocock/skills](https://github.com/mattpocock/skills/compare/49dd158d1076134a641b33efb035946536778336...5beb35b040e3de97e54fa9e386d7e42d15c295c2) | 1 | 2 | 列表筛选，非逐行审计 |
| [affaan-m/ECC](https://github.com/affaan-m/ECC/compare/76aaa77df6adc5b889e689007bf99b9a4f74af34...90606c8315ee09cafc303515c5f33024db6b9882) | 23 | 60 | 列表筛选，非逐行审计 |
| [langgenius/dify](https://github.com/langgenius/dify/compare/823f40e71fc9e045a9ff2aa903a74b5b001dff33...0d06488de5dfc0ae49b28be5ffb19c8b819ef364) | 85 | 300 | 达列表上限，完整性未核 |
| [farion1231/cc-switch](https://github.com/farion1231/cc-switch/compare/f92ff0b03964188f1cd011d9302ab8869d7a8219...e4873bc8aa2555225d4867ec2f04b1290f1d21d9) | 58 | 259 | 列表筛选，非逐行审计 |
| [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps/compare/874bc13a57aa2ba1266a84f2444808ce3093efb6...6c16b23f1bacd0fdf240bb5141ef45e59e82c306) | 2 | 2 | 列表筛选，非逐行审计 |
| [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/compare/56ea9cf174ed86786187daa9de0e6247cb0747e4...623a9a9037d006ea727f8213f084d02a6b6f11b5) | 2 | 2 | README 翻译/使用说明，不作行为增量 |
| [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify/compare/86c57be8204673c2a1b9849a3292a7dd3ab373d8...847a93f3cab5e2c82ea9170014b21cd2c52a4417) | 37 | 137 | 列表筛选；partial-read 建议已去重 |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill/compare/b9ca2fd8047f4c72d7da90ebc1c1203e57c72cd2...6010f91a9935f1c167dfc500fb1a475681892e6b) | 6 | 55 | 列表筛选；profile 归属建议已去重 |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow/compare/085924a3d0cbf797d23fddc830f14cc6e5531256...66508d7522015ab6582105130da691e2803eba0d) | 93 | 300 | 达列表上限，完整性未核 |
| [lobehub/lobehub](https://github.com/lobehub/lobehub/compare/fae57cfd558b14aff1047212fb4cf564f9ca44f0...9cc0cfbba4b8244b62e4272f584fe266b21c12e6) | 128 | 300 | 达列表上限，完整性未核 |

9 库 HEAD 不变：andrej-karpathy-skills、anthropics/skills、JavaGuide、30-seconds-of-code、Caveman、addyosmani/agent-skills、RuView、app-ideas、Archify。不把其既有正文计作新发布；HEAD 相同亦不证明所有 release、设置或上游内容未变。ECC、cc-switch 等没有形成必须复制的新通用技能证据；大平台变更只完成有界筛选。

### 唯一新增候选：compaction/resume 资格核验

**状态：研究候选，未实现、未运行、未采纳；未证实本仓缺陷，不启动行为实测或新研发包。**

[Superpowers v7.0.1 发布说明](https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/RELEASE-NOTES.md)（10/21）把压缩后的恢复、修复循环和最终审核转到按阶段读取的 references；[SDD 正文](https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/subagent-driven-development/SKILL.md)以既有 ledger/Git 事实恢复任务。[size 测试](https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/tests/skill-size/test-skill-size.sh)实际使用 `wc -c`，达到 20,000 字节即失败；这比非 ASCII 文本的字符限制更严，是上游采用的静态门槛，未在本轮运行，不能推广为所有 Codex/Claude/其它 host 的通用阈值。

[公开故障报告 #2481](https://github.com/obra/superpowers/issues/2481)描述特定 Claude Code 扩展版本中重新附加技能被截到 20,000 字符、五轮上限位于截断点后，任务继续超过 18 轮。报告者明确没有移除 Superpowers 的复现对照，因果未获证实，仅属可能解释之一；发布说明的修复与该案例相关，不证明当前本机 host 已复现或已获修复。只保留故障机制，不转载其会话标识、私人上下文或日志。

编辑端读回本地固定版本 `0d34a1d45bd3436afd0cc7f9caf5a56251bb859c` 的 `skills/dev-tests/references/workflow.md`、`skills/to-task/references/task-ledger.md` 及 `skills/ops-client/references/session-protocols.md`：分别已有恢复时对齐原 case ID/证据、最新暂停与逐项恢复边界、exact-session 绑定和未知提交对账。这是编辑端本地去重结果，不声称外部审查已访问该未推送提交。因此最小下一步仅为**核当前冻结版本已有检查是否覆盖真实压缩/恢复条件**：授权/拒绝和单写交接是否仍可找回、已完成任务是否不重派、未知提交是否先核原请求、关键 reference 是否仍可达、终态是否仍不冒充交付。完全覆盖则结项无实现；缺覆盖且另有明确执行授权时，才考虑在既有测试中补反例，不复制 ledger、重试或完成规则。

未来获准验证时须固定模型/host 版本、输入、代码和工具环境，比较有/无压缩，检查上述可观察结果。平台不能模拟就标未验证，不以文件长度通过代替行为通过。拆分也可能造成引用不可达或恢复加载丢失，不能只按字数缩短采纳。预期减少重复读取/返工只是待验证假设，数值未知；不导入上游完整设计审批或实施流程。

### 补充旁证与不重复采纳项

| 固定公开依据 | 去重判断 |
| --- | --- |
| [Claude Code v2.1.307](https://github.com/anthropics/claude-code/releases/tag/v2.1.307)，10/21 22:17 UTC | 官方说明新增 safety_event，并修复 HTTP MCP 断连重复调用、锁定 keychain 被误报认证问题、睡眠导致连接超时及 transcript token 占位。它们是 Claude Code 的实现说明，不代表本地 Codex/ZCode 已获修复；原 ops-* 的先对账、拒绝不可绕过、ambiguous 门禁及 usage 缺失规则已覆盖核心语义，不再加同义运行规则或强接 OTel。旧占位记录不因升级变为真实用量。 |
| [Claude Code v2.1.308](https://github.com/anthropics/claude-code/releases/tag/v2.1.308)，10/22 | 发布说明仅泛称修复和可靠性改善，无足以新增本仓规则的具体内容。 |
| [Gemini CLI 10/22 nightly](https://github.com/google-gemini/gemini-cli/releases/tag/v0.67.0-nightly.20261022.g09d81bf11) | 官方列出 home 工作目录重复 agent 加载、只读文件/hardlink 原子写保护等修复；它是 nightly，不据此安装、升级或删目标/只读边界。 |
| [Caveman HONEST-NUMBERS 固定正文](https://github.com/JuliusBrussee/caveman/blob/bad48a0e1df55e05e3f52249afa35ecc1909ee76/docs/HONEST-NUMBERS.md) | 原 HEAD 未变，仅作既有主张的反证补读。文风输出缩短不等于 input/context 压缩；十题单次输出长度近似值不证明语义/技术等价、可计费总成本或最新规则效果。既有严格指标已覆盖；若未来授权比较，须有普通“简洁回答”控制，并计 input/output/cache、返工和完整验收。 |
| [Matt Pocock 固定 README](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/README.md) | 插件/技能复制二选一和 orchestrator/discipline 分工仅作来源与重复加载线索；尚无本仓新增缺陷证据，不添全局门禁，不导入 grill、issue 写入或新 wiki 系统。单次 commit 中带日期/版本的事实记录不构成新研究系统需求。 |

[OpenAI ChatGPT & Codex changelog](https://learn.chatgpt.com/docs/changelog)（区别于 10/21 节引用的 API changelog）在研究交接可得页面中最新明确日期仍为 10/14；该检索范围没有取得 10/21–22 新条目。交接的 releases 接口空结果不证明产品无更新；套餐/模型可用性旧消息不重复计为本轮新能力。这里沿用交接范围，不宣称编辑端独立重放全部官方查询。

Graphify partial-read、Deer-flow 失败产物、Taste profile 归属及 Codex hooks/默认零值已在 10/19–21 记录，不重复采纳。角色目录、科学技能清单、热门排名或收藏不触发批量安装；未核 X 选题不形成新任务。

### 本轮真实结果与停止点

本轮产出仅为公开来源研究及固定文档增量、原序快照和范围澄清。未改 Skills、未执行上游脚本、未启动候选行为实验或其它研发包；旧实现验收只引用，不冒称本次复跑。A/B/C、端到端耗时、input/output/cache token、返工、人工介入及质量配对均未采集，缺失不填 0，无提效百分比或采纳收益结论。本轮仅新增恢复资格核验这一研究候选；全部旧日期记录及既有待查项继续保留，不恢复 paused 队列。

## 2026-10-22（北京时间）｜统一接收复盘中的 Skills 改进

用户将本轮 AI 复盘涉及 Skills 的既有改进统一交由本任务承接。两个原实施会话及其子代理已明确停止 Skills 写入、无在途 Git 操作；原工作树 56 路径冻结清单保持原样。其它仓库、安装及发布不在本次接管范围。

继承成果包括 browser/client/device 职责拆分与路由迁移、产品提问与交付策略、写作及测试边界、评估器的固定版本和缺失证据处理，以及若干已有独审修复。本任务保留先前反馈 recorder 修复、语义重复资产和失败阶段用例；只对真实重叠做内容合并，不把他人整树改动冒充原四文件增量。

新增收口限定于已发现缺口：CSS 比较次数采用既有 visual protocol 的 required_comparison_passes，并保留同视口/状态及修正后复验；repo-map render 使用实际 adapter 支持输入；repo-audit 明确只读 probe、意外漂移停止与风险级别；repo-review 对齐既有 computed finding 门槛并修正失实引用。未放宽 Complete 条件，未引入通用新框架。旧 repo-map 运行先于新鲜度文字补充，仍按旧字节引用。

统一候选清单 SHA-256 为 `5ec73b3098381af7ac3b73fb00fdd6e63192475853599c601aaea619ad541402`。固定版本完整门禁实际通过：20 包、471 项 Python 测试、102/102 路由、0 context warnings、协议同步及 DESIGN.md 检查。执行器的 shell 挂起、Node 路径遗漏和库存摘要更新时序失败均保留原始日志，不计作模型行为失败或被后次通过抹去。使用既存工具和进程级环境，没有安装或修改宿主配置。

实现与逐层证据边界见 Skills 的 `docs/quality/unified-skills-validation.md`；原始交接、冻结清单、命令、子代理结果、ZCode 真实终态与本地提交由任务回执关联。继承的审查队列各自保留原会话，不重发不明请求；最终组合审查针对新组合字节及集成风险。旧 454/455/456/461/466 数量不替代本次门禁。实际业务验收、全月成功率/账单分母、完整实时案例重跑和端到端提效仍未验证；不推送、不合 main。

## 2026-10-22（北京时间）｜失败阶段验收与本地采纳边界

本轮从 Skills 固定代码基线 `309d5ebcb5e204911645cc8bf596d595d895850e` 创建隔离非 main 分支，由原执行会话单写。原 Skills 11 个 dirty 文件未纳入；旧维护工作树中与本任务相关的 10 月 19 日文档增量按原字节读回并继承，原工作树及 main 不动。本轮正式提交、独审与最终证据以交付回执为准，不能把工作树存在当成已提交或已安装。

### 已筛选的最小变化

- **采用：** ops-client 增加七类维护反例，覆盖 registry connected 与 CreateProcess 失败的分层、恢复超时、初始化阶段失败、已接收 turn 对账、历史锁屏/他方工具缺失、截断结果和拒绝不可绕过；继续复用现有 submit-once、授权和后置条件规则，不添加新恢复框架。
- **采用：** ZCode 示例在已有配置发现步骤补可执行文件与原 builtin 配置存在/可读检查，并要求按安装布局解析。实际原配置存在于 bundle 的 config/provider 目录；默认 launcher 查找失败不等于安装资源缺失。使用原构建支持的进程内绑定，doctor 退出 0；不读取凭据内容，不建替代配置或切换账号。
- **采用：** 一个可执行缺口已复现：反馈 recorder 接受显式标为 failed-before-submit 的 review-attempt。规范早已禁止，不再加同义说明；实现增加拒绝检查及正反例，保留 submitted / ambiguous 和无新字段旧事件兼容。修改前聚焦 15 项测试一项失败；修改后通过。这不证明过去真实调用曾写入错误事件，也不让 recorder 从缺失字段推断提交事实。
- **仅补回归：** human-writing 六个合成跨篇案例与维护判据。现有 repeated reasoning 规则继续有效；先前额外运行段落没有质量增量证据，不采用。旧六次/36 答复只保留历史边界，不算本次复跑或当前质量认证。
- **拒绝扩展：** 不把 Graphify 提示约束说成 Codex 硬覆盖门禁，不移植厂商业务技能、另造通用日志框架、删除 canonical 协议副本，或强接 OTel Development 遥测。没有本地缺口与收益证据的材料保持参考状态。

### 本地交付关联

Skills 已本地提交至 `feat/skills-ops-acceptance-2026-10-22`，固定 SHA 为 `addbb661b1f8180f35449822aaab0a0eb08ef7b2`，未推送、未合 main、未安装到宿主。提交仅含本任务九个文件；原工作树的 11 个 dirty 文件完整保留，原 main 不动。实现与验证摘要为该提交的 `docs/quality/ops-stage-validation.md`，用例与 recorder 测试仍在 Skills，研究文档不复制其完整实现。

最终 canonical `bash scripts/check-skills.sh` 在锁定环境自然退出 0：19 包、455 项测试、92/92 路由、contract_errors=0、regressions=0、context warnings=0，共享协议及 DESIGN.md 检查通过。92 是干净固定基线的本轮计数；原 dirty 工作树额外三条路由未被裹挟，旧 95 项记录不冒充本轮结果。

真实 ZCode CLI 0.17.0 在同一精确会话先审查冻结八文件，再对六个变更路径复审；provider 账本归属 bigmodel / glm-5.3。两轮均自然 exit 0、projection idle，增量结论无阻断项。首轮建议推动 all-event 拒绝检查、可选字段契约及资产映射补齐；复审通过。两条非阻断证据建议另用临时夹具补验：隔离 I/O 夹具分别证明旧基线接受三类矛盾事件、当前版全部拒绝且不落盘，当前省略 completion_state 的合法 review-attempt 持久化回读匹配；受审源码未再变更。

ZCode plan 模式未能独立执行哈希/测试命令，其结论来自源码、原始 trace 和实际留存门禁日志的静态复核；哈希由本地执行方复算，不把它说成独立 runtime 重跑。原始命令、JSONL、红绿日志、清单、ZCode 原生结果与终态保存在 Skills 忽略的 `.codex/artifacts/` / `.codex/reviews/`，不是已公开上传的材料。提交源码不等于所有会话已加载，也不证明实际客户端业务链或端到端提效。

### 本轮验证与限制

使用已有 Homebrew Python 3.14.6 的缓存环境，PyYAML 6.0.2 / jsonschema 4.25.1 及已有 DESIGN.md 0.4.0 校验器；没有安装。系统 Python 依赖版本不符的第一次 canonical 入口失败保留；改用现存锁定环境后全门禁执行。最终完整门禁、独立审查和提交状态关联 Skills 的固定交付版本及证据，不复用历史 453/95 计数冒充本次通过。

四次新 Codex CLI 0.163.0 决策运行固定八个合成输入，以 B/C/C/B 顺序、同一请求模型 gpt-6.1-sol / medium 和 read-only 工具策略执行，均自然退出 0。B 是基线参考，C 增加配置预检段落；这不是实际客户端重连、业务发送或自动技能路由验收。有效 provider 快照、全局上下文隔离、TTL 子桶和实际账单缺失；输入 usage 的变化大于规则文本变化，存在混杂，因此不宣称 token、成本或真实端到端效率收益。

独立审查只使用用户指定的 ZCode，冻结候选文件哈希和实际日志；报告写出不替代自然终态，Codex 不兼任其审查者。最终受审版本、发现处理和提交证据见本节后的交付关联；未观察的真实业务工作流仍为 Not verified。

## 2026-10-21（北京时间）｜研究交接筛选落库

复用当日研究附件（文件 SHA-256：`14003a805d77746f4e6142e6a871c8ab58674d5073d860a47acb57cbadda511d`），不重做前 20 采集，也不将收藏全量同步。附件中的上游比较属于原研究交接，本轮未重放全部仓库审计。

| 固定来源 | 本地取舍与验收边界 |
| --- | --- |
| [Graphify partial-read 修复](https://github.com/Graphify-Labs/graphify/commit/8a982c4a927e2f185036c339bee7a999364b8c9a) | 参考缺失 coverage / 部分读取误作完整的反例；repo-map 已有覆盖门禁，未证新 runtime 缺口，不加同义规则、不安装 Graphify |
| [Deer-flow 失败输出](https://github.com/bytedance/deer-flow/commit/033fb1aa1f7c9b606380c1cfba7ddf49bcdc77ce) | 借鉴“失败不能作为成功产物”的可执行判据，落实本轮阶段测试；不复制平台工具或整套框架 |
| [Taste profile 清理](https://github.com/Leonxlnx/taste-skill/commit/99c1877abedc943436241a1e9d1a1a9825c152dd) | 只参考归属与后置条件；不把全机进程列表设唯一单写前提，不扩大删除权限 |
| human-writing 既有重复论证门槛和真实系列失败反馈 | 合成固定正反例，保护合法连续性、局部编辑与事实；不录入私人稿件，不增加没有收益的泛化规则 |

[官方 prompt caching](https://developers.openai.com/api/docs/guides/prompt-caching)与 [10 月 20 日 changelog](https://developers.openai.com/api/docs/changelog)已交叉核读：适用模型的 30 分钟/12 小时写入分别为普通输入价 1.25/2.5 倍，是总写入价；读取单独计算。评测需分开普通输入、读取、写入及 TTL 子桶，不能重复计费，字段缺失写缺失。CLI 订阅 usage 不能直接转换为 API 账单，也不能用命中字数或文字缩短代替端到端收益。

### 每日维护覆盖

10 月 15–16 日记录在 main，10 月 18 日在原维护分支已提交，10 月 19 日候选在本分支按原内容继承，10 月 21 日附件在上表去重落库。10 月 20 日完整交付正文尚未在本任务恢复；本轮两次定向 Library 标题检索也未取得正文，这不证明文件不存在。只有后续附件的引用，故不补写一个虚构的 10 月 20 日独立记录。该来源缺口保留为未核，不阻止已取得材料的有界采纳。

## 2026-10-19（北京时间）｜版本去重、解析待查与遥测边界

### 结论与版本适用范围

维持 P0/P1，不新增 Skill 或实施任务。10 月 18 日的两个入口描述与六类截图近邻场景继续沿用，不重复算新增。今日唯一新增待查项是重复 YAML mapping key 的现有校验覆盖；尚未证实本仓缺陷，不启动修复或模型实验。

- **最新本地文档已读回：** `de95cd81403f0f3de4f081493e7b7f74f4c7e503` 的完整固定文档已逐字节核对，SHA-256 为 `b5cf05c0b6ddae6cbc1708b3da91b9f64549cfa56238f29f23f176b65e37565f`，未推送。因此早期研究稿“未读本地最终全文”的限制已解除；以下与该终版去重，旧日期正文保留。
- **真实远端：** 协调方于 UTC 15:20 通过 GitHub 连接读取 [Handbook branches](https://api.github.com/repos/idaibin/ai-handbook/branches?per_page=100) 与 [Skills branches](https://api.github.com/repos/idaibin/skills/branches?per_page=100)。Handbook main 仍为 `1859577953ae342dadf265a7e1172d4e62574c5f`，Skills [main@27f8aa1e1028ec20e1b59d63b167d4b1c48fbca6](https://github.com/idaibin/skills/tree/27f8aa1e1028ec20e1b59d63b167d4b1c48fbca6)、feat/development `349c7106473376780d5557690a1eaec2a9931381` 均未变。这是连接器交接证据，不表示文档编辑端的 Git 连接已恢复。
- **远端与本地区分：** 发布研究基线 27f8aa1 的 20 包、92 个静态 case、tests/dev-tests 并存是旧事实。今日本地只读核为 `b1ab634581b97c9e4eaddfb61a664d489857ded2`、19 包；tests 包已删除，其 api-and-logic、page-walkthrough、test-record、workflow 参考迁入 dev-tests，并新增 performance-measurement。路由清单仍 92 个 case，但内容已变；work-retro 的 validation/eval-cases 也已有提交变化。两个入口 description 则仍与 27f8aa1 相同。上述本地工作区当时干净，不建议重复迁移，不把远端 20 包当本地现状，也不证明安装、宿主加载或测试通过。
- **历史限制：** 028f7afe 的 compare/commit 读取返回 404，完整历史 diff 仍未完成，不能推定提交不存在。固定来源与去重完成即止；门户性能验收优先，旧 paused 队列不恢复。

### 改变来源的适用判断

前 20 集合及原序与 10 月 18 日相同，7 个 HEAD 变化、13 个相同。只深入相关变化文档；大 compare 可能受文件上限影响，不宣称全代码审计。下表为已审研究交接的静态来源判断，编辑时未重放全部网页读取。

| 改变来源与固定证据 | 本仓适用判断 |
| --- | --- |
| [taste-skill CHANGELOG](https://github.com/Leonxlnx/taste-skill/blob/b9ca2fd8047f4c72d7da90ebc1c1203e57c72cd2/CHANGELOG.md)记录 10 月 19 日 2.1.0–2.1.2；2.1.2 修复 description 未引用冒号导致未加载，并增加 strict/uniqueKeys 检查 | 仅引出下方解析覆盖待查。2.1.1 的旧样式显式调用、合并重设计不作为重复合并本地 tests/dev-tests 的理由 |
| [cc-switch 4.0.16](https://github.com/farion1231/cc-switch/blob/f92ff0b03964188f1cd011d9302ab8869d7a8219/docs/release-notes/v4.0.16-en.md)涉及托盘、会话、路由与模型元数据修复 | 是客户端修复，不是模型官方能力发布；未确认本地采用，不改 ops-client/ask-ai、不安装或换账号 |
| [Archify update-awareness](https://github.com/tt-a1i/archify/blob/25cf37080fc8b1dbe758a4efc3935b55f3327083/archify/references/update-awareness.md)将更新摘要视作不可信数据，检查失败不阻塞交付 | 现有证据与权限边界可覆盖；未见本仓更新器适用缺口，不新增流程 |
| [DeerFlow data-analysis](https://github.com/bytedance/deer-flow/blob/085924a3d0cbf797d23fddc830f14cc6e5531256/skills/public/data-analysis/SKILL.md)明确依赖准备、脚本不自动安装、输入顺序/名称绑定缓存 | 具体实现修复，不泛化为全目录规则 |
| [LobeHub acceptance Skill](https://github.com/lobehub/lobehub/blob/fae57cfd558b14aff1047212fb4cf564f9ca44f0/.agents/skills/acceptance/SKILL.md) 0.8.1 统一计划/自写 round 产物、本地逐步保存后单次发布及 preflight/dry-run，依赖 lh 平台 | 现有 dev-tests 及旧 tests 参考已有 case 复用与证据契约，不导入其平台命令或发布门禁 |

Dify 与 awesome-llm-apps 只核 HEAD 变化及提交索引，未取得足以新增本仓规则的相关证据，未深读全部代码。Caveman/Graphify HEAD 未变，不计为今日增量；stars 与上游宣传不证明质量或本地提效。

### 唯一新增待查项：重复 YAML 键覆盖

**状态：待查，未实现、未运行、未采纳；不是本仓缺陷结论，也不新开实施任务。** 目标归现有 [validate-skills.py](https://github.com/idaibin/skills/blob/27f8aa1e1028ec20e1b59d63b167d4b1c48fbca6/scripts/validate-skills.py)及其测试，不建 Skill 或框架。

研究已读发布基线的 [test_validate_skills.py](https://github.com/idaibin/skills/blob/27f8aa1e1028ec20e1b59d63b167d4b1c48fbca6/scripts/test_validate_skills.py)、[check-skills.sh](https://github.com/idaibin/skills/blob/27f8aa1e1028ec20e1b59d63b167d4b1c48fbca6/scripts/check-skills.sh)及 validator：已有 `yaml.safe_load`、类型、长度、OpenAI policy、block scalar 正例，不重复增加通用 YAML 解析。SafeLoader、uniqueKeys 的索引查询无命中，不证明全树没有其他检查，也不证明实际宿主行为；本地 b1ab634 的完整重复键校验链仍未核完。

最小下一步仅是核现有完整校验链与宿主对重复 mapping key 的处理，证实适用缺口后才考虑负例。若后续获执行授权，固定 parser/host 版本，将重复 name/description/policy 键负例与 quoted/block scalar 正例成对核对，保留合法包；静态通过不当宿主加载通过。风险包括宿主差异、YAML merge/别名合法输入与额外维护复杂度。预期可减少解析歧义及不可发现包风险，数值未知，没有成本改善结论。

### 官方工具增量：仅作未来遥测资格待查

独立来源交接核稳定版 Codex 0.163 与 10 月 19 日 alpha.5 的 Pre/PostModelRequest hooks；固定证据为 [model_request.rs](https://github.com/openai/codex/blob/70b3bb6d8814ab3f2045238b4ae14c43da99783b/codex-rs/hooks/src/events/model_request.rs)、[turn.rs](https://github.com/openai/codex/blob/70b3bb6d8814ab3f2045238b4ae14c43da99783b/codex-rs/core/src/session/turn.rs)，源码许可 [Apache-2.0](https://github.com/openai/codex/blob/70b3bb6d8814ab3f2045238b4ae14c43da99783b/LICENSE)。这不是本机版本、安装状态或收益证据；许可也不构成安装或外发授权。

- **数据完整性：** usage 可能为空；cache_write 默认 0 不能解释为厂商实际报告 0。缺 request ID、attempt 序号和时间戳，重试关联仍需单独核定，未知不填 0。
- **安全边界：** command 完整 payload 包含 cwd、transcript_path、session/turn 及未脱敏错误。observation-only 限制输出不能改模型上下文，不是 shell 权限隔离。字段最小化、接收方及具体授权须先明确，不默认启用或传给新接收器。
- **成本边界：** 同步 hook 延迟工具分发，内部 sampling 计时不含全部 hook 开销；比较必须计入端到端成本。

状态为未来遥测资格待查，不启用、不安装、不执行、不宣称收益；无新增模型官方能力结论。研究交接所见 Claude 2.1.303 稳定更新仅泛称 bugfix，不据此删除约束。

### 10 月 19 日搜索快照

检索时间：**2026-10-19 23:06 Asia/Shanghai（UTC 15:06）**。原生 GitHub 仓库搜索 `query=skills sort:stars-desc`，`page=1`，`per_page=20`；[搜索入口](https://github.com/search?q=skills&type=repositories&s=stars&o=desc)。随后逐仓读取 stars 与默认 HEAD，非原子快照；REST search URL 不受 fetch 支持，原生连接不返回 total_count/incomplete_results。20 项 stars/SHA 均取得，保留原序，仍未独立证明全球检索完整性；不是逐仓质量认证。

| 原序 | 仓库 | Stars | 固定 SHA | 相对 10 月 18 日 HEAD |
| ---: | --- | ---: | --- | --- |
| 1 | [obra/superpowers](https://github.com/obra/superpowers) | 301,968 | [`bb92a77741419a4ab5f06e711a283343f1ada0c3`](https://github.com/obra/superpowers/tree/bb92a77741419a4ab5f06e711a283343f1ada0c3) | 相同 |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | 297,082 | [`49dd158d1076134a641b33efb035946536778336`](https://github.com/mattpocock/skills/tree/49dd158d1076134a641b33efb035946536778336) | 相同 |
| 3 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | 283,782 | [`76aaa77df6adc5b889e689007bf99b9a4f74af34`](https://github.com/affaan-m/ECC/tree/76aaa77df6adc5b889e689007bf99b9a4f74af34) | 相同 |
| 4 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | 221,138 | [`2c606141936f1eeef17fa3043a72095b4765b9c2`](https://github.com/multica-ai/andrej-karpathy-skills/tree/2c606141936f1eeef17fa3043a72095b4765b9c2) | 相同 |
| 5 | [anthropics/skills](https://github.com/anthropics/skills) | 182,158 | [`dbd4588f9e1033efb41dad4bef2f7947c8993d44`](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44) | 相同 |
| 6 | [Snailclimb/JavaGuide](https://github.com/Snailclimb/JavaGuide) | 159,138 | [`50f02a5984c062fe7221629d0a6a40ec15c26fd7`](https://github.com/Snailclimb/JavaGuide/tree/50f02a5984c062fe7221629d0a6a40ec15c26fd7) | 相同 |
| 7 | [langgenius/dify](https://github.com/langgenius/dify) | 158,888 | [`823f40e71fc9e045a9ff2aa903a74b5b001dff33`](https://github.com/langgenius/dify/tree/823f40e71fc9e045a9ff2aa903a74b5b001dff33) | 变化 |
| 8 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | 146,280 | [`f92ff0b03964188f1cd011d9302ab8869d7a8219`](https://github.com/farion1231/cc-switch/tree/f92ff0b03964188f1cd011d9302ab8869d7a8219) | 变化 |
| 9 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 142,296 | [`874bc13a57aa2ba1266a84f2444808ce3093efb6`](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/874bc13a57aa2ba1266a84f2444808ce3093efb6) | 变化 |
| 10 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 137,501 | [`56ea9cf174ed86786187daa9de0e6247cb0747e4`](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/56ea9cf174ed86786187daa9de0e6247cb0747e4) | 相同 |
| 11 | [Chalarangelo/30-seconds-of-code](https://github.com/Chalarangelo/30-seconds-of-code) | 129,257 | [`bd756f8b2283a38560efe83cb30af38324d4e9e9`](https://github.com/Chalarangelo/30-seconds-of-code/tree/bd756f8b2283a38560efe83cb30af38324d4e9e9) | 相同 |
| 12 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | 128,872 | [`86c57be8204673c2a1b9849a3292a7dd3ab373d8`](https://github.com/Graphify-Labs/graphify/tree/86c57be8204673c2a1b9849a3292a7dd3ab373d8) | 相同 |
| 13 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | 113,604 | [`bad48a0e1df55e05e3f52249afa35ecc1909ee76`](https://github.com/JuliusBrussee/caveman/tree/bad48a0e1df55e05e3f52249afa35ecc1909ee76) | 相同 |
| 14 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 108,484 | [`aeac41d4d005999432bb7312f7ff06383a91d59d`](https://github.com/addyosmani/agent-skills/tree/aeac41d4d005999432bb7312f7ff06383a91d59d) | 相同 |
| 15 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 99,199 | [`b9ca2fd8047f4c72d7da90ebc1c1203e57c72cd2`](https://github.com/Leonxlnx/taste-skill/tree/b9ca2fd8047f4c72d7da90ebc1c1203e57c72cd2) | 变化 |
| 16 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | 98,755 | [`a1ca023ee872683d160250d47ae3d4d228af55a0`](https://github.com/ruvnet/RuView/tree/a1ca023ee872683d160250d47ae3d4d228af55a0) | 相同 |
| 17 | [florinpop17/app-ideas](https://github.com/florinpop17/app-ideas) | 98,260 | [`9e8dd00f10b881babc273d66949b7ffa0e310097`](https://github.com/florinpop17/app-ideas/tree/9e8dd00f10b881babc273d66949b7ffa0e310097) | 相同 |
| 18 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | 85,718 | [`25cf37080fc8b1dbe758a4efc3935b55f3327083`](https://github.com/tt-a1i/archify/tree/25cf37080fc8b1dbe758a4efc3935b55f3327083) | 变化 |
| 19 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | 84,140 | [`085924a3d0cbf797d23fddc830f14cc6e5531256`](https://github.com/bytedance/deer-flow/tree/085924a3d0cbf797d23fddc830f14cc6e5531256) | 变化 |
| 20 | [lobehub/lobehub](https://github.com/lobehub/lobehub) | 83,327 | [`fae57cfd558b14aff1047212fb4cf564f9ca44f0`](https://github.com/lobehub/lobehub/tree/fae57cfd558b14aff1047212fb4cf564f9ca44f0) | 变化 |

本日两轮可得列表比较中原序不变、20 项 stars 均增加；相同 SHA 仅指记录的默认 HEAD，不推断 release、设置或全部上游内容不变。完整来源检索、全部代码审计及所有 release 比较均未完成。

### 本轮结果与未验证边界

- **真实完成：** 研究交接固定今日快照、审阅相关变化与官方 hooks 源码；编辑读回最新本地文档，区分发布基线与本地已提交迁移，重算 20 行字段差异。来源内容采用已独立审查的研究交接，不称文档编辑端独立重放了全部网页核验。
- **来源覆盖限制：** 10 月 18 日后的相关邮箱限定查询没有新增可用线索；可访问 Reddit 搜索未获改变候选判断的一手增量，X 仅做域名限定搜索且无相关可核结果，未全面站内覆盖。这里只记录范围，不收录私人内容，不写成全网无变化。
- **仍未验证：** 用户实际安装/加载内容、全部代码审计、本地完整重复键校验链、实际宿主行为及 alpha hooks 运行。最新本地文档全文已核，不再列作缺失；本轮未修改 Skills、未跑技能实验、未安装或启用工具。
- **效率数据：** A 无技能/B 当前/C 精简未运行；端到端耗时、input/output/cached/总 token、返工、人工介入与配对质量均未采集，不填 0、不宣称收益。文档提交不改变任何候选的实施、测试或采纳状态。

## 2026-10-18（北京时间）｜既有 P1 收窄与来源快照

### 结论与固定依据

本日不新增 Skill、不启动研发包。保留 P0/P1，将既有路由 P1 收窄为“两个入口描述＋纯截图等缺失反例”；复盘、证据层级、旧结果重绑、动效开关与性能口径已有 owner/reference，先核实际覆盖，避免重复文字。以下是研究交接的静态核验与建议，编辑时只做文档、归档读回及字段比较；规范存在不等于已执行，没有真实 A/B/C、耗时或 token 遥测，不能认定提效。

- **文档基线：** [Handbook main@1859577953ae342dadf265a7e1172d4e62574c5f](https://github.com/idaibin/ai-handbook/blob/1859577953ae342dadf265a7e1172d4e62574c5f/research/agent-skills/skills-optimization.md)，blob `23cd78183793b9fe11d897846bac9a4811d8bdc6`，当时固定文档止于 10 月 16 日；本次编辑已核本地文件与真实远端 main 同基线。
- **Skills 研究基线：** [main@27f8aa1e1028ec20e1b59d63b167d4b1c48fbca6](https://github.com/idaibin/skills/tree/27f8aa1e1028ec20e1b59d63b167d4b1c48fbca6)。交接记录递归树未截断，按 `skills/<name>/SKILL.md` 计 20 包，[路由清单](https://github.com/idaibin/skills/blob/27f8aa1e1028ec20e1b59d63b167d4b1c48fbca6/evals/skill-routing-cases.json)计 92 个 case；只是文件盘点，不证明本地安装、92 条通过或真实路由行为。交接另记 `feat/development@349c7106473376780d5557690a1eaec2a9931381`，不能替代 main 或安装状态。
- **历史边界：** `028f7afe552cd55c0984e3a173b646058682b461` 到该 main 的 GitHub compare 返回 404，历史全量 diff 未完成，不推定历史提交不存在。此次已找回 10 月 17 日未提交候选中的 20 行快照，见下文；不把归档候选或旧审查结论当作已合入 main。
- **范围与停止条件：** 固定来源、去重现有 owner、给出最小候选即止。门户性能验收优先；不恢复旧研究队列，不新增实施任务，不修改 Skills、不运行研发实验。研究只读公共源码与官方网页，未调用外部 AI；文档维护未启动浏览器或运行项目测试。

### 静态增量与去重

以下“已核”均指研究交接对固定文件的静态核验，不是本轮本机运行结果。

| 已核内容 | 最小建议与证据边界 |
| --- | --- |
| [work-retro](https://github.com/idaibin/skills/blob/27f8aa1e1028ec20e1b59d63b167d4b1c48fbca6/skills/work-retro/SKILL.md)及其 [validation](https://github.com/idaibin/skills/blob/27f8aa1e1028ec20e1b59d63b167d4b1c48fbca6/skills/work-retro/references/validation.md)已有跨项目复盘、来源去重、局部例外、先核现有检查、优先导航/修检查/删除、有效 no-finding 与无可比遥测不宣称节省 | 引用现有 owner，不另建复盘规则；只证明规范存在 |
| Matt Pocock retro [当前 49dd158d…](https://github.com/mattpocock/skills/blob/49dd158d1076134a641b33efb035946536778336/skills/engineering/retro/SKILL.md)与[旧 a7d038f6…](https://github.com/mattpocock/skills/blob/a7d038f6bf7f01b516408e95e2fb56e0b338fa6f/skills/engineering/retro/SKILL.md)均为 blob `12149acf2dd23b4514dec57b04a6293eaa1352fa` | 内容未变，不重复移植；上游关于 reviewer 压力等判断不当通用事实 |
| [dev-tests](https://github.com/idaibin/skills/blob/27f8aa1e1028ec20e1b59d63b167d4b1c48fbca6/skills/dev-tests/SKILL.md)已有基线变化后证据重绑、分层证据与完成判据；[roles-and-performance](https://github.com/idaibin/skills/blob/27f8aa1e1028ec20e1b59d63b167d4b1c48fbca6/skills/dev-tests/references/roles-and-performance.md)已分开测量条件、真实结果、动画启用/禁用、fixture 与实际绘制浏览器证据 | 旧绿不默认批准新基线；不复制为新 Skill，覆盖和执行另验 |
| tests 的 [test-record](https://github.com/idaibin/skills/blob/27f8aa1e1028ec20e1b59d63b167d4b1c48fbca6/skills/tests/references/test-record.md)、[workflow](https://github.com/idaibin/skills/blob/27f8aa1e1028ec20e1b59d63b167d4b1c48fbca6/skills/tests/references/workflow.md)、[page-walkthrough](https://github.com/idaibin/skills/blob/27f8aa1e1028ec20e1b59d63b167d4b1c48fbca6/skills/tests/references/page-walkthrough.md)已有完整 assertion 对应当前证据、独立 readback、同状态比较与禁止报告自证 | 仍需真实结果，文档不算实现或通过 |
| [92 条清单](https://github.com/idaibin/skills/blob/27f8aa1e1028ec20e1b59d63b167d4b1c48fbca6/evals/skill-routing-cases.json)没有纯截图专用 case，ops-client 正常 case 混合进程与窗口证据 | 支持收窄 P1 的推断；不能证明当前版本真实误路由 |

### 唯一保留的具体候选：精炼既有 P1

**状态：candidate，未实施、未晋升、未安装。** 这是历史已批准研究方向的具体化，不是新的已证实缺陷或执行授权。

目标仅为 [repo-audit](https://github.com/idaibin/skills/blob/27f8aa1e1028ec20e1b59d63b167d4b1c48fbca6/skills/repo-audit/SKILL.md)与 [ops-client](https://github.com/idaibin/skills/blob/27f8aa1e1028ec20e1b59d63b167d4b1c48fbca6/skills/ops-client/SKILL.md)的 description。前者现用 surface 概括对象，后者列举部分操作机制，纯观察/截图入口仍可更明确。拟议文本为：

- repo-audit：`Audit bounded frontend, Java or Rust source. Excludes screenshot-only inspection and change review.`
- ops-client：`Inspect, capture or operate desktop clients and emulator apps; includes background task submissions and progress queries.`

保留现有 owner、参考、权限、目标身份、运行证据与停止边界。用户上传静态图片只需图像理解，不引入客户端操作；`capture` 不自动授权未请求的桌面控制。收益假设是减少误 owner 与无关仓库读取，字符减少不等于实测 token 减少，节省数值未知。

沿用现有评测记录，只补实际缺失 case，不另建框架。后续获授权时先查 metadata/catalog parity，再在授权宿主取得真实路由 trace，至少覆盖：

1. 命名桌面客户端只观察并截图：ops-client，不读仓库、不操作控件。
2. 模拟器内应用只截图：ops-client，保留 device 绑定。
3. 仅分析上传的静态截图：图像理解，不引入仓库或客户端控制。
4. 审查指定路径源码：repo-audit；固定 diff 仍归 repo-review。
5. 截图并审查指定源码：分别保留两个 owner 及各自证据与权限。
6. capture 权限/能力缺失：仅阻塞 capture，不换路线越过拒绝，不以静态源码代替截图证据。

过度排除截图可能漏掉需源码的视觉审查，简化可能削弱 CLI/后台会话发现，不同宿主对 capture 理解也可能不同。真实对照继续采用上文 A/B/C：冻结模型、仓库、Skills 与环境，交错重复，路由与完整研发分开；质量、完整验收和权限先过关，再比较端到端耗时和实际 token。漏路由、误触发、额外写入、证据降级或无可复现收益则保留当前描述，不因字数更短采纳。**本轮未改 description、未跑宿主路由，质量/时间/token 对照均 Not verified。**

### 官方设计依据与不采纳项

- OpenAI [2026-09-11 Astra 指导](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra)支持明确而短的触发描述、根文档按需路由、按任务读取资料及提前定义完成条件；支持设计候选，不证明跨模型 catalog 的具体约束已可删除，也不覆盖用户权限。
- Anthropic [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)建议只补模型缺少的信息、按风险设自由度、在目标模型上测试。页面本轮研究已读，无可核固定修订号，不宣称今日新增能力。
- OpenAI [2026-01-22 评测指南](https://developers.openai.com/blog/eval-skills)要求关联输入、trace、产物与可检查标准，区分显式/隐式/邻近负例；项目已有相应方法，只补来源，不新建框架。[官方对齐记录](https://github.com/idaibin/skills/blob/27f8aa1e1028ec20e1b59d63b167d4b1c48fbca6/docs/quality/official-skill-alignment.md)标注 Reviewed 2026-07-30，补来源仍需后续授权，不写成已完成本地能力复测。
- [Caveman 固定 README](https://github.com/JuliusBrussee/caveman/blob/bad48a0e1df55e05e3f52249afa35ecc1909ee76/README.md)宣传 54 次运行/18 个问答及另一 85 任务的成本结果，自述 Auto 差异主要与 effort 选择有关且属阶段结果；不构成本项目同模型、任务、权限的配对证据。这里只做资格筛选，未核完整 benchmark，不安装或移植“压缩全部输入”、截断日志方案。
- Stars、README 百分比不能证明适用性或质量；压缩丢失断言、跳过、错误或权限信息会损害完成判据。P0 继续先核实际断言/覆盖；交接所见 runner 测试涉及完整技能读取、失败/顺序与最终写入后检查，但本轮未运行、未完成全部验收分支审计，不能宣布零断言/跳过/截断分支全绿或缺失。无增量证据时保留 no-finding。

### GitHub skills 原顺序快照及上轮比较

研究检索时间：**2026-10-18 22:57 Asia/Shanghai（UTC 14:57，分钟精度）**。GitHub repository search，`q=skills sort:stars-desc`，`page=1`，`per_page=20`；[可复查查询链接](https://github.com/search?q=skills&type=repositories&s=stars&o=desc)。以下为研究交接返回的 20 项原序；stars 来自仓库 metadata，SHA 来自随后读取的默认分支 ref，非原子快照，文档编辑时未重新检索。

连接未返回 `total_count/incomplete_results`，公共搜索页返回 429，raw repository-search fetch 端点不支持，不能独立证明全局完整性；这里只称“本轮可得的前 20 结果”，不补齐、不重排、不只保留 Agent Skills。宽词含普通项目、目录与应用；没有逐仓深读或质量认证。

已读回 **10 月 17 日未提交候选归档**，其文档 SHA-256 为 `73b2134569272c33f94e7657931ba1cd99e0aeff0b012dc4a5c7eda8b21d3c39`，20 行原序 Stars/默认分支/HEAD 可用；该候选未进入 main。上轮搜索窗口为 UTC 15:03:55–15:04:01，metadata/HEAD 补采于 15:04:10–15:04:12，同样非原子且缺检索完整性字段。故修正初稿“未取得上轮完整快照”的范围：**已有两轮可得 20 行的字段比较，仍没有全局完整性证明或完整代码 diff。**

两轮仓库集合相同，默认分支均相同；7 个 HEAD 变化、13 个相同，20 项 stars 均增加。taste-skill 从 16 到 15，RuView 从 15 到 16，其余原序不变。这里的变化仅指两次返回列表；不推广为全站排名。SHA 相同不证明 release、仓库设置或所有上游代码未变，未变来源不重复深读；本日未重采 release 快照，不声称 release 无变化。

| 原序 | 仓库 | Stars | 默认分支 | 固定 SHA |
| ---: | --- | ---: | --- | --- |
| 1 | [obra/superpowers](https://github.com/obra/superpowers) | 301,493 | main | [`bb92a77741419a4ab5f06e711a283343f1ada0c3`](https://github.com/obra/superpowers/tree/bb92a77741419a4ab5f06e711a283343f1ada0c3) |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | 295,814 | main | [`49dd158d1076134a641b33efb035946536778336`](https://github.com/mattpocock/skills/tree/49dd158d1076134a641b33efb035946536778336) |
| 3 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | 283,033 | main | [`76aaa77df6adc5b889e689007bf99b9a4f74af34`](https://github.com/affaan-m/ECC/tree/76aaa77df6adc5b889e689007bf99b9a4f74af34) |
| 4 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | 220,868 | main | [`2c606141936f1eeef17fa3043a72095b4765b9c2`](https://github.com/multica-ai/andrej-karpathy-skills/tree/2c606141936f1eeef17fa3043a72095b4765b9c2) |
| 5 | [anthropics/skills](https://github.com/anthropics/skills) | 181,919 | main | [`dbd4588f9e1033efb41dad4bef2f7947c8993d44`](https://github.com/anthropics/skills/tree/dbd4588f9e1033efb41dad4bef2f7947c8993d44) |
| 6 | [Snailclimb/JavaGuide](https://github.com/Snailclimb/JavaGuide) | 159,112 | main | [`50f02a5984c062fe7221629d0a6a40ec15c26fd7`](https://github.com/Snailclimb/JavaGuide/tree/50f02a5984c062fe7221629d0a6a40ec15c26fd7) |
| 7 | [langgenius/dify](https://github.com/langgenius/dify) | 158,781 | main | [`b953e69a0eb397e625337812e0319ab770f18783`](https://github.com/langgenius/dify/tree/b953e69a0eb397e625337812e0319ab770f18783) |
| 8 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | 145,792 | main | [`77c6dc793d4fbc13bc96163d55d747b02f887a8b`](https://github.com/farion1231/cc-switch/tree/77c6dc793d4fbc13bc96163d55d747b02f887a8b) |
| 9 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 142,196 | main | [`fba2c90c568b3a61d8080be5cee38ed6908d8779`](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/fba2c90c568b3a61d8080be5cee38ed6908d8779) |
| 10 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 137,093 | main | [`56ea9cf174ed86786187daa9de0e6247cb0747e4`](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/56ea9cf174ed86786187daa9de0e6247cb0747e4) |
| 11 | [Chalarangelo/30-seconds-of-code](https://github.com/Chalarangelo/30-seconds-of-code) | 129,243 | master | [`bd756f8b2283a38560efe83cb30af38324d4e9e9`](https://github.com/Chalarangelo/30-seconds-of-code/tree/bd756f8b2283a38560efe83cb30af38324d4e9e9) |
| 12 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | 128,144 | v8 | [`86c57be8204673c2a1b9849a3292a7dd3ab373d8`](https://github.com/Graphify-Labs/graphify/tree/86c57be8204673c2a1b9849a3292a7dd3ab373d8) |
| 13 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | 113,402 | main | [`bad48a0e1df55e05e3f52249afa35ecc1909ee76`](https://github.com/JuliusBrussee/caveman/tree/bad48a0e1df55e05e3f52249afa35ecc1909ee76) |
| 14 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 108,055 | main | [`aeac41d4d005999432bb7312f7ff06383a91d59d`](https://github.com/addyosmani/agent-skills/tree/aeac41d4d005999432bb7312f7ff06383a91d59d) |
| 15 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 98,716 | main | [`f624f37a8c650b9cc550253104925efe4c8de246`](https://github.com/Leonxlnx/taste-skill/tree/f624f37a8c650b9cc550253104925efe4c8de246) |
| 16 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | 98,589 | main | [`a1ca023ee872683d160250d47ae3d4d228af55a0`](https://github.com/ruvnet/RuView/tree/a1ca023ee872683d160250d47ae3d4d228af55a0) |
| 17 | [florinpop17/app-ideas](https://github.com/florinpop17/app-ideas) | 98,234 | master | [`9e8dd00f10b881babc273d66949b7ffa0e310097`](https://github.com/florinpop17/app-ideas/tree/9e8dd00f10b881babc273d66949b7ffa0e310097) |
| 18 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | 85,239 | main | [`b25142deac4b19b293e45b6bf6d69351d3c8f3b6`](https://github.com/tt-a1i/archify/tree/b25142deac4b19b293e45b6bf6d69351d3c8f3b6) |
| 19 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | 84,066 | main | [`62130caa8285826863e4779cd58a9bb1f8298018`](https://github.com/bytedance/deer-flow/tree/62130caa8285826863e4779cd58a9bb1f8298018) |
| 20 | [lobehub/lobehub](https://github.com/lobehub/lobehub) | 83,307 | canary | [`0e6d403e859b59a0a5cfda37849b804cadf84523`](https://github.com/lobehub/lobehub/tree/0e6d403e859b59a0a5cfda37849b804cadf84523) |

两轮 HEAD 变化项如下；链接只固定前后端点，未完成这些区间的代码审计。

| 仓库 | 10 月 17 日 HEAD | 10 月 18 日 HEAD |
| --- | --- | --- |
| langgenius/dify | [a5a937a01d11985ca51eb60c204e84dc88239827](https://github.com/langgenius/dify/tree/a5a937a01d11985ca51eb60c204e84dc88239827) | [b953e69a0eb397e625337812e0319ab770f18783](https://github.com/langgenius/dify/tree/b953e69a0eb397e625337812e0319ab770f18783) |
| farion1231/cc-switch | [73f37c4b2de4acc5c7075cd89073a5728ed41330](https://github.com/farion1231/cc-switch/tree/73f37c4b2de4acc5c7075cd89073a5728ed41330) | [77c6dc793d4fbc13bc96163d55d747b02f887a8b](https://github.com/farion1231/cc-switch/tree/77c6dc793d4fbc13bc96163d55d747b02f887a8b) |
| Shubhamsaboo/awesome-llm-apps | [40b16b66e5257c528059bb93ca9410b55d39278a](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/40b16b66e5257c528059bb93ca9410b55d39278a) | [fba2c90c568b3a61d8080be5cee38ed6908d8779](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/fba2c90c568b3a61d8080be5cee38ed6908d8779) |
| JuliusBrussee/caveman | [81958ad82f2e2da4417778f81f8a3c838d81b798](https://github.com/JuliusBrussee/caveman/tree/81958ad82f2e2da4417778f81f8a3c838d81b798) | [bad48a0e1df55e05e3f52249afa35ecc1909ee76](https://github.com/JuliusBrussee/caveman/tree/bad48a0e1df55e05e3f52249afa35ecc1909ee76) |
| tt-a1i/archify | [88d1ae4498b6a1df610badf690c5406882622d15](https://github.com/tt-a1i/archify/tree/88d1ae4498b6a1df610badf690c5406882622d15) | [b25142deac4b19b293e45b6bf6d69351d3c8f3b6](https://github.com/tt-a1i/archify/tree/b25142deac4b19b293e45b6bf6d69351d3c8f3b6) |
| bytedance/deer-flow | [7e22e42365cccc30d3473d3c2c120e2b13ce163c](https://github.com/bytedance/deer-flow/tree/7e22e42365cccc30d3473d3c2c120e2b13ce163c) | [62130caa8285826863e4779cd58a9bb1f8298018](https://github.com/bytedance/deer-flow/tree/62130caa8285826863e4779cd58a9bb1f8298018) |
| lobehub/lobehub | [7963bbc159bdbb537c5a7299c16d62df155417e5](https://github.com/lobehub/lobehub/tree/7963bbc159bdbb537c5a7299c16d62df155417e5) | [0e6d403e859b59a0a5cfda37849b804cadf84523](https://github.com/lobehub/lobehub/tree/0e6d403e859b59a0a5cfda37849b804cadf84523) |

### 本轮结果与未验证边界

- **研究真实产出：** 固定上述 20 项原序快照，静态盘点 20 包/92 case，去重已有 owner、补官方设计来源，并具体化既有 P1。编辑追加核实了文档基线及 10 月 17 日归档 hash，重算两轮快照字段差异；未重放研究的全部网页读取。
- **仍未验证：** 历史全量 diff、GitHub 前 20 的全局完整性、所有包完整静态/行为验证、本地安装状态、当前功能/性能验收及本地模型能力变化。研究候选未实施，文档保存或提交不能改变此状态。
- **效率数据：** 本日真实对照的端到端耗时、input/output/cached/总 token、返工、人工介入及质量配对均未采集，不能填 0 或声称节省。历史 canary 仍仅为下方单对证据。
- **后续条件：** 继续当前优先任务；仅在另有执行授权且环境空闲时，核上述 P1 的小范围缺失 case，再决定是否保留候选。这是候选验证条件，不是新增实施任务。

## 2026-10-16（北京时间）｜初始化维护范围

- **变化与依据：** 按本次批准建立固定记录；Handbook 维护基线为 `main@61c6c8ae5cd39a98c3e5d421f40afa4c0a2533a5`。仅建立本文件与目录入口。
- **建议：** 优先处理上表 P0/P1；后续针对明确问题核对上游 Skills 的固定提交差异及模型官方发布说明，再决定描述、流程、验收哪些可删、哪些仍需保留。每项记录官方来源、发布日期、模型配置和本地适用差异。
- **预期收益：** 减少误触发、重复读取及无效验收成本；数值未知。
- **验证方案：** 按上述三组口径实施；此次只进行文档、链接和差异核验。
- **真实结果：** 文档初始化；未运行 Skills 对照或模型能力复测，未修改 Skills。模型官方能力变化对照尚未完成，无新增上游能力结论。

## 2026-10-15（北京时间）｜历史证据，非今日复测

以下内容由本次批准的历史交接提供，记录于 2026-10-16；本次未重放原始运行。Skills 固定依据为 [feat/development@028f7afe552cd55c0984e3a173b646058682b461](https://github.com/idaibin/skills/tree/028f7afe552cd55c0984e3a173b646058682b461)，不代表当前分支或安装状态。

| 观察与依据 | 具体建议 | 预期收益（未证实） | 验证方案与真实结果 |
| --- | --- | --- | --- |
| 只读桌面截图曾误路由到 repo-audit | 精简触发描述，明确桌面观察与仓库审查各自的输入、输出及边界；避免为截图引入仓库审查流程 | 减少误路由、无关读取和工具调用 | 固定纯截图、纯仓库审查及混合请求作正反例，比较三组路由与任务质量；本次未复测 |
| 历史摘要为 18 包、69 路由；交接所称当时现状为 19 包，当前路由数未知 | 先固定版本并统一包/路由计数口径，再修正过时描述；不沿用 69 作为当前数量 | 避免错误规模判断与不必要的流程包装 | 对固定清单与实际触发覆盖核对；19 包不是今日重新盘点结果，当前数量未复核 |
| 唯一有效 canary 对照仅一对，token 未知，见下表 | 保留为诊断线索，不据此采纳精简方案或宣称收益 | 新对照可识别读取和路由开销，收益待测 | 固定任务、配置、代码和环境重跑三组并重复；现有证据不足以证明收益 |
| 现有契约已禁止将零断言/缺失断言当作通过 | 先核已有实现与测试覆盖；只为未覆盖的跳过、日志截断等反例补测试或必要规则，删除重复规则须有覆盖依据 | 降低指令冗余，同时保持完整验收 | 检查已有用例与结果判据，确认跳过/截断不会误报通过；本次未核覆盖、未补实现或测试 |
| 模型官方能力变化对照未完成 | 暂不以“模型已会”为由删除具体约束；取得官方变化依据并用无技能组核验后再决策 | 避免重复包装，也避免误删仍有价值的约束 | 官方文档对照与本地固定任务验证均待完成 |

历史 canary 的可得指标：

| 条件 | 耗时 | 工具调用 | token | 返工 / 人工介入 / 质量 / 权限 |
| --- | ---: | ---: | --- | --- |
| 基线 | 23.112 秒 | 2 | 未知 | 未提供，不能推定通过 |
| 候选 | 52.756 秒 | 4 | 未知 | 未提供，不能推定通过 |

这一对中候选耗时更长、工具调用更多；样本仅一对，完整实验配置与其它指标不足，不可推广为稳定退化或收益。后续真实结果与 Skills 实现/测试链接待补，本文件初始化不改变其验证状态。
