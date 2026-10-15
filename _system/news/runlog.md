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
2026-10-05 | 入力 63 件 | 前処理後 51 件 | 採用 10 件（本編 8 + Explore 2）+ Stack メモ 0 件 | 警告: なし（Google News・Finextra・47NEWS・NYT・X は取得不可で Web 検索により確認。Dan Adler の発言時期と Noah Smith 記事の本文は未確認。Stack の該当記事なし。X の Frontier Academy 投稿は「10/4」だが報道は 10/2 発表）
2026-10-06 | 入力 77 件 | 前処理後 62 件 | 採用 10 件（本編 8 + Explore 2）+ Stack メモ 3 件 | 警告: なし（Finextra は 403、Google News のリダイレクトは開けず Web 検索で確認。Wikimedia・Codex Cloud・Beam は本文取得。Stack メモ 3 件は本文未確認。本編 3 は複数記事を 1 項目に統合。楽天の 1.01 億件は真偽未確認）
2026-10-07 | 入力 79 件 | 前処理後 71 件 | 採用 10 件（本編 8 + Explore 2）+ Stack メモ 1 件 | 警告: なし（OpenAI 数学の記事は 403 で本文未確認、「見出しより」扱い。東北 3 行・JPMorgan・BI 調査は Google News のリダイレクトが開けず Web 検索で確認。Spring は要約のみ。本編 5・6 は複数記事を 1 項目に統合。BI の開発者調査は本文未確認のため不採用）
2026-10-08 | 入力 78 件 | 前処理後 64 件 | 採用 10 件（本編 8 + Explore 2）+ Stack メモ 3 件 | 警告: なし（OpenAI GPT-6 は 403 で不採用。InfoQ・Reuters(Tesla EU) は Google News のリダイレクトが開けず本文未確認で「見出しより」扱い。日販・Anthropic は X 投稿を Web 検索で確認、ゲーム AI 費用は検索で裏取りできず不採用。本編 1 は 4 記事を 1 項目に統合。Stack メモ 3 件は本文未確認）
2026-10-09 | 入力 71 件 | 前処理後 59 件 | 採用 10 件（本編 8 + Explore 2）+ Stack メモ 2 件 | 警告: なし（CNBC は 403、AP・Reuters は取得不可、日経は未取得。OpenAI 売上・Microsoft 永住権・ARTEX・Google・IndexBox は「見出しより」扱いで Web 検索を併用。ARTEX の「公開停止」は検索で裏取りできず。Pragmatic Engineer は有料のため冒頭のみ。Stack メモ 2 件は本文未確認。本編 1 はブックオフ・金融庁、本編 4 は MAS・ベトナム、本編 3 は X 3 件を 1 項目に統合）
2026-10-10 | 入力 71 件 | 前処理後 60 件 | 採用 10 件（本編 8 + Explore 2）+ Stack メモ 2 件 | 警告: なし（Ars Technica・Reuters(Stellantis)・NHK 等の Google News リダイレクトは開けず、Stellantis は Web 検索のうえ「見出しより」扱い、東北 3 行は検索で確認。本編 2 は mtlynch 記事と X 投稿、本編 3 は NHK・陸奥新報・ABA の 3 件を統合。本編 7 は X 投稿を起点に ITmedia 記事で確認。Stack メモ 2 件は本文未確認。IDCF の攻撃者側の数字は運営元未確認）
2026-10-11 | 入力 49 件 | 前処理後 39 件 | 採用 10 件（本編 8 + Explore 2）+ Stack メモ 1 件 | 警告: なし（Google News・X のリダイレクトは開けず。本編 4（X 投稿 3 件を統合）・7（FinTech Global）・8（ABC17）は本文未確認で「見出しより」扱いし、7・8 は Web 検索で周辺情報を補足。Chrome 4GB の記事は 5/19 の再掲載、TBS の北東北 3 行は 10/2 の発表、X の OpenAI 数学は 10/6 の発表で不採用。Brief IA は裏取りできず不採用。Stack メモ 1 件は本文未確認。Unix 認証の記事は本編外）
2026-W41 weekly | 👍 49 / 👎 21 | 提案 2 件（重み変更 1・検索キーワード追加 1。保留 2 件） | 警告: なし
2026-10-12 | 入力 85 件 | 前処理後 73 件 | 採用 14 件（本編 11 + Explore 3）+ Stack メモ 3 件 | 警告: なし（本編が 12 件に届かず 11 件。Google News・X のリダイレクトと Phoronix・Inc.・Finextra・Substack は 403 などで開けず。本編 5（VentureBeat）・10（ET CIO）・11（Phoronix）・9（X 投稿 3 件を統合）と Explore 13（Japan Times）・14（Inc.）は「見出しより」扱いで Web 検索を併用。本編 2 の Harvard 研究は見出しの「解決した課題は増えない」を裏取りできず、確認できた範囲だけ記載。Gunma-第四北越の統合は 2026 年 3 月の最終合意済みで不採用。Yandex は 10/11 掲載済みで重複。Karpathy の投稿は日付が確認できず不採用。FIS・米国の AI 事象報告義務化は本文・裏取りなしで不採用。Stack メモ 3 件は本文未確認）
2026-10-13 | 入力 93 件 | 前処理後 74 件 | 採用 15 件（本編 12 + Explore 3）+ Stack メモ 2 件 | 警告: なし（Google News のリダイレクトは開けず。本編 4（Check Point）・6（Economic Times）・7（日経、Legalscape 提携は検索で確認）・8（Bloomberg）・10（MIXED）と Explore 14（Valeo）・15（BigGo）は「見出しより」扱いで Web 検索を併用し、Valeo・SBI の関与は裏取りできず。Ars Technica は取得不可で 10/12 の Harvard 研究と同件のため重複扱い。IMF ブログは 404 で不採用。Linus Torvalds は 10/12 掲載済み、TBS の東北 3 行は 10/2 の発表で不採用。事故・セキュリティは本編 2 件（安野提言・フランス冷蔵設備）で、Fake Claude Code インストーラーは上限で落とした（cap）。GLM-Legal は本文取得不可で不採用。Stack メモ 2 件のうち Zenn は本文未確認）
2026-10-14 | 入力 96 件 | 前処理後 66 件 | 採用 15 件（本編 12 + Explore 3）+ Stack メモ 2 件 | 警告: 本文を確認できず外した（unfetched）: Indian Express（FDE 求人 1,807% 増。検索で出た別媒体の記事は 5 月掲載・数字も別で差し替えず）、Finextra（SBS・UOB・Credit Agricole・Agentic AI 導入記事は 403）、SiliconANGLE（Chainguard）、CIO Dive、Zelos（Gasgoo）、ACT News、FinTech Global、Biz/Zine、梶谷健人の note、秋田魁新報・日経ヴェリタス（秋田銀の記事は 10/2 の統合検討開始の続き。検索でも本文なし）。本文を読めたものだけを採用し「見出しより」の項目は 0 件。old: AudioEye のアクセシビリティ調査（9/30 発表）、VS Code 1.141（10/7 リリース）。dup: 日経の Anthropic「デジタル粘菌」は 10/13 本編 1 と同件。X は 6 件が告知・宣伝で exclude。事故・セキュリティは本編 1 件（SBI 証券）で、フランスの冷蔵設備攻撃（10/13 掲載済み）は cap。本編 1 は HN・Lobsters・Google News・The Register を統合、本編 8（Gemini 4）は HN・はてブ・Snowflake、本編 9 は HN・ITmedia を統合。Claude Code v2.1.299 のリリース日は本文取得時に不整合があり日付は不記載。Stack メモ 2 件のうち SvelteKit は本文確認済み、Spring は週次まとめの要約
2026-10-15 | 入力 92 件 | 前処理後 71 件 | 採用 15 件（本編 12 + Explore 3）+ Stack メモ 2 件 | 警告: 差し替え: 日経→朝日新聞（Yahoo!ニュース。みずほ AI Bootcamp）, Finextra→Banking Dive（JPMorgan）, The New Stack→LWN（Torvalds。New Stack は見出しのみ取得で、競合状態の詳細は LWN の範囲に限定）。本文取得不可で不採用（unfetched）: Analytics India Magazine・ETHRWorld・BW（FDE 求人 19 倍。検索でも 19 倍の裏取りができず）、CNBC（Dell）、MarketWatch（日産）、朝鮮日報、秋田魁新報、36 Kr、ｄメニュー（FSB 指針は検索でも原文未確認）、Android Authority（Google の電話番号連携）、Finextra（Starling は 403）。old: Data for Progress（9/29 公表。Explore 候補から外した）、ビジネス+IT の北東北 3 行（統合協議入りは 10/1 の発表）。本編 12（NEC）は X 投稿のみで本文扱い、元報道は未確認。本編 9（Uber）は書き起こし未取得で要点まで。Stack メモ 2 件は本文未確認。事故・セキュリティは本編 1 件（SneakPeek）＋Explore 1 件（Starlink）で上限内。Nikkei 以外の入力エラーなし
