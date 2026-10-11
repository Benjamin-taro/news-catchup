# news-catchup で Claude と話すときの手引き

このリポジトリは、技術・キャリアのニュースを毎朝集めて Obsidian で読む個人用の仕組み。全体像と運用は `README.md`、
日次・週次の自動処理の手順書は `_system/news/prompts/` にある。ここには、**会話で記事を引いて考えるとき**の約束だけ書く。

## データの所在（どこに何があるか）

| 場所 | 中身 | 言語・粒度 |
|---|---|---|
| `_system/news/candidates/YYYY-MM-DD.jsonl` | その日に集まった記事 **全部**（落としたものも）。原題・URL・`topic`・`terms`・`type`・点数・採否・Digest 番号 | 原題は英語が多い。`terms` は日本語の正規化キーワード |
| `Digest/YYYY-MM-DD.md` | その日に選ばれた 15 件（2026-10-11 までは 10 件）の日本語要約（一言で・要点・So what）と、読み手の 👍/👎 | 日本語 |
| `wiki/articles/` | 👍 を付けた記事のノート（1 記事 1 ノート）。`## 自分のメモ` は読み手の欄 | 日本語 |
| `wiki/topics/` | 話題ごとの「現状のまとめ」「論点と立場」「問い」。`## 自分の考え` は読み手の欄 | 日本語 |
| `_system/news/questions.md` | 読み手がいま答えを持っていない問いと、今の見立て | 読み手が書く |
| `_system/news/interests.md` | 選別のキーワードと重み | 週次レビューも書き換える |

検索は `python3 scripts/find_articles.py` を使う。候補ログ・Digest・wiki を横断して Markdown で出す。

```bash
python3 scripts/find_articles.py FDE キャリア             # OR 検索、直近 28 日
python3 scripts/find_articles.py --and AI レビュー --shown  # AND、Digest に載ったものだけ
python3 scripts/find_articles.py --topic career --days 0  # 話題コードで全期間
python3 scripts/find_articles.py --terms                  # terms の一覧（検索語を決めるときに）
```

話題コード：`ai-work` `ai-enterprise` `career` `bigtech` `incident` `agent-infra` `llm` `banking` `legal-tech` `autonomous` `stack` `other`

## 問いについて聞かれたら（`/question` と同じ手順）

1. `_system/news/questions.md` を読み、対象の問い・見立て・「揺らぐとしたら」を押さえる。
2. `find_articles.py` で引く。検索語は問いの名詞だけでなく、`--terms` の一覧から近い語を 3〜5 個選ぶ。英語の原題にも当たるよう英語の語も混ぜる。期間は既定 28 日、少なければ `--days 0`。
3. 該当記事を **支持する／揺らす／関係はあるがどちらでもない** に分ける。判断の軸は「揺らぐとしたら」に書かれた事実に当たるか。迷ったら元記事を WebFetch で読む（Digest の要約だけで断定しない）。
4. 出力は次の順。(a) 揺らす記事を先に、1 件 1〜2 行で「何が見立てのどこに当たるか」。(b) 支持する記事。(c) 見立ての書き換え案を 1〜2 行（書き換え不要ならそう言う）。(d) 集める経路に穴があれば、足す検索語の案。
5. `questions.md` を書き換えるのは、読み手が「直して」と言ったときだけ。直すときは「見立て」の行と「更新」の日付を変える。

## やってはいけないこと

- `Digest/` の 👍/👎 のチェック、`wiki/` の `## 自分の考え`・`## 自分のメモ`、`_system/news/feedback-log.md` は書き換えない。
- 日次・週次の自動処理（`_system/news/prompts/`、`scripts/curate.sh`、`.github/workflows/`）を、頼まれていないのに変えない。
- このリポジトリは **Public**。読み手の個人的な事情を含む文章を、頼まれていないのにファイルへ書かない。
- 新しいサービスや依存を増やさない。スクリプトは標準ライブラリだけで書く。
