---
type: article
day: 2026-10-26
vote: up
score: 56
kind: 調査・データ
source: "Lynch Lab"
url: "https://lynchlab.net/llm-skin-cancer"
main_topic: "[[LLM とモデル競争]]"
topics:
  - "[[LLM とモデル競争]]"
entities:
  - "[[Anthropic]]"
  - "[[OpenAI]]"
digest: "[[Digest/2026-10-26]]"
digest_rank: 14
---

# 10 年前の CNN が皮膚がん診断で最新 LLM を上回る。GPT-6 Astra と Claude Fable 5.1 の正診は 42%、CNN は 62%

> [!summary] 一言で
> Lynch 研究室のブログが、生検済みの皮膚病変 200 件で、汎用 LLM と古い画像認識モデル（Inception v3）を比べた。

- 第 1 候補の正診は GPT-6 Astra 84 件（42%）、Claude Fable 5.1 85 件（42%）、CNN 125 件（62%）。悪性黒色腫 30 件のうち正診は LLM が 8・11 件、CNN が 13 件。
- ただし CNN は既定の閾値で悪性黒色腫 18 件を「退院可」とした（LLM は 3〜4 件）。安全面では CNN に大きな懸念が残る。
- 限界として、悪性黒色腫が 30 件と少ない、LLM は各 1 回のみ、全件が生検済みで難しい症例に偏る、データセットが LLM の学習に含まれていた可能性がある。

> [!tip] So what
> 汎用モデルより専用の小さなモデルが勝つ領域がある、という例。1 研究室のブログで査読はない。

**トピック**：[[LLM とモデル競争]]
**登場**：[[Anthropic]]、[[OpenAI]]
**出典**：[Lynch Lab](https://lynchlab.net/llm-skin-cancer)（[[Digest/2026-10-26|2026-10-26 の Digest]] 14 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
