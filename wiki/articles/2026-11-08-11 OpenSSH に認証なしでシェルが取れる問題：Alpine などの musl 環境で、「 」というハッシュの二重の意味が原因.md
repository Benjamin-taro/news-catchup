---
type: article
day: 2026-11-08
vote: up
score: 46
kind: 議論・意見
source: "sunshowers.io"
url: "https://sunshowers.io/posts/sshole/"
main_topic: "[[セキュリティ事故]]"
topics:
  - "[[セキュリティ事故]]"
entities:
  - "[[OpenSSH]]"
digest: "[[Digest/2026-11-08]]"
digest_rank: 11
---

# OpenSSH に認証なしでシェルが取れる問題：Alpine などの musl 環境で、「*」というハッシュの二重の意味が原因

![](https://sunshowers.io/images/4-aaaaaa-card.jpg)

> [!summary] 一言で
> sunshowers 氏が、musl libc 環境の OpenSSH で、パスワード認証なしにシェル（場合によって root）が取れる問題を解説した（11/6）。

- 原因は、パスワードハッシュ「*」が、Unix ではアカウントのロック、musl の `crypt` では長すぎるパスワードへのエラー応答（2012 年以降）という二つの意味で使われていたこと。sshd がロック済みアカウントのログインでもハッシュを計算するため、両者が噛み合った。
- 対象は PAM を使わない musl 環境で、公式の Alpine AWS イメージなどが含まれる。
- 筆者はメモリ安全性の問題ではなく、エラーを型で表現させる Rust 的な規範の話だと述べ、「LLM エージェントがあれば C でも安全」という主張に反論している。

> [!tip] So what
> 個別の脆弱性だが、エラー値の設計という一般的な教訓がある。修正状況や実際の被害は記事からは確認できていない。

**トピック**：[[セキュリティ事故]]
**登場**：[[OpenSSH]]
**出典**：[sunshowers.io](https://sunshowers.io/posts/sshole/)（[[Digest/2026-11-08|2026-11-08 の Digest]] 11 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
