#!/bin/bash
# Claude Code を非対話モードで起動し、日次キュレーション／週次レビューの手順書を実行する。
# 使い方：scripts/curate.sh daily | weekly（launchd の com.yuki.news-daily / com.yuki.news-weekly から呼ばれる）
set -uo pipefail
cd "$(dirname "$0")/.."

case "${1:-}" in
  daily)  PROMPT_FILE="_system/news/prompts/daily-curation.md" ;;
  weekly) PROMPT_FILE="_system/news/prompts/weekly-review.md" ;;
  *) echo "usage: $0 daily|weekly" >&2; exit 2 ;;
esac

echo "=== $(date '+%F %T') $1 start"
git pull --rebase --autostash -q || echo "git pull failed (続行)"

/Users/iseyuki/.local/bin/claude -p \
  "今日は $(date '+%Y-%m-%d（%a）') です。${PROMPT_FILE} を読み、その手順に厳密に従って実行してください。終わったら、作成・更新したファイルと runlog に書いた行を短く報告してください。" \
  --allowedTools "Read" "Write" "Edit" "Glob" "Grep" "WebFetch" "WebSearch" \
  --disallowedTools "Bash" \
  --permission-mode dontAsk
status=$?
echo "=== $(date '+%F %T') $1 claude exit=$status"

scripts/publish.sh
