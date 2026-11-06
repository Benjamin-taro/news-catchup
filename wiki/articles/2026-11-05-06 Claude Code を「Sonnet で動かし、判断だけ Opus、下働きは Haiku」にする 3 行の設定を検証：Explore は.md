---
type: article
day: 2026-11-05
vote: up
score: 66
kind: 解説
source: "Zenn（scalar_sol_blog）"
url: "https://zenn.dev/scalar_sol_blog/articles/20261103-104939-claude-code-model-split"
main_topic: "[[AI と開発者の働き方]]"
topics:
  - "[[AI と開発者の働き方]]"
entities:
  - "[[Claude Code]]"
digest: "[[Digest/2026-11-05]]"
digest_rank: 6
---

# Claude Code を「Sonnet で動かし、判断だけ Opus、下働きは Haiku」にする 3 行の設定を検証：Explore は Haiku にならず、advisor は呼ばれない

![](https://res.cloudinary.com/zenn/image/upload/s--KIw64TQz--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:Claude%2520Code%2520%25E3%2582%2592%2520Sonnet%2520%25E3%2581%25A7%25E5%258B%2595%25E3%2581%258B%25E3%2581%2597%25E3%2580%2581%25E5%2588%25A4%25E6%2596%25AD%25E3%2581%25A0%25E3%2581%2591%2520Opus%2520%25E3%2581%25AB%25E7%259B%25B8%25E8%25AB%2587%25E3%2581%2595%25E3%2581%259B%25E3%2580%2581%25E4%25B8%258B%25E5%2583%258D%25E3%2581%258D%25E3%2581%25AF%2520Haiku%2520%25E3%2581%25AB%25E4%25BB%25BB%25E3%2581%259B%25E3%2582%258B...%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_34:wfukatsu%2Cx_220%2Cy_108/bo_3px_solid_rgb:d6e3ed%2Cg_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9zdGF0aWMuemVubi5zdHVkaW8vdXNlci11cGxvYWQvYXZhdGFyLzIyYWQ5MTcyZjMuanBlZw==%2Cr_20%2Cw_90%2Cx_92%2Cy_102/g_south_west%2Ch_34%2Cl_default:og-publication-pro-mark-xcosax%2Cw_34%2Cx_217%2Cy_158/co_rgb:6e7b85%2Cg_south_west%2Cl_text:notosansjp-medium.otf_30:Scalar%2520Solution%2520Engi...%2Cx_255%2Cy_160/bo_4px_solid_white%2Cg_south_west%2Ch_50%2Cl_fetch:aHR0cHM6Ly9zdGF0aWMuemVubi5zdHVkaW8vdXNlci11cGxvYWQvYXZhdGFyLzBhZjQwOTk3NDYuanBlZw==%2Cr_max%2Cw_50%2Cx_139%2Cy_84/v1627283836/default/og-base-w1200-v2.png?_a=BACMTiAE)

> [!summary] 一言で
> Zenn の検証記事が、`settings.json` の 3 キーで役割ごとのモデル分担を作り、実際にどう動くかを `claude -p` で確かめた。

- 設定は `model: sonnet`、`advisorModel: opus`、`env.CLAUDE_CODE_SUBAGENT_MODEL: haiku`。general-purpose サブエージェントは Haiku で動いたが、組み込みの Explore はメインの Sonnet を継承した。Explore も変えるには `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1` などが必要。
- advisor は有効でも指示しないと一度も呼ばれない。在庫引当の課題で、Sonnet のみは 29 秒・$0.29、advisor を呼ばせると 85 秒・$0.98、Opus のみは 83 秒・$1.01（API 定価換算、各 1 回）。
- 結論は、advisor はコスト削減の仕組みではなく、長い作業の要所で使うと割に合う可能性があるというもの。

> [!tip] So what
> 「安くなるはず」の設定が思った通りには動かない箇所を、数字つきで示した実例。各条件 1 回の結果で、目安として読む。

**トピック**：[[AI と開発者の働き方]]
**登場**：[[Claude Code]]
**出典**：[Zenn（scalar_sol_blog）](https://zenn.dev/scalar_sol_blog/articles/20261103-104939-claude-code-model-split)（[[Digest/2026-11-05|2026-11-05 の Digest]] 6 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
