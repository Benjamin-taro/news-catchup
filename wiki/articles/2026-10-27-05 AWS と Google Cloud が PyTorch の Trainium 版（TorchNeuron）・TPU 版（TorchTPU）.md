---
type: article
day: 2026-10-27
vote: up
score: 60
kind: 製品・発表
source: "Publickey"
url: "https://www.publickey1.jp/blog/26/awsgoogle_cloudpytorchaws_trainiumgoogle_cloud_tpunvidia.html"
main_topic: "[[LLM とモデル競争]]"
topics:
  - "[[LLM とモデル競争]]"
entities:
  - "[[AWS]]"
  - "[[Google Cloud]]"
  - "[[PyTorch]]"
digest: "[[Digest/2026-10-27]]"
digest_rank: 5
---

# AWS と Google Cloud が PyTorch の Trainium 版（TorchNeuron）・TPU 版（TorchTPU）をオープンソースで公開。NVIDIA の CUDA からの移行に挑む

![](https://www.publickey1.jp/2026/yycsrzk6.jpg)

> [!summary] 一言で
> 両社が PyTorch Conference 2026（10/20〜21）で、自社 AI チップ向けの PyTorch バックエンドを誰でも使える形にした。

- AWS の TorchNeuron はパブリックベータで、`.to('neuron')` に切り替えるだけで Trainium 上で動き、eager 実行と torch.compile にも対応。Google Cloud の TorchTPU は torch.compile との統合で性能を狙う。どちらも以前は限定公開だった。
- PyTorch は事実上 CUDA 上で動かすのが標準で、周辺ソフトも CUDA の性能を前提に作られてきた。Linux Foundation の 2024 年調査では AI 研究・開発の 70% 超が PyTorch を使う。
- 記事は、乗り換えの可否は互換性だけでなく、ライブラリ連携、実際の性能、コスト、運用のしやすさ次第だと指摘する。

> [!tip] So what
> NVIDIA の優位を支えてきたソフトの壁を、クラウド各社が埋めにきている。性能の数字は出ておらず、効果は実ワークロードでの検証待ち。

**トピック**：[[LLM とモデル競争]]
**登場**：[[AWS]]、[[Google Cloud]]、[[PyTorch]]
**出典**：[Publickey](https://www.publickey1.jp/blog/26/awsgoogle_cloudpytorchaws_trainiumgoogle_cloud_tpunvidia.html)（[[Digest/2026-10-27|2026-10-27 の Digest]] 5 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
