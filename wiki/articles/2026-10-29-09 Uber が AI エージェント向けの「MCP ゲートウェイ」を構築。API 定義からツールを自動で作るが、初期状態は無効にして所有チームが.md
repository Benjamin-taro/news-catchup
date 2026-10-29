---
type: article
day: 2026-10-29
vote: up
score: 62
kind: 解説
source: "ByteByteGo"
url: "https://blog.bytebytego.com/p/how-uber-built-a-gateway-for-ai-agents"
main_topic: "[[AI エージェントの基盤と安全性]]"
topics:
  - "[[AI エージェントの基盤と安全性]]"
entities:
  - "[[Uber]]"
digest: "[[Digest/2026-10-29]]"
digest_rank: 9
---

# Uber が AI エージェント向けの「MCP ゲートウェイ」を構築。API 定義からツールを自動で作るが、初期状態は無効にして所有チームが承認

![](https://substackcdn.com/image/fetch/$s_!ASmN!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F635bad96-b0a7-4c3f-a1e7-9038bdefd67b_3336x1982.png)

> [!summary] 一言で
> ByteByteGo が、数千のサービスを持つ Uber が AI エージェントの社内ツール利用を一本化した仕組みを解説した。

- 各チームが個別に MCP 連携を作って権限管理や所在が散らばったため、ツールのカタログ（Registry）と実際の通信を処理する Proxy Gateway に分けた。HTTP・gRPC・TChannel が混在する既存サービスは、IDL からツール定義を自動生成し、LLM で説明文を改善する。
- 自動で見つかったツールは初期状態で無効。所有チームが内容を確認して有効にし、変更は差分承認を経る。認可はサーバーだけでなくツール単位（同じインシデント管理でも「読み取り」と「状態変更」を分ける）で、応答の個人情報のマスクもできる。
- ツール定義が文脈を埋める問題には、段階的に探す Omni MCP、必要な項目だけ返す Response Projection、シェルとファイルで処理する Code Mode を追加した。

> [!tip] So what
> エージェントの導入が進むほど、モデルより「接続部分の統制」が仕事になる例。ツールごとの認可と「発見と許可の分離」は、権限管理の設計の参考になる。記事にレイテンシやツール数の実数はなく、Uber 自身の説明に基づく。

**トピック**：[[AI エージェントの基盤と安全性]]
**登場**：[[Uber]]
**出典**：[ByteByteGo](https://blog.bytebytego.com/p/how-uber-built-a-gateway-for-ai-agents)（[[Digest/2026-10-29|2026-10-29 の Digest]] 9 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
