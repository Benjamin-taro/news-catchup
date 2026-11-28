---
type: article
day: 2026-11-26
vote: up
score: 68
kind: 事故・障害
source: "1Password 公式"
url: "https://1password.com/blog/update-on-nov-2026-security-incident"
main_topic: "[[セキュリティ事故]]"
topics:
  - "[[セキュリティ事故]]"
entities:
  - "[[1Password]]"
  - "[[GitHub]]"
digest: "[[Digest/2026-11-26]]"
digest_rank: 6
---

# 1Password、従業員の GitHub アカウント経由で侵入。顧客の氏名・メールなど管理データが流出、金庫は無事

![](https://images.ctfassets.net/3091ajzcmzlr/3yu0DTU3edoU7HK8MxkW54/c5e7801fb8c0d7d52295da96af7e8013/business_2x.webp)

> [!summary] 一言で
> 1Password が、従業員の社内 GitHub アカウントが乗っ取られ、バックエンドに悪意あるコードを入れられて一部顧客の管理データが取得されたと公表した。

- 11/19 に調査を開始し 11/25 に公表。流出は氏名・メール・公開鍵・SRP パラメータ・招待や復旧メール内のトークンなど。金庫の中身と鍵、アプリは影響なし。対象は「一部」とだけで人数は不明。
- 攻撃者は非公開リポジトリのソースを複製し、インフラの秘密情報を持つ CI/CD にも入った。全認証情報をローテーションし、招待・復旧コードを 6 桁から 10 桁の英数字に延長した。
- 乗っ取りの経緯は書かれていない。公表では、提供済みトークンを使った乗っ取りの形跡は社内で確認していない。

> [!tip] So what
> 製品ではなく開発者のアカウントと CI/CD が入口になった例。AI エージェントにも開発環境の権限を渡す流れの中で、入口の管理が問われる。

**トピック**：[[セキュリティ事故]]
**登場**：[[1Password]]、[[GitHub]]
**出典**：[1Password 公式](https://1password.com/blog/update-on-nov-2026-security-incident)・[BigGo ファイナンス](https://finance.biggo.jp/news/86bd3431-ad2e-4b18-b885-4fb6393beb46)（[[Digest/2026-11-26|2026-11-26 の Digest]] 6 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
