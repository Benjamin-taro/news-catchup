---
type: article
day: 2026-11-22
vote: up
score: 58
kind: 解説
source: "Zenn（chobitnet）"
url: "https://zenn.dev/chobitnet/articles/mikoto-voice-call"
main_topic: "[[AI と開発者の働き方]]"
topics:
  - "[[AI と開発者の働き方]]"
entities:
  - "[[Claude Code]]"
digest: "[[Digest/2026-11-22]]"
digest_rank: 4
---

# 朝 7 時半に Claude Code から iPhone に電話がかかる。Mac Studio 内で完結する音声エージェントを個人で自作

![](https://res.cloudinary.com/zenn/image/upload/s--hV9itdjG--/c_fit%2Cg_north_west%2Cl_text:notosansjp-medium.otf_55:%25E6%259C%259D7%25E6%2599%2582%25E5%258D%258A%25E3%2580%2581Claude%2520Code%25E3%2581%258B%25E3%2582%2589%25E3%2581%25AE%25E9%259B%25BB%25E8%25A9%25B1%25E3%2581%25A7%25E8%25B5%25B7%25E3%2581%2593%25E3%2581%2595%25E3%2582%258C%25E3%2581%259F%2Cw_1010%2Cx_90%2Cy_100/g_south_west%2Cl_text:notosansjp-medium.otf_37:chobitnet%2Cx_203%2Cy_121/g_south_west%2Ch_90%2Cl_fetch:aHR0cHM6Ly9zdGF0aWMuemVubi5zdHVkaW8vdXNlci11cGxvYWQvYXZhdGFyLzVjZjYyYjg1YjkuanBlZw==%2Cr_max%2Cw_90%2Cx_87%2Cy_95/v1627283836/default/og-base-w1200-v2.png?_a=BACMTiAE)

> [!summary] 一言で
> 著者が、Claude Code のエージェント「みこと」から iPhone の通常の着信画面で電話をかけ、声で指示や雑談ができる仕組みを作った。

- 聞き取りは mlx-whisper、即答は Claude Haiku、調査はターミナルの Claude Code、声は AivisSpeech のローカル合成。すべて自宅の Mac Studio で動き、接続は Tailscale。会話サーバーは Python 約 1,200 行、iOS アプリは Swift 約 1,450 行。
- 発信は PushKit の VoIP 通知で起こして CallKit の着信画面を出す。APNs への送信はライブラリを使わず、openssl で署名した JWT を curl で送っている。11/15 未明に初めて声で話せ、同日夜に初めて電話がかかった。
- 未解決は 3 人同時通話での声の重なりと、Haiku が直近 30 やりとりしか持たず、サーバー再起動で流れが途切れる点。

> [!tip] So what
> 個人開発では、業務で許されにくい「エージェントから人に電話する」ような自由な使い方が先に試される。1 人の自作の記録で、一般化はできない。

**トピック**：[[AI と開発者の働き方]]
**登場**：[[Claude Code]]
**出典**：[Zenn（chobitnet）](https://zenn.dev/chobitnet/articles/mikoto-voice-call)（[[Digest/2026-11-22|2026-11-22 の Digest]] 4 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
