---
type: article
day: 2026-11-26
vote: up
score: 92
kind: 議論・意見
source: "Pragmatic Engineer"
url: "https://newsletter.pragmaticengineer.com/p/how-anthropic-builds-software-in"
main_topic: "[[AI と開発者の働き方]]"
topics:
  - "[[AI と開発者の働き方]]"
  - "[[FDE とエンジニアのキャリア]]"
entities:
  - "[[Anthropic]]"
  - "[[Claude Code]]"
digest: "[[Digest/2026-11-26]]"
digest_rank: 1
---

# Anthropic が Messages API を 5 か月で Rust に移行。人が精査したのはコードの約 2 割、レビューの要否は Claude が判定

![](https://substackcdn.com/image/fetch/$s_!MUG0!,w_1200,h_600,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff7f42984-2bb8-4041-bee8-3c81b2fa48ab_1280x720.png)

> [!summary] 一言で
> Anthropic のプラットフォーム責任者 Katelyn Lesse が、Rust 経験者のいない少人数で API を書き換え、PR レビューにも Claude の分類器を使っていると語った。

- Messages API を Python のモノリスから Rust へ約 5 か月で移行。担当は数人で、Rust の専門家はいなかった。旧 API と並べて動かす「シャドーモード」で応答が一致するまで直した。
- 生成された Rust コードを人が細かく見たのは約 20%。守りの中心は「検証できること」で、全 PR に走る Claude の分類器がリスクに応じて人のレビューの要否・人数・担当チームを決める（SDK 更新や不安定テストの修正は人のレビューを省ける）。
- コーディング面接は、手書きをやめた優秀な候補者が落ちるため廃止し、エージェントと組んで解く形式を試行中。昇進の評価は「完了までの時間」ではなく CPU 削減・遅延短縮・障害回避などの影響で見る。オンコールは Claude が先に切り分ける段階まで来ているが、人を呼ばない運用はまだ。

> [!tip] So what
> 「レビュー・運用判断は人に残る」という見立てに対し、レビューの要否判断そのものと一次切り分けが AI 側に移っている実例。一方で計画・チーム間の調整にかかる時間は AI 導入前と変わらないとも語られており、残るのは「何を検証可能にするか」を決める仕事、という読み方ができる。

**トピック**：[[AI と開発者の働き方]]、[[FDE とエンジニアのキャリア]]
**登場**：[[Anthropic]]、[[Claude Code]]
**出典**：[Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/how-anthropic-builds-software-in)・[Anthropic: Migrating our Messages API to Rust（Google News 経由・元記事）](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE91blh2eENvd0hsR25fTlhrSkktUlc3djUxb3NYdGo2dm1maGJfZlhvU3NhSS1rWk45WDczZnpiUzVrOEFWVVA1aDRfSXo3YkpfY0RuSzdESDVlU1FqN1VBV1N3Mm5ZdTQ?oc=5)（[[Digest/2026-11-26|2026-11-26 の Digest]] 1 番）

## 自分のメモ
<!-- 読んで考えたことを書く欄です。Claude は書き換えません -->
