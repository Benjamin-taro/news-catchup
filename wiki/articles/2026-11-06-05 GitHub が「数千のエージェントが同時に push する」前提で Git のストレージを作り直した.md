---
type: article
day: 2026-11-06
vote: up
score: 64
kind: 製品・発表
source: "GitHub Blog"
url: "https://github.blog/engineering/architecture-optimization/inside-githubs-new-git-storage-architecture/"
main_topic: "[[AI エージェントの基盤と安全性]]"
topics:
  - "[[AI エージェントの基盤と安全性]]"
  - "[[AI と開発者の働き方]]"
entities:
  - "[[GitHub]]"
digest: "[[Digest/2026-11-06]]"
digest_rank: 5
---

# GitHub が「数千のエージェントが同時に push する」前提で Git のストレージを作り直した

![](https://github.blog/wp-content/uploads/2026/01/4ba0cd42388a255e04c78e5143548f22e577d68e0f15f68e6a3c76c18b927981-1920x1080-1.png)

> [!summary] 一言で
> GitHub は、1 つのリポジトリに数千のエージェントが同時に書き込めるよう Git のストレージ基盤を再設計し、社内テストで 5,000 同時エージェント・毎秒 7,200 push を処理したと発表した。

- 参照（ブランチ等）の更新だけを専用のレプリケーション・ログ「Ref-CAS」で合意させ、パック等の不変データは Azure Blob Storage に置く。読み書きは使い捨て可能な仮想レプリカが担い、パックの統合・GC は専用ノードがバックグラウンドで行う。
- あるリポジトリのリクエスト数は 3〜5 月に約 4 倍（1 日約 4,400 万から約 1 億 8,100 万）に増えた。最も忙しいリポジトリでも現状は毎秒数十回の書き込みが上限で、目標は現在の要求を 2 桁上回る規模。
- 限定プライベートプレビューを開始し、来年初頭に広く提供する予定。

> [!tip] So what
> エージェントの増加で、コード置き場の側が先に設計を変えざるをえなくなっている例。性能の数字は GitHub 自身の社内テストの結果なので、一般提供後の実測を待ちたい。

**トピック**：[[AI エージェントの基盤と安全性]]、[[AI と開発者の働き方]]
**登場**：[[GitHub]]
**出典**：[GitHub Blog](https://github.blog/engineering/architecture-optimization/inside-githubs-new-git-storage-architecture/)（[[Digest/2026-11-06|2026-11-06 の Digest]] 5 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
