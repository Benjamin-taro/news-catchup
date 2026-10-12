---
type: article
day: 2026-10-12
vote: up
score: 70
kind: 解説
source: "Zenn（aiautolog）"
url: "https://zenn.dev/aiautolog/articles/claude-md-state-cli-write-scope"
main_topic: "[[AI エージェントの基盤と安全性]]"
topics:
  - "[[AI エージェントの基盤と安全性]]"
  - "[[AI と開発者の働き方]]"
entities:
  - "[[Claude Code]]"
digest: "[[Digest/2026-10-12]]"
digest_rank: 7
---

# Claude Code に状態ファイルを直接触らせず CLI に一本化。書き込み範囲を CLAUDE.md で縛る運用

![](https://res.cloudinary.com/zenn/image/upload/s--vpYeu6YK--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:Claude%2520Code%2520%25E3%2581%25AB%25E7%258A%25B6%25E6%2585%258B%25E3%2583%2595%25E3%2582%25A1%25E3%2582%25A4%25E3%2583%25AB%25E3%2582%2592%25E7%259B%25B4%25E6%258E%25A5%25E8%25A7%25A6%25E3%2582%2589%25E3%2581%259B%25E3%2581%25AA%25E3%2581%2584%25E3%2580%2582CLI%2520%25E3%2581%25AB%25E4%25B8%2580%25E6%259C%25AC%25E5%258C%2596%25E3%2581%2597%25E3%2581%25A6%25E6%259B%25B8%25E3%2581%258D%25E8%25BE%25BC%25E3%2581%25BF%25E7%25AF%2584%25E5%259B%25B2%25E3%2582%2592%2520CLAUDE.md%2520%25E3%2581%25A7%25E7%25B8%259B%25E3%2582%258B%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_37:%25E3%2581%2582%25E3%2581%2584%2Cx_203%2Cy_121/g_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUNnOG9jS1d2cDBVdkNuVFQ4cVJSelg3Tk5BMHduT0NxQnlydmlDaXRTSTl0QU0ycEhEYktRPXMyNTAtYw==%2Cr_max%2Cw_90%2Cx_87%2Cy_95/v1627283836/default/og-base-w1200-v2.png?_a=BACMTiAE)

> [!summary] 一言で
> 複数の Claude Code エージェントに業務を分担させるとき、状態ファイルの編集を CLI に集約し、部署ごとの書き込み範囲を CLAUDE.md に書く設計を紹介した記事。

- 直接編集をやめる理由は、フロントマターの書き間違いに誰も気づけない、複数エージェントが同じファイルを触ると正しい変更が分からない、の 2 点など。`task:claim` や `run:record` のようなコマンドを経由させ、出力は JSON に揃える。
- 禁止領域には「黙って直す」のではなく改善案を承認依頼として出させる。`git commit`/`push` は禁止し、保存は専用コマンドに一本化。そのコマンドは鍵らしき文字列や認証ファイルを含むコミットを拒否する。
- 毎晩、点検役のエージェントがコミット履歴を読んで違反を探し、直近で 3 件の候補が出た（原因は未確定、誤検知もある）。ルール文書同士の矛盾も見つかった。

> [!tip] So what
> 「禁止を書く」だけでなく、拒否する仕組みと点検役まで含めて初めて権限が効く、という実例。個人運用でも、書き込み範囲を CLAUDE.md に明記する手は取り入れやすい。

**トピック**：[[AI エージェントの基盤と安全性]]、[[AI と開発者の働き方]]
**登場**：[[Claude Code]]
**出典**：[Zenn（aiautolog）](https://zenn.dev/aiautolog/articles/claude-md-state-cli-write-scope)（[[Digest/2026-10-12|2026-10-12 の Digest]] 7 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
