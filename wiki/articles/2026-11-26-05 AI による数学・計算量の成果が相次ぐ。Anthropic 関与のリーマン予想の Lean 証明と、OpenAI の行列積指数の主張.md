---
type: article
day: 2026-11-26
vote: up
score: 70
kind: 製品・発表
source: "Aaronson のブログ"
url: "https://scottaaronson.blog/?p=10379"
main_topic: "[[LLM とモデル競争]]"
topics:
  - "[[LLM とモデル競争]]"
  - "[[AI と開発者の働き方]]"
entities:
  - "[[Anthropic]]"
  - "[[Lean]]"
  - "[[OpenAI]]"
  - "[[Scott Aaronson]]"
digest: "[[Digest/2026-11-26]]"
digest_rank: 5
---

# AI による数学・計算量の成果が相次ぐ。Anthropic 関与のリーマン予想の Lean 証明と、OpenAI の行列積指数の主張

![](https://s0.wp.com/_si/?t=eyJpbWciOiJodHRwczpcL1wvc2NvdHRhYXJvbnNvbi5ibG9nXC93cC1jb250ZW50XC91cGxvYWRzXC8yMDIxXC8xMFwvY3JvcHBlZC1KYWNrZXQuZ2lmIiwidHh0IjoiU2h0ZXRsLU9wdGltaXplZCIsInRlbXBsYXRlIjoiZWRnZSIsImZvbnQiOiIiLCJibG9nX2lkIjoxMjk1MjA1ODB9.siOtN7gHw4tefA_rZickBw4GfI6tPxGgOQ1AXr2ZoOQMQ)

> [!summary] 一言で
> Anthropic 関係者と Claude が作ったリーマン予想（GRH）の Lean 証明が公開され、Scott Aaronson は OpenAI の「行列積の指数 ω は 9/4」という主張を紹介した。

- GRH の Lean 4 形式化は読みやすい版で約 30 万行、短縮版で約 7.6 万行。ビルドに 12 コアで 1〜2 時間かかる。機械検査は通ったが、人が通読してはおらず論文もない。
- OpenAI は 11/24 のプレプリントで ω=9/4 の下限を主張し、有限フーリエ変換の線形ゲート計算量でも N(log N)^(1/2+o(1)) を主張。Aaronson は、両社の主張は Lean 証明書で裏づけられてきたとの理解を示すが、この ω の論文に Lean 証明書があるとは書いていない。
- 形式化した命題が意図どおりかは機械検査だけでは保証されないと、リポジトリ自身も注意している。

> [!tip] So what
> 検証まで機械側に寄る流れの極端な例。ただし「命題が正しく書かれているか」を人が確かめる部分は残る。

**トピック**：[[LLM とモデル競争]]、[[AI と開発者の働き方]]
**登場**：[[Anthropic]]、[[Lean]]、[[OpenAI]]、[[Scott Aaronson]]
**出典**：[Aaronson のブログ](https://scottaaronson.blog/?p=10379)・[grh-lean（GitHub）](https://github.com/lsernau/grh-lean)（[[Digest/2026-11-26|2026-11-26 の Digest]] 5 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
