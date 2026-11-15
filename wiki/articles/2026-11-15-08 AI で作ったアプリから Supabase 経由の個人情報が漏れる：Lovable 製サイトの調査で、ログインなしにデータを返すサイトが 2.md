---
type: article
day: 2026-11-15
vote: up
score: 55
kind: 調査・データ
source: "Crissy Field（調査報告）"
url: "https://www.crissyfield.de/research/lovable-en/"
main_topic: "[[セキュリティ事故]]"
topics:
  - "[[セキュリティ事故]]"
  - "[[AI と開発者の働き方]]"
entities:
  - "[[Lovable]]"
  - "[[Supabase]]"
digest: "[[Digest/2026-11-15]]"
digest_rank: 8
---

# AI で作ったアプリから Supabase 経由の個人情報が漏れる：Lovable 製サイトの調査で、ログインなしにデータを返すサイトが 24,664

![](https://www.crissyfield.de/images/research-lovable-opengraph.jpg)

> [!summary] 一言で
> 独 Crissy Field の調査が、Lovable で作られ Supabase を使うサイトのアクセス制御の不備を示し、パスポート番号や 20 万件超のチャットが読める例を挙げた。

- 159,041 の Lovable プロジェクトを調べ、34,545 が Supabase を使っていた。うち 24,664 のサイトが、ログインなしでページ読み込み時に Supabase のデータを返していた。メールアドレスを含むテーブルは 7,403 サイトで 10,560 件。ただし約 30% という割合は漏えい率の確定値ではなく、サンプルも代表的ではないと調査側が断っている。
- 例として、ドイツのフォーラムの 8 万件超のプロフィールと 20 万件超のチャット、パスポート番号を含む 1,000 件超の記録、28 万通のメールなどが挙がる。原因は Supabase 連携のアクセス制御の誤りで、Lovable の利用規約はデータの扱いの責任を顧客に置く。
- 調査は 11/2 付の Handelsblatt の記事に付随する。ページには Lovable 側の回答は載っていない。推奨は、実データを扱う前に専門家が権限を確認すること。

> [!tip] So what
> 誰でも AI でアプリを作れる状況で、権限設定の責任が作り手に残るという構図が数字で出た。個人開発の自由度と、公開前のセキュリティ確認の担い手の問題が重なる。

**トピック**：[[セキュリティ事故]]、[[AI と開発者の働き方]]
**登場**：[[Lovable]]、[[Supabase]]
**出典**：[Crissy Field（調査報告）](https://www.crissyfield.de/research/lovable-en/)（[[Digest/2026-11-15|2026-11-15 の Digest]] 8 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
