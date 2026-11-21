---
type: article
day: 2026-11-20
vote: up
score: 74
kind: 議論・意見
source: "jschuster.org"
url: "https://jschuster.org/blog/2026/11/19/design-for-understandability/"
main_topic: "[[AI と開発者の働き方]]"
topics:
  - "[[AI と開発者の働き方]]"
entities: []
digest: "[[Digest/2026-11-20]]"
digest_rank: 4
---

# LLM 時代ほど「理解しやすさ」を設計で作れ。Google の Code Health での講演

![](https://jschuster.org/blog/wp-content/uploads/2026/10/page_6.png)

> [!summary] 一言で
> Jonathan Schuster 氏が、生成コードの品質責任は開発者にあるとして、局所的に推論できるコードを作る 3 つの設計手法を示した。

- 目標は「テストを実行せずに、すべての行の振る舞いを予測できる状態」。2025 年 11 月の Google 社内 Code Health Summit での講演の記録。
- 手法は、契約による設計（二分探索の前提と戻り値を明記）、データ不変条件（クラスで保証し、呼び出し元を全部調べなくて済むようにする）、副作用と大域状態の分離（「機能的なコア、命令的なシェル」）の 3 つ。
- コンテキストが小さいほど LLM も有用に働くので、局所的推論の設計は LLM 活用にも有利と述べている。レビューでは不変条件の維持を確認項目に加えることを勧めている。

> [!tip] So what
> 人間の役割を「コードが保守可能で健全かを判断すること」と置く議論で、大局観・設計・レビューが残るという見立てに近い。具体的な手法が付いているので、レビュー観点にそのまま使える。

**トピック**：[[AI と開発者の働き方]]
**出典**：[jschuster.org](https://jschuster.org/blog/2026/11/19/design-for-understandability/)（[[Digest/2026-11-20|2026-11-20 の Digest]] 4 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
