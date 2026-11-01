---
type: article
day: 2026-11-01
vote: up
score: 66
kind: 事故・障害
source: "Zenn（sugawara_ai）"
url: "https://zenn.dev/sugawara_ai/articles/ai-news-20261031"
main_topic: "[[セキュリティ事故]]"
topics:
  - "[[セキュリティ事故]]"
  - "[[AI エージェントの基盤と安全性]]"
entities:
  - "[[Claude Code]]"
  - "[[Cursor]]"
digest: "[[Digest/2026-11-01]]"
digest_rank: 3
---

# Cursor の配布所で公式 Claude Code 拡張に裏口、約12時間配布された

![](https://res.cloudinary.com/zenn/image/upload/s--k_0SccK8--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:%25E5%2585%25AC%25E5%25BC%258F%25E3%2581%25AEClaude%25E6%258B%25A1%25E5%25BC%25B5%25E3%2581%25AB%25E8%25A3%258F%25E5%258F%25A3%25E3%2580%2581%25E7%25B4%258412%25E6%2599%2582%25E9%2596%2593%25E3%2580%2582AI%25E9%2581%2593%25E5%2585%25B7%25E3%2582%2592%25E3%2581%25A9%25E3%2581%2586%25E5%25AE%2588%25E3%2582%258B%25E3%2581%258B%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_37:%25E8%258F%2585%25E5%258E%259F%25E5%258F%258B%25E5%2592%258C%2Cx_203%2Cy_121/g_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUNnOG9jSUJfd2tWRGJ6UktoZC11RldsQUxwZU5lTUpaUGxGWXAyeWJpRTdIamlDbWNPMTgwT3M9czI1MC1j%2Cr_max%2Cw_90%2Cx_87%2Cy_95/v1627283836/default/og-base-w1200-v2.png?_a=BACMTiAE)

> [!summary] 一言で
> Cursor の拡張機能配布所にあった公式の Claude Code 拡張の版 2.1.313 に裏口が仕込まれ、約12時間配布されたと伝えられている。

- セキュリティ会社 Phorion が発見し、読み込まれると利用者の操作なしで動く。公式アカウントへの侵入経路はまだ分かっていない。
- 配布期間の約12時間は Ars Technica の報道として引用されている（読めたのは日本語の Zenn のまとめで、一次報道は未確認）。Cursor は該当版を取り下げ、他の配布先からも取り下げられた。
- 同日の Claude Code v2.1.314 には作業フォルダ外への書き込みを拒否する設定 `blockWritesOutsideWorkingDirectories` が入ったが、この裏口を止めるものではない。

> [!tip] So what
> エージェントの権限設定だけでなく、拡張機能そのものの供給元が攻撃面になる。開発環境に入れる拡張の版や配布経路を確認する運用が要る。

**トピック**：[[セキュリティ事故]]、[[AI エージェントの基盤と安全性]]
**登場**：[[Claude Code]]、[[Cursor]]
**出典**：[Zenn（sugawara_ai）](https://zenn.dev/sugawara_ai/articles/ai-news-20261031)（[[Digest/2026-11-01|2026-11-01 の Digest]] 3 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
