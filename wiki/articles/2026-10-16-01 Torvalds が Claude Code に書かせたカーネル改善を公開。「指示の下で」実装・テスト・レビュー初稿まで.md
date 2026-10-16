---
type: article
day: 2026-10-16
vote: up
score: 90
kind: 報道
source: "GIGAZINE"
url: "https://gigazine.net/news/20261016-linus-torvalds-claude-code/"
main_topic: "[[AI と開発者の働き方]]"
topics:
  - "[[AI と開発者の働き方]]"
entities:
  - "[[Linus Torvalds]]"
  - "[[Claude Code]]"
digest: "[[Digest/2026-10-16]]"
digest_rank: 1
---

# Torvalds が Claude Code に書かせたカーネル改善を公開。「指示の下で」実装・テスト・レビュー初稿まで

![](https://i.gzn.jp/img/2026/10/16/linus-torvalds-claude-code/00.png)

> [!summary] 一言で
> Linus Torvalds 氏が、ページキャッシュの参照カウント競合を解消する新ブランチを、実装・テスト・カバーレター初稿まで Claude Code に書かせて公開した。

- 対象は「noref-filemap-read-with-llm」ブランチ。folio 構造体への参照なしでページキャッシュから読めるようにし、多数のスレッドが 1 つのファイルから少量ずつ読むときの競合をなくす。Torvalds 氏は作業を「自分の指示の下で」Claude Code が行ったと明言し、計測は自分の機器で行った。
- 性能は 1 スレッドでは差がなく、8 スレッドや 4 コア 4 スレッドで大きく改善するとグラフで示された（具体的な数値は記事にない）。Linux 7.4 のマージウィンドウで取り込まれるかが注目点。
- カーネル開発では、AI 利用を示す「Assisted-by:」タグの義務を外す方向の議論も進む。Torvalds 氏は、AI で読みやすくした結果、長年潜んでいたバグも見つかったと述べたという。

> [!tip] So what
> 昨日の Digest 6（レビューで競合が見つかった件）の続報。AI を使う側の最高責任者が、役割分担と作業の流れまで公開したことで、AI 生成コードの扱いが「是非」から「運用の作法」の議論に移っている。元の LKML 投稿は 403 で読めず、内容は GIGAZINE の紹介記事による。

**トピック**：[[AI と開発者の働き方]]
**登場**：[[Linus Torvalds]]、[[Claude Code]]
**出典**：[GIGAZINE](https://gigazine.net/news/20261016-linus-torvalds-claude-code/)・[LKML（元投稿）](https://lore.kernel.org/lkml/CAHk-=whTs09_ozN+e09GU68N1wPP56MUzDjrg9rnKxQUa0A_4Q@mail.gmail.com/)（[[Digest/2026-10-16|2026-10-16 の Digest]] 1 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
