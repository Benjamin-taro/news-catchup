---
type: article
day: 2026-11-11
vote: up
score: 80
kind: 解説
source: "Zenn（luvtechno）"
url: "https://zenn.dev/luvtechno/articles/isucon2026-preparation"
main_topic: "[[AI と開発者の働き方]]"
topics:
  - "[[AI と開発者の働き方]]"
entities:
  - "[[Claude Code]]"
digest: "[[Digest/2026-11-11]]"
digest_rank: 3
---

# ISUCON2026 優勝者は、人が介入しない Claude Code エージェントを 3 か月かけて作り込んだ

![](https://res.cloudinary.com/zenn/image/upload/s--FlBezkdp--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:ISUCON2026%2520%25E3%2581%25A7%25E5%2584%25AA%25E5%258B%259D%25E3%2581%2597%25E3%2581%25BE%25E3%2581%2597%25E3%2581%259F%25EF%25BC%2588%25E6%25BA%2596%25E5%2582%2599%25E7%25B7%25A8%25EF%25BC%2589%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_37:Yoshinori%2520Kawasaki%2Cx_203%2Cy_121/g_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUNnOG9jTEpMVlQ2WjlNQlhlcndlbDZoY1JYUDVLSjAxYWNITUdNcmUwVThZTG5EaDY4PXM5Ni1j%2Cr_max%2Cw_90%2Cx_87%2Cy_95/v1627283836/default/og-base-w1200-v2.png?_a=BACMTiAE)

> [!summary] 一言で
> ISUCON2026 の優勝者が、8 時間の競技を人間の監視なしで解かせる Claude Code エージェントの準備記録を公開した。

- 準備は 2026 年 8〜10 月。評価 run 159 回（延べ 674 時間、約 200 億トークン）を回し、commit 3,889 件のうち約 76% を Claude Code が書いた。
- 構成は 3 種類を比較。手順を作り込んだ full は、素の Claude Code に近い bare に負けた。本番は bare に最低限の仕組み（作業を止めさせない Stop フック、スコア頭打ち時の監査役サブエージェント、API エラー時の再開）を足した lite。
- 素の状態では git を使わない、範囲外の設定ファイルを書き換える、といった問題が出た。同じ構成でもスコアが大きくばらつくため、1 回の結果で判断しない。評価対象の選定や構成の採用は人の判断として残った。

> [!tip] So what
> エージェントに任せる範囲を広げるほど、人の仕事は「評価環境と止め方・戻し方の設計」に移る。著者自身、普段の開発に通用するかは分からないとしている。

**トピック**：[[AI と開発者の働き方]]
**登場**：[[Claude Code]]
**出典**：[Zenn（luvtechno）](https://zenn.dev/luvtechno/articles/isucon2026-preparation)・[はてブ](https://zenn.dev/luvtechno/articles/isucon2026-preparation)（[[Digest/2026-11-11|2026-11-11 の Digest]] 3 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
