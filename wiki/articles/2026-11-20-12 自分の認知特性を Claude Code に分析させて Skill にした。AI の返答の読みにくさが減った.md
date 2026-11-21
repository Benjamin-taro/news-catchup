---
type: article
day: 2026-11-20
vote: up
score: 62
kind: 解説
source: "shibayu36 のブログ"
url: "https://blog.shibayu36.org/entry/2026/11/17/120000"
main_topic: "[[AI と開発者の働き方]]"
topics:
  - "[[AI と開発者の働き方]]"
entities:
  - "[[Claude Code]]"
digest: "[[Digest/2026-11-20]]"
digest_rank: 12
---

# 自分の認知特性を Claude Code に分析させて Skill にした。AI の返答の読みにくさが減った

![](https://cdn.image.st-hatena.com/image/scale/1fc598bf9933e879d45c8b8cb0402b3541079adc/backend=imagemagick;version=1;width=1300/https%3A%2F%2Fcdn-ak.f.st-hatena.com%2Fimages%2Ffotolife%2Fs%2Fshiba_yu36%2F20261115%2F20261115102037.png)

> [!summary] 一言で
> shibayu36 さんは、セッションログから自分が理解に詰まった発言を集めて Claude Code に分析させ、「writing-for-shibayu36」という Skill を作った。

- 手順は、困りごとを伝える、`~/.claude/projects` のログから「どういうこと」「なんだっけ」などの発言と直前の返答を組にして原因を分類させる、特性の仮説を 1 つずつ確認する、Skill に落とす、CLAUDE.md で毎回読み込ませる、の 5 段階。
- 「理解できない語が出るとそこで止まる」という、自覚のなかった特性も見つかった。
- before は「案B を取り入れるなら…」と離れた箇所を指す返答。after は参照先の中身を返答内に書き直す形になった。

> [!tip] So what
> 他人の Skill を使うより自分のログを分析させるほうが効く、という実践的な知見。ログ分析で個人の癖を Skill にする手順は、チームの CLAUDE.md にも応用できる。

**トピック**：[[AI と開発者の働き方]]
**登場**：[[Claude Code]]
**出典**：[shibayu36 のブログ](https://blog.shibayu36.org/entry/2026/11/17/120000)（[[Digest/2026-11-20|2026-11-20 の Digest]] 12 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
