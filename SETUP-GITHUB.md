# GitHub auto-commit setup

The briefing is regenerated daily at 6:00 AM by the Cowork scheduled task. These steps push each day's edition to GitHub automatically, using **your** GitHub login (no tokens stored anywhere by Claude).

Run everything below in Terminal, from this folder:

```bash
cd ~/Cursor/DailyCyberBriefing
```

## 1. One-time: create the repo and first push

If you have the GitHub CLI (`gh`) installed and logged in (`gh auth login`):

```bash
rm -f .git/index.lock                 # clear the leftover lock from setup
gh repo create daily-briefing --public --source=. --remote=origin --push
```

That creates the public repo `daily-briefing` under your account and pushes everything.

**No `gh`?** Create an empty repo named `daily-briefing` at https://github.com/new (no README), then:

```bash
rm -f .git/index.lock
git remote add origin https://github.com/<your-username>/daily-briefing.git
git push -u origin main
```

## 2. Make daily pushes automatic (launchd)

```bash
cp com.dailybriefing.push.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.dailybriefing.push.plist
```

This runs `daily-push.sh` every day at 6:30 AM (just after the 6:00 AM regeneration), committing and pushing any changes. Logs go to `/tmp/dailybriefing-push.log`.

To test it immediately:

```bash
bash daily-push.sh
```

To stop the automation later:

```bash
launchctl unload ~/Library/LaunchAgents/com.dailybriefing.push.plist
```

## Notes

- The 6:00 AM Cowork task writes the files; the 6:30 AM launchd job pushes them. Both run only while your Mac is on (and, for the Cowork task, while the Claude app is open).
- `daily-push.sh` skips the commit entirely on days with no changes, so you won't get empty commits.
- If you later get the GitHub connector working inside Cowork, the push step can move into the 6:00 AM task itself and you can remove the launchd job.
