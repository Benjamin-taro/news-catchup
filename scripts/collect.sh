#!/bin/bash
# Matcha を実行し、フィードの取得エラーがあれば最大 3 回まで取り直す。
# 同じ日の再実行では、失敗したフィードの記事が消えることがあるので、いちばん件数が多い結果を残す。
set -uo pipefail
cd "$(dirname "$0")/.."
OUT="inbox/matcha/$(date +%F).md"
CONFIG="_system/matcha/config.yaml"
BEST=$(mktemp); best_n=-1

for attempt in 1 2 3; do
  err=$(/usr/local/bin/matcha -c "$CONFIG" 2>&1 >/dev/null)
  [ -n "$err" ] && echo "$err" >&2
  n=$(grep -c '](http' "$OUT" 2>/dev/null || echo 0)
  echo "$(date '+%F %T') attempt $attempt: $n items"
  if [ "$n" -gt "$best_n" ]; then cp "$OUT" "$BEST"; best_n=$n; fi
  echo "$err" | grep -q "Error" || break
  sleep 60
done
cp "$BEST" "$OUT"; rm -f "$BEST"
