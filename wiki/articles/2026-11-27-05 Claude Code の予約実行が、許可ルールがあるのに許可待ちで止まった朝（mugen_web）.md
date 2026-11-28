---
type: article
day: 2026-11-27
vote: up
score: 62
kind: 解説
source: "Zenn（mugen_web）"
url: "https://zenn.dev/mugen_web/articles/scheduled-claude-code-permission-stalls"
main_topic: "[[AI と開発者の働き方]]"
topics:
  - "[[AI と開発者の働き方]]"
  - "[[AI エージェントの基盤と安全性]]"
entities:
  - "[[Claude Code]]"
digest: "[[Digest/2026-11-27]]"
digest_rank: 5
---

# Claude Code の予約実行が、許可ルールがあるのに許可待ちで止まった朝（mugen_web）

![](https://res.cloudinary.com/zenn/image/upload/s--rxeZGhOl--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:Claude%2520Code%25E3%2581%25AE%25E4%25BA%2588%25E7%25B4%2584%25E5%25AE%259F%25E8%25A1%258C%25E3%2581%258C%25E3%2580%2581%25E8%25A8%25B1%25E5%258F%25AF%25E5%25BE%2585%25E3%2581%25A1%25E3%2581%25A7%25E6%25AD%25A2%25E3%2581%25BE%25E3%2581%25A3%25E3%2581%259F%25E6%259C%259D%25E3%2581%25AE%25E8%25A8%2598%25E9%258C%25B2%25E3%2580%2582%25E8%25A8%25B1%25E5%258F%25AF%25E3%2583%25AB%25E3%2583%25BC%25E3%2583%25AB%25E3%2581%258C%25E3%2581%2582%25E3%2581%25A3%25E3%2581%25A6%25E3%2582%2582%25E8%2581%259E%25E3%2581%258B%25E3%2582%258C%25E3%2581%259F%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_37:MUGEN%2520WEB%2Cx_203%2Cy_121/g_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUNnOG9jTGFEMXVhMTJBamkzcEZqNVltXzdGVzVRR1JHSFFNWnJBcXZ1Tkg0Rk9OLUFxNnJBPXMyNTAtYw==%2Cr_max%2Cw_90%2Cx_87%2Cy_95/v1627283836/default/og-base-w1200-v2.png?_a=BACMTiAE)

> [!summary] 一言で
> mugen_web が、毎朝の確認を予約実行していた Claude Code が許可待ちで 4 回止まり、原因を切り分けられないまま予約実行をやめた記録を公開した。

- 2026 年 11 月 24 日の朝、日付つき Markdown への書き込み、x.com と note.com への移動、Chrome の `wait` 操作の 4 か所で停止。`.claude/settings.json` の `permissions.allow` には `Write` や `mcp__claude-in-chrome` が入っていたのに確認が出た。
- Chrome 操作は、1.2 秒待つループを 6 回回す処理が 45 秒でタイムアウトし、新しいタブを作るとタブ番号も変わった。開く場所を 2 か所に絞る、タブを使い回す、といった対策を先に入れた。
- 翌 25 日も許可を求められた。作業フォルダを移動したことが原因の可能性はあるが未確認で、筆者は見守れる会話の中で確認する方式に切り替えた。

> [!tip] So what
> 無人で任せる運用では、許可の挙動が読めないと止まるか、設定の抜けを疑うことになる、という現場の記録。原因は確定しておらず、1 人の環境での事例。

**トピック**：[[AI と開発者の働き方]]、[[AI エージェントの基盤と安全性]]
**登場**：[[Claude Code]]
**出典**：[Zenn（mugen_web）](https://zenn.dev/mugen_web/articles/scheduled-claude-code-permission-stalls)（[[Digest/2026-11-27|2026-11-27 の Digest]] 5 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
