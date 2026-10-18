# Skills 优化记录

## 当前建议与状态

目标：缩短研发总时间、减少 token，同时保持交付质量、完整验收和权限边界。模型已可靠具备的能力不重复包装为 Skill；保留能补足具体缺口、提供项目约束或可执行资源的内容。

| 优先级 | 当前建议 | 状态 |
| --- | --- | --- |
| P0 | 先核验收覆盖，再针对跳过、日志截断等缺口补反例；不重复堆叠已有规则 | 现有规范静态已核；实际覆盖与运行待核 |
| P1 | 精炼 repo-audit / ops-client 两个入口描述，补纯截图等实际缺失反例 | 既有候选收窄；未改描述、未跑真实路由 |
| P1 | 固定条件对照无技能、当前技能、精简技能，验证端到端增量 | 未运行；真实耗时、token 与质量配对未采集 |
| P2 | 对照官方模型能力与上游 Skills 变化，删除无增量的描述、流程或验收要求 | 官方设计依据已补；本地能力与收益对照未做 |

本文件及[目录入口](README.md)是 2026-10-16 新批准的维护范围。旧研究的 [paused 状态与阶段关闭边界](../stage-reviews/2026-08-11-repository-research-stage-closure.md)继续有效；不恢复批量扫描、顺序深研或其它项目。建议不等于执行，也不等于已证实收益。

此处保存研究依据、建议及结果摘要；实现、测试和可执行验收归 [idaibin/skills](https://github.com/idaibin/skills)。后续以固定提交、测试路径及结果链接关联，不在此复制实现或私密会话、邮件、凭据。

## 验证与记录口径

- 三组为 A 无额外技能、B 当前技能、C 精简技能；这与既有 [Skills / Forgeway 配对评测](../../experiments/skills-forgeway-paired-evaluation-v1/README.md)的 A/B/C 分组不同，不混用结论，也不启动该实验。
- 运行前固定任务输入、验收标准、代码基线 SHA、Skills 提交与内容摘要、模型版本/快照（不可得时注明别名及日期）、reasoning/provider/预算、执行器和工具版本、系统环境、网络及权限配置。各组只改变 Skills 条件，使用独立干净环境并记录实际加载内容。
- 对同一固定任务交错运行三组并重复；预先确定任务范围、重复数及质量门槛，避免事后挑最好的一次。将简单路由任务与完整研发任务分开报告；局部工具减少不能替代研发总时间改善。
- 每次记录端到端耗时（含读取、重试、验收）、可得 input/output/cached/总 token、工具调用数、返工次数、人工介入次数及耗时、功能与回归质量、验收完整性、权限越界或额外授权。缺失项写“未知/未采集”，不能填 0；token 不完整时不能宣称 token 节省或等预算优势。
- 验收由独立结果判据决定，保留失败、跳过与基础设施异常；先确认实际运行了哪些断言及覆盖，再判断通过。只有质量和完整验收达标、权限边界保持，且重复对照支持成本改善，才考虑采纳；退化或证据不足则保留原方案或继续验证。

每条记录使用北京时间（Asia/Shanghai）日期，区分来源发生日、记录日与复测日。至少包含：变化与固定来源、具体删改建议、依据、预期收益、验证方案、真实结果及实现/测试链接。预期收益是待验证假设；结果分别标记历史证据、今日静态核验或真实运行。

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
