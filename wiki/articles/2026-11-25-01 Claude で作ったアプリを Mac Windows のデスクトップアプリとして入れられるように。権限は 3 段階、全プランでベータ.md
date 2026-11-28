---
type: article
day: 2026-11-25
vote: up
score: 88
kind: 製品・発表
source: "ITmedia"
url: "https://www.itmedia.co.jp/news/article/2611/25/2000003431/"
main_topic: "[[AI と開発者の働き方]]"
topics:
  - "[[AI と開発者の働き方]]"
  - "[[AI エージェントの基盤と安全性]]"
entities:
  - "[[Anthropic]]"
  - "[[Claude]]"
digest: "[[Digest/2026-11-25]]"
digest_rank: 1
---

# Claude で作ったアプリを Mac / Windows のデスクトップアプリとして入れられるように。権限は 3 段階、全プランでベータ

![](https://www.itmedia.co.jp/news/article/ogp/2611/25/2000003431/10012879/2048)

> [!summary] 一言で
> Anthropic が 11/24、Claude のアーティファクトを「Install as app」でデスクトップアプリ化する機能をベータで公開した。

- パッケージ化や署名は不要で、Claude アカウントをそのまま使うため API キーも要らない。元のアーティファクトを直すとアプリも自動更新され、リンクで共有すれば受け取った人もインストールできる。
- 権限は「標準（ブラウザ相当）」「強化（最前面表示・グローバルショートカット・通知）」「フルアクセス（確認なしでプログラムを実行し、ファイルの読み取り・変更・削除ができる）」の 3 段階。フルアクセスは自分が作ったアプリ（Team / Enterprise では同じ組織のメンバーが作ったもの）にだけ付けられ、更新のたびに再確認される。
- Team は機能が最初から有効でフルアクセスは無効、Enterprise はオーナーが有効にするまで使えず、管理者が組織全体で権限を設定できる。HIPAA 対応の組織では使えない。Anthropic はインストール前の審査をしないと明記している。

> [!tip] So what
> 社内の小さな業務アプリを非エンジニアが作って配る道が公式に開いた一方、業務側ではフルアクセスの既定オフ・管理者の制御が付いており、Q7 の「業務側にどこまで自由度を渡すか」の線引きの実例になる。X では「社内業務アプリは自分で作る時代」という反応が出ているが、権限の運用実績はまだない。

**トピック**：[[AI と開発者の働き方]]、[[AI エージェントの基盤と安全性]]
**登場**：[[Anthropic]]、[[Claude]]
**出典**：[ITmedia](https://www.itmedia.co.jp/news/article/2611/25/2000003431/)・[X の投稿（Google News 経由）](https://news.google.com/rss/articles/CBMiZEFVX3lxTFBzN0N0SUdiN2R0TU1aVnRfb2QtZi1oaXAtenFlSU5BN2J1ZGhLVWpLVXQ4dGstaU5tVHdmTUJJYlQwQUhtcFVxV0N5Y1RnQzlyOGlHQWNackhvRUNIZGU5d3NKUm4?oc=5)（[[Digest/2026-11-25|2026-11-25 の Digest]] 1 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
