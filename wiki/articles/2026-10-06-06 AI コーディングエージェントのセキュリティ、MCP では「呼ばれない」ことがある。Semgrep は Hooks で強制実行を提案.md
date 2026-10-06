---
type: article
day: 2026-10-06
vote: up
score: 80
kind: 解説
source: "Semgrep"
url: "https://semgrep.dev/blog/2026/mcp-vs-hooks-ai-agent-security/"
main_topic: "[[AI エージェントの基盤と安全性]]"
topics:
  - "[[AI エージェントの基盤と安全性]]"
  - "[[AI と開発者の働き方]]"
entities:
  - "[[Semgrep]]"
  - "[[MCP]]"
digest: "[[Digest/2026-10-06]]"
digest_rank: 6
---

# AI コーディングエージェントのセキュリティ、MCP では「呼ばれない」ことがある。Semgrep は Hooks で強制実行を提案

![](https://semgrep.dev/assets/mcp-gives-agents-tools-hooks-give-security-control.png)

> [!summary] 一言で
> Semgrep が、エージェントにセキュリティ検査を組み込む方法として、MCP は任意呼び出し、Hooks は毎回必ず実行できる点で役割が違うと解説した。

- MCP はエージェントがいつ使うかを自分で決めるため、必須の統制の置き場所としては弱い。Hooks は環境側がエージェントの動作の節目で必ず介入できる。
- 同社の「Semgrep Guardian」は MCP サーバー、Hooks、Skills を 1 つにまとめ、生成されたファイルを毎回スキャンして、問題がなくなるまで再生成させる。

> [!tip] So what
> エージェントの安全性を「お願いするプロンプト」ではなく「決定的に実行される仕組み」で担保する方向が具体化している。ただし Semgrep は自社製品を売る側なので、主張と宣伝を分けて読む必要がある。

**トピック**：[[AI エージェントの基盤と安全性]]、[[AI と開発者の働き方]]
**登場**：[[Semgrep]]、[[MCP]]
**出典**：[Semgrep](https://semgrep.dev/blog/2026/mcp-vs-hooks-ai-agent-security/)（[[Digest/2026-10-06|2026-10-06 の Digest]] 6 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
