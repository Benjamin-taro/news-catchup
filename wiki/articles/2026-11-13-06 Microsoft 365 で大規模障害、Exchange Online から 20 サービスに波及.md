---
type: article
day: 2026-11-13
vote: up
score: 60
kind: 事故・障害
source: "piyolog"
url: "https://piyolog.hatenadiary.jp/entry/2026/11/13/114230"
main_topic: "[[セキュリティ事故]]"
topics:
  - "[[セキュリティ事故]]"
entities:
  - "[[Microsoft 365]]"
digest: "[[Digest/2026-11-13]]"
digest_rank: 6
---

# Microsoft 365 で大規模障害、Exchange Online から 20 サービスに波及

![](https://ogimage.blog.st-hatena.com/10257846132616586766/14729835035337762288/1794555297)

> [!summary] 一言で
> 2026-11-13 未明から Microsoft 365 で障害が起き、Outlook を含む最大 20 サービスに影響して、夕方になっても全面復旧していない。

- 日本時間 1:17 に Exchange Online の障害が始まり、3:26 に他サービスへ拡大。原因は当初「負荷」と説明されたが、多数のサーバーが自動ヘルスチェックに失敗して落ち、残りに負荷が移ったと改められた。障害開始と相関するネットワーク構成変更があり、10:06 に巻き戻しを開始。
- 政府共通の業務環境（GSS）を含め、国内で自治体・大学・企業・金融機関の公表が 37 組織に上った（piyolog 集計）。
- Microsoft は「悪意ある活動は把握していない」とし、根本原因は事後報告書で示すと説明している（16 時時点）。

> [!tip] So what
> メールや認証を 1 社の基盤に寄せる構造の脆さが表に出た。構成変更とヘルスチェック失敗の連鎖という点は、自社の運用にも当てはまる。

**トピック**：[[セキュリティ事故]]
**登場**：[[Microsoft 365]]
**出典**：[piyolog](https://piyolog.hatenadiary.jp/entry/2026/11/13/114230)・[ITmedia](https://www.itmedia.co.jp/news/article/2611/13/2000003161/)・[日経（元記事・有料）](https://www.nikkei.com/article/DGXZQOGN12CY20S6A111C2000000/)（[[Digest/2026-11-13|2026-11-13 の Digest]] 6 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
