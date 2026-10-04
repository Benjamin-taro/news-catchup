# Run Log

日次・週次タスクが末尾に 1 行ずつ追記する。月 1 回、入力件数の推移とソースの死活を確認する。

```
形式（日次）: YYYY-MM-DD | 入力 N 件 | 前処理後 M 件 | 採用 K 件 | 警告: なし
形式（週次）: YYYY-Www weekly | 👍 A / 👎 B | 提案 C 件 | 警告: なし
```

2026-09-28 | matcha 初回実行 | 入力 64 件（初日・既読なし） | 警告: なし（閾値 20 件は暫定。1 週間後に見直す）
2026-09-28 | 入力 75 件 | 前処理後 48 件 | 採用 10 件 | 警告: なし（Claude Code で手動の試行。Google News の OpenAI DeployCo 記事は 5 月の発表だったため除外）
2026-09-28 | 再生成（基準を Trend 重視に変更） | 入力 75 件 | 採用 10 件 + Stack メモ 3 件 | 警告: なし
2026-09-29 | 入力 27 件 | 前処理後 20 件 | 採用 9 件（本編 7 + Explore 2）+ Stack メモ 2 件 | 警告: 06:00 に Google News が 404・再実行で HN が通信エラー（手動で取り直し済み）。収集を scripts/collect.sh（リトライ付き）に変更
2026-09-29 skip: already done
2026-09-29 skip: already done
2026-09-30 | 入力 28 件 | 前処理後 17 件 | 採用 10 件（本編 8 + Explore 2）+ Stack メモ 1 件 | 警告: なし（Computer Weekly は Google News のリダイレクトを開けず、Web 検索で内容を確認。Stack の該当記事が少ない）
2026-10-01 | 入力 60 件 | 前処理後 30 件 | 採用 10 件（本編 8 + Explore 2）+ Stack メモ 3 件 | 警告: なし（Google News のリダイレクトは開けず、Norvig 記事は本文未確認で「見出しより」扱い。SMBC Olive 72% の記事は 9 月上旬の発表のため除外）
2026-10-02 | 入力 60 件 | 前処理後 30 件 | 採用 10 件（本編 8 + Explore 2）+ Stack メモ 2 件 | 警告: なし（47news・Reuters・朝鮮日報は取得不可。ヤマトは Web 検索、Accenture は Web 検索で確認。Stack メモ 2 件は本文確認の対象外で、JEP 540 は詳細未確認）
2026-10-03 | 入力 40 件 | 前処理後 28 件 | 採用 10 件（本編 8 + Explore 2）+ Stack メモ 1 件 | 警告: なし（Google News のリダイレクトは開けず Web 検索で確認。Four Horsemen は 403 で検索要約のみ、Eric Schwartz／Amex は未確認で「見出しより」扱い。Stack の該当記事が少ない）
2026-10-04 | 入力 51 件 | 前処理後 30 件 | 採用 10 件（本編 8 + Explore 2）+ Stack メモ 1 件 | 警告: なし（Guardian は取得不可で Web 検索により確認、New Stack も検索要約のみ。RHCOS 10 は未確認。Stack の該当記事が少ない。Publickey の記事内公開日表記が 10/5 でずれていたため日付は不記載）
2026-W40 weekly | 👍 46 / 👎 23 | 提案 2 件 | 警告: なし
