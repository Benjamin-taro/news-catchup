---
type: article
day: 2026-10-03
vote: up
score: 68
kind: 事故・障害
source: "frankwiles.com"
url: "https://frankwiles.com/posts/i-got-targeted/"
main_topic: "[[セキュリティ事故]]"
topics:
  - "[[セキュリティ事故]]"
entities:
  - "[[Git]]"
digest: "[[Digest/2026-10-03]]"
digest_rank: 7
---

# 「案件の依頼」を装い git の post-checkout フックで認証情報を狙う手口

![](https://frankwiles.com/og/posts/i-got-targeted.jpg?v=1tsueg2)

> [!summary] 一言で
> 開発者の Frank Wiles 氏が、フリーランス案件を装った攻撃に狙われた体験を 10/2 に公開した。

- 相手は NDA と称して Dropbox で資料を共有し、「NDA は別ブランチにある」と言って Git リポジトリをクローンさせようとした。リポジトリ内の `post-checkout` フックが checkout で自動実行され、Vercel 経由で不正なバイナリを取得・実行する仕組み。
- 対策は、クローンした直後にフックを確認する習慣と、怪しいやり取りをセキュリティ担当へすぐ報告すること。

> [!tip] So what
> 開発者を狙う手口は、「依頼を受けてリポジトリを開く」という普段の動作に紛れる。エージェントにリポジトリを触らせる場面でも、フックの実行は同じ種類のリスクになる（これは筆者の主張ではなく私の推測）。

**トピック**：[[セキュリティ事故]]
**登場**：[[Git]]
**出典**：[frankwiles.com](https://frankwiles.com/posts/i-got-targeted/)（[[Digest/2026-10-03|2026-10-03 の Digest]] 7 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
