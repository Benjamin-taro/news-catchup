---
type: article
day: 2026-11-23
vote: up
score: 46
kind: 解説
source: "Qiita（yamamoto_a_genee）"
url: "https://qiita.com/yamamoto_a_genee/items/76562c5c80032ad9e962"
main_topic: "[[AI と開発者の働き方]]"
topics:
  - "[[AI と開発者の働き方]]"
  - "[[AI エージェントの基盤と安全性]]"
entities: []
digest: "[[Digest/2026-11-23]]"
digest_rank: 11
---

# Agent Harness を理解するため、約 150 行の Python で自作してみた

![](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-user-contents.imgix.net%2Fhttps%253A%252F%252Fcdn.qiita.com%252Fassets%252Fpublic%252Farticle-ogp-background-afbab5eb44e0b055cce1258705637a91.png%3Fixlib%3Drb-4.1.1%26w%3D1200%26blend64%3DaHR0cHM6Ly9xaWl0YS11c2VyLXByb2ZpbGUtaW1hZ2VzLmltZ2l4Lm5ldC9odHRwcyUzQSUyRiUyRnMzLWFwLW5vcnRoZWFzdC0xLmFtYXpvbmF3cy5jb20lMkZxaWl0YS1pbWFnZS1zdG9yZSUyRjAlMkY0MzA1MDA4JTJGNzE4YmZlNjc1MzFiODg4YTAzM2E0NDU4ODVhYWEzOTcwMjBkZTg3NSUyRnhfbGFyZ2UucG5nJTNGMTc3NDMzNTAyNz9peGxpYj1yYi00LjEuMSZhcj0xJTNBMSZmaXQ9Y3JvcCZtYXNrPWVsbGlwc2UmYmc9RkZGRkZGJmZtPXBuZzMyJnM9YTE5N2UxZjE2ODVjYWMzY2VlNjM4MGZlMThmMGFmY2Q%26blend-x%3D120%26blend-y%3D462%26blend-w%3D90%26blend-h%3D90%26blend-mode%3Dnormal%26mark64%3DaHR0cHM6Ly9xaWl0YS1vcmdhbml6YXRpb24taW1hZ2VzLmltZ2l4Lm5ldC9odHRwcyUzQSUyRiUyRnMzLWFwLW5vcnRoZWFzdC0xLmFtYXpvbmF3cy5jb20lMkZxaWl0YS1vcmdhbml6YXRpb24taW1hZ2UlMkZiNWFlY2JlOWIwYWVmMzU2ZGNlMTJiNjA3MWRlZWMxMjU4OGM5NjkzJTJGb3JpZ2luYWwuanBnJTNGMTcwOTcyMDcwNT9peGxpYj1yYi00LjEuMSZ3PTQ0Jmg9NDQmZml0PWNyb3AmbWFzaz1jb3JuZXJzJmNvcm5lci1yYWRpdXM9OCZiZz1GRkZGRkYmYm9yZGVyPTIlMkNGRkZGRkYmZm09cG5nMzImcz1lNmM0YmM3MjlmODQ2NmNkMWViYzJmMzRkMTA5MWQ4Yw%26mark-x%3D186%26mark-y%3D515%26mark-w%3D40%26mark-h%3D40%26s%3D3052d3c6b067f2f389ce2137801ab62f?ixlib=rb-4.1.1&w=1200&fm=jpg&mark64=aHR0cHM6Ly9xaWl0YS11c2VyLWNvbnRlbnRzLmltZ2l4Lm5ldC9-dGV4dD9peGxpYj1yYi00LjEuMSZ3PTk2MCZoPTMyNCZ0eHQ9QWdlbnQlMjBIYXJuZXNzJUUzJTgyJTkyJUU3JTkwJTg2JUU4JUE3JUEzJUUzJTgxJTk5JUUzJTgyJThCJUUzJTgxJTlGJUUzJTgyJTgxJUUzJTgxJUFCJUUzJTgwJTgxMTUwJUU4JUExJThDJUUzJTgxJUJCJUUzJTgxJUE5JUUzJTgxJUFFUHl0aG9uJUUzJTgxJUE3JUU4JTg3JUFBJUU0JUJEJTlDJUUzJTgxJTk3JUUzJTgxJUE2JUUzJTgxJUJGJUUzJTgxJTlGJnR4dC1hbGlnbj1sZWZ0JTJDdG9wJnR4dC1jb2xvcj0lMjMxRTIxMjEmdHh0LWZvbnQ9SGlyYWdpbm8lMjBTYW5zJTIwVzYmdHh0LXNpemU9NTYmdHh0LXBhZD0wJnM9ZTU5Mjk1NGJiZTQxMDU0ZWQ4ZWFiZThhNzQ1ZWZiYzk&mark-x=120&mark-y=112&blend64=aHR0cHM6Ly9xaWl0YS11c2VyLWNvbnRlbnRzLmltZ2l4Lm5ldC9-dGV4dD9peGxpYj1yYi00LjEuMSZ3PTgzOCZoPTU4JnR4dD0lNDB5YW1hbW90b19hX2dlbmVlJnR4dC1jb2xvcj0lMjMxRTIxMjEmdHh0LWZvbnQ9SGlyYWdpbm8lMjBTYW5zJTIwVzYmdHh0LXNpemU9MzYmdHh0LXBhZD0wJnM9MTExMWZkZDRkNTU0NDMwMWIzMDJkNjcwYWVjY2JiYjM&blend-x=242&blend-y=454&blend-w=838&blend-h=46&blend-fit=crop&blend-crop=left%2Cbottom&blend-mode=normal&txt64=5qCq5byP5Lya56S-R2VORUU&txt-x=242&txt-y=539&txt-width=838&txt-clip=end%2Cellipsis&txt-color=%231E2121&txt-font=Hiragino%20Sans%20W6&txt-size=28&s=88633c988ff913b12d7b2b11368accd6)

> [!summary] 一言で
> Qiita の記事が、LLM のツール呼び出しループを約 150 行で実装し、「Agent = LLM + Harness」の役割分担を整理した。

- ツールはファイルの読み書きとコマンド実行。ワークスペース外のパスを拒否し、許可リスト外のコマンドは実行前に確認する。出力の切り詰め、ステップ数の上限、JSON Lines のトレースも備える。
- API キーなしで制御ロジックを確かめるテスト（FakeClient）を用意した。Python の bytecode キャッシュのせいで修正後も古いコードが動く問題に当たり、コマンドごとに一時キャッシュ先を指定して回避した。
- 筆者の結論は、許可リストや承認は利便性の仕組みで安全な境界にはならず、信頼できないコードは隔離環境で動かすべき、というもの。

> [!tip] So what
> エージェントの中身を小さく作って理解する入門的な記事。隔離のない承認だけでは守れない、という点は 6・4 とつながる。

**トピック**：[[AI と開発者の働き方]]、[[AI エージェントの基盤と安全性]]
**出典**：[Qiita（yamamoto_a_genee）](https://qiita.com/yamamoto_a_genee/items/76562c5c80032ad9e962)（[[Digest/2026-11-23|2026-11-23 の Digest]] 11 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
