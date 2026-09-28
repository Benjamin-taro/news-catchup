# 技術ニュース収集システム 設計図・構築手順書

> 目的：Google Alerts のメールを読む作業をやめ、SWE のホットトピックを毎朝 10 件前後の要約として Obsidian で受け取る。👍/👎 で基準を育て、キャリアを考える材料にする。
> 前提：Mac、Obsidian Vault、Matcha（導入済み）、Claude Cowork（Claude Desktop）

---

## 0. 設計原則

1. **取得はコード、判断は LLM。** 収集は Matcha と launchd で機械的に行う。LLM に「今日のニュースを探して」とは頼まない。
2. **トークンを使うのは「絞る」段階だけ。** 生データの取り込みはトークンゼロにする。Plaud パイプラインと同じ考え方。
3. **上限を固定する。** 1 日最大 10 件、1 ソース最大 3 件、要約は 1 件 2 行まで。読み切れなくなったらソースを減らすか重みを下げる。ソースは増やさない。
4. **設定の真実は 1 ファイル。** 関心は `interests.md` にだけ書く。プロンプトもキーワードもすべて Vault 内で管理する。
5. **自動で書き換えさせない。** 週次の見直しは「提案 → 自分で承認」にする。
6. **壊れても気づけるようにする。** 毎日のダイジェストに入力件数を出し、異常なら警告する。

---

## 1. 全体アーキテクチャ

```
┌─────────────── [1. 集める] トークン 0 ───────────────┐
│ launchd 06:00                                         │
│  └─ Matcha                                            │
│      ├─ feeds: HN Best / はてブ IT / Spring / K8s …   │
│      ├─ feeds: Google Alerts の RSS                   │
│      └─ google_news_keywords                          │
│  → Vault/inbox/matcha/2026-09-28.md（生データ、読まない）│
└───────────────────────────────────────────────────────┘
                         ↓
┌──────── [2. 絞る] Cowork 日次タスク（ローカル実行）────────┐
│ 入力：当日の matcha ファイル + interests.md + feedback-log │
│ 処理：重複排除 → 除外語 → 1ソース3件 → 0–100 採点        │
│       → 上位 8 件 + Explore 枠 2 件 → 各 2 行要約        │
│ 出力：Vault/Digest/2026-09-28.md（👍/👎 チェック付き）    │
└───────────────────────────────────────────────────────┘
                         ↓
┌──────── [3. 育てる] Cowork 週次タスク（日曜）──────────┐
│ 1 週間分の 👍/👎 を集計 → feedback-log.md に追記         │
│ interests.md の「提案」欄に重み変更・新キーワードを書く    │
│ 👍 記事を wiki/tech/<トピック>.md に追記                 │
│ Weekly/2026-W39.md に「今週のトレンド 3 行」を作成        │
└───────────────────────────────────────────────────────┘
```

### Cowork の実行環境に関する制約（重要）

- Cowork のスケジュールタスクは通常クラウドで動き、Mac の特定フォルダには紐づけられない。
- **ローカルファイル（Obsidian Vault）を使うタスクはローカルでのみ実行される。** 実行時に Mac が起動していて、Claude Desktop アプリが開いている必要がある。
- そのため次のように分担する。
  - 収集（Matcha）は OS の launchd で動かす。Cowork が止まっていても生データは溜まる。
  - 絞る・育てるタスクは「Mac を開いている時間帯」に置く。取りこぼした日は手動で実行する。タスクは冪等にしておく（§5-2）。
- 仕様は変わりやすいので、Phase 2 で必ず 1 回実機で挙動を確認する。

---

## 2. Vault のディレクトリ構成

