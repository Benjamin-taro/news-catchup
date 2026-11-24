---
type: article
day: 2026-11-23
vote: up
score: 58
kind: 解説
source: "Zenn（ojisan_ai_lab）"
url: "https://zenn.dev/ojisan_ai_lab/articles/claude-code-compact-stack-20261122"
main_topic: "[[AI と開発者の働き方]]"
topics:
  - "[[AI と開発者の働き方]]"
entities:
  - "[[Claude Code]]"
digest: "[[Digest/2026-11-23]]"
digest_rank: 7
---

# Claude Code の `/compact` を重ねると、決まりは残り、貼った表は 2 回目で消える

![](https://res.cloudinary.com/zenn/image/upload/s--X_Iafdv_--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:Claude%2520Code%25E3%2581%25AE%2520%252Fcompact%2520%25E3%2582%2592%25E9%2587%258D%25E3%2581%25AD%25E3%2582%258B%25E3%2581%25A8%25E4%25BD%2595%25E3%2581%258C%25E6%25B6%2588%25E3%2581%2588%25E3%2582%258B%25EF%25BC%259F%2520%25E6%25B1%25BA%25E3%2581%25BE%25E3%2582%258A10%25E5%2580%258B%25E3%2581%25AF%25E6%25AE%258B%25E3%2582%258A%25E3%2580%2581%25E6%259C%2580%25E5%2588%259D%25E3%2581%25AE%25E8%25A1%25A830%25E8%25A1%258C%25E3%2581%25AF%25E4%25BD%259C%25E6%25A5%25AD%25E3%2582%2592%25E6%258C%259F%25E3%2582%2580...%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_37:%25E3%2581%258A%25E3%2581%2598%25E3%2581%2595%25E3%2582%2593AI%25E3%2583%25A9%25E3%2583%259C%2Cx_203%2Cy_121/g_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9zdGF0aWMuemVubi5zdHVkaW8vdXNlci11cGxvYWQvYXZhdGFyLzZhYjlkMjRhMmYuanBlZw==%2Cr_max%2Cw_90%2Cx_87%2Cy_95/v1627283836/default/og-base-w1200-v2.png?_a=BACMTiAE)

> [!summary] 一言で
> ojisan_ai_lab が、`/compact` を重ねたときに何が残るかを 32 回の実測で確かめた。

- 最初に伝えた「決まり 10 個」は 32 回中 31 回で 10 個とも書けた。残る 1 回は 1 個が言い換えられ、言っていない「毎週」が混ざった。
- 経費の表 30 行は、作業を挟むと 2 回目の要約で 18 回すべてで 0 行。作業を挟まず `/compact` だけなら 4 回とも 30 行のまま残った。3 回目の連続 `/compact` は 5 回とも「Not enough messages」で失敗した。
- 環境は Claude Code 2.1.330 の `claude -p`、モデルは claude-sonnet-5-5。条件ごとに 3〜5 回と少なく、自動圧縮は対象外。

> [!tip] So what
> 決まりは CLAUDE.md、生データはファイルに置いて読み直させる、という使い分けの根拠になる。ただし 1 人・少数回の検証で、傾向の目安にとどまる。

**トピック**：[[AI と開発者の働き方]]
**登場**：[[Claude Code]]
**出典**：[Zenn（ojisan_ai_lab）](https://zenn.dev/ojisan_ai_lab/articles/claude-code-compact-stack-20261122)（[[Digest/2026-11-23|2026-11-23 の Digest]] 7 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
