# The Daily Briefing

A self-updating daily news briefing across three sections — **Cyber**, **AI**, and **Tech** — rendered as a single tabbed webpage (`index.html`) in a PwC-styled editorial layout.

## How it works

Every morning at 6:00 AM a scheduled task spawns one agent per section. Each agent:

1. Reads its source roster (`sources*.json`), researches the last 24–72 hours of news, and writes a dated, prioritized, categorized section.
2. Runs a discovery pass — finding, vetting, and adding new reputable sources (capped per day, deduped by domain), logging every change.
3. Rebuilds its standalone sources page.

A final step assembles the three sections into the tabbed `index.html`, and the result is committed here.

## Files

| File | Purpose |
|------|---------|
| `index.html` | The tabbed briefing (Cyber / AI / Tech) |
| `sources.html`, `sources-ai.html`, `sources-tech.html` | Per-section source rosters (human-readable) |
| `sources.json`, `sources-ai.json`, `sources-tech.json` | Machine-readable rosters (source of truth) |
| `sources-changelog*.md` | Logs of how each roster evolves over time |
| `section-*.html` | Intermediate per-section fragments (regenerated daily) |

## Reading it

Open `index.html` in any browser and switch tabs. The "Sources" link in the masthead follows the active tab.
