---
type: article
day: 2026-11-10
vote: up
score: 58
kind: 議論・意見
source: "GitHub（gemini_files）"
url: "https://github.com/thisisme6598/gemini_files/"
main_topic: "[[セキュリティ事故]]"
topics:
  - "[[セキュリティ事故]]"
  - "[[LLM とモデル競争]]"
entities:
  - "[[Google]]"
  - "[[Gemini]]"
digest: "[[Digest/2026-11-10]]"
digest_rank: 14
---

# 「Gemini が Drive のファイルやメールを人間の査読者に回す」と主張する GitHub 上の検証（第三者の確認なし）

![](https://opengraph.githubassets.com/a87ac41276b91a269e54c91f94e7c6e36572181b3d22633ae42451dcae549fda/thisisme6598/gemini_files)

> [!summary] 一言で
> 個人の検証リポジトリが、Gemini に連携した Gmail・Drive の内容が人間のレビュー担当者に見られうると主張し、HN で話題になっている。

- 2023 年の Workspace 拡張の発表では「人間のレビュアーには見られない」とされていたが、その約束が事実上覆ったと筆者は主張する。根拠として Google Help の記事の更新と、2023 年のブログ記事に追記された注意書きを挙げる。
- 連携が有効だと、旅行や請求に触れるだけで @ なしでも Workspace 検索が走るとし、取得内容は 4 段階（何も取れない〜ファイル全文）で確率的に変わると報告している。
- 根拠は筆者本人の再現テストのみで、Google の声明や第三者の検証はページにない。

> [!tip] So what
> AI にメールや文書をつなぐ業務利用では、「誰が中身を見うるか」の規約が判断材料になる。ただし本件は一個人の主張で、確定した事実ではない。

**トピック**：[[セキュリティ事故]]、[[LLM とモデル競争]]
**登場**：[[Google]]、[[Gemini]]
**出典**：[GitHub（gemini_files）](https://github.com/thisisme6598/gemini_files/)（[[Digest/2026-11-10|2026-11-10 の Digest]] 14 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
