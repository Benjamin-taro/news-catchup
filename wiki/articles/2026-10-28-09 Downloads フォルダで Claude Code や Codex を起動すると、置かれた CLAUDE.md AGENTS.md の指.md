---
type: article
day: 2026-10-28
vote: up
score: 47
kind: 解説
source: "Zenn（hoshiorange）"
url: "https://zenn.dev/hoshiorange/articles/44-downloads-folder-agent-launch"
main_topic: "[[AI エージェントの基盤と安全性]]"
topics:
  - "[[AI エージェントの基盤と安全性]]"
  - "[[セキュリティ事故]]"
entities:
  - "[[Claude Code]]"
  - "[[Codex]]"
digest: "[[Digest/2026-10-28]]"
digest_rank: 9
---

# Downloads フォルダで Claude Code や Codex を起動すると、置かれた CLAUDE.md / AGENTS.md の指示に従ってしまう。研究元の再現では Codex で 90% 超、Claude Code で約 50%

![](https://res.cloudinary.com/zenn/image/upload/s--NQMolz-v--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:Downloads%25E3%2581%25A7claude%25E3%2582%2592%25E8%25B5%25B7%25E5%258B%2595%25E3%2581%2599%25E3%2582%258B%25E3%2581%25A8%25E4%25B9%2597%25E3%2581%25A3%25E5%258F%2596%25E3%2582%2589%25E3%2582%258C%25E3%2581%2586%25E3%2582%258B%25E3%2580%2582%25E7%25A7%2581%25E3%2581%25AEPC%25E3%2582%2582%25E5%258D%25B1%25E3%2581%2586%25E3%2581%2584%25E8%25A8%25AD%25E5%25AE%259A%25E3%2581%25A0%25E3%2581%25A3%25E3%2581%259F%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_37:%25E3%2581%25BB%25E3%2581%2597%2Cx_203%2Cy_121/g_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9zdGF0aWMuemVubi5zdHVkaW8vdXNlci11cGxvYWQvYXZhdGFyLzlmZTA3MzA0YWEuanBlZw==%2Cr_max%2Cw_90%2Cx_87%2Cy_95/v1627283836/default/og-base-w1200-v2.png?_a=BACMTiAE)

> [!summary] 一言で
> Forever Security の研究を紹介した Zenn の記事で、エージェントを起動する場所が攻撃の入口になりうる、という検証が示された。

- 悪意ある `AGENTS.md` / `CLAUDE.md` が Downloads に置かれ、エージェントがそれを従うべき指示として読む。ブラウザは既定で保存先を尋ねずに Downloads へ保存でき、実行ファイルでないため OS の警告も出ない。
- 再現では、Codex がユーザー共通の `~/.codex/config.toml` にツールサーバーを追記し、Claude Code はプロジェクトの `.claude/settings.json` で `ANTHROPIC_BASE_URL` を攻撃者のサーバーに向けた。成功率は研究元の自社検証で、第三者の検証はない。
- 成立条件は、Downloads などで起動すること、そのフォルダを信頼済みにしていること、権限確認を省略していること。対策は、プロジェクトフォルダで起動し、`pwd` で確認し、`bypassPermissions` を避けること。

> [!tip] So what
> 個人開発で「信頼済み」「権限確認なし」にする自由度が、そのまま入口になる例で、Q7 の個人開発と業務開発の分かれ目に関わる。研究元はエージェント監視製品の販売元で、リスクを大きく見せる動機がありうる。

**トピック**：[[AI エージェントの基盤と安全性]]、[[セキュリティ事故]]
**登場**：[[Claude Code]]、[[Codex]]
**出典**：[Zenn（hoshiorange）](https://zenn.dev/hoshiorange/articles/44-downloads-folder-agent-launch)・[note（Claude Code 研究所）](https://news.google.com/rss/articles/CBMiW0FVX3lxTE41cnI1YWJpMWhzSlExS19Wbm1qamtrXzlQZWNlY1p4RmkzVHNmZHdVWXZobmhDY3pOV0pWeHJXY0VTc1JVUDZQalFHYXBRVE5nOWpjY3hBYUxRY3M?oc=5)（[[Digest/2026-10-28|2026-10-28 の Digest]] 9 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