```
Vault/
├─ _system/news/
│   ├─ interests.md          # 関心キーワードと重み（唯一の設定）
│   ├─ feedback-log.md       # 週次集計の履歴（週次タスクが追記）
│   ├─ runlog.md             # 日次タスクの実行ログ（件数・警告）
│   └─ prompts/
│       ├─ daily-curation.md # 日次タスクの手順書
│       └─ weekly-review.md  # 週次タスクの手順書
├─ inbox/matcha/             # Matcha の出力（生データ）
├─ Digest/                   # 日次ダイジェスト（読むのはここだけ）
├─ Weekly/                   # 週次まとめ
└─ wiki/tech/                # 👍 記事をトピック別に蓄積
```

**ポイント**
- ダイジェストはデイリーノートに直接書き込まず、`Digest/YYYY-MM-DD.md` という別ファイルに出す。Obsidian で編集中のファイルと Cowork の書き込みが衝突しないようにするため。デイリーノートのテンプレートに `[[Digest/{{date}}]]` のリンクを入れておく。
- プロンプトを Vault に置くと、Cowork タスクの指示文は「このファイルを読んで従って」の 1 行で済む。手順の変更は Markdown を直すだけでよく、Git で履歴も残る。

---

## 3. 構築手順（段階導入）

| Phase | 期間 | やること | 完了条件 |
|---|---|---|---|
| 1 | 第 1 週 | Google Alerts の RSS 化、Matcha の統合、launchd 設定 | アラートメールがゼロになり、毎朝 `inbox/matcha/` にファイルができる |
| 2 | 第 2 週 | `interests.md` と日次キュレーションタスク | 毎朝 `Digest/` に 10 件のダイジェストが出る |
| 3 | 第 3〜4 週 | 👍/👎 と週次レビュータスク | `interests.md` に提案が出て、承認する運用が回る |
| 4 | 2 か月目〜 | wiki 化、Plaud 連携 | 👍 記事がトピックノートに溜まる |

**各 Phase は完了条件を満たしてから次に進む。** 一気に作ると、どこで壊れたか分からなくなる。

---

## 4. Phase 1：集める

### 4-1. Google Alerts をメールから RSS に切り替える

1. https://www.google.com/alerts を開く。
2. 各アラートの ✏️（編集）→「オプションを表示」を開く。
3. **頻度を「その都度」にする**（RSS を選ぶための条件）。
4. **配信先を「RSS フィード」にする** →「アラートを更新」。
5. 一覧に出る RSS アイコンのリンクをコピーし、後で Matcha の `feeds` に入れる。
6. 全アラートで繰り返す。メールが届かなくなったことを翌日に確認する。

> Google Alerts と `google_news_keywords` はどちらもキーワード検索型で、重複しやすい。Google Alerts で細かい条件（完全一致・除外語など）を付けたいものだけ残し、単純なキーワードは Matcha 側に寄せる、と役割を決めておく。

### 4-2. Matcha の設定（config.yaml の例）

```yaml
markdown_dir_path: /Users/<you>/Vault/inbox/matcha

feeds:
  # --- 人気度プロキシ型（S/N 比が高い） ---
  - http://hnrss.org/best 10
  - https://b.hatena.ne.jp/hotentry/it.rss 10
  - https://lobste.rs/rss 5
  # --- スタック専門 ---
  - https://spring.io/blog.atom 5
  - https://qiita.com/tags/java/feed 5
  - https://zenn.dev/topics/kubernetes/feed 5
  - https://www.publickey1.jp/atom.xml 5
  # --- 深さ枠（週 1〜数本） ---
  - https://newsletter.pragmaticengineer.com/feed 3
  - https://blog.bytebytego.com/feed 3
  # --- Google Alerts の RSS（4-1 で取得） ---
  - https://www.google.com/alerts/feeds/XXXXXXXX/YYYYYYYY 5

google_news_keywords: Spring Boot,Kubernetes,Forward Deployed Engineer,Spring AI

# LLM 要約は使わない（絞る段階は Cowork に任せる）
```

**要確認リスト**（URL・キー名は実物で確認してから入れる）
- [ ] KubeWeekly、LWKD、Baeldung Java Weekly の RSS URL（各サイトのフッターや RSS アイコンで確認）
- [ ] Zenn / Qiita のタグ名（自分が追いたいタグに変える）
- [ ] Matcha の設定ファイル指定方法と、キー名の正確な綴り（README の `notification _webhook_url` のようにスペースが混じった誤記がある）
- [ ] 末尾の件数指定（` 10`）が全フィードで効くこと

