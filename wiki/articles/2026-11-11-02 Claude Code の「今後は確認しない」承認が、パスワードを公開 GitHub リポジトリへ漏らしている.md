---
type: article
day: 2026-11-11
vote: up
score: 78
kind: 事故・障害
source: "Let's Data Science"
url: "https://letsdatascience.com/news/apiiro-finds-claude-code-approvals-leak-secrets-into-public-99d400fd"
main_topic: "[[セキュリティ事故]]"
topics:
  - "[[セキュリティ事故]]"
  - "[[AI エージェントの基盤と安全性]]"
entities:
  - "[[Claude Code]]"
  - "[[Apiiro]]"
digest: "[[Digest/2026-11-11]]"
digest_rank: 2
---

# Claude Code の「今後は確認しない」承認が、パスワードを公開 GitHub リポジトリへ漏らしている

![](https://lh3.googleusercontent.com/J6_coFbogxhRI9iM864NL_liGXvsQp2AupsKei7z0cNNfDvGUmWUy20nuUhkREQyrpY4bEeIBuc=s0-w300-rw)

> [!summary] 一言で
> セキュリティ企業 Apiiro は、Claude Code が承認済みコマンドを平文で保存する設定ファイルから、公開リポジトリに秘密情報が漏れていると報告した。

- `.claude/settings.local.json` の公開コピー 10 万 4,185 件のうち 1,122 件（約 1.1%）に実際の秘密情報があった。履歴や保存された会話記録まで含めると 1,994 リポジトリで 2,539 件、DB パスワード 379 件、Supabase のサービスロールキー 122 件、AWS キー 23 件など。
- 「Yes, and don't ask again」を選ぶと、コマンドに含まれるパスワードごと許可ルールとして保存される。ファイルは開発者の全体 gitignore には入るが、プロジェクトの `.gitignore` には入らない。比較した 16 のエージェントのうち、既定でこの形で保存するのは Claude Code だけだと Apiiro は述べる。
- Gitleaks が 564 件、TruffleHog が 643 件を検出し、215 件は両方とも見逃した。`PGPASSWORD=` のようにコマンド中に直接書かれたパスワードは鍵の形式に当たらないため。対策は漏れた認証情報の失効、ファイルの追跡解除、環境変数の利用、`.claude/` のスキャン対象への追加。

> [!tip] So what
> エージェントに権限を渡す運用では、「承認の記録」自体が漏えい経路になる。Q7 の「業務側でどこまで自由を許すか」を考える具体材料。数字は Apiiro の報告で、二次報道（LDS）経由で確認した。

**トピック**：[[セキュリティ事故]]、[[AI エージェントの基盤と安全性]]
**登場**：[[Claude Code]]、[[Apiiro]]
**出典**：[Let's Data Science](https://letsdatascience.com/news/apiiro-finds-claude-code-approvals-leak-secrets-into-public-99d400fd)・[Dark Reading（元候補・取得不可）](https://news.google.com/rss/articles/CBMigAFBVV95cUxNRzM1dS1lRkR4UnVNV3A5VXlueFdaQ0p4NzlybjRTZXpqWkYwc19nRHR6Nm1YdTRaRkNkWk5tUnhBMS1yaEJHTnhSYXYybWM5blVCaUxKVi1ITmZCRVVCdW1VRFpmMVRTRndfR0owOVFESkhnZ0poTGVlZVVTc3Vtcw?oc=5)（[[Digest/2026-11-11|2026-11-11 の Digest]] 2 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
