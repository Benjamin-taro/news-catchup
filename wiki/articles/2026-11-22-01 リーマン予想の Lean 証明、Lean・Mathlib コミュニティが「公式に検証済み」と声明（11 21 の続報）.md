---
type: article
day: 2026-11-22
vote: up
score: 72
kind: 報道
source: "Lean community blog"
url: "https://leanprover-community.github.io/blog/posts/riemann-hypothesis/"
main_topic: "[[LLM とモデル競争]]"
topics:
  - "[[LLM とモデル競争]]"
  - "[[AI と開発者の働き方]]"
entities:
  - "[[Levent Alpöge]]"
digest: "[[Digest/2026-11-22]]"
digest_rank: 1
---

# リーマン予想の Lean 証明、Lean・Mathlib コミュニティが「公式に検証済み」と声明（11/21 の続報）

![](https://leanprover-community.github.io/blog/meta-twitter.png)

> [!summary] 一言で
> Alpöge 氏が 11/20 に公開したリーマン予想の Lean 証明について、Lean と Mathlib のコミュニティが 4 つの基準で検証したとする共同声明を出した。

- 証明は Mathlib だけに依存する Lean ライブラリで、規模は約 1,700 万行。数十人が同じ証明のエクスポートを再現し、Lean のカーネルや第三者製を含む複数のチェッカーを通った。
- 定理の述べ方が Mathlib の `RiemannHypothesis` の定義と一致することも、2 つの専用ツール（`comparator`、`con-leche --compare`）で確認した。検証は元のソースではなく、悪意あるコードを避けるための無害化したエクスポートに対して行っている。
- 声明が保証するのは形式コードの正しさで、数学的なアイデアの理解ではない。「新しいアイデアを数学者が説明する作業はこれから」と書き、査読の代わりでもないと断っている。ページは AI の利用には触れていない。

> [!tip] So what
> 形式検証が済むと「証明が正しいか」の確認は機械側に移るが、何が証明の鍵だったかを読み解く仕事は人に残る。11/21 の初報では人の精査待ちだった点が一段進んだ。

**トピック**：[[LLM とモデル競争]]、[[AI と開発者の働き方]]
**登場**：[[Levent Alpöge]]
**出典**：[Lean community blog](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/)・[ITmedia（元記事・未確認）](https://www.itmedia.co.jp/news/article/2611/22/2000003388/)（[[Digest/2026-11-22|2026-11-22 の Digest]] 1 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
