---
type: article
day: 2026-10-24
vote: up
score: 80
kind: 調査・データ
source: "Anthropic Research"
url: "https://www.anthropic.com/research/attack-surface-reduction"
main_topic: "[[AI と開発者の働き方]]"
topics:
  - "[[AI と開発者の働き方]]"
  - "[[AI エージェントの基盤と安全性]]"
entities:
  - "[[Anthropic]]"
  - "[[Claude]]"
  - "[[OpenSSH]]"
digest: "[[Digest/2026-10-24]]"
digest_rank: 1
---

# Anthropic が Claude で「攻撃対象領域」を減らす研究を公開。OSS 25 件・約 500 万行で 493 件の問題、OpenSSH では認証前に届くコードの約 5 分の 1 を除去

![](https://www-cdn.anthropic.com/images/4zrzovbb/website/6d4a0d28992ade92d6fa63646fd9c9d318245c6c-2400x1260.jpg)

> [!summary] 一言で
> 個々の脆弱性を探すのではなく、「認証前に到達できるコード」や危険な設定の組み合わせを Claude に洗い出させ、到達可能性そのものを下げる手法の初期研究。

- 対象は C・C++・Java・PHP・Python などの OSS 25 件（500 万行超）。約 17,000 の設定オプションを棚卸しし、うち 3,842 件がセキュリティ関連。警告もドキュメントもない危険な設定の組み合わせが 162 件、うち 94 件はセキュリティ制御を暗黙に無効化していた。
- OpenSSH 10.4 では、実験的な耐量子署名（ML-DSA-44）の約 4,500 行が既定設定で認証前のクライアントから到達でき、認証前コードの約 16% を占めた。報告とパッチの末に 10.6 で修正が入り、未認証クライアントが届くコードの約 5 分の 1 が消えた。
- 逆引き DNS を無効にするとホスト名の拒否ルールが効かなくなる問題が 4 プロジェクトで見つかり、2 つのオプションの衝突でクライアント証明書の検証が無効になる例は 21 年間残っていた。3 段階の分析を再利用できる Claude のスキルにまとめ、OSS-Scanner への統合を進めている。

> [!tip] So what
> 「設計・運用判断・設定の読み解きは人に残る」という見立てに対し、設定の相互作用のような経験が物を言う領域を AI が掘り当てた実例。ただし結果は Anthropic 自身の研究で、第三者の再現はまだない。

**トピック**：[[AI と開発者の働き方]]、[[AI エージェントの基盤と安全性]]
**登場**：[[Anthropic]]、[[Claude]]、[[OpenSSH]]
**出典**：[Anthropic Research](https://www.anthropic.com/research/attack-surface-reduction)（[[Digest/2026-10-24|2026-10-24 の Digest]] 1 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
