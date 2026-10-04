---
type: article
day: 2026-09-28
vote: up
score: 74
kind: 解説
source: "ByteByteGo"
url: "https://blog.bytebytego.com/p/ai-agents-can-think-now-they-can"
main_topic: "[[AI エージェントの基盤と安全性]]"
topics:
  - "[[AI エージェントの基盤と安全性]]"
  - "[[AI の企業導入]]"
entities:
  - "[[Stripe]]"
  - "[[Machine Payments Protocol]]"
digest: "[[Digest/2026-09-28]]"
digest_rank: 8
---

# AI エージェントが自分で支払いをする時代：Stripe の「MPP」の仕組み

![](https://substackcdn.com/image/fetch/$s_!wmgK!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F80af75d2-3c28-4cd1-9372-0e932a1099e1_1589x2048.png)

> [!summary] 一言で
> Stripe と Tempo が作った、AI エージェント同士の決済プロトコル「Machine Payments Protocol（MPP）」の解説。

- 2026 年 3 月に立ち上がった。HTTP 402 を使い、サーバーが支払い条件を示す → エージェントが支払いの証明を返す → サーバーが領収を返す、という 3 段階で決済する。
- セッション機能で細かい支払いを 1 つにまとめ、手数料を抑えられる。
- 2026 年 8 月時点で、約 3 万件の MPP 決済が実行されている。

> [!tip] So what
> 記事の言葉を借りれば、本質は「決済から人間が消えること」。AI × 金融の中でも、決済や与信の前提が変わる分野で、金融系のキャリアを考えるなら押さえておきたい。

**トピック**：[[AI エージェントの基盤と安全性]]、[[AI の企業導入]]
**登場**：[[Stripe]]、[[Machine Payments Protocol]]
**出典**：[ByteByteGo](https://blog.bytebytego.com/p/ai-agents-can-think-now-they-can)（[[Digest/2026-09-28|2026-09-28 の Digest]] 8 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
