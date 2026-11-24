---
type: article
day: 2026-11-24
vote: up
score: 74
kind: 調査・データ
source: "GitHub（anthropics/formal-math）"
url: "https://github.com/anthropics/formal-math/tree/main/vp-vnp"
main_topic: "[[AI と開発者の働き方]]"
topics:
  - "[[AI と開発者の働き方]]"
  - "[[LLM とモデル競争]]"
entities:
  - "[[Anthropic]]"
digest: "[[Digest/2026-11-24]]"
digest_rank: 4
---

# Anthropic の社内モデルが「VP ≠ VNP」の証明を発見、証明も Lean の形式化も AI が書いた。人間の数学者はまだ確認していない

![](https://opengraph.githubassets.com/64bf3f533d00cb8b588541c0ba8a11aff11b02cc9c2feda52c95b22b025ebd9f/anthropics/formal-math)

> [!summary] 一言で
> Anthropic が、代数的計算量の未解決問題に関する結果と、その Lean 4 の形式化を GitHub に公開した。人間による検証は済んでいない。

- 主張は、あらゆる体で、永久式（permanent）とハミルトン閉路多項式を計算する回路の大きさが m^(c·(log m)^(1/3)) を超えるというもの。これが正しければ VP ⊊ VNP になるが、README は「P vs NP は解かない」と明記している。
- 論文と Lean の証明は両方とも AI が書いた。証明は Mathlib のみに依存し、CI では 2 つ目の独立した検証器（nanoda）でも照合する。ただし「定理の文が論文の主張と一致しているか」は機械では確認されず、論文の付録 Q の対応表に頼る。
- リポジトリは保守されず、貢献も受け付けない研究成果物として置かれている。

> [!tip] So what
> Q1 の「残るのは設計・レビュー」に対し、検証まで機械側に寄った例。ただし人が残るのは「問いの文が正しいかを確かめる」部分で、その確認はまだ誰もしていない。数学の話で、ソフトウェアの仕事にそのまま当てはまるとは言えない。

**トピック**：[[AI と開発者の働き方]]、[[LLM とモデル競争]]
**登場**：[[Anthropic]]
**出典**：[GitHub（anthropics/formal-math）](https://github.com/anthropics/formal-math/tree/main/vp-vnp)（[[Digest/2026-11-24|2026-11-24 の Digest]] 4 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