**ソースの上限**：フィードは 10〜12 本までにする。追加したくなったら、代わりに 1 本外す。

### 4-3. launchd で毎朝 06:00 に実行

`~/Library/LaunchAgents/com.yuki.matcha.plist`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>com.yuki.matcha</string>
  <key>ProgramArguments</key>
  <array>
    <string>/usr/local/bin/matcha</string>
    <!-- 設定ファイルの指定方法は README に合わせる -->
  </array>
  <key>WorkingDirectory</key><string>/Users/<you>/.config/matcha</string>
  <key>StartCalendarInterval</key>
  <dict><key>Hour</key><integer>6</integer><key>Minute</key><integer>0</integer></dict>
  <key>StandardOutPath</key><string>/tmp/matcha.out.log</string>
  <key>StandardErrorPath</key><string>/tmp/matcha.err.log</string>
</dict>
</plist>
```

```bash
launchctl load ~/Library/LaunchAgents/com.yuki.matcha.plist
launchctl start com.yuki.matcha      # 手動で 1 回試す
ls ~/Vault/inbox/matcha/             # ファイルができたか確認
cat /tmp/matcha.err.log              # エラーがないか確認
```

> `StartCalendarInterval` は、指定時刻に Mac がスリープしていた場合、復帰後に実行される。電源オフだった場合は実行されない。
> バイナリのパスは `which matcha` で確認する。Homebrew（Apple Silicon）なら `/opt/homebrew/bin/matcha`。

### Phase 1 完了チェック
- [ ] Google Alerts のメールが来なくなった
- [ ] 3 日連続で `inbox/matcha/YYYY-MM-DD.md` が生成された
- [ ] 生データの件数感を把握した（1 日およそ何件か → §5 の警告閾値に使う）

---

## 5. Phase 2：絞る

### 5-1. `interests.md` を作る

`_system/news/interests.md`

```markdown
# Interests（ニュース選別の唯一の基準）

## Core（重み 3）— 今の仕事に直結
- Spring Boot / Spring Framework
- Java（JDK リリース、言語機能）
- Kubernetes / OpenShift
- Angular
- Platform Engineering / CI/CD

## Career（重み 2）— 次のキャリアを考える材料
- Forward Deployed Engineer
- AI in banking / fintech
- エンジニアのキャリア・組織論

## Explore（重み 1）— 広げたい領域
- Spring AI / MCP / LLM アプリ開発
- 自動運転

## Exclude（見たくないもの）
- 暗号資産の価格ニュース
- ガジェットのセール・プレゼント企画
- 「〇〇選」系のまとめ記事

## 提案（週次タスクが書く／未承認）
<!-- 採用するものは上のセクションに移し、不要なものは消す -->
```

- キーワードは各セクション 3〜7 個程度にする。多すぎると採点がぼやける。
- 現在の Google Alerts のテーマを全部ここに書き出し、重みを付け直すところから始める。

### 5-2. 日次キュレーションの手順書

`_system/news/prompts/daily-curation.md`

```markdown
# 日次キュレーション手順

あなたは Yuki のための技術ニュース編集者です。以下の手順を順番に実行してください。

## 0. 冪等チェック
- 今日の日付を YYYY-MM-DD とする。
- `Digest/YYYY-MM-DD.md` が既に存在すれば、何もせず
  runlog.md に「YYYY-MM-DD skip: already done」と追記して終了する。

## 1. 入力を読む
- `inbox/matcha/YYYY-MM-DD.md`（なければ直近の未処理日のファイル）
- `_system/news/interests.md`
- `_system/news/feedback-log.md` の直近 4 週分
- 入力ファイルが見つからない場合は、Digest に「⚠️ 本日の収集データがありません。
  launchd / Matcha を確認してください」とだけ書いて終了する。

