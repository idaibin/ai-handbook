import Link from "next/link";

export default function NotFound() {
  return (
    <section className="emptyState notFoundState">
      <h1>未找到 Registry 记录</h1>
      <p>该 ID 不在当前只读投影中。</p>
      <Link href="/" className="primaryLink">
        返回查询页
      </Link>
    </section>
  );
}
