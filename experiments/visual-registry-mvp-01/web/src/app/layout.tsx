import type { Metadata } from "next";
import Link from "next/link";
import "./globals.css";

export const metadata: Metadata = {
  title: {
    default: "Visual Registry",
    template: "%s · Visual Registry",
  },
  description: "Visual Contract、PromptCase 与独立图片结果的只读查询界面。",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="zh-CN">
      <body>
        <header className="siteHeader">
          <div className="headerInner">
            <Link href="/" className="brand" aria-label="Visual Registry 首页">
              <span className="brandMark">VR</span>
              <span>
                <strong>Visual Registry</strong>
                <small>Prompt 类型与独立图片结果查询</small>
              </span>
            </Link>
            <nav aria-label="主导航">
              <Link href="/">全部</Link>
              <Link href="/styles/">Styles</Link>
              <Link href="/prompts/">Prompts</Link>
            </nav>
            <span className="headerStatus">有效独立图片 0 / 4</span>
          </div>
        </header>
        <main className="pageShell">{children}</main>
      </body>
    </html>
  );
}
