# news-catchup

SWE のホットトピックを毎朝 10 件前後の要約として Obsidian で受け取る仕組み。
設計と構築手順は [tech-news-system-blueprint.md](tech-news-system-blueprint.md) を参照。

## 流れ

| 段階 | 実行 | 時刻 | 出力 |
|---|---|---|---|
| 集める | launchd → `scripts/collect.sh`（Matcha をリトライ付きで実行） | 毎日 06:00（ロンドン時間） | `inbox/matcha/YYYY-MM-DD.md` |
| 絞る | launchd → `scripts/curate.sh daily`（Claude Code を `claude -p` で起動し `_system/news/prompts/daily-curation.md` を実行） | 毎日 08:00（ロンドン時間） | `Digest/YYYY-MM-DD.md` |
| 公開 | launchd → `scripts/publish.sh`（OGP 画像を埋め込んで push）→ GitHub Actions | 8:30・10:00・13:00・19:00・23:00 | https://benjamin-taro.github.io/news-catchup/ |
| 育てる | launchd → `scripts/curate.sh weekly`（`_system/news/prompts/weekly-review.md`） | 日曜 20:00（ロンドン時間） | `Weekly/YYYY-Www.md`、`wiki/tech/` |

## ディレクトリ

```
_system/news/
  interests.md        関心キーワードと重み（唯一の設定）
  feedback-log.md     週次集計の履歴
  runlog.md           実行ログ
  prompts/            キュレーションの手順書（curate.sh が読む）
_system/matcha/
  config.yaml         Matcha の設定（フィード・google_news_keywords）
inbox/matcha/         Matcha の生データ（Git 管理外）
Digest/               日次ダイジェスト（読むのはここだけ）
Weekly/               週次まとめ
wiki/tech/            👍 記事のトピック別蓄積
```

## 日々の使い方

- `Digest/` の当日ファイルを読み、気になったものだけ 👍 / 👎 にチェックを付ける。
- 週 1 回、`interests.md` の「提案」欄を見て、採用するものを上のセクションに移す。

## Matcha（収集）

- 設定：`_system/matcha/config.yaml`（launchd の `~/Library/LaunchAgents/com.yuki.matcha.plist` がこのファイルを `-c` で指定）
- 既読 DB：`~/.config/matcha/matcha.db`（Git 管理外。消すと既読がリセットされる）
- ログ：`/tmp/matcha.out.log`、`/tmp/matcha.err.log`
- 手動実行：`launchctl kickstart gui/$(id -u)/com.yuki.matcha`（`scripts/collect.sh` 経由。取得エラーがあれば最大 3 回取り直し、件数が最も多い結果を残す）

## 公開（GitHub Pages）

- `scripts/publish.sh`：`scripts/add_images.py` で Digest に OGP 画像を埋め込み、変更があれば commit・push する。
  launchd の `~/Library/LaunchAgents/com.yuki.news-publish.plist` から 1 日 5 回実行（ログ：`/tmp/news-publish.*.log`）。
- push されると GitHub Actions（`.github/workflows/pages.yml`）が `scripts/build_site.py` でサイトを作り、Pages に公開する。
- 手動で公開：`launchctl kickstart gui/$(id -u)/com.yuki.news-publish`
- ローカルでサイトを確認：`python3 scripts/build_site.py && open _site/index.html`

## キュレーション（Claude Code）

- `scripts/curate.sh daily|weekly`：Claude Code を非対話モードで起動し、手順書を実行する。終わったら `scripts/publish.sh` で公開する。
  - 許可するツールは Read / Write / Edit / Glob / Grep / WebFetch / WebSearch だけ（Bash は禁止、`--permission-mode dontAsk`）。
- launchd：`com.yuki.news-daily`（平日 8:00）、`com.yuki.news-weekly`（日曜 20:00）。ログは `/tmp/news-daily.log`、`/tmp/news-weekly.log`。
- 取りこぼした日や作り直したいとき：`launchctl kickstart gui/$(id -u)/com.yuki.news-daily`
  （その日の Digest がすでにあれば skip する。作り直すときは先に `Digest/YYYY-MM-DD.md` を消す）
