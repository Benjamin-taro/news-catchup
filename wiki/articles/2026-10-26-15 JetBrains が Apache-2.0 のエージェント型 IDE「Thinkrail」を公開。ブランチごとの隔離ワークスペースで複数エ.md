---
type: article
day: 2026-10-26
vote: up
score: 48
kind: 製品・発表
source: "GitHub（JetBrains/thinkrail）"
url: "https://github.com/JetBrains/thinkrail"
main_topic: "[[AI エージェントの基盤と安全性]]"
topics:
  - "[[AI エージェントの基盤と安全性]]"
  - "[[AI と開発者の働き方]]"
entities:
  - "[[JetBrains]]"
digest: "[[Digest/2026-10-26]]"
digest_rank: 15
---

# JetBrains が Apache-2.0 のエージェント型 IDE「Thinkrail」を公開。ブランチごとの隔離ワークスペースで複数エージェントを並列実行

![](https://opengraph.githubassets.com/362e4fc68dd0e69e5549dde551f8275bffc452128ca8fbbfb32e490336893c84/JetBrains/thinkrail)

> [!summary] 一言で
> JetBrains の GitHub リポジトリで、コーディングエージェント「pi」を中核にした IDE が公開されている。

- Git の worktree でブランチごとに独立した作業環境を作り、複数のエージェントを並列に動かす。PR の CI 状況やレビュー状態も表示する。
- `SPEC.md` をコードと並べて管理し、エージェントが専用ツールで読み書きする。既存の Agent Skills を読み込め、MCP は読み取り専用でない呼び出しに確認を求める。
- 安定版は 0.1.2、ナイトリーは 0.2.0 系。ページに公開日の記載はない。

> [!tip] So what
> IDE の側が「複数エージェントの並列作業」を前提に作り直されつつある例。初期版で、実用性は未確認。

**トピック**：[[AI エージェントの基盤と安全性]]、[[AI と開発者の働き方]]
**登場**：[[JetBrains]]
**出典**：[GitHub（JetBrains/thinkrail）](https://github.com/JetBrains/thinkrail)（[[Digest/2026-10-26|2026-10-26 の Digest]] 15 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
