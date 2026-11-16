---
type: article
day: 2026-11-16
vote: up
score: 48
kind: 議論・意見
source: "yorickpeterse.com"
url: "https://yorickpeterse.com/articles/migrating-from-github-to-codeberg/"
main_topic: "[[AI と開発者の働き方]]"
topics:
  - "[[AI と開発者の働き方]]"
  - "[[開発スタック]]"
entities:
  - "[[GitHub]]"
  - "[[Codeberg]]"
digest: "[[Digest/2026-11-16]]"
digest_rank: 10
---

# 「AI の低品質 PR が増えた」ことを理由に GitHub から Codeberg へ移った Inko 作者

> [!summary] 一言で
> Yorick Peterse 氏が、AI 生成の質の低い PR や GitHub への不信を理由に、約 70 リポジトリのうち主要なものを Codeberg に移した手間と課題をまとめた。

- 理由は、AI 生成の無駄な PR が増えて本来の共同作業の場ではなくなったこと、GitHub の信頼性の低下、Codeberg の AI コンテンツへの方針。
- CI は Forgejo Actions に置き換え（互換は不完全）、Mac Mini と自宅サーバーのランナーで Linux・macOS・FreeBSD を回す。コンテナは Buildah を使い、複数アーキテクチャを 1 つのマニフェストにまとめた。
- Codeberg は自前のインスタンスより遅く、障害の連絡も少なめ。組織の容量上限 1.5 GiB が足りず、コンテナ画像の一部はまだ GitHub に置いている。

> [!tip] So what
> OSS 側が AI 生成コードの流入を理由にホスティング先を変える例。レビューを受ける側の負荷が、プラットフォーム選びに及び始めている。ただし 1 人のメンテナの判断で、移行が広がっているというデータではない。

**トピック**：[[AI と開発者の働き方]]、[[開発スタック]]
**登場**：[[GitHub]]、[[Codeberg]]
**出典**：[yorickpeterse.com](https://yorickpeterse.com/articles/migrating-from-github-to-codeberg/)（[[Digest/2026-11-16|2026-11-16 の Digest]] 10 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
