---
type: article
day: 2026-10-29
vote: up
score: 46
kind: 事故・障害
source: "We Have a Problem"
url: "https://emudhra.we-have-a-problem.com/apple.html"
main_topic: "[[セキュリティ事故]]"
topics:
  - "[[セキュリティ事故]]"
entities:
  - "[[Apple]]"
digest: "[[Digest/2026-10-29]]"
digest_rank: 15
---

# Apple の macOS 同梱の git・curl・python3 は、侵害された eMudhra の証明書を今も信頼。macOS 27.2 でも直らず、手動の回避策も元に戻った

> [!summary] 一言で
> 研究者らのページが、10/28 時点で Apple の開発者向けツールが侵害された eMudhra のルート証明書を信頼したままだと指摘している。

- Apple へは 10/17 に通知済み。10/26 公開の macOS 27.2 でも修正されず、利用者が手動で適用していた回避策まで元に戻った。Safari など Apple のネットワーク枠組みを使うアプリは保護済み。他の多くのプロジェクト（ボランティア運営が多い）は数日前に修正を公開した。
- 経路上の攻撃者が HTTPS 通信を傍受でき、`https://` の git clone/pull で攻撃者のコードが届く恐れや、GitHub トークンなどの認証情報の傍受がありうる。CI で macOS ランナーを使う場合はサプライチェーンの観点で確認が必要。
- 当面の対策は、影響を受けるルート証明書を `/etc/ssl/cert.pem` から手動で削除すること。更新のたびに戻る可能性があるので、確認と再適用が要る。

> [!tip] So what
> eMudhra の話題（10/25 など）の続きで、信頼の起点（ルート証明書）の管理が OS ベンダー頼みになっている構図が見える。ページは Dennis Jackson 氏らによるもので Apple の見解は未確認、攻撃の実例の報告もない。

**トピック**：[[セキュリティ事故]]
**登場**：[[Apple]]
**出典**：[We Have a Problem](https://emudhra.we-have-a-problem.com/apple.html)（[[Digest/2026-10-29|2026-10-29 の Digest]] 15 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
