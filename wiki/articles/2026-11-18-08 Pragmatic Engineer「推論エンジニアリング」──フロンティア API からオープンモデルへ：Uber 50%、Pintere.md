---
type: article
day: 2026-11-18
vote: up
score: 58
kind: 解説
source: "The Pragmatic Engineer"
url: "https://newsletter.pragmaticengineer.com/p/inference-engineering-for-software-engineers"
main_topic: "[[LLM とモデル競争]]"
topics:
  - "[[LLM とモデル競争]]"
  - "[[AI の企業導入]]"
entities: []
digest: "[[Digest/2026-11-18]]"
digest_rank: 8
---

# Pragmatic Engineer「推論エンジニアリング」──フロンティア API からオープンモデルへ：Uber 50%、Pinterest 90%、AT&T 56% のトークン単価減

![](https://substackcdn.com/image/fetch/$s_!k1yV!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8fecea03-44c9-44ef-8f85-fc46e4e4f69a_910x1062.png)

> [!summary] 一言で
> Pragmatic Engineer が、ソフトウェアエンジニアが知っておくべき LLM 推論の運用（モデル・提供元の選び方、遅延、キャッシュ）をまとめた。

- 単価はオープンモデルへの移行で Uber 約 50%、Pinterest 90%、AT&T 56% 下がったとされる。自己申告の稼働率は Anthropic 99.5%、OpenAI 99.97%。タスク単価の比較例は Sonnet 5.5 が 5.46 ドル、Kimi K3 が 2.00 ドル（約 60% 安い）。
- 選ぶときは公開ベンチマークでなく、自社トラフィックでの評価で、トークン単価でなくタスク単価で比べる。提供元ごとの精度は基準モデルの 93〜102% とばらつく。
- 遅延は p95・p99 の尾が重く、原因はノイジーネイバー・コールドスタート・KV キャッシュの再構築。記事はキャッシュの先が有料のため、GPU 構成や投機的デコードの部分は確認できていない。

> [!tip] So what
> LLM を呼ぶ側の技術判断（コスト・遅延・可用性）が、アプリ開発者の仕事に入ってきたことを示す。数字は各社の自己申告や紹介された例。

**トピック**：[[LLM とモデル競争]]、[[AI の企業導入]]
**出典**：[The Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/inference-engineering-for-software-engineers)（[[Digest/2026-11-18|2026-11-18 の Digest]] 8 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
