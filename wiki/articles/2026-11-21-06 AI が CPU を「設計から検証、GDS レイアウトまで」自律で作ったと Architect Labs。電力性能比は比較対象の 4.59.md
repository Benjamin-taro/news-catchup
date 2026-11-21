---
type: article
day: 2026-11-21
vote: up
score: 70
kind: 製品・発表
source: "Architect Labs"
url: "https://architectlabs.com/blog/frostbite"
main_topic: "[[AI と開発者の働き方]]"
topics:
  - "[[AI と開発者の働き方]]"
  - "[[LLM とモデル競争]]"
entities:
  - "[[Architect Labs]]"
digest: "[[Digest/2026-11-21]]"
digest_rank: 6
---

# AI が CPU を「設計から検証、GDS レイアウトまで」自律で作ったと Architect Labs。電力性能比は比較対象の 4.59 倍と主張

![](https://main--gleeful-begonia-6bb5f3.netlify.app/_next/static/media/frostbite-cover.3n9ytugnquhlr.jpg)

> [!summary] 一言で
> Architect Labs は 11/18、AI のエージェント群が新しい命令セットと汎用 CPU「Frostbite」を設計し、7nm のレイアウトまで仕上げたと発表した。

- 独自の仕様言語 ASL を Lean に変換して定理証明し、Lean は 80 万行超。システムモデルは RTL に合わせて較正し、電力の推定は約 5% 以内で一致した。
- 結果は、7nm で合成時 800MHz、最終レイアウトで 500MHz。性能/電力の幾何平均は 25 ワークロードで比較 CPU の 4.59 倍（探索に使った 10 件で 6.02 倍、未使用の 15 件で 3.83 倍）、性能/面積は平均 8.77 倍。
- 人の役割は、ワークロードの分類と評価の分割、仕様言語と検証基盤の整備、ガードレールの設定。群が動き出した後は AI が自律で反復したと説明している。

> [!tip] So what
> 設計と検証の両方を AI が回す例で、「設計は人の仕事」という見方に当たる。数字は自社の申告で、実チップでの確認や第三者による再現はこの記事にはない。

**トピック**：[[AI と開発者の働き方]]、[[LLM とモデル競争]]
**登場**：[[Architect Labs]]
**出典**：[Architect Labs](https://architectlabs.com/blog/frostbite)（[[Digest/2026-11-21|2026-11-21 の Digest]] 6 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
