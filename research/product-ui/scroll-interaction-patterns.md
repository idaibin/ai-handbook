# 滚动交互检索卡 / Scroll interaction patterns

- 核实日期：2026-10-08。
- 来源线索：[鱼皮 X 帖](https://x.com/yupi996/status/2107735426769551691)。原帖访问返回 403，未直接阅读全文；不以其为技术结论的证据。
- 已阅读主来源：[Motion React scroll animation](https://motion.dev/docs/react-scroll-animations)，涵盖触发、进度联动、视差和竖滚驱动横移的示例；[MDN `position`](https://developer.mozilla.org/en-US/docs/Web/CSS/position)、[scroll snap 基本概念](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_scroll_snap/Basic_concepts) 支持吸附定位和滚动停靠术语。
- 证据级别：官方文档静态阅读；未实现样例、运行浏览器或验证目标项目。

| 中英检索关键词 | 机制与何时用 | 可复用需求表述 |
| --- | --- | --- |
| 滚动触发 / Scroll-triggered | 元素进入或离开视口、达到阈值时触发状态动画。适合卡片入场、内容显现；与滚动距离不要求逐帧对应。Motion 提供 `whileInView`、`useInView` 和 `viewport` 配置。 | “卡片进入可视区域后淡入；明确触发阈值、是否只播放一次及退出后的状态。” |
| 滚动联动 / Scroll-linked | 将滚动位置或 0–1 进度映射为样式值。适合阅读进度、随滚动推进的叙事或图像揭示。Motion 的 `useScroll` 与 `useTransform` 可定义目标元素、起止区间和映射值。 | “以指定容器的滚动进度驱动进度条；标明起止位置及 0–1 到视觉属性的映射。” |
| 视差 / Parallax | 不同图层按不同速度移动，形成深度感；是滚动联动的一种用途。适合需要空间层次的视觉段落。 | “前景与背景采用不同位移范围，背景移动较慢；定义滚动区间、位移幅度及减少动态效果时的表现。” |
| 粘性定位 / Sticky | 元素在滚动容器内到达指定边距后吸附，受包含块边界限制。适合章节标题、分组导航或横移段落的固定视窗；本身不要求动画。 | “章节导航到达容器顶部后吸附，离开所属章节时解除；明确滚动容器和顶部偏移。” |
| 滚动停靠 / Scroll snap | 滚动容器结束一次滚动时对齐到子项的停靠位置。适合卡片、图集或分段内容的对齐；子项不必占满屏幕。明确 `scroll-snap-type` 的轴和严格度，以及子项 `scroll-snap-align`。 | “横向卡片列表滚动后靠近时对齐卡片起点；卡片保持内容所需宽度，不强制整屏；定义停靠轴和松紧程度。” |
| 横向滚动段落 / Horizontal scroll section | Motion 原例用较高的竖向容器与 `position: sticky` 视窗，将竖向 `scrollYProgress` 映射为内容的横向 `x` 位移。适合按滚动推进的横向叙事；并非要求用户直接横向滚轮滚动。 | “用户竖向滚动穿过该段时，固定视窗内的卡片列逐步向左移动；明确段落高度、横移终点和退出后的页面流向。” |

这些是不同维度：触发时机、连续映射、图层速度、布局吸附、滚动终点对齐和运动方向可以按需求组合。例如横向滚动段落可同时使用 Sticky 与 Scroll-linked；Scroll snap 是否加入须另行决定。先描述体验，再选择 CSS 或 Motion 实现。

## 使用边界

- 上表机制按官方文档概括；“适合”和引号内需求是可复用设计推断，不是原帖原文或已完成的项目规范。
- 未测试移动端触控、键盘操作、减弱动态效果、浏览器兼容、性能、不同内容高度和滚动容器嵌套。实际项目需在目标仓库单独验证。
- Motion 文档的横移例使用竖向滚动驱动位移；不可据此把所有 Horizontal scroll 都定义成竖滚驱动，也不可把 Scroll snap 定义成必须整屏切换。