## 2. 前処理
- タイトルがほぼ同じ記事（同じ話題の別ソース）は 1 件にまとめ、ソースを併記する。
- Exclude に該当するものを除外する。
- 1 ソースあたり最大 3 件にする。

## 3. 採点（0–100）
- 次の観点で採点する：
  - interests.md のキーワードとの関連度 × 重み（Core 3 / Career 2 / Explore 1）
  - feedback-log で 👍 が多い傾向に近いものは加点、👎 が多い傾向は減点
  - 一次情報（公式リリース、著者本人の記事）を二次まとめより優先する
- 各記事に「採点理由」を 1 行で付ける（例：「Core: Spring Boot のメジャーリリース」）。

## 4. 選定
- スコア上位 8 件を選ぶ。
- 加えて、スコアに関係なく「普段の関心の外だが知っておく価値がある」記事を
  Explore 枠として 2 件選ぶ（フィルターバブル対策）。

## 5. 出力
`Digest/YYYY-MM-DD.md` を下のフォーマットで作成する。
- 要約は日本語で各 2 行まで。英語記事も日本語で要約する。
- 記事の本文を長く引用しない。
- リンクは元記事の URL にする。

## 6. ログ
runlog.md に 1 行追記する：
`YYYY-MM-DD | 入力 N 件 | 前処理後 M 件 | 採用 10 件 | 警告: …`
入力件数が {閾値} 件未満なら「⚠️ 入力が少ない」と警告を書く。
```

`{閾値}` は Phase 1 で把握した通常件数の半分くらいにする。

### 5-3. ダイジェストの出力フォーマット

```markdown
---
date: 2026-09-28
type: digest
input: 142
selected: 10
---
# Tech Digest 2026-09-28

