---
type: article
day: 2026-11-17
vote: up
score: 76
kind: 調査・データ
source: "ITmedia NEWS"
url: "https://www.itmedia.co.jp/news/article/2611/16/2000003244/"
main_topic: "[[AI エージェントの基盤と安全性]]"
topics:
  - "[[AI エージェントの基盤と安全性]]"
  - "[[セキュリティ事故]]"
entities:
  - "[[Google]]"
  - "[[Claude Code]]"
digest: "[[Digest/2026-11-17]]"
digest_rank: 4
---

# Google が「人間なしで脆弱性を見つけて悪用する AI フレームワーク」を初観測、攻撃者は Claude Code の設定ファイルも書き換えた

![](https://www.itmedia.co.jp/news/article/ogp/2611/16/2000003244/10012270/2048)

> [!summary] 一言で
> Google の GTIG が四半期の AI 脅威レポートで、パッチ公開前後のソースを比較して脆弱性発見から攻撃コード実行までを自動で行う「exploit_agent」を初めて確認したと発表した。

- ゼロデイ攻撃は 2025 年の月平均 8 件から 2026 年は月平均 11 件、8 月は 22 件に増え、1〜8 月の脆弱性・エクスプロイトの公開数はほぼ倍増した。
- 北朝鮮関連の疑いがある UNC6836 は、侵入後に社内リポジトリの Claude Code 設定ファイルを書き換え、起動時にバックドアが取得されるように仕込んでいた。
- 盗んだ認証情報で企業のクラウドの LLM を使う「LLMJacking」では、Mandiant 対応の 1 日で 10 万ドル超、最大で累計 100 万ドルの不正利用があった。

> [!tip] So what
> エージェントの設定ファイル自体が攻撃の足場になった実例で、権限管理の話に直結する。数字は Google 自身の観測。

**トピック**：[[AI エージェントの基盤と安全性]]、[[セキュリティ事故]]
**登場**：[[Google]]、[[Claude Code]]
**出典**：[ITmedia NEWS](https://www.itmedia.co.jp/news/article/2611/16/2000003244/)（[[Digest/2026-11-17|2026-11-17 の Digest]] 4 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
