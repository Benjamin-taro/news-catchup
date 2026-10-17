---
type: article
day: 2026-10-17
vote: up
score: 95
kind: 解説
source: "claude.dev ブログ"
url: "https://claude.dev/blog/solving-code-review-at-anthropic/"
main_topic: "[[AI と開発者の働き方]]"
topics:
  - "[[AI と開発者の働き方]]"
entities:
  - "[[Anthropic]]"
  - "[[Claude Code]]"
digest: "[[Digest/2026-10-17]]"
digest_rank: 1
---

# Claude Code チームのコードレビュー：AI が約 90% を書き、PR は 2 倍超、revert は 40% 以上減

![](https://claude.dev/blog/solving-code-review-at-anthropic/og.png)

> [!summary] 一言で
> Anthropic の Claude Code チームが 10 月 15 日、AI がコードの約 90% を書く状況でレビューを「最後の関門」から「書いている間に常時動く仕組み」へ作り替えた方法を公開した。

- 6〜9 月でマージされた PR は 2 倍以上、revert 率は 40% 以上減った。モノレポの 1 日あたりの変更数は 5 月の約 2,500 件から 9 月に 30,000 件超へ増えた。
- リスクで承認を分ける。低リスク（ドキュメント等）は自動チェックのみ、中は人間 1 人、高は 2 人。エージェントの承認は人間の承認に数えない。AI のバグレビューは複数エージェントが並列で探し、別のエージェントが投票して誤検知を除く。
- 過去のインシデントや revert を評価セットにして毎日採点した結果、1 回で通る率は 65% → 78%、5 ラウンド以上かかる率は 8.9% → 1.5% になった。人間の仕事は「作るべきか」「高リスクのコード」「証拠の確認」「結果への責任（Land it, you own it）」へ移った。

> [!tip] So what
> 「人が全行を読む」から「何が壊れうるかを機械と人のどちらで捉えるか」へ、レビューの目的を置き換えた具体例。数字は Anthropic 自身の社内計測で、他社の環境にそのまま当てはまるとは限らない。

**トピック**：[[AI と開発者の働き方]]
**登場**：[[Anthropic]]、[[Claude Code]]
**出典**：[claude.dev ブログ](https://claude.dev/blog/solving-code-review-at-anthropic/)・[npaka（note）](https://news.google.com/rss/articles/CBMiT0FVX3lxTE5Yb2gwS2txeWpzdzdBX3pQcmt5MWVLUVUxM1ZPTDBja3Bucnd6RXV4a0MxY0xxS2pITkRGZS12Vld5aU1FTElUMEgzekgwcjg?oc=5)（[[Digest/2026-10-17|2026-10-17 の Digest]] 1 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
