---
type: article
day: 2026-10-21
vote: up
score: 64
kind: 調査・データ
source: "Zenn（bpr_prot）"
url: "https://zenn.dev/bpr_prot/articles/32e8dc4f89a8ce"
main_topic: "[[AI と開発者の働き方]]"
topics:
  - "[[AI と開発者の働き方]]"
  - "[[AI エージェントの基盤と安全性]]"
entities:
  - "[[Claude Code]]"
  - "[[Codex]]"
digest: "[[Digest/2026-10-21]]"
digest_rank: 7
---

# AI に管理画面を作らせたら裏の扉も閉めるか。Claude Code と Codex で 12 回試し、12 回とも閉めた。ただし管理者のメールが画面に残る回が 5 回

![](https://res.cloudinary.com/zenn/image/upload/s--O5aS4H05--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:AI%25E3%2581%25AB%25E7%25AE%25A1%25E7%2590%2586%25E7%2594%25BB%25E9%259D%25A2%25E3%2582%2592%25E4%25BD%259C%25E3%2582%2589%25E3%2581%259B%25E3%2581%259F%25E3%2582%2589%25E3%2580%2581%25E8%25A3%258F%25E3%2581%25AE%25E6%2589%2589%25E3%2581%25BE%25E3%2581%25A7%25E9%2596%2589%25E3%2582%2581%25E3%2582%258B%25E3%2581%258B%25E3%2580%2582Claude%2520Code%25E3%2581%25A8Codex%25E3%2581%25A712%25E5%259B%259E%25E8%25A9%25A6%25E3%2581%2597%25E3%2581%259F%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_37:BPR%2520Prot.%2Cx_203%2Cy_121/g_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9zdGF0aWMuemVubi5zdHVkaW8vdXNlci11cGxvYWQvYXZhdGFyLzk5MTMzYTU5OWEuanBlZw==%2Cr_max%2Cw_90%2Cx_87%2Cy_95/v1627283836/default/og-base-w1200-v2.png?_a=BACMTiAE)

> [!summary] 一言で
> Zenn の記事が、小さな予約アプリに管理画面を作らせ、ログインなし・一般ユーザー・管理者の 3 状態で管理用 API を呼んで検証した。

- Claude Code 2.1.299 と Codex CLI（gpt-5.6-sol）に、頼み方 2 通り（「管理者だけ」の指示あり／なし）を各 3 回、計 12 回。ログインなしと一般ユーザーに管理データが返らない、管理者は使える、自分を管理者に変えられない、のいずれも 12/12。指示の有無で差はなかった。
- 別の問題として、管理者のメールアドレスがログイン欄に最初から入っていた回が 12 回中 5 回。元アプリのテスト用の値を AI が新しい画面にも広げたとみられる。
- 著者は、AI の説明文を信じず、ログアウトや一般ユーザーの状態で管理用 URL を直接開いて確かめる、公開前にテスト用の値を点検する、と結論している。

> [!tip] So what
> 「AI は権限チェックを忘れる」という通説が、この範囲では当てはまらなかった。一方で見落とされたのは機能の外にある「入力欄の初期値」だった。試したのは 1 アプリ・各条件 3 回だけで、一般化はできない。

**トピック**：[[AI と開発者の働き方]]、[[AI エージェントの基盤と安全性]]
**登場**：[[Claude Code]]、[[Codex]]
**出典**：[Zenn（bpr_prot）](https://zenn.dev/bpr_prot/articles/32e8dc4f89a8ce)（[[Digest/2026-10-21|2026-10-21 の Digest]] 7 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
