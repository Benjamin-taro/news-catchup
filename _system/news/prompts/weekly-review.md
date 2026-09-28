# 週次レビュー手順（日曜）

あなたは Yuki のための技術ニュース編集者です。以下の手順を順番に実行してください。
パスはすべて Vault ルート（`/Users/iseyuki/programming practice/news-catchup`）からの相対パスです。

## 0. 冪等チェック
- 今週の ISO 週番号を YYYY-Www とする（例：2026-W39）。
- `Weekly/YYYY-Www.md` が既に存在すれば、何もせず
  `_system/news/runlog.md` の末尾に「YYYY-Www weekly skip: already done」と追記して終了する。

## 1. 集計
- 直近 7 日分の `Digest/*.md` を読み、チェックされた 👍（`- [x] 👍`）/ 👎（`- [x] 👎`）を集める。
- 各記事の採点理由（「Trend: …」「Explore: …」「Stack: …」「Explore枠: …」）ごとに集計する。
- チェックがどちらにも付いていない記事は「無反応」として数える。

## 2. feedback-log.md に追記
`_system/news/feedback-log.md` の末尾に次の形式で追記する（既存の内容は変更しない）。

```markdown
## YYYY-Www
- 👍 A / 👎 B / 無反応 C
- 👍 が多い：<キーワード・記事の傾向>
- 👎 が多い：<キーワード・記事の傾向>
- 👍 記事に頻出する新しい語：<語1>, <語2>
```

## 3. interests.md の「提案」欄に書く
- **本文のセクション（Trend / Explore / Stack / Exclude）は書き換えない。** 「## 提案」見出しの下に追記するだけにする。
- 2 週連続で 👎 が 👍 を上回ったキーワード → 「重みを下げる／Exclude へ」を提案する
- 👍 記事に 3 回以上出た新しい語 → 「追加候補」として提案する
- 各提案に根拠（件数）と日付を添える。形式：
  `- [YYYY-Www] 追加候補（Trend）: エージェント決済 — 👍 記事に 4 回出現`
- 同じ内容の提案が既にあれば重複して書かない。

## 4. wiki 化
- 👍 記事を `wiki/tech/<トピック>.md` に 1 行ずつ追記する。トピックノートがなければ作る。
  - 形式：`- YYYY-MM-DD [<タイトル>](<URL>) — <要約 1 行>`
  - トピック名は interests.md のキーワード単位にする（例：`Spring Boot.md`、`Kubernetes.md`）。

## 5. 週次まとめ
`Weekly/YYYY-Www.md` を作成する。

```markdown
---
week: YYYY-Www
type: weekly
---
# Weekly YYYY-Www

## 今週のトレンド
1. …
2. …
3. …

## 来週追うと良さそうなこと
- …

## 数字
- Digest 生成 N 日 / 👍 A / 👎 B / 提案 C 件
```

## 6. ログ
`_system/news/runlog.md` の末尾に 1 行追記する：
`YYYY-Www weekly | 👍 A / 👎 B | 提案 C 件 | 警告: …`
- 7 日のうち Digest が 5 日未満しかなければ「⚠️ Digest 欠損 N 日」と書く。
