---
type: article
day: 2026-10-19
vote: up
score: 76
kind: 調査・データ
source: "Zenn（mskbhd）"
url: "https://zenn.dev/mskbhd/articles/lab-1027-claude-code"
main_topic: "[[AI エージェントの基盤と安全性]]"
topics:
  - "[[AI エージェントの基盤と安全性]]"
  - "[[AI と開発者の働き方]]"
entities:
  - "[[Claude Code]]"
digest: "[[Digest/2026-10-19]]"
digest_rank: 3
---

# Claude Code の公式プラグイン security-guidance を 18 回実行して測定。脆弱コードは止めず、サブスク認証の headless では LLM レビューが動かなかった

![](https://res.cloudinary.com/zenn/image/upload/s--Q6wffBSp--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:Claude%2520Code%25E3%2581%25AEsecurity-guidance%25E3%2581%25AF%25E8%2584%2586%25E5%25BC%25B1%25E3%2582%25B3%25E3%2583%25BC%25E3%2583%2589%25E3%2582%2592%25E6%25AD%25A2%25E3%2582%2581%25E3%2582%258B%25E3%2581%258B%252018%25E5%259B%259E%25E5%25AE%259F%25E8%25A1%258C%25E3%2581%2597%25E3%2581%25A6%25E6%25B8%25AC%25E3%2581%25A3%25E3%2581%259F%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_37:mskbhd%2Cx_203%2Cy_121/g_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9zdGF0aWMuemVubi5zdHVkaW8vdXNlci11cGxvYWQvYXZhdGFyLzUyNzVlNTNkNzUuanBlZw==%2Cr_max%2Cw_90%2Cx_87%2Cy_95/v1627283836/default/og-base-w1200-v2.png?_a=BACMTiAE)

> [!summary] 一言で
> Zenn の記事が、Claude Code 2.1.299 で公式プラグイン security-guidance (v2.0.13) を実測し、「遮断はしない」うえに、使い方によってはレビュー層が黙ってスキップされると報告した。

- 正規表現の層は、危険なコード 15 件のうち 7 件にだけ警告し、SQL インジェクションと秘密情報は 0 件。安全なコード 8 件には 1 件の誤検知（コメント内の `eval(`）。公式ドキュメントにも書き込みやコミットを止める層はないとある。
- LLM レビュー層は、サブスクリプション認証の `claude -p` では 4 タスクすべてでスキップされ、画面にエラーも出なかった。API キーを渡すと危険なコード 6 件をすべて指摘したが、指摘を受けて直した例は 0 件。レビュー 1 回あたり 0.017〜0.080 ドル、4.6〜10.7 秒。
- 結果を左右したのはプラグインよりモデルで、Opus は頼んでいなくても SQL インジェクションや pickle を安全な実装に置き換え、Haiku は頼まれたとおり脆弱なコードを書いた。

> [!tip] So what
> 「セキュリティ用プラグインを入れたから安心」とは言えず、安全の担保は権限をモデルの外に置く仕組み（hooks での遮断など）の側にあるという実測。各条件 1 回ずつの実行で、対話モードは未検証。

**トピック**：[[AI エージェントの基盤と安全性]]、[[AI と開発者の働き方]]
**登場**：[[Claude Code]]
**出典**：[Zenn（mskbhd）](https://zenn.dev/mskbhd/articles/lab-1027-claude-code)（[[Digest/2026-10-19|2026-10-19 の Digest]] 3 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
