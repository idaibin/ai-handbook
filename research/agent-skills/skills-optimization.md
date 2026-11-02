# Skills 优化记录

## 当前建议与状态

> 2026-11-01（北京时间）更新：增加写作/视觉入口一致性研究与有界上游观察；建议均为待验证候选，不表示已采用或完成行为验收。

目标：缩短研发总时间、减少 token，同时保持交付质量、完整验收和权限边界。模型已可靠具备的能力不重复包装为 Skill；保留能补足具体缺口、提供项目约束或可执行资源的内容。

| 优先级 | 当前建议 | 状态 |
| --- | --- | --- |
| P0 | 先核验收覆盖，再针对跳过、日志截断等缺口补反例；不重复堆叠已有规则 | 待核覆盖、待验证 |
| P1 | 精简路由描述：明确只读桌面截图与仓库审查的触发边界 | 历史误路由支持该候选，尚未实施 |
| P1 | 固定条件对照无技能、当前技能、精简技能，验证端到端增量 | 待执行；历史单对 canary 不能证明收益 |
| P2 | 对照官方模型能力与上游 Skills 变化，删除无增量的描述、流程或验收要求 | 官方能力对照未完成，不先认定冗余 |

本文件及[目录入口](README.md)是 2026-10-16 新批准的维护范围。旧研究的 [paused 状态与阶段关闭边界](../stage-reviews/2026-08-11-repository-research-stage-closure.md)继续有效；不恢复批量扫描、顺序深研或其它项目。建议不等于执行，也不等于已证实收益。

