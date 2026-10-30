---
type: article
day: 2026-10-30
vote: up
score: 74
kind: 解説
source: "note（🐰）"
url: "https://note.com/hgffdgn654/n/n92467b83a1c1"
main_topic: "[[AI と開発者の働き方]]"
topics:
  - "[[AI と開発者の働き方]]"
  - "[[FDE とエンジニアのキャリア]]"
entities:
  - "[[Claude Code]]"
digest: "[[Digest/2026-10-30]]"
digest_rank: 3
---

# デザイナーが Figma を離れ、Claude Code で既存リポジトリ上のモックを作る運用

![](https://assets.st-note.com/production/uploads/images/329775375/rectangle_large_type_2_4a37721baf34426709979f4b1ee50325.png?fit=bounds&quality=85&width=1280)

> [!summary] 一言で
> SaaS のソロデザイナーが、PM の AI 製モックを起点に、GitHub 上のアプリのコードと Storybook を使って Claude Code で UI デザインを進める運用を、文脈の三層分けとあわせて報告している。

- 前提はアプリのリポジトリ、shadcn ベースのコンポーネント、Storybook、トークンの JSON、GitHub から呼べる Claude Code。デザイン用ブランチは `design/123-reservation-list` のように接頭辞を付け、マージしない。流れは Issue 選択、ブランチ作成、モック作成、PM 確認、実装依頼。
- Claude Code への文脈は「常駐」「取りに行かせる」「その場で渡す」の 3 層に分け、「指示は削る、文脈は盛る」方針にした。入力が長いほど性能が下がるという 2026 年の論文などを根拠に、1 画面ずつ短いやりとりを重ねる。
- Figma の作業時間、とくにプロトタイプ確認の工数が減った。一方でバナーや発想の段階では Figma を使い続け、出力の良し悪しを判断するのはデザイナーだとしている。

> [!tip] So what
> デザイナーがコードのリポジトリ上で動く画面を作る例で、職種の境目が動いている実例になる。ただし筆者自身は、判断（審美眼・どこに力を入れるか）が人に残るとも書いている。

**トピック**：[[AI と開発者の働き方]]、[[FDE とエンジニアのキャリア]]
**登場**：[[Claude Code]]
**出典**：[note（🐰）](https://note.com/hgffdgn654/n/n92467b83a1c1)（[[Digest/2026-10-30|2026-10-30 の Digest]] 3 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
