---
type: article
day: 2026-11-16
vote: up
score: 62
kind: 解説
source: "Zenn（アセロラ）"
url: "https://zenn.dev/acerola_jp/articles/claude-code-commit-size-guard"
main_topic: "[[AI と開発者の働き方]]"
topics:
  - "[[AI と開発者の働き方]]"
entities:
  - "[[Claude Code]]"
digest: "[[Digest/2026-11-16]]"
digest_rank: 4
---

# Claude Code のコミットを 100 行以内に分けさせる：CLAUDE.md より pre-commit フックが効いた

![](https://res.cloudinary.com/zenn/image/upload/s--NY1WRzZV--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:Claude%2520Code%2520%25E3%2581%25AE%25E3%2582%25B3%25E3%2583%259F%25E3%2583%2583%25E3%2583%2588%25E3%2582%2592100%25E8%25A1%258C%25E4%25BB%25A5%25E5%2586%2585%25E3%2581%25AB%25E5%2588%2586%25E3%2581%2591%25E3%2581%2595%25E3%2581%259B%25E3%2582%258B%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_37:%25E3%2582%25A2%25E3%2582%25BB%25E3%2583%25AD%25E3%2583%25A9%2Cx_203%2Cy_121/g_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9zdGF0aWMuemVubi5zdHVkaW8vdXNlci11cGxvYWQvYXZhdGFyL2FmOTgyYjM3NzMuanBlZw==%2Cr_max%2Cw_90%2Cx_87%2Cy_95/v1627283836/default/og-base-w1200-v2.png?_a=BACMTiAE)

> [!summary] 一言で
> acerola_jp 氏が、大きな変更を頼んだときのコミットサイズを、CLAUDE.md の指示と git の pre-commit フックで比べた。

- 指定なしでは 1 コミットに 298 行・426 行が集まった。CLAUDE.md に「100 行以内」と書くと 2 回とも 6 コミットに分かれ、最大は 59 行・66 行。
- pre-commit フック（追加と削除の合計が 100 行超で拒否）では、最初の一括コミットが拒否され、Claude 自身が 6 つに分け直した（最大 76・80 行）。
- 「まとめて 1 つに」と頼むと、CLAUDE.md の回は 1 回目に 139 行で上限を超えた。フックの回は 2 回ともコミットせず人の判断を求め、`--no-verify` での回避はしなかった。各条件 2 回ずつで、PR 全体の行数は 304〜427 行のまま減らない。

> [!tip] So what
> 指示は普段の動きを決めるが、依頼と衝突すると負けうる。確実に守らせたい線引きはフックのような外側の仕組みに置く、という使い分けが数字で見える。レビューしやすい単位に AI の出力を切る工夫にもなる。ただし試行回数は少ない。

**トピック**：[[AI と開発者の働き方]]
**登場**：[[Claude Code]]
**出典**：[Zenn（アセロラ）](https://zenn.dev/acerola_jp/articles/claude-code-commit-size-guard)（[[Digest/2026-11-16|2026-11-16 の Digest]] 4 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
