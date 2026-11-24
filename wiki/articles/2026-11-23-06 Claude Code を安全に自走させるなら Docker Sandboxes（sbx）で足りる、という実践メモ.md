---
type: article
day: 2026-11-23
vote: up
score: 62
kind: 解説
source: "note（YamaC）"
url: "https://note.com/yamac_/n/n198bdc344c64"
main_topic: "[[AI と開発者の働き方]]"
topics:
  - "[[AI と開発者の働き方]]"
  - "[[AI エージェントの基盤と安全性]]"
entities:
  - "[[Claude Code]]"
  - "[[Docker Sandboxes]]"
digest: "[[Digest/2026-11-23]]"
digest_rank: 6
---

# Claude Code を安全に自走させるなら Docker Sandboxes（sbx）で足りる、という実践メモ

![](https://assets.st-note.com/production/uploads/images/339175432/rectangle_large_type_2_490a1a8344ed92ccfd09322236cc3e11.jpeg?fit=bounds&quality=85&width=1280)

> [!summary] 一言で
> note の記事が、Claude Code や Codex を microVM 内で動かす Docker Sandboxes の使い方と、通信制限の効き方を実機で確かめた。

- 筆者は「9 割くらいのケースはこれで足りる」と見る。Claude Code 標準の `/sandbox` はシェルコマンドしか隔離せず、ファイルツールや MCP はホスト側で動くため、無人運用には不十分だとする。
- 通信は既定で拒否。Balanced を選ぶと GitHub の 3 ホストなどだけ許可され、example.com や YouTube は遮断、`sbx policy allow network` で個別に許可できた。Docker Desktop は不要で、ローカル実行は商用でも無料。
- 注意点：共有フォルダー内の `.env` は読める。Claude Code は既定で `--dangerously-skip-permissions` 付きで起動し、MCP のローカル stdio サーバーはホスト側で動く。

> [!tip] So what
> 「確認を絞る代わりに隔離を厚くする」設計を個人で作る手順が具体的に出てきた。1 人の検証なので、組織での運用は別途有料の管理機能や設定確認が要る。

**トピック**：[[AI と開発者の働き方]]、[[AI エージェントの基盤と安全性]]
**登場**：[[Claude Code]]、[[Docker Sandboxes]]
**出典**：[note（YamaC）](https://note.com/yamac_/n/n198bdc344c64)（[[Digest/2026-11-23|2026-11-23 の Digest]] 6 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
