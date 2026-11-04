---
type: article
day: 2026-11-04
vote: up
score: 72
kind: 製品・発表
source: "Publickey（Review Max）"
url: "https://www.publickey1.jp/blog/26/githubcopilot_code_review_maxgithub_universe_2026.html"
main_topic: "[[AI エージェントの基盤と安全性]]"
topics:
  - "[[AI エージェントの基盤と安全性]]"
  - "[[AI と開発者の働き方]]"
entities:
  - "[[GitHub]]"
digest: "[[Digest/2026-11-04]]"
digest_rank: 6
---

# GitHub Universe 2026：Copilot Code Review に複数モデルの「Max」。書き込みスループット 180 倍も 2027 年初頭に

![](https://www.publickey1.jp/2026/copilot-codereviewmax-githubuniverse2603.png)

> [!summary] 一言で
> GitHub が 10 月 28〜29 日の Universe で、複数のモデルで独立にレビューする「Copilot Code Review Max」と、エージェント増加に備えた基盤刷新を発表した。

- Max は既存の Lite・Balanced に加わる 3 段目。複数モデルの独立したレビューエージェントの出力を、集約エージェントが突き合わせて確認してから報告する。ReviewBench の重大度の高い問題の検出で最高の F1 とされるが、数値は未掲載。現在はパブリックプレビュー。
- 基盤は Azure への移行、コンピュートとストレージの分離、書き込みロックをリポジトリ単位からブランチ単位へ。5,000 エージェントが 1 リポジトリで作業して毎秒 7,200 回の書き込みを処理（従来は毎秒数十回）。社内検証で第三者の確認はない。
- 移行は 2027 年初頭までに全ユーザーへ。

> [!tip] So what
> コードを書く側が増えるほどレビューと基盤が詰まる、という前提で各社が動いていることが分かる。レビューを多モデルの AI に寄せる流れは Q1 の見立てを揺らす材料になりうるが、性能の数字は自社評価。

**トピック**：[[AI エージェントの基盤と安全性]]、[[AI と開発者の働き方]]
**登場**：[[GitHub]]
**出典**：[Publickey（Review Max）](https://www.publickey1.jp/blog/26/githubcopilot_code_review_maxgithub_universe_2026.html)・[Publickey（180 倍）](https://www.publickey1.jp/blog/26/github180aigithub_universe_2026.html)（[[Digest/2026-11-04|2026-11-04 の Digest]] 6 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
