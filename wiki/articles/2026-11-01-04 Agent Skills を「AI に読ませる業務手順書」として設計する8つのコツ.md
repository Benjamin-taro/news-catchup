---
type: article
day: 2026-11-01
vote: up
score: 62
kind: 解説
source: "風屋 Tech Blog"
url: "https://techblog.kazaneya.com/20261030-agent-skills/"
main_topic: "[[AI と開発者の働き方]]"
topics:
  - "[[AI と開発者の働き方]]"
  - "[[AI エージェントの基盤と安全性]]"
entities:
  - "[[Claude Code]]"
digest: "[[Digest/2026-11-01]]"
digest_rank: 4
---

# Agent Skills を「AI に読ませる業務手順書」として設計する8つのコツ

![](https://techblog.kazaneya.com/assets/images/kazaneya_OGP.png)

> [!summary] 一言で
> 日程調整スキルを例に、Agent Skills を新入社員向けマニュアルと同じ発想で作る設計指針をまとめた記事。

- 決まりきった処理（空き枠計算など）はスクリプトに任せ、AI には文面作成と判断だけを担当させる。出力先（本人だけ／共有チャット／取引先）ごとに書ける情報の範囲を分ける。
- 手順書だけを渡した別の AI に試運転させ、成果物と自己申告を照合する。過去の不具合は再発防止のテストとして残す。
- 例では候補は5日分を目標に最低3日、空き枠は30分単位で前後30分のバッファがなければ一段下げる、社外への送信は「送る／作り直す／自分で送る」の3択で承認を取る。

> [!tip] So what
> スキルを「業務ルールをテストで固定した手順書」として育てる考え方で、業務での Claude 活用の具体像として参考になる。個人の自由度と社外送信の承認を分ける線引きは Q7 にも関わる。

**トピック**：[[AI と開発者の働き方]]、[[AI エージェントの基盤と安全性]]
**登場**：[[Claude Code]]
**出典**：[風屋 Tech Blog](https://techblog.kazaneya.com/20261030-agent-skills/)（[[Digest/2026-11-01|2026-11-01 の Digest]] 4 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
