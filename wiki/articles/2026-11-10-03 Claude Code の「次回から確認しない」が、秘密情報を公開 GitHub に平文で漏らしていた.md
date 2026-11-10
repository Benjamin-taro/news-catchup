---
type: article
day: 2026-11-10
vote: up
score: 78
kind: 事故・障害
source: "iTnews"
url: "https://www.itnews.com.au/news/dont-ask-again-in-anthropics-claude-code-leaks-developer-secrets-630203"
main_topic: "[[セキュリティ事故]]"
topics:
  - "[[セキュリティ事故]]"
  - "[[AI と開発者の働き方]]"
entities:
  - "[[Claude Code]]"
  - "[[Anthropic]]"
digest: "[[Digest/2026-11-10]]"
digest_rank: 3
---

# Claude Code の「次回から確認しない」が、秘密情報を公開 GitHub に平文で漏らしていた

![](https://i.nextmedia.com.au/News/crn-690-stock-servers.jpg)

> [!summary] 一言で
> Apiiro の調査で、Claude Code の許可ルール保存の仕様により、DB パスワードや API キーが公開リポジトリの設定ファイルに残っていた。

- 公開 GitHub の約 10 万 4 千件の `.claude/settings.local.json` のうち 1,122 件に実際の秘密情報があり、計 1,379 件。内訳は DB パスワード 379、Supabase の service-role キー 122、SSH ログイン 43、AWS キー 23 など。古い版や履歴まで含めると 2,539 件・1,994 リポジトリ、63 組織に及ぶ。
- 「don't ask again」で承認したコマンドに秘密情報が直書きされていると、そのまま平文で保存される。既存スキャナーの取りこぼしも大きく、gitleaks は 564 件、TruffleHog は 643 件で、215 件はどちらも検出できなかった。
- Anthropic の Boris Cherny 氏は問題を認め、秘密情報スキャンの組み込みなどを検討中。ファイルは自動で gitignore されるので、露出は手動コミットによるものだと主張している。

> [!tip] So what
> エージェントに権限を渡す運用では、承認の保存先もリスクになる。コマンドに秘密情報を書かず環境変数で参照し、承認はパターン単位にする、という具体策が出ている。

**トピック**：[[セキュリティ事故]]、[[AI と開発者の働き方]]
**登場**：[[Claude Code]]、[[Anthropic]]
**出典**：[iTnews](https://www.itnews.com.au/news/dont-ask-again-in-anthropics-claude-code-leaks-developer-secrets-630203)・[Ars Technica（元記事）](https://news.google.com/rss/articles/CBMiogFBVV95cUxNNkpLSnVERzJwSlRmNmZJOTBaZkhzaERjNWREVE9qOGpYbHZuTGdEZW5xbFhEb2l2dEc5WURrS252YmJuRGJudWQ1WnlEVDRXdkEwZWNJeFNoWkhiZzVNX1NQNmlDMTN4b0k5NEtwclJmeEt1Q1A5dno1QTlPd3VOeXZrV1dRLS1tdUQ1T1poeDBwSkVSY1FuLUZZSU5qbzFZSVE?oc=5)・[note（国内向け解説）](https://news.google.com/rss/articles/CBMiWkFVX3lxTE81d2dfYkcxMEZvWVRlTnlVQzhOcmh6LWpjWkdOMkxnT0dSUy1pX1NkSFZucHV5TkRla09GcEZ0MWxBNXlrOXFnY25ZaVJJX1Q1ejgxdDBIdjZOUQ?oc=5)（[[Digest/2026-11-10|2026-11-10 の Digest]] 3 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
