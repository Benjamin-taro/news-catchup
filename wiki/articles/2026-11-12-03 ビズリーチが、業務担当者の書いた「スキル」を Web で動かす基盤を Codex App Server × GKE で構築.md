---
type: article
day: 2026-11-12
vote: up
score: 76
kind: 解説
source: "Zenn（ビズリーチ）"
url: "https://zenn.dev/bizreach_aps/articles/3accc0a17e6a93"
main_topic: "[[AI と開発者の働き方]]"
topics:
  - "[[AI と開発者の働き方]]"
  - "[[AI エージェントの基盤と安全性]]"
entities:
  - "[[ビズリーチ]]"
  - "[[Codex]]"
digest: "[[Digest/2026-11-12]]"
digest_rank: 3
---

# ビズリーチが、業務担当者の書いた「スキル」を Web で動かす基盤を Codex App Server × GKE で構築

![](https://res.cloudinary.com/zenn/image/upload/s--X6_0HHsU--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:%25E6%259A%2597%25E9%25BB%2599%25E7%259F%25A5%25E3%2582%2592%25E3%2582%25B9%25E3%2582%25AD%25E3%2583%25AB%25E3%2581%25AB%25E3%2580%2581%25E3%2582%25B9%25E3%2582%25AD%25E3%2583%25AB%25E3%2582%2592%25E3%2583%2597%25E3%2583%25AD%25E3%2583%2580%25E3%2582%25AF%25E3%2583%2588%25E3%2581%25AB%2520%25E2%2580%2595%2520Codex%2520App%2520Server%2520%25C3%2597%2520GKE%2520%25E3%2581%25AE%25E5%25AE%259F%25E8%25A1%258C%25E5%259F%25BA%25E7%259B%25A4%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_34:ozwts%2Cx_220%2Cy_108/bo_3px_solid_rgb:d6e3ed%2Cg_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9zdGF0aWMuemVubi5zdHVkaW8vdXNlci11cGxvYWQvYXZhdGFyL2ZiOWJiMTRmMmUuanBlZw==%2Cr_20%2Cw_90%2Cx_92%2Cy_102/co_rgb:6e7b85%2Cg_south_west%2Cl_text:notosansjp-medium.otf_30:BizReach%2520AI%2520Product%2520S...%2Cx_220%2Cy_160/bo_4px_solid_white%2Cg_south_west%2Ch_50%2Cl_fetch:aHR0cHM6Ly9zdGF0aWMuemVubi5zdHVkaW8vdXNlci11cGxvYWQvYXZhdGFyLzg4YTRkMjcxNmUuanBlZw==%2Cr_max%2Cw_50%2Cx_139%2Cy_84/v1627283836/default/og-base-w1200-v2.png?_a=BACMTiAE)

> [!summary] 一言で
> ビズリーチの AI Product Studio は、ローカルの Claude Code で動かしていた業務のスキルを、そのまま Web から実行できる基盤にした。

- 依頼ごとに GKE 上の隔離環境（OSS の Agent Sandbox）を用意し、中で Codex App Server を動かす。ブラウザを閉じても処理は続き、指示・やり直し・人の修正は DB に記録する。
- Claude Agent SDK と比較して Codex App Server を選んだ決め手は、Apache-2.0 の OSS で、モデル提供元を設定で切り替えられること（実際に途中で切り替えた）。Amazon Bedrock AgentCore も検討し、記録・実行・文脈を自前で持つため見送った。比較は公式ドキュメントの整理で実測ではない。
- 暗黙知 → スキル（確率的）→ オブジェクト（決定的）と固めていき、価値が確かな型だけをプロダクトの機能にする。効くスキルを見分け続けられるかが課題とされ、数字はない。

> [!tip] So what
> 業務担当者がスキルを書き、エンジニアは基盤と「固める判断」を担うという分担で、技術職と非技術職の垣根が薄れる側の実例（Q3 を支持）。まだ走り始めた段階で、成果の数字はない。

**トピック**：[[AI と開発者の働き方]]、[[AI エージェントの基盤と安全性]]
**登場**：[[ビズリーチ]]、[[Codex]]
**出典**：[Zenn（ビズリーチ）](https://zenn.dev/bizreach_aps/articles/3accc0a17e6a93)（[[Digest/2026-11-12|2026-11-12 の Digest]] 3 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
