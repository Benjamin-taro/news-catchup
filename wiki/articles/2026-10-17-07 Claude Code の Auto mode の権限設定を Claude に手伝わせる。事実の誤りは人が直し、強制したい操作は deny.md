---
type: article
day: 2026-10-17
vote: up
score: 72
kind: 解説
source: "Zenn（koki_n22）"
url: "https://zenn.dev/koki_n22/articles/04174e8cca69ab"
main_topic: "[[AI エージェントの基盤と安全性]]"
topics:
  - "[[AI エージェントの基盤と安全性]]"
  - "[[AI と開発者の働き方]]"
entities:
  - "[[Claude Code]]"
digest: "[[Digest/2026-10-17]]"
digest_rank: 7
---

# Claude Code の Auto mode の権限設定を Claude に手伝わせる。事実の誤りは人が直し、強制したい操作は deny/ask に

![](https://res.cloudinary.com/zenn/image/upload/s--Hg9ZQRLX--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:Claude%2520Code%2520Auto%2520mode%25E3%2581%25AE%25E6%25A8%25A9%25E9%2599%2590%25E8%25A8%25AD%25E5%25AE%259A%25E3%2582%2592Claude%25E3%2581%25AB%25E6%2589%258B%25E4%25BC%259D%25E3%2582%258F%25E3%2581%259B%25E3%2581%259F%25E3%2582%2589%25E3%2581%258B%25E3%2581%25AA%25E3%2582%258A%25E6%25A5%25BD%25E3%2581%25AB%25E3%2581%25AA%25E3%2581%25A3%25E3%2581%259F%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_37:koki_n22%2Cx_203%2Cy_121/g_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUFUWEFKdzJOTE9mR0hiLTctLUlPODdCTWxucHBQMG16NFNfUGpTazBrMEU9czk2LWM=%2Cr_max%2Cw_90%2Cx_87%2Cy_95/v1627283836/default/og-base-w1200-v2.png?_a=BACMTiAE)

> [!summary] 一言で
> Zenn の記事が、`/auto-mode-setup` で初期設定を生成し、誤りをレビューして運用に乗せるまでの実践を、拒否された具体例つきで書いた。

- `~/.claude/settings.json` の `autoMode.environment` に、信頼するリポジトリ・ツール・外部通信先を自動生成。既存の `permissions.allow/ask/deny` は変わらない。生成内容には誤りがあり、信頼対象の範囲（実行したリポジトリのみ→管理する全リポジトリ）や、本番 DB と使い捨てテスト DB の区別を人が直した。
- 拒否されたら報告で終わらず「今回だけ許可／ask に登録／中止」を提示するルールを `CLAUDE.md` に書いた。ただし設定変更が `Self-Modification` で拒否され、「今回だけ許可」でも通らず、最終的に `/permissions` から人が許可した例も載せている。
- 毎回確認したい操作（例：`claude -p *`）だけ `ask` にして、ほかは分類器に任せた。`gh pr merge` は煩わしくなり ask から外した。

> [!tip] So what
> 権限の自動化は「自動生成して、人が事実を直す」二段で回すのが現実的、という個人の記録。`CLAUDE.md` の指示は強制力がなく、止めたい操作は `deny/ask` で明示する、という点は 10/16 の hooks の話と同じ方向。

**トピック**：[[AI エージェントの基盤と安全性]]、[[AI と開発者の働き方]]
**登場**：[[Claude Code]]
**出典**：[Zenn（koki_n22）](https://zenn.dev/koki_n22/articles/04174e8cca69ab)（[[Digest/2026-10-17|2026-10-17 の Digest]] 7 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