此处保存研究依据、建议及结果摘要；实现、测试和可执行验收归 [idaibin/skills](https://github.com/idaibin/skills)。后续以固定提交、测试路径及结果链接关联，不在此复制实现或私密会话、邮件、凭据。

## 验证与记录口径

- 三组为 A 无额外技能、B 当前技能、C 精简技能；这与既有 [Skills / Forgeway 配对评测](../../experiments/skills-forgeway-paired-evaluation-v1/README.md)的 A/B/C 分组不同，不混用结论，也不启动该实验。
- 运行前固定任务输入、验收标准、代码基线 SHA、Skills 提交与内容摘要、模型版本/快照（不可得时注明别名及日期）、reasoning/provider/预算、执行器和工具版本、系统环境、网络及权限配置。各组只改变 Skills 条件，使用独立干净环境并记录实际加载内容。
- 对同一固定任务交错运行三组并重复；预先确定任务范围、重复数及质量门槛，避免事后挑最好的一次。将简单路由任务与完整研发任务分开报告；局部工具减少不能替代研发总时间改善。
- 每次记录端到端耗时（含读取、重试、验收）、可得 input/output/cached/总 token、工具调用数、返工次数、人工介入次数及耗时、功能与回归质量、验收完整性、权限越界或额外授权。缺失项写“未知/未采集”，不能填 0；token 不完整时不能宣称 token 节省或等预算优势。
- 验收由独立结果判据决定，保留失败、跳过与基础设施异常；先确认实际运行了哪些断言及覆盖，再判断通过。只有质量和完整验收达标、权限边界保持，且重复对照支持成本改善，才考虑采纳；退化或证据不足则保留原方案或继续验证。

每条记录使用北京时间（Asia/Shanghai）日期，区分来源发生日、记录日与复测日。至少包含：变化与固定来源、具体删改建议、依据、预期收益、验证方案、真实结果及实现/测试链接。预期收益是待验证假设；结果分别标记历史证据、今日静态核验或真实运行。

## 2026-11-01（北京时间）｜写作、视觉入口与有界上游观察

### 可复用结论与验证边界

研究范围包括研发、写作、海报、卡片、PPT 与排版。不因新增领域另建协调包，也不把资料收录当采用。
- 源码、已安装副本与实际加载入口应分别核验；源码已有规则时，先查分发/加载一致性，不补同义规则。包索引数量不能代表全部宿主能力。
- 文案语义、格式/图像生产与审批/发布应分别归属；职责声明冲突时保留未核状态，不据入口名字推定已有替代执行能力，也不自动删除供应商工具。
- 静态检查通过不能替代模型行为或权限执行证明。检查器应有能够击穿实际消费者假设的反例；此处不报告新的模型实验或运行验收。

### 待评精简候选

[human-writing content-modes.md 固定来源](https://github.com/idaibin/skills/blob/182a5023e5d91bb1b71725ec4ba219b855d2a57a/skills/human-writing/references/content-modes.md)的短文事实闭包说明，可对照同版本 [Source-Based Editing Check](https://github.com/idaibin/skills/blob/182a5023e5d91bb1b71725ec4ba219b855d2a57a/skills/human-writing/references/fact-integrity.md#source-based-editing-check)，评估改为精确引用并保留短文特有边界。第95–96行多稿信息用途差异不应随之删除。候选尚未实施，也没有模型 A/B 或真实成品验收；文字或字节减少不证明 token、耗时或质量收益。下一步只在固定输入、权限、模型和验收条件下比较源事实保真、格式与多稿用途，记录退化及未知，不用已曝光场景冒充盲测。

### 上游变化：只读定点，不把排序当能力

- [mattpocock/skills 比较](https://github.com/mattpocock/skills/compare/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa...4ae2317ddb22b046e26455e4f9c9b3aaaf62212d)：chief-of-staff 改为优先已有共享 wiki；已有权威文档时应复用，不另建同义台账。新 software-factory 位于 in-progress；其术语和自动任务/发布流程不直接迁入，也不扩当前授权。仓 metadata 为 MIT，未作全许可审计。
- [ui-ux-pro-max 比较](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/compare/28b3b8dee8c976df4fa3e94aed4e092ad43fcb03...9a3f14f7423037ccb8feeb4fee7482291b9c820e)：主要为 AutoClaw 路径/入口兼容，Python 脚本显式解析自身目录。不能称视觉质量提升，也不因新增宿主安装其六个子包；当前无同类已证失败，不复制实现。
- [addyosmani agent-skills quality gate](https://github.com/addyosmani/agent-skills/blob/8bfcc1f9916f2eea55494d8c1fa7f4bde867dd9e/skills/constraint-driven-development/scripts/quality-gate.mjs) 与 [原CLI反例](https://github.com/addyosmani/agent-skills/blob/8bfcc1f9916f2eea55494d8c1fa7f4bde867dd9e/scripts/quality-gate-test.js)：区分阻断发现与报告不可用，覆盖空扫描、未知severity、浏览器错误URL等。仅静态核读，不是运行PASS；有效HTTP地址也不证明正确任务页或完整覆盖。借鉴的是测试实际消费者的失效输入，现有本地门需先核对应缺口，不搬通用新门。

### GitHub skills 本日返回原序

查询 `skills sort:stars-desc`，page1/per_page20；[原搜索入口](https://github.com/search?q=skills&type=repositories&s=stars&o=desc)。搜索UTC 2026-10-31 16:04:57–16:05:05，metadata/default HEAD 16:05:11–16:05:17（BJT11/1 00:04:57–00:05:17）。与10/31快照约24小时5分钟间隔，非完整自然日；20成员/顺序同前，11 HEAD不变、9变化。stars为逐仓metadata时读值，非搜索响应原子值；搜索未给total_count/incomplete_results，不能认证全站完整性。9个compare仅摘要筛选，LobeHub文件返回300可能截断；其余变化未全量审查，未变仓不重读。以下保留当次采样的原序与固定版本；这是一份有界观察，不代表当前实时排序或完整上游审计。

| 原序 | 仓库 | Stars | ΔStars | 默认分支 | 固定 SHA |
| ---: | --- | ---: | ---: | --- | --- |
| 1 | [obra/superpowers](https://github.com/obra/superpowers) | 309841 | +619 | main | [`2ce8aa15d05bd57213e6f746f953aafb7ded7a8b`](https://github.com/obra/superpowers/tree/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b) |
| 2 | [mattpocock/skills](https://github.com/mattpocock/skills) | 308056 | +871 | main | [`4ae2317ddb22b046e26455e4f9c9b3aaaf62212d`](https://github.com/mattpocock/skills/tree/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d) |
| 3 | [affaan-m/ECC](https://github.com/affaan-m/ECC) | 293807 | +634 | main | [`b38be6a7f6350964d59328b52f0624e1d1d552d1`](https://github.com/affaan-m/ECC/tree/b38be6a7f6350964d59328b52f0624e1d1d552d1) |
| 4 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | 227301 | +611 | main | [`2c606141936f1eeef17fa3043a72095b4765b9c2`](https://github.com/multica-ai/andrej-karpathy-skills/tree/2c606141936f1eeef17fa3043a72095b4765b9c2) |
| 5 | [anthropics/skills](https://github.com/anthropics/skills) | 185760 | +697 | main | [`ca45fc496a3436251f191354091d557da31c15b5`](https://github.com/anthropics/skills/tree/ca45fc496a3436251f191354091d557da31c15b5) |
| 6 | [langgenius/dify](https://github.com/langgenius/dify) | 160090 | +83 | main | [`4c521a3c0a1f60607c8a7bcf90792f34adcf18d0`](https://github.com/langgenius/dify/tree/4c521a3c0a1f60607c8a7bcf90792f34adcf18d0) |
| 7 | [Snailclimb/JavaGuide](https://github.com/Snailclimb/JavaGuide) | 159363 | +19 | main | [`992dae31eade2a34ba8dbbbcf5ed9de5511325ec`](https://github.com/Snailclimb/JavaGuide/tree/992dae31eade2a34ba8dbbbcf5ed9de5511325ec) |
| 8 | [farion1231/cc-switch](https://github.com/farion1231/cc-switch) | 150594 | +234 | main | [`66d530d6efb68e57f51a97217b0146684f1990bd`](https://github.com/farion1231/cc-switch/tree/66d530d6efb68e57f51a97217b0146684f1990bd) |
| 9 | [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps) | 143568 | +73 | main | [`6c16b23f1bacd0fdf240bb5141ef45e59e82c306`](https://github.com/Shubhamsaboo/awesome-llm-apps/tree/6c16b23f1bacd0fdf240bb5141ef45e59e82c306) |
| 10 | [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | 143292 | +380 | main | [`9a3f14f7423037ccb8feeb4fee7482291b9c820e`](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/9a3f14f7423037ccb8feeb4fee7482291b9c820e) |
| 11 | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | 139865 | +616 | v8 | [`a0946f962af31b19bff941b453f6dae9a7077c7a`](https://github.com/Graphify-Labs/graphify/tree/a0946f962af31b19bff941b453f6dae9a7077c7a) |
| 12 | [Chalarangelo/30-seconds-of-code](https://github.com/Chalarangelo/30-seconds-of-code) | 129378 | +2 | master | [`bd756f8b2283a38560efe83cb30af38324d4e9e9`](https://github.com/Chalarangelo/30-seconds-of-code/tree/bd756f8b2283a38560efe83cb30af38324d4e9e9) |
| 13 | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | 116473 | +204 | main | [`9b68f7ed12b05e7efaff18e65c5a3fc2849fd0a4`](https://github.com/JuliusBrussee/caveman/tree/9b68f7ed12b05e7efaff18e65c5a3fc2849fd0a4) |
| 14 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 112130 | +210 | main | [`8bfcc1f9916f2eea55494d8c1fa7f4bde867dd9e`](https://github.com/addyosmani/agent-skills/tree/8bfcc1f9916f2eea55494d8c1fa7f4bde867dd9e) |
| 15 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | 106788 | +678 | main | [`12af471f627f866411b4bd785b19646d3672784c`](https://github.com/Leonxlnx/taste-skill/tree/12af471f627f866411b4bd785b19646d3672784c) |
| 16 | [ruvnet/RuView](https://github.com/ruvnet/RuView) | 101838 | +135 | main | [`5728b90949e60e3f908d996997d453147c1794e0`](https://github.com/ruvnet/RuView/tree/5728b90949e60e3f908d996997d453147c1794e0) |
| 17 | [florinpop17/app-ideas](https://github.com/florinpop17/app-ideas) | 98421 | +16 | master | [`9e8dd00f10b881babc273d66949b7ffa0e310097`](https://github.com/florinpop17/app-ideas/tree/9e8dd00f10b881babc273d66949b7ffa0e310097) |
| 18 | [tt-a1i/archify](https://github.com/tt-a1i/archify) | 92049 | +294 | main | [`a4065941f12be7967436261d9934784e381d423c`](https://github.com/tt-a1i/archify/tree/a4065941f12be7967436261d9934784e381d423c) |
| 19 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) | 84762 | +36 | main | [`a9bd03ef572a4898ea1ba977e906408dc2f28d7d`](https://github.com/bytedance/deer-flow/tree/a9bd03ef572a4898ea1ba977e906408dc2f28d7d) |
| 20 | [lobehub/lobehub](https://github.com/lobehub/lobehub) | 83639 | +27 | canary | [`bf259e60ee422d5613f6dff46acaf69119c35a24`](https://github.com/lobehub/lobehub/tree/bf259e60ee422d5613f6dff46acaf69119c35a24) |

**结果与下一条件：** 本日为有界采样及静态阅读；没有运行上游测试、模型调用或真实成品验收。耗时、token、质量收益未知。后续先核既有能力是否已覆盖，再决定是否做获准的局部验证；本记录不授权安装、生成、发布或改动其他项目。

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
