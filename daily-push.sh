#!/usr/bin/env bash
# Commit the day's briefing and push it to GitHub.
#
# - Reads the GitHub token from ./push.env (gitignored) as $GITHUB_PAT.
# - Does all git work in a throwaway temp clone, so a stale/read-only
#   .git/index.lock in the synced folder can never block the push.
# - The token is passed via an HTTP auth header, so it is never written
#   into the git remote URL or config.
#
# Run manually:  bash daily-push.sh
# Or let launchd run it daily (see SETUP-GITHUB.md).
set -uo pipefail
SRC="$(cd "$(dirname "$0")" && pwd)"

# --- load token from local env file ------------------------------------
if [ -f "$SRC/push.env" ]; then
  # shellcheck disable=SC1091
  source "$SRC/push.env"
fi
: "${GITHUB_PAT:?GITHUB_PAT not set — create push.env with: export GITHUB_PAT=github_pat_...}"

REMOTE="https://github.com/swoodsec/DailyCyberBriefing.git"
AUTH="$(printf 'x-access-token:%s' "$GITHUB_PAT" | base64 | tr -d '\n')"
HDR="http.extraheader=Authorization: Basic ${AUTH}"

# --- work in a temp clone ----------------------------------------------
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT
if ! git -c "$HDR" clone --quiet "$REMOTE" "$WORK/repo" 2>/dev/null; then
  # empty repo (no commits yet) — start fresh
  mkdir -p "$WORK/repo"
  ( cd "$WORK/repo" && git init -q && git branch -M main && git remote add origin "$REMOTE" )
fi
cd "$WORK/repo" || exit 1

# --- sync current files in (never the secret or git metadata) ----------
rsync -a --exclude='.git' --exclude='push.env' --exclude='*.env' "$SRC"/ ./

git config user.name  "Andrew Swartwood"
git config user.email "aswartwood@gmail.com"
git add -A

if git diff --cached --quiet; then
  echo "$(date '+%Y-%m-%d %H:%M:%S') — no changes to commit"
  exit 0
fi

git commit -q -m "Daily briefing: $(date '+%A, %B %-d, %Y')"
if git -c "$HDR" push -q origin HEAD:main; then
  echo "$(date '+%Y-%m-%d %H:%M:%S') — pushed to origin/main"
else
  echo "$(date '+%Y-%m-%d %H:%M:%S') — commit made, but push FAILED (check token scope / network)"
  exit 1
fi
