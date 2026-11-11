---
type: article
day: 2026-11-11
vote: up
score: 88
kind: 解説
source: "ByteByteGo"
url: "https://blog.bytebytego.com/p/how-github-used-ai-to-port-copilot"
main_topic: "[[AI と開発者の働き方]]"
topics:
  - "[[AI と開発者の働き方]]"
entities:
  - "[[GitHub]]"
  - "[[GitHub Copilot]]"
digest: "[[Digest/2026-11-11]]"
digest_rank: 1
---

# GitHub が Copilot の実行基盤 43 万行を、AI エージェント群と開発者 1 人で数か月かけて Rust に移植

![](https://substackcdn.com/image/fetch/$s_!t5iH!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2e64b9e1-d8ca-427a-b096-38cffbb4851e_4024x1604.png)

> [!summary] 一言で
> GitHub は Copilot の共通ランタイムを TypeScript から Rust へ書き直し、AI エージェントを使った開発者 1 人が数か月で終えたという（通常は大人数で約 2 年の規模）。

- 移植対象は本番の TypeScript 約 43 万行（当初見積もりは約 13 万行）。コンポーネントごとに 1 本の PR で置き換え、旧コードは同じ変更で削除した。AI のトークン費用は約 12 万ドル（約 1,360 億トークン）。
- 調整役のエージェントが約 3 万行のファイルを 1 時間かけて分析し、15 の子セッションに分割。複数モデルのレビューエージェントが旧新コードを 1 行ずつ突き合わせ、人間は設計・インターフェース契約・リスクの高い箇所に集中した。
- 結果はクライアント作成から 1 ターン完了までが 5.25 秒から 292 ミリ秒（約 18 倍）、10 クライアント時のメモリ増は 1,383MB から 126MB。一方で、整数が小数になる微妙な退行や、エージェントがテストを弱める懸念が出ており、強い E2E テストが前提だったと書かれている。

> [!tip] So what
> 「書く」作業はエージェントに寄せ、人は設計・契約・検証の仕組みづくりに回るという Q1 の見立てに沿う実例。ただし費用や検証の設計は記事の自己申告で、第三者による品質比較はない。

**トピック**：[[AI と開発者の働き方]]
**登場**：[[GitHub]]、[[GitHub Copilot]]
**出典**：[ByteByteGo](https://blog.bytebytego.com/p/how-github-used-ai-to-port-copilot)（[[Digest/2026-11-11|2026-11-11 の Digest]] 1 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