## 1. Spring Boot 4.1 released
- 〈要約 1 行目〉
- 〈要約 2 行目〉
- 🔗 [spring.io](https://…) ｜ 82点｜Core: Spring Boot のリリース
- [ ] 👍
- [ ] 👎

## 2. …

---
## 🧭 Explore
## 9. …
```

- 👍/👎 は付けたいものだけ付ける。全件に付ける必要はない。
- 読まなかった日はそのままにする。未読ゼロは目指さない。

### 5-4. Cowork にスケジュールタスクを登録する

1. Claude Desktop → Cowork →「Scheduled」→「New task」。
2. 指示文（短くする）：
   ```
   Obsidian Vault（/Users/<you>/Vault）の
   _system/news/prompts/daily-curation.md を読み、その手順に厳密に従って実行してください。
   ```
3. Vault フォルダへのアクセスを許可する。
4. 実行時刻：**Mac を開いていることが多い時間**（例：平日 07:30）。
5. 保存したら **「今すぐ実行」で 1 回試し**、次の点を確認する。
   - [ ] ローカル実行になっているか（Vault に書き込めたか）
   - [ ] 2 回目の実行で「skip」になるか（冪等性）
   - [ ] Mac のスリープ中や Desktop アプリを閉じている時刻にどうなるか

### Phase 2 完了チェック
- [ ] 5 日連続で Digest が生成された（手動実行の日を含めてよい）
- [ ] 10 件のうち「読んでよかった」が半分以上ある
- [ ] runlog.md に件数が記録されている

---

## 6. Phase 3：育てる

### 6-1. 週次レビューの手順書

`_system/news/prompts/weekly-review.md`

```markdown
# 週次レビュー手順（日曜）

## 1. 集計
- 直近 7 日分の `Digest/*.md` を読み、チェックされた 👍 / 👎 を集める。
- 各記事の採点理由（どのキーワード・セクションで拾われたか）ごとに集計する。

## 2. feedback-log.md に追記
```
## 2026-W39
- 👍 12 / 👎 5 / 無反応 53
- 👍 が多い：Spring Boot リリース系、K8s の実運用記事
- 👎 が多い：自動運転の資金調達ニュース
- 👍 記事に頻出する新しい語：Virtual Threads, Gateway API
```

## 3. interests.md の「提案」欄に書く（本文のセクションは書き換えない）
- 2 週連続で 👎 が 👍 を上回ったキーワード → 「重みを下げる／Exclude へ」を提案
- 👍 記事に 3 回以上出た新しい語 → 「追加候補」として提案
- 各提案に根拠（件数）を添える

## 4. wiki 化
- 👍 記事を `wiki/tech/<トピック>.md` に 1 行ずつ追記する
  （日付・タイトル・リンク・要約 1 行）。トピックノートがなければ作る。

## 5. 週次まとめ
- `Weekly/YYYY-Www.md` に「今週のトレンド 3 行」と「来週追うと良さそうなこと 1 つ」を書く。
```

### 6-2. 自分の作業（週 5 分）
1. `interests.md` の「提案」欄を見る。
2. 採用するものは上のセクションに移し、不要なものは消す。
3. 必要なら Matcha の `google_news_keywords` にも反映する。

### Phase 3 完了チェック
- [ ] 2 週続けて週次レビューが回った
- [ ] 提案を 1 つ以上採用または却下した
- [ ] Digest の「読んでよかった」率が上がった実感がある

---

## 7. Phase 4：発展（任意）

### 7-1. wiki の育て方
- `wiki/tech/` のトピックノートがある程度溜まったら、月 1 回 Cowork に「各トピックの現状を 5 行で要約してノート冒頭を更新して」と頼む（LLM Wiki 方式）。
- wiki の内容を日次採点の参考にしてもよい（「既に知っている話題は減点、進展があれば加点」）。

### 7-2. Plaud との接続
- Plaud パイプライン（Autoflow → GAS → Vault）で要約が Vault に入るようになったら、週次タスクの入力に Plaud 要約のフォルダを加える。
- 会話の中で出た「気になる技術・人・会社」を `interests.md` の「提案」に回す。
- 取り込みはトークンゼロの経路のまま維持する。LLM は週次の提案生成にだけ使う。

---

## 8. 運用ルール

| ルール | 内容 |
|---|---|
| 件数上限 | Digest は 10 件（うち Explore 2 件）で固定 |
| ソース上限 | Matcha のフィードは 12 本まで。追加するときは 1 本外す |
| 未読 | 溜めない。読まなかった日の Digest は放置でよい |
| フィードバック | 気になったものだけ 👍/👎。1 日 0 件でもよい |
| 見直し | 週 1 回、提案欄を 5 分だけ見る |
| 月次点検 | runlog.md を見て、入力件数の推移とソースの死活を確認する |

---

## 9. トラブルシューティング

| 症状 | 確認すること |
|---|---|
| `inbox/matcha/` にファイルがない | `launchctl list \| grep matcha`、`/tmp/matcha.err.log`、Mac の電源状態 |
| Digest に「⚠️ 収集データなし」 | 上と同じ。Matcha を手動実行して Cowork タスクを再実行する |
| Digest が作られない | Cowork の「Scheduled」で実行履歴を確認。Desktop アプリが開いていたか、Vault へのアクセス許可はあるか |
| 入力件数が急に減った | フィードの URL 変更や廃止。runlog の警告を見て該当ソースを確認する |
| 同じ話題ばかり並ぶ | Explore 枠が機能しているか確認。Core の重みを見直す |
| つまらない記事が多い | Exclude を足すより、まずソースを 1 本減らす |

---

## 10. 決めておくこと（着手前チェック）

- [ ] Vault の絶対パス
- [ ] 日次タスクの実行時刻（Mac を確実に開いている時間）
- [ ] 1 日の件数（10 件で始め、2 週後に見直す）
- [ ] Digest の要約言語（日本語で統一 / 英語記事は英語のまま、など）
- [ ] Google Alerts で残すアラートと、Matcha に移すキーワードの仕分け
- [ ] Vault を Git 管理するか（プロンプトと interests.md の変更履歴が残るのでおすすめ）
