---
type: article
day: 2026-11-24
vote: up
score: 92
kind: 製品・発表
source: "TechCrunch"
url: "https://techcrunch.com/2026/11/23/anthropic-launches-claude-ship-letting-ai-agents-review-fix-and-approve-code-changes/"
main_topic: "[[AI と開発者の働き方]]"
topics:
  - "[[AI と開発者の働き方]]"
  - "[[AI エージェントの基盤と安全性]]"
entities:
  - "[[Anthropic]]"
  - "[[Claude Code]]"
digest: "[[Digest/2026-11-24]]"
digest_rank: 1
---

# Anthropic が「Claude Ship」を発表。コードのレビュー・修正に加え、承認まで AI エージェントが担う

![](https://techcrunch.com/wp-content/uploads/2026/10/GettyImages-2295579000.jpg?resize=1200,800)

> [!summary] 一言で
> Anthropic が 11/23、PR のレビュー・CI 修正・自動承認をまとめた Claude Ship をベータで公開し、「出荷してよいか」の判断まで AI に広げた。

- 構成は 3 つ。Code Review（一般提供。Quick / Standard / Deep の 3 段階）、PR Steward（ベータ。CI 失敗・マージ競合・レビュー指摘を直し、push のたびに変更内容と戻し方をコメントする）、Claude Approvals（ベータ。リポジトリに置いた自然言語の承認ポリシーに従って自動承認する）。
- 対象は Claude Team / Enterprise の GitHub リポジトリのみ。承認は最初に「観察のみ」モードで動かすことを勧めており、1 リポジトリから始める・月額の上限を決める・人に回す変更を決める、といった制御がある。
- Anthropic は、Claude Code チームでは Claude がコードの大半を書いており、PR 後の工程も同じ速さにしたかったと説明している。TechCrunch は「自動承認エージェント」が目新しい点だと指摘している。

> [!tip] So what
> Q1 で「人に残る」とした「レビュー」の最後の関門、承認そのものが製品になった。ただし承認の基準は人が書くポリシーで、何を人に回すかを決める仕事は残る。実際の承認精度の数字は記事にない。

**トピック**：[[AI と開発者の働き方]]、[[AI エージェントの基盤と安全性]]
**登場**：[[Anthropic]]、[[Claude Code]]
**出典**：[TechCrunch](https://techcrunch.com/2026/11/23/anthropic-launches-claude-ship-letting-ai-agents-review-fix-and-approve-code-changes/)・[ZDNET（Google News 経由）](https://news.google.com/rss/articles/CBMibkFVX3lxTE1YdzNqWWozWExIQnJEYk9QUjFkcWU2V1ZSa2NfOHJod1pOQjNuTVpKQlAzUFg2dDNhN2x0WExPeEJ6NGhIWTZEdjdYWVJjOUxlWXZoeFNhTmxuWjQyRjZrQnRHaThQRUthVC1fSzVn?oc=5)（[[Digest/2026-11-24|2026-11-24 の Digest]] 1 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
