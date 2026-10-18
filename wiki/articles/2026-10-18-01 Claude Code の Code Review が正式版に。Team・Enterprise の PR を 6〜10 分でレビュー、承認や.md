---
type: article
day: 2026-10-18
vote: up
score: 88
kind: 製品・発表
source: "Zenn（zundamon_tools）"
url: "https://zenn.dev/zundamon_tools/articles/claude-news-weekly-2026-10-18"
main_topic: "[[AI と開発者の働き方]]"
topics:
  - "[[AI と開発者の働き方]]"
  - "[[AI エージェントの基盤と安全性]]"
entities:
  - "[[Claude Code]]"
  - "[[Anthropic]]"
digest: "[[Digest/2026-10-18]]"
digest_rank: 1
---

# Claude Code の Code Review が正式版に。Team・Enterprise の PR を 6〜10 分でレビュー、承認やブロックはしない

![](https://res.cloudinary.com/zenn/image/upload/s--_cqzt2kb--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:Claude%2520Code%2520%25E9%2580%25B1%25E9%2596%2593%25E3%2583%258B%25E3%2583%25A5%25E3%2583%25BC%25E3%2582%25B9%25EF%25BC%258810%252F11%25E3%2580%259C10%252F17%25EF%25BC%2589%25EF%25BC%259ACode%2520Review%2520%25E6%25AD%25A3%25E5%25BC%258F%25E7%2589%2588%25E3%2583%25BBidle%2520comp...%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_37:%25E3%2581%259A%25E3%2582%2593%25E3%2581%25A0%25E3%2582%2582%25E3%2582%2593%25E3%2581%25AE%25E5%25AE%259F%25E9%25A8%2593%25E9%2581%2593%25E5%2585%25B7%25E7%25AE%25B1%2Cx_203%2Cy_121/g_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9zdGF0aWMuemVubi5zdHVkaW8vdXNlci11cGxvYWQvYXZhdGFyLzJiNGRhMmQyODEuanBlZw==%2Cr_max%2Cw_90%2Cx_87%2Cy_95/v1627283836/default/og-base-w1200-v2.png?_a=BACMTiAE)

> [!summary] 一言で
> Claude Code の週間まとめ（Zenn）によると、10 月 15 日に GitHub PR の自動レビュー「Code Review」が Team・Enterprise 向けに正式版になり、同じ週に idle compaction など 2.1.299〜2.1.302 の挙動変更も入った。

- Code Review は管理者が有効にすれば開発者側の設定が不要。多くのレビューはプレビュー時の約 20 分から 6〜10 分になった。深さは Quick・Standard（既定）・Deep からリポジトリごとに選べる。PR の承認・ブロックはしない。
- 費用は利用者ではなく組織の usage credits に請求される。Enterprise は 2027 年 1 月 15 日までの申請で 1 万ドル以上のクレジットを受け取れる（受け取りから 30 日で失効）。Zero Data Retention・HIPAA 構成や CMEK の組織、Pro・Max は対象外（ローカルの `/code-review` は全プランで使える）。
- 2.1.299 の idle compaction は、20 万トークン超の会話を約 54 分放置すると 1 時間のキャッシュが切れる前に圧縮する（`"idleCompaction": false` で停止可）。MCP の allow ルール `mcp__a` は別サーバーに効かなくなり、PreToolUse の `updatedInput` は検証されて未知のキーは捨てられる。hooks で入力を書き換えている場合は確認が要る。

> [!tip] So what
> レビューを「承認する人」ではなく「見落としを探す常時の検査」として製品化する動きで、10/17 の Anthropic 社内の事例の続きにあたる。時間短縮の数字は公式の説明で、第三者の検証は見当たらない。

**トピック**：[[AI と開発者の働き方]]、[[AI エージェントの基盤と安全性]]
**登場**：[[Claude Code]]、[[Anthropic]]
**出典**：[Zenn（zundamon_tools）](https://zenn.dev/zundamon_tools/articles/claude-news-weekly-2026-10-18)（[[Digest/2026-10-18|2026-10-18 の Digest]] 1 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
