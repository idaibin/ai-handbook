# Verification

## Local source checks

```bash
npm run validate:source
```

该检查不依赖第三方包，验证：

- 只有 `src/app`，不存在重复根目录 `app/`；
- 不维护原生 `index.html` / 独立 `.js` 源码；
- Prompt SHA-256 与冻结文本一致；
- `r01-r04` 四个结果身份存在；
- 当前 0/4 图片状态保持真实。

## Full Next.js gate

```bash
npm install
npm run verify
```

验收：

- TypeScript 通过；
- Next.js App Router 构建通过；
- 静态导出包含查询页、列表页与全部详情页；
- React 搜索和过滤可用；
- Prompt 文本与 ImageResult 分区展示；
- 未提供真实证据的图片不会显示为已验证。
