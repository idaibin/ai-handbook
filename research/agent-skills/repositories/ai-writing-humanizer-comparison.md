# “去 AI 味”十项来源审查与 human-writing 更新依据

日期：2026-08-12  
状态：固定版本审查完成；生产 Skill 已选择性更新  
原始线索：[X 帖子](https://x.com/i/status/2087181801458716889)

## 结论

帖子图片中的十项并不是十个同类、独立、经过验证的写作 Skill。固定 Git tree 审查后：

- `taste-skill` 是前端 UI 设计 Skill，不是文字 humanizer。
- `ai-flavor-remover` 只有一份 README 提示词，不是 Agent Skill。
- `chatgpt-comparison-detection` 是 2023 年 HC3 数据与检测代码，不是 Skill，也不能证明当前文本作者身份。
- `Humanizer-zh` 明示继承 `humanizer` 并参考 `stop-slop`，不能算独立证据。
- `nuwa-skill` 主要用于人物思维与表达建模，不是通用去味器。
- 其余项目虽有可复用方法，但多数缺少真实文本质量基准；若照搬示例，还会新增事实、技术机制、指标或第一人称经历。

因此，本次没有合并词语黑名单、标点禁令、固定比例、检测规避或人物模仿。生产更新只吸收了三项能补足现有 `human-writing` 的语义规则：

1. 诊断严重度、改写力度与用户授权范围必须分离。
2. 改写前后核对主体—动作—对象、完成态、强度和受保护片段。
3. 当口号或隐喻把观察、解释和判断压成一团时，只拆开来源已支持的层次，不为解释隐喻而补事实。

## 固定来源与真实分类

| # | 来源 | 固定提交 | 真实类型 | 审查结论 |
| --- | --- | --- | --- | --- |
| 1 | [blader/humanizer](https://github.com/blader/humanizer/tree/523374dee72d67c7b2b5f858ea0094ffda49c3ac) | `523374dee72d67c7b2b5f858ea0094ffda49c3ac` | Markdown Agent Skill | 条件吸收；事实保真规则正确，但多个示例与规则冲突并虚构细节 |
| 2 | [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh/tree/91f3d394db8419c20d67ebe22a96cf8fee0a404b) | `91f3d394db8419c20d67ebe22a96cf8fee0a404b` | 旧版中文翻译/汇编 | 非独立证据；示例系统性增加人物、年份、项目和“我”的经历 |
| 3 | [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop/tree/8da1f030185bdfe8471220585162991eaeb970e9) | `8da1f030185bdfe8471220585162991eaeb970e9` | Markdown Agent Skill | 有用提醒与绝对禁令混杂；示例还违反自身规则 |
| 4 | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill/tree/e988add20dab0fa97d7a76781c48961c8184288e) | `e988add20dab0fa97d7a76781c48961c8184288e` | 前端 UI/视觉设计 Skill | 榜单误分类；只迁移“先读 brief、保留现状、按约束检查”的元方法 |
| 5 | [hylarucoder/ai-flavor-remover](https://github.com/hylarucoder/ai-flavor-remover/tree/919386756cf568edf0ac9bd40ae96a9eeea6e21e) | `919386756cf568edf0ac9bd40ae96a9eeea6e21e` | 单文件提示词 | 不是 Skill；检测率为作者自报且不可复现 |
| 6 | [MrGeDiao/shuorenhua](https://github.com/MrGeDiao/shuorenhua/tree/5a5fe6d82b9fcd6be7c70c0cbd00416caff4e161) | `5a5fe6d82b9fcd6be7c70c0cbd00416caff4e161` | 中文 Agent Skill，含 references/evals/scripts | 方法最完整之一；脚本可运行，但示例仍大量补造实现和指标 |
| 7 | [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill/tree/27642f5bfed2dc1bbf8ee59a2c1ee602a626bbd7) | `27642f5bfed2dc1bbf8ee59a2c1ee602a626bbd7` | 人物建模元 Skill | 跨样本抽取方法可借；第一人称人格扮演与名人声音复现拒绝 |
| 8 | [dongbeixiaohuo/writing-agent](https://github.com/dongbeixiaohuo/writing-agent/tree/cd411cfbc44f03dc0513b2f5ec3804f13896f5eb) | `cd411cfbc44f03dc0513b2f5ec3804f13896f5eb` | 完整写作工作流、agents、Skills、脚本和 App | 工程闭环最强；事实边界、授权语料、局部补丁值得吸收，质量宣传未独立验证 |
| 9 | [Hello-SimpleAI/chatgpt-comparison-detection](https://github.com/Hello-SimpleAI/chatgpt-comparison-detection/tree/1f8c15c28f87e09a5abfd86ee6e15005dc7d2119) | `1f8c15c28f87e09a5abfd86ee6e15005dc7d2119` | HC3 数据集与检测器训练代码 | 不是 Skill；旧模型/旧分布词表不能充当作者身份判决或改稿目标 |
| 10 | [OUBIGFA/De-AI-Prompt-Enhancer-Writer-Booster-SKILL](https://github.com/OUBIGFA/De-AI-Prompt-Enhancer-Writer-Booster-SKILL/tree/b050eefa88af3709ec24fc0b353740ccb151f563) | `b050eefa88af3709ec24fc0b353740ccb151f563` | 两个活动 Markdown Skills 与弱审计脚本 | 保真、结构先行、局部修补可借；硬词表、作者复刻和 README 示例拒绝 |

## 逐项验证摘要

### 1. humanizer

保留其模式簇、稳定术语、模糊归因、假范围、chatbot 残留、diff 旁白、空洞结尾与推测补白检查。拒绝把词、破折号、三项列表或被动句当单点证据。

其最高风险是运行时示例与“保留每个 claim、不得新增事实”的合同相冲突：示例会补入法国大革命原因、缓存层、哈希表、复杂度、性能机制等原文没有的内容，也会删掉原始来源和数字。因此只能吸收抽象编辑动作，不能复制示例。

### 2. Humanizer-zh

仓库明确说明翻译自 `humanizer`、参考 `stop-slop`。24 个编号模式对应 `humanizer` 的旧版本，快速检查和评分又来自 `stop-slop`，所以不是第二份独立验证。

中文版示例更高风险：连续加入机构、年份、采访、项目、软件功能、朋友对话与个人感受。中文没有英文 `-ing` 形态，英文词表和标题大小写规则也不能直译成中文证据。

### 3. stop-slop

可保留“删空话、直写主体、还原具体 claim、避免连续假高潮”。拒绝全禁副词、被动、非人施事、Wh- 开头、破折号和三项列表。这些结构可能承载范围、频率、证据强度、未知行动者、真实对照或清晰枚举。

其推荐示例仍使用自己禁止的破折号、对照、副词和短句，因此示例只代表作者偏好，不能当验证过的 transformation。35/50 一类分数没有校准语料，属于伪精确。

### 4. taste-skill

核心合同是 landing page、portfolio 和 redesign 的 Anti-Slop Frontend Skill。UI 的 hero 字数、卡片、字体、颜色、动画与全局破折号禁令不进入写作规则。

可迁移的只是流程：先读 brief、受众和约束；模糊时只问会改变方向的问题；改造前审计现状；保留已有 voice；交付前执行明确检查。仓库没有文字行为 benchmark。

### 5. ai-flavor-remover

固定 tree 只有 README，没有 `SKILL.md`、frontmatter、references、脚本、测试、样本、模型配置或 LICENSE。所谓检测率下降缺少原文、改稿、检测器版本、运行次数与日志，无法复现。

目的、读者、语气和保留关键数据是合理提示；强行加入情绪、第一人称、感官细节、反问，以及承诺“彻底摆脱机器痕迹”均拒绝。

### 6. shuorenhua

最有价值的是 protected spans、数字与修饰对象绑定、主体—动作—目标—完成态—强度关系账本、场景语域、scope 与力度分离、pattern-first 诊断，以及先保真后风格的双遍回读。

确定性仓库检查可运行，但不能证明 LLM 改写质量。多份 positive examples、scene packs、eval samples 会补出缓存、重试、负责人、版本、CVE、延迟和测试数据；主合同与示例不一致。因此只移植原则和回归思想。

### 7. nuwa-skill

可借跨多个样本和场景抽取稳定特征、区分事实/引文/观察/推断、保留人物内部矛盾、资料不足时声明边界等研究方法。

活动模板同时要求“成为人物”、始终使用第一人称并降低持续免责声明，容易把真实人物履历说成模型亲历。内部代理 fidelity 分数没有原始答卷、真人盲评或外部基准。人物冒充、签名句复刻与“像本人”KPI 均不进入通用写作 Skill。

### 8. writing-agent

这是工程验证最完整的来源：有事实检查、内容哈希失效、授权语料风格建模、局部 humanizer、工作流和大量确定性测试。最值得保留的是：正文变化会使旧事实检查失效；用户没提供经历就明确记录为无；风格阶段禁止新增事实、经历、数字、人物、日期、地点、引语与因果结论。

限制是工程测试主要验证工作流与脚本合同，而非真实读者质量。仓库仍含强制反三项、零感叹号扣分、注入“凌晨三点/朋友老张”等旧规则，以及把模拟读者的愤怒和转发欲当质量标准；这些均拒绝。

### 9. chatgpt-comparison-detection / HC3

固定 tree 没有 Agent Skill，只有 2023 年数据、词频与检测训练代码。其数据来自早期 ChatGPT，论文自身承认来源不平衡、特殊 prompt 可绕过、单句检测更难；仓库也没有证明对当前模型分布有效。

词表混有速率限制、hCaptcha 等采集流程文本，说明表面词项会受数据管道污染。human-writing 因而明确拒绝作者身份判定和检测规避：一个词、标点或检测分数不能授权改稿。

### 10. De-AI Prompt Enhancer

保留“不新增事实、案例、数据、结论”“结构→语气→句式→词语”“局部问题做局部补丁”“无来源权威补来源或降级”“改平改薄就回滚”。

拒绝正文词项清零、固定次数阈值、同义替换逃逸清单和特定在世作者复刻。审计脚本虽然输出 `OK`，但失败条件主要挂在固定 tree 不存在的 `.test/` 路径，对两个活动 Skill 基本没有行为断言。README 还引用固定 tree 中不存在的工具，效果示例会删除事实并新增评价。

## 采用与拒绝账本

| 候选规则 | 处理 | 证据边界 |
| --- | --- | --- |
| 事实、引文、观察、推断分层 | 采用 | 多源重复支持；仍需逐 claim 人工核对 |
| 保护数字及其对象、主体关系、完成态和强度 | 采用并加强 | 可做确定性比较，但同义改写仍需语义审阅 |
| 诊断严重度、改写力度、授权 scope 分离 | 采用 | 防止局部请求变成整篇重构 |
| 口号/隐喻的语义分层 | 采用 | 仅拆来源已有层次，不能补机制 |
| 多样本、跨场景风格画像 | 条件采用 | 只用用户提供或明确授权语料；观测值不是固定配额 |
| 词表、标点、句式和检测分数 | 仅作聚类信号 | 不判作者身份，不见词即删 |
| 主动语态、短句、反问、三项列表 | 依体裁与读者失败判断 | 无通用禁令或最低/最高次数 |
| 增加情绪、第一人称、感官细节和故事 | 仅在来源已有或用户授权时 | 否则属于作者身份与事实虚构 |
| 名人声音与人格模拟 | 拒绝进入通用 Skill | 可抽象功能特征，不复制签名表达或冒充亲历 |
| 优化检测率、保证“像人类” | 拒绝 | 当前证据不足且会把编辑目标变成规避检测 |

## 执行验证

| 来源 | 已执行验证 | 能证明什么 | 不能证明什么 |
| --- | --- | --- | --- |
| humanizer | `python3 scripts/validate-package.py` 通过 | 包结构、版本、规则编号和行数一致 | 改写质量与事实保真 |
| Humanizer-zh / stop-slop / taste-skill / ai-flavor-remover | 静态 tree 与核心文件审查 | 类型、合同、继承、规则冲突 | 行为效果 |
| shuorenhua | Python 编译、`make_blind.py --check`、`check_repo.py` 通过；hard metrics 烟测能抓明显 protected span 丢失 | 84 用例生成物同步、仓库引用完整、粗粒度保留检查可执行 | 历史模型得分与真实文本质量；原始模型输出未入库 |
| nuwa-skill | 核心规则、模板、示例与 quality scripts 静态审查 | 研究流程和结构检查内容 | 人物忠实度；内部代理分数不是外部验证 |
| writing-agent | `npm ci --ignore-scripts`；131 Python tests 通过、2 skipped；脚本、workflow、docs、runtime sync 检查通过 | 工程合同、哈希失效、结构与脚本可靠性 | 真实读者是否认为成稿更自然 |
| HC3 | 全部 15 文件、论文限制与代码路径审查 | 它是旧检测研究而非 Skill；存在域偏移和采集污染风险 | 当前作者身份可靠判定 |
| De-AI | `node scripts/style_audit.js` 输出 `OK`，并审查其失败路径 | 脚本可运行 | 两个活动 Skill 有效；关键断言没有实际测试覆盖 |

生产候选还使用四个互相独立的黑盒代理做了前向行为验证：

- **语义分层：PASS。** 删除“换心手术”后，周二、40% 流量、`3.2% → 1.1%`、继续迁移判断与完成日期未定全部保留，没有补流量去向、执行者或日期。
- **表面形式反误杀：PASS。** 合法被动句、三项列表、破折号、问句和“复核者比执行者重要”的真实对照均原样保留。
- **授权范围：PASS。** 只压缩指定的第二段，标题、其他段落、列表、顺序与未知完成日期未变化，也没有为“稳定性提升”补造机制。
- **长度约束：PASS。** 在 80 字硬约束下保留日期、两个指标、迁移结论和完成日期未定，按读者价值删去过程信息；终稿 62 字，无新增事实或立场变化。

这些用例验证的是本次新增合同在当前模型上的代表性行为，不等于跨模型统计结论。

代表性输入固定为：含 `40%`、`3.2% → 1.1%` 与未知完成日期的“换心手术”段落；含被动句、三项指标、破折号、问句与真实对照的实验段落；明确要求只改第二段、不得移动标题和列表的迁移计划；以及要求 80 字内保留日期、两个指标、结论和不确定性的压缩任务。逐项验收均直接比较源文与终稿，而不是依赖检测器分数。

## 对生产 human-writing 的最小更新

更新文件：

- `skills/human-writing/SKILL.md`
- `skills/human-writing/references/style-diagnostics.md`
- `skills/human-writing/references/eval-cases.md`
- `skills/human-writing/references/quality-rubric.md`

没有重复写入目标 Skill 已具备的规则：事实与来源完整性、受保护文本、模式簇而非黑名单、作者样文优先、不制造第一人称、先保真后风格、最小编辑和拒绝检测规避。新增内容只覆盖本轮审查确认的缺口。

## 限制

- 本报告验证的是固定提交中的实现、规则、示例、脚本和可复现测试，不声称证明任一 Skill 能稳定让文本“更像人”。
- 没有使用 AI 检测器作为成功指标；检测器分数不能证明作者身份，也不是本项目的产品目标。
- 规则采用是语义级重写，没有复制上游长段落、作者范文或人物签名表达。
