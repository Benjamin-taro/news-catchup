---
type: article
day: 2026-11-26
vote: up
score: 58
kind: 解説
source: "kinoko dev"
url: "https://dev.sin5d.com/meta-muse-usage"
main_topic: "[[AI と開発者の働き方]]"
topics:
  - "[[AI と開発者の働き方]]"
  - "[[AI エージェントの基盤と安全性]]"
entities:
  - "[[Meta]]"
  - "[[Muse]]"
digest: "[[Digest/2026-11-26]]"
digest_rank: 11
---

# Meta の AI エージェント「Muse」を 1 か月使って：階層型メモリと IDENTITY.md の設計

![](https://dev.sin5d.com/bl-content/uploads/Museデフォルトアバター-Jolly-jpg.jpg)

> [!summary] 一言で
> kinoko dev が、2026 年 9 月に公開された Meta の Muse を 1 か月使い、設計の特徴と癖をまとめた。

- ユーザーごとに VM が割り当てられるクラウド型で、無料版は Muse Spark 1.3 固定、有料版は Muse Wonder 固定（モデルは切り替え不可）。筆者は毎日約 10 万文字を生成しても週間上限に届いていない。
- 常時読み込まれるのは MEMORY.md だけで、日別要約・ユーザー・人物・組織を階層的に保存。IDENTITY.md で口調やロールを設定でき、ロールで応答の質が大きく変わる。サイドチャットは独自のコンテキストを持つ。
- 簡単なコーディングは得意でなく、メモリを手で編集すると過去の記録と矛盾して混乱する。短い指示のたびに記憶を検索してコンテキストを使い切ることが「性能低下」の原因と筆者は見ている。

> [!tip] So what
> Claude Code の Skills・メモリ設計と似た構造が、他社の一般向けエージェントにも入ってきた。記憶と役割をファイルで持つ設計が事実上の共通形になりつつある。

**トピック**：[[AI と開発者の働き方]]、[[AI エージェントの基盤と安全性]]
**登場**：[[Meta]]、[[Muse]]
**出典**：[kinoko dev](https://dev.sin5d.com/meta-muse-usage)（[[Digest/2026-11-26|2026-11-26 の Digest]] 11 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
