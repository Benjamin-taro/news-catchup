# news-catchup

SWE のホットトピックを毎朝 10 件前後の要約として Obsidian で受け取る仕組み。
設計と構築手順は [tech-news-system-blueprint.md](tech-news-system-blueprint.md) を参照。

## 流れ

| 段階 | 実行 | 時刻 | 出力 |
|---|---|---|---|
| 集める | launchd → Matcha | 毎日 06:00 | `inbox/matcha/YYYY-MM-DD.md` |
| 絞る | Cowork 日次タスク（`_system/news/prompts/daily-curation.md`） | 平日 08:00 | `Digest/YYYY-MM-DD.md` |
| 育てる | Cowork 週次タスク（`_system/news/prompts/weekly-review.md`） | 日曜 | `Weekly/YYYY-Www.md`、`wiki/tech/` |

## ディレクトリ

```
_system/news/
  interests.md        関心キーワードと重み（唯一の設定）
  feedback-log.md     週次集計の履歴
  runlog.md           実行ログ
  prompts/            Cowork タスクの手順書
inbox/matcha/         Matcha の生データ（Git 管理外）
Digest/               日次ダイジェスト（読むのはここだけ）
Weekly/               週次まとめ
wiki/tech/            👍 記事のトピック別蓄積
```

## 日々の使い方

- `Digest/` の当日ファイルを読み、気になったものだけ 👍 / 👎 にチェックを付ける。
- 週 1 回、`interests.md` の「提案」欄を見て、採用するものを上のセクションに移す。
