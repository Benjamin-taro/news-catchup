---
type: article
day: 2026-10-22
vote: up
score: 62
kind: 解説
source: "Zenn（ojisan_ai_lab）"
url: "https://zenn.dev/ojisan_ai_lab/articles/claude-code-auto-mode-setup-20261022"
main_topic: "[[AI と開発者の働き方]]"
topics:
  - "[[AI と開発者の働き方]]"
  - "[[AI エージェントの基盤と安全性]]"
entities:
  - "[[Claude Code]]"
digest: "[[Digest/2026-10-22]]"
digest_rank: 9
---

# Claude Code の /auto-mode-setup を 2 回目に実行。下書きの「理由づけ」が実際の記録と合わなかった

![](https://res.cloudinary.com/zenn/image/upload/s--AOrF6Y-Y--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:Claude%2520Code%25E3%2581%25AE%2520%252Fauto-mode-setup%2520%25E3%2582%25922%25E5%259B%259E%25E7%259B%25AE%25E3%2581%25AB%25E8%25B5%25B0%25E3%2582%2589%25E3%2581%259B%25E3%2581%259F%25E3%2582%2589%25E3%2580%2581%25E4%25B8%258B%25E6%259B%25B8%25E3%2581%258D%25E3%2581%25AE%25E7%2590%2586%25E7%2594%25B1%25E3%2581%25A5%25E3%2581%2591%25E3%2581%258C%25E3%2581%258A%25E3%2581%2598%25E3%2581%2595%25E3%2582%2593%25E3%2581%25AE%25E8%25A8%2598%25E9%258C%25B2...%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_37:%25E3%2581%258A%25E3%2581%2598%25E3%2581%2595%25E3%2582%2593AI%25E3%2583%25A9%25E3%2583%259C%2Cx_203%2Cy_121/g_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9zdGF0aWMuemVubi5zdHVkaW8vdXNlci11cGxvYWQvYXZhdGFyLzZhYjlkMjRhMmYuanBlZw==%2Cr_max%2Cw_90%2Cx_87%2Cy_95/v1627283836/default/og-base-w1200-v2.png?_a=BACMTiAE)

> [!summary] 一言で
> 自動承認モードの設定を作る機能を 2 か月ぶりに走らせた著者が、生成された下書きの根拠に事実と違う点があったと報告した。

- 約 35 秒のスキャンで、soft_deny が 72 → 74 行に増え、ログフォルダの一括削除と認証情報ファイルへの書き込みの 2 つのルールが加わった。
- 「分類器に何度も拒否された」という理由は、記録にある 20 件の拒否に削除の件がなく、合わなかった。「このプロジェクトだけを選んだ」という注記も、そんな選択肢は出ていなかった。
- 受け入れるか捨てるかは全か無かなので、保存前にルールと注記を読み、`settings.json` をバックアップするよう勧める。1 台の PC での観察で、拒否の件数が減ったかどうかは判断できないと著者も認めている。

> [!tip] So what
> 権限の設定を AI に下書きさせるときは、出てきた理由づけも検証が要る。「権限を渡す自由度」（Q7）の実務の具体例。

**トピック**：[[AI と開発者の働き方]]、[[AI エージェントの基盤と安全性]]
**登場**：[[Claude Code]]
**出典**：[Zenn（ojisan_ai_lab）](https://zenn.dev/ojisan_ai_lab/articles/claude-code-auto-mode-setup-20261022)（[[Digest/2026-10-22|2026-10-22 の Digest]] 9 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
