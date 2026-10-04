# news-catchup

SWE のホットトピックを毎朝 10 件前後の要約として Obsidian で受け取る仕組み。
設計と構築手順は [tech-news-system-blueprint.md](tech-news-system-blueprint.md) を参照。

## 流れ

| 段階 | 実行（GitHub Actions。Mac は不要） | 時刻（ロンドン時間） | 出力 |
|---|---|---|---|
| 集める | `curate.yml` の中で、今日の収集データがなければ `scripts/collect.sh` を実行（手動の取り直しは `collect.yml`） | Digest 作成の直前 | `inbox/matcha/YYYY-MM-DD.md` |
| 絞る | `curate.yml` → `scripts/curate.sh daily`（Claude Code が `daily-curation.md` を実行）→ 画像埋め込み → Pages 公開 | 05:37〜13:37 の毎時に確認し、今日の Digest がなければ作る | `Digest/YYYY-MM-DD.md` |
| 育てる | `curate.yml` → `scripts/curate.sh weekly`（`weekly-review.md`） | 日曜 20:07〜（毎時確認、未作成なら作る） | `Weekly/YYYY-Www.md`、`wiki/tech/` |
| 👍/👎 | サイトのボタン（`site-src/vote.js`）が GitHub の Digest を直接書き換える | いつでも | https://benjamin-taro.github.io/news-catchup/ |
| Obsidian 同期 | Mac の launchd → `scripts/publish.sh`（pull と、Obsidian での 👍/👎 の push） | 8:30・10:00・13:00・19:00・23:00 | — |

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

## 分析用の記録（候補ログ）

- 日次の処理は、落とした記事も含めた全候補を `_system/news/candidates/YYYY-MM-DD.jsonl` に記録する
  （フィード・検索キーワード・話題・種類・点数・採否・Digest での番号）。
- Google News はキーワードごとに 1 フィードに分けてある（`_system/matcha/config.yaml`）。どのキーワードが効いたかを区別するため。
- 集計：`python3 scripts/source_stats.py --by feed|keyword|topic|type|publisher [--days 28]`
  （集めた件数 → Digest に載った件数 → 👍/👎）。フィードやキーワードを入れ替える根拠にする。
- データが 4 週間ほどたまったら、👍/👎 を目的変数にした回帰で、採点の重みとキーワード候補を見直す。
