#!/usr/bin/env bash
# Commits any changes in this folder and pushes to GitHub.
# Run manually, or let the launchd job (see SETUP-GITHUB.md) run it daily.
set -uo pipefail
cd "$(dirname "$0")" || exit 1

# Clear any stale lock (harmless if none exists)
rm -f .git/index.lock 2>/dev/null || true

git add -A
if git diff --cached --quiet; then
  echo "$(date '+%Y-%m-%d %H:%M:%S') — no changes to commit"
  exit 0
fi

git commit -m "Daily briefing: $(date '+%Y-%m-%d')" >/dev/null
if git push origin main; then
  echo "$(date '+%Y-%m-%d %H:%M:%S') — pushed to origin/main"
else
  echo "$(date '+%Y-%m-%d %H:%M:%S') — commit made locally but push failed (check 'git remote -v' and your GitHub auth)"
  exit 1
fi
