---
type: article
day: 2026-09-28
vote: up
score: 85
kind: 製品・発表
source: "Publickey（AWS）"
url: "https://www.publickey1.jp/blog/26/awsaistrandsllm.html"
main_topic: "[[AI エージェントの基盤と安全性]]"
topics:
  - "[[AI エージェントの基盤と安全性]]"
  - "[[AI の企業導入]]"
entities:
  - "[[AWS]]"
  - "[[Docker]]"
  - "[[Microsoft]]"
digest: "[[Digest/2026-09-28]]"
digest_rank: 3
---

# AWS・Docker・Microsoft が AI エージェントの「実行基盤」を相次いで発表

![](https://www.publickey1.jp/2026/F420bYCD.jpg)

> [!summary] 一言で
> エージェントを「作る」段階から、「どこで安全に動かすか」の競争に移り始めている。

- **AWS「Strands ハーネス」**（OSS）：数行でエージェントを作れて、Claude・GPT・Gemini・Ollama を入れ替えられる。シェル実行やファイル操作が最初から使える。コンテキストが 85% を超えると要約で圧縮し、Linux コンテナならどこにでもデプロイできる。
- **Docker「Cloud Sandboxes」**：エージェントの作業環境を、止めずにローカルとクラウドの間で移せる。数十時間の作業や 100 以上のサブエージェントの同時起動に対応し、料金は 1 時間約 10 円から。
- **Microsoft「Copilot Managed Runtime」**（プレビュー）：AI が作ったアプリを Microsoft 365 と同じテナントの中で実行し、管理者が一元管理できる。

> [!tip] So what
> ベンダーが競っているのは、モデルの性能より「権限・隔離・管理」。2 番の OpenAI の件とも同じ論点で、企業に AI を入れる仕事の中心はこのあたりになっていきそう。

**トピック**：[[AI エージェントの基盤と安全性]]、[[AI の企業導入]]
**登場**：[[AWS]]、[[Docker]]、[[Microsoft]]
**出典**：[Publickey（AWS）](https://www.publickey1.jp/blog/26/awsaistrandsllm.html)・[Publickey（Docker）](https://www.publickey1.jp/blog/26/docker_cloud_snadboxesai.html)・[Publickey（Microsoft）](https://www.publickey1.jp/blog/26/copilot_managed_runtimemicrosoft_365.html)（[[Digest/2026-09-28|2026-09-28 の Digest]] 3 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
