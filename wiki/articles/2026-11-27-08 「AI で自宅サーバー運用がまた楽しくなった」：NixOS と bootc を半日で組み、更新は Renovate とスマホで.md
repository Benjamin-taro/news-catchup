---
type: article
day: 2026-11-27
vote: up
score: 56
kind: 議論・意見
source: "janlukas.blog"
url: "https://janlukas.blog/posts/ai-self-hosting"
main_topic: "[[AI と開発者の働き方]]"
topics:
  - "[[AI と開発者の働き方]]"
entities: []
digest: "[[Digest/2026-11-27]]"
digest_rank: 8
---

# 「AI で自宅サーバー運用がまた楽しくなった」：NixOS と bootc を半日で組み、更新は Renovate とスマホで

> [!summary] 一言で
> Jan-Lukas Else 氏が、AI のコーディングエージェントのおかげで自宅サーバーと VPS の構成変更の手間が減り、自己ホスティングへの熱が戻ったと書いた。

- 構成を Git に置いているため、エージェントが通常のソフトウェアと同じように扱える。Debian ベースの bootc イメージは AI で半日、なければ少なくとも 1 週間かかったと見積もる。
- Renovate が更新 PR を出し、GitHub Actions か Forgejo Actions がビルドとデプロイを行う。スマホでレビューしてマージする。請求書や Linux ISO を取ってくる小さな道具は、OSS を探さず Go で自作している。
- 注意点として、サービスが増えるほど保守が増えること、AI 製のコードにバグやセキュリティ問題が入りうること、作れるから作ってしまう誘惑を挙げている。

> [!tip] So what
> 個人の環境では、AI の効果が「新しい技術を試すコスト」に出る、という体験談。業務側の話ではなく、数字も本人の見積もり。

**トピック**：[[AI と開発者の働き方]]
**出典**：[janlukas.blog](https://janlukas.blog/posts/ai-self-hosting)（[[Digest/2026-11-27|2026-11-27 の Digest]] 8 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
