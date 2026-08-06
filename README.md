# The Daily Briefing

A self-updating daily news briefing across three sections — **Cyber**, **AI**, and **Tech** — rendered as a single-page webapp (`index.html`) with a vertical section/category sidebar, a month **calendar** to browse past editions, and a light/dark theme toggle.

## How it works

Every morning at 6:00 AM a scheduled task spawns one agent per section. Each agent:

1. Reads its source roster (`sources*.json`) and the dedup ledger (`seen-stories.json`), runs broad headline sweeps plus roster feeds for the last 24–72 hours, and writes a dated, prioritized, categorized section fragment.
2. Skips stories already published in recent editions unless there's a material update, to avoid repeats.
3. Runs a discovery pass — finding, vetting, and adding new reputable sources (capped per day, deduped by domain), logging every change, and rebuilding its sources page.

Two scripts then finish the build:

- `build-data.py <date>` parses the three `section-*.html` fragments into a structured `data/<date>.json` edition and updates `seen-stories.json`.
- `build-index.py` inlines **all** archived editions into `index.html`, so the calendar and every past day render from a single self-contained file.

The result is committed and pushed via `daily-push.sh`.

## Files

| File | Purpose |
|------|---------|
| `index.html` | The briefing webapp (sidebar nav + calendar), generated — do not hand-edit |
| `data/<date>.json` | One structured record per day; the edition archive (never deleted) |
| `seen-stories.json` | Dedup ledger of recently published stories (per section, ~45-day window) |
| `build-data.py` | Parses section fragments → `data/<date>.json`, updates the ledger |
| `build-index.py` | Inlines all editions into `index.html` |
| `sources.json`, `sources-ai.json`, `sources-tech.json` | Machine-readable source rosters (source of truth) |
| `sources.html`, `sources-ai.html`, `sources-tech.html` | Human-readable source rosters |
| `sources-changelog*.md` | Logs of how each roster evolves over time |
| `section-*.html` | Intermediate per-section fragments (regenerated daily) |
| `daily-push.sh` | Commits and pushes the edition to GitHub |

## Reading it

Open `index.html` in any browser. Pick a section (Cyber / AI / Tech) in the left sidebar; its categories appear beneath it as jump links. Use the calendar or the ‹ › day arrows to browse past editions, and the ☾/☀ button to switch light/dark.

## Rebuilding manually

```bash
python3 build-data.py "$(date +%F)"   # after the section-*.html fragments exist
python3 build-index.py                # regenerate index.html from data/*.json
```
