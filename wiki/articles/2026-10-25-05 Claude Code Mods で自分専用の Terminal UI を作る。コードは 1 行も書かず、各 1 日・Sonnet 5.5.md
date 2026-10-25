---
type: article
day: 2026-10-25
vote: up
score: 68
kind: 解説
source: "Zenn（metalmental）"
url: "https://zenn.dev/metalmental/articles/20261025_claude-code-mods"
main_topic: "[[AI と開発者の働き方]]"
topics:
  - "[[AI と開発者の働き方]]"
entities:
  - "[[Claude Code]]"
digest: "[[Digest/2026-10-25]]"
digest_rank: 5
---

# Claude Code Mods で自分専用の Terminal UI を作る。コードは 1 行も書かず、各 1 日・Sonnet 5.5 だけで実装

![](https://res.cloudinary.com/zenn/image/upload/s--wwesL5-y--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:Claude%2520Code%2520Mods%25E3%2581%25A7%25E4%25BD%259C%25E3%2582%258B%25E8%2587%25AA%25E5%2588%2586%25E5%25B0%2582%25E7%2594%25A8%25E3%2581%25AETerminal%2520UI%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_37:metalmental%2Cx_203%2Cy_121/g_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUNnOG9jSzJYbHgtVTZpT1J6VWI0WVZiYjlTUWNoa1FMRzZnalktdmFiZl9YYjJocHd3dk01NHY9czk2LWM=%2Cr_max%2Cw_90%2Cx_87%2Cy_95/v1627283836/default/og-base-w1200-v2.png?_a=BACMTiAE)

> [!summary] 一言で
> 10 月に入った Claude Code の Mods（TypeScript 製の拡張。v2.1.287 以降）で、ステータスラインと UI 拡張を作った実例。

- Mods の仕様は標準 skill の `plugin-authoring` に概要・型定義・コード例が入っている。Sandbox の制限を受けないため注意が必要と著者は書く。
- statusline は、ディレクトリ名のクリックでパスをコピー、PR 番号のクリックで Web を開く、7 日間の利用枠のリセット日時、各言語のバージョン表示、Git 状態やレビューコマンドのボタンなどを備える。
- ui-plus は、直近 2 件以外のメッセージの自動折りたたみ、表やコードブロックの Markdown コピー、回答中だけツール実行ログを表示する機能。それぞれ約 1 日、コードを書かずに作ったという。

> [!tip] So what
> 道具の見た目や操作を「自然言語で自分用に作り替える」ことが現実的な作業量になった例。Sandbox の外で動く点は、権限管理の観点で確認が要る。

**トピック**：[[AI と開発者の働き方]]
**登場**：[[Claude Code]]
**出典**：[Zenn（metalmental）](https://zenn.dev/metalmental/articles/20261025_claude-code-mods)（[[Digest/2026-10-25|2026-10-25 の Digest]] 5 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
