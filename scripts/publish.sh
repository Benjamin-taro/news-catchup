#!/bin/bash
# Digest に画像を埋め込み、Vault の変更（Digest・Weekly・wiki・設定）を GitHub に push する。
# launchd（com.yuki.news-publish）から 1 日数回呼ばれる。変更がなければ何もしない。
set -euo pipefail
cd "$(dirname "$0")/.."

git pull --rebase --autostash -q
/usr/bin/python3 scripts/add_images.py >/dev/null
git add Digest Weekly wiki _system/news
if git diff --cached --quiet; then
  echo "$(date '+%F %T') nothing to publish"
  exit 0
fi
git commit -q -m "Publish $(date '+%F %H:%M')"
git push -q
echo "$(date '+%F %T') published"
