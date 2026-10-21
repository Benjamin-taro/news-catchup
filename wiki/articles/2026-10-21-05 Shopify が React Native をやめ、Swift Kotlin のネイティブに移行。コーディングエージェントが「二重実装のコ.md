---
type: article
day: 2026-10-21
vote: up
score: 68
kind: 解説
source: "ByteByteGo"
url: "https://blog.bytebytego.com/p/why-shopify-migrated-from-react-native"
main_topic: "[[AI と開発者の働き方]]"
topics:
  - "[[AI と開発者の働き方]]"
  - "[[大手テック企業の動き]]"
entities:
  - "[[Shopify]]"
digest: "[[Digest/2026-10-21]]"
digest_rank: 5
---

# Shopify が React Native をやめ、Swift/Kotlin のネイティブに移行。コーディングエージェントが「二重実装のコスト」を下げた

![](https://substackcdn.com/image/fetch/$s_!MkGV!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8f16b553-719b-4fcb-a2f8-8f02dbe22c71_4158x2062.png)

> [!summary] 一言で
> ByteByteGo が、Shopify がモバイルアプリを React Native からネイティブへ作り直した理由と結果を解説した。

- 2020 年に採用した理由は、機能を iOS と Android で二重に作らないため。2025 年には保守コストが増え、さらにエージェントが機能を片方のプラットフォームからもう片方へ移植できるとプロトタイプで確認できたため、二重実装の不利が薄れた。
- Shop アプリは 12 週間でネイティブ版を公開。iOS の起動は約 3,200ms から約 2,400ms、Android は約 4,400ms から約 2,200ms、Android のアプリサイズは 293MB から 184MB。300 画面超の Shopify アプリ本体が次の移行対象。
- 移行を小さくレビューできる単位に切る社内ツール Helix を作り、ビジネスロジックを UI から切り離してヘッドレスな CLI で挙動をテストできるようにした。

> [!tip] So what
> 「AI でコードが安く書ける」ことが、クロスプラットフォーム基盤という設計判断そのものを動かし始めた例。数字は Shopify の自己申告を ByteByteGo が整理したもの。

**トピック**：[[AI と開発者の働き方]]、[[大手テック企業の動き]]
**登場**：[[Shopify]]
**出典**：[ByteByteGo](https://blog.bytebytego.com/p/why-shopify-migrated-from-react-native)（[[Digest/2026-10-21|2026-10-21 の Digest]] 5 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
