---
type: article
day: 2026-10-26
vote: up
score: 58
kind: 解説
source: "Zenn（rimon）"
url: "https://zenn.dev/rimon/articles/45c1fd2f015af8"
main_topic: "[[AI と開発者の働き方]]"
topics:
  - "[[AI と開発者の働き方]]"
entities:
  - "[[Claude Code]]"
digest: "[[Digest/2026-10-26]]"
digest_rank: 9
---

# 「私が 5 種類のコーディングエージェントを使い分ける理由」。Claude Code を窓口に、Codex・Antigravity・OpenCode・Cursor Agent を CLI から呼ぶ

![](https://res.cloudinary.com/zenn/image/upload/s--EFERL7ev--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:%25E7%25A7%2581%25E3%2581%258C5%25E7%25A8%25AE%25E9%25A1%259E%25E3%2581%25AE%25E3%2582%25B3%25E3%2583%25BC%25E3%2583%2587%25E3%2582%25A3%25E3%2583%25B3%25E3%2582%25B0%25E3%2582%25A8%25E3%2583%25BC%25E3%2582%25B8%25E3%2582%25A7%25E3%2583%25B3%25E3%2583%2588%25E3%2582%2592%25E4%25BD%25BF%25E3%2581%2584%25E5%2588%2586%25E3%2581%2591%25E3%2582%258B%25E7%2590%2586%25E7%2594%25B1%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_37:%25E3%2583%259F%25E3%2583%25A2%2520%2520%25E3%2583%2595%25E3%2582%25A9%25E3%2583%25AF%25E3%2583%25BC%25E3%2583%2589CTO%25E3%2583%25BBCPO%2Cx_203%2Cy_121/g_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9zdGF0aWMuemVubi5zdHVkaW8vdXNlci11cGxvYWQvYXZhdGFyL2ZmZjQwODdjMmEuanBlZw==%2Cr_max%2Cw_90%2Cx_87%2Cy_95/v1627283836/default/og-base-w1200-v2.png?_a=BACMTiAE)

> [!summary] 一言で
> Zenn の記事で、著者が Claude Code を窓口にして 4 つの別エージェントを使い分ける運用を紹介した。

- Claude Code は要件の解釈・設計・DB 設計・フロントのデザイン。Codex は画面操作・思考を要する作業と画像生成。Antigravity は記事や資料（Claude の日本語が分かりにくいことがあるため）。Cursor Agent は Slack をきっかけにした実行と会社のコード。
- 私用のコーディングは OpenCode + DeepSeek 4.1 Flash で低コストに大量に回す。規約・プライバシーの不安があるため会社のコードは読ませない。Codex のトークンが切れたときは以前 Cursor（Grok 4.7）、最近は OpenCode に引き継ぐ。
- 使い分けの理由は、モデルごとの得手不得手と、Claude のトークン不足の 2 点。性能は LMArena や CursorBench で追い、文章の品質などは主観の評価。

> [!tip] So what
> 個人では複数のモデルを使い分ける一方、会社のコードには線を引く、という個人と業務の差（Q7）が出ている例。評価は著者の主観で、1 人の運用記録。

**トピック**：[[AI と開発者の働き方]]
**登場**：[[Claude Code]]
**出典**：[Zenn（rimon）](https://zenn.dev/rimon/articles/45c1fd2f015af8)（[[Digest/2026-10-26|2026-10-26 の Digest]] 9 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
