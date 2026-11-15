---
type: article
day: 2026-11-13
vote: up
score: 74
kind: 解説
source: "Speaker Deck（Michael Tedder）"
url: "https://speakerdeck.com/falken/boku-no-claude-code-no-tsukaikata"
main_topic: "[[AI と開発者の働き方]]"
topics:
  - "[[AI と開発者の働き方]]"
  - "[[AI エージェントの基盤と安全性]]"
entities:
  - "[[Claude Code]]"
  - "[[Codex]]"
digest: "[[Digest/2026-11-13]]"
digest_rank: 1
---

# Claude Code を自宅マシンで常時動かし、Discord から操作する運用（札幌 Meetup LT）

![](https://files.speakerdeck.com/presentations/9c2451b8b99f4a269ce6f420bc0480ae/slide_0.jpg?41338374)

> [!summary] 一言で
> Claude Code を権限確認なしで常時動かしつつ、専用ユーザー・最小権限・人の最終承認で被害範囲を絞る個人運用の実例が、2026-11-12 の札幌 Claude Code Meetup で共有された。

- Ubuntu の LXC コンテナ上の sudo なし専用ユーザーで `bypassPermissions` を使い、被害はホームディレクトリ内に限定。main への直接 push は禁止、AWS は最小限の IAM 権限で、デプロイは毎回本人が承認する。
- Issue → ブランチ実装 → CI → Codex によるレビュー → 👍 とグリーンが揃ったら Claude がマージ、という流れ。一度注意したことをルール化した永続メモリが約 160 件ある。
- 実例として、フリート管理ページを深夜 1 時にスマホの Discord から依頼し、約 50 分で完成、PR 3 件をマージ。Codex レビューが本物のバグを 1 件見つけた。

> [!tip] So what
> 個人開発では「権限を渡し切る代わりに、隔離と最後の承認で守る」運用が成り立っている。業務側が同じ自由度を許すかを考える材料になる（Q7）。

**トピック**：[[AI と開発者の働き方]]、[[AI エージェントの基盤と安全性]]
**登場**：[[Claude Code]]、[[Codex]]
**出典**：[Speaker Deck（Michael Tedder）](https://speakerdeck.com/falken/boku-no-claude-code-no-tsukaikata)（[[Digest/2026-11-13|2026-11-13 の Digest]] 1 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
