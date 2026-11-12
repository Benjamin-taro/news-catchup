---
type: article
day: 2026-11-12
vote: up
score: 58
kind: 製品・発表
source: "Google 公式"
url: "https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/"
main_topic: "[[LLM とモデル競争]]"
topics:
  - "[[LLM とモデル競争]]"
  - "[[AI エージェントの基盤と安全性]]"
entities:
  - "[[Gemini]]"
  - "[[Google]]"
digest: "[[Digest/2026-11-12]]"
digest_rank: 7
---

# Google の Gemini Decisions API：1 回の入力に最大 1,000 問を 150〜250 ms で判定、入力 100 万トークン 0.10 ドル

![](https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini__decisions__blog-header_2784x1566.width-1300.png)

> [!summary] 一言で
> Google は、文章を生成せずに「はい／いいえ・選択肢・採点」を確率で返す専用モデル `gemini-decision-1` の API を 11 月 11 日に発表した。

- テキスト・画像・音声・動画・PDF を合わせて最大 256K トークンの入力に、最大 1,000 問を 1 回で評価する。選択肢は 2〜255、各回答に 0〜1 の確信度が付き、曖昧なものは別経路や人に回せる。
- 遅延は端から端まで 150〜250 ms、料金は入力 100 万トークン 0.10 ドル・出力 0 ドル。Google は Gemini 3.5 Flash-Lite（Interactions API）より約 5 倍安いと主張。
- 用途はツール選択、ポリシー確認、モデルのルーティング、文脈の採点。OpenRouter や LangChain などへの統合を順次展開し、Google Cloud 版は「近日」。

> [!tip] So what
> 生成ではなく「判定」に絞ったモデルが、エージェントの部品（振り分け・検査）として切り出され始めた。数字は Google の自己申告で、第三者の検証はない。

**トピック**：[[LLM とモデル競争]]、[[AI エージェントの基盤と安全性]]
**登場**：[[Gemini]]、[[Google]]
**出典**：[Google 公式](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-decisions-api/)（[[Digest/2026-11-12|2026-11-12 の Digest]] 7 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
