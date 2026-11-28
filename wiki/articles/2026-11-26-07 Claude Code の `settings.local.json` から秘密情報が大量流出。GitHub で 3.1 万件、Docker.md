---
type: article
day: 2026-11-26
vote: up
score: 66
kind: 調査・データ
source: "GitGuardian"
url: "https://news.google.com/rss/articles/CBMidEFVX3lxTE40Qkk1c0cxQ1llaUhBaGNaQzhycVdBSk1PY1JCZWcxbVVBXzlSQXlla2hjT0VmSFVrV3E5SUJxcDRfYnlkQWdpQ2lLLWhwbW5ZZ3ZsbXRCd2VtekJsMzlST180VFpGdlZjRTZnX0tpTDdvSllK?oc=5"
main_topic: "[[AI エージェントの基盤と安全性]]"
topics:
  - "[[AI エージェントの基盤と安全性]]"
  - "[[セキュリティ事故]]"
entities:
  - "[[GitGuardian]]"
  - "[[Claude Code]]"
digest: "[[Digest/2026-11-26]]"
digest_rank: 7
---

# Claude Code の `settings.local.json` から秘密情報が大量流出。GitHub で 3.1 万件、Docker Hub にも

> [!summary] 一言で
> GitGuardian が、「今後は確認しない」で保存される許可ルールに混じった API キーが、公開リポジトリと Docker イメージに多数漏れていると報告した。

- 公開 GitHub の `.claude/settings.local.json` に 31,088 件（23,276 リポジトリ）、うち 5,343 件が検出時に有効。`settings.json` は 8,271 件。
- Docker Hub の公開イメージにも 613 件（有効 99 件、543 リポジトリ・7,625 タグ）。有効な Cloudflare トークンが 1 つのイメージの 559 タグに入っていた例もある。
- 原因は、鍵を含むコマンドを承認すると鍵ごと許可ルールに保存されること。`COPY . .` で git 管理外のファイルまで同梱され、`.dockerignore` が `.claude/` を除外していないと出る。月次の流出は 4 月の 12,535 件から 10 月の 959 件へ 92% 減（理由は不明）。

> [!tip] So what
> 個人検証の延長でエージェントに権限を渡す運用が、業務に近づくほど漏えい経路になる。許可ルールの保管場所と配布物への混入は、ツール側の仕様に任せず自分で確認する対象。

**トピック**：[[AI エージェントの基盤と安全性]]、[[セキュリティ事故]]
**登場**：[[GitGuardian]]、[[Claude Code]]
**出典**：[GitGuardian](https://news.google.com/rss/articles/CBMidEFVX3lxTE40Qkk1c0cxQ1llaUhBaGNaQzhycVdBSk1PY1JCZWcxbVVBXzlSQXlla2hjT0VmSFVrV3E5SUJxcDRfYnlkQWdpQ2lLLWhwbW5ZZ3ZsbXRCd2VtekJsMzlST180VFpGdlZjRTZnX0tpTDdvSllK?oc=5)（[[Digest/2026-11-26|2026-11-26 の Digest]] 7 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
