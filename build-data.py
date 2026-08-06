#!/usr/bin/env python3
"""Parse the day's section-*.html fragments into data/<date>.json and update the
dedup ledger (seen-stories.json).

Usage:  python3 build-data.py 2026-08-06

- Reads section-cyber.html, section-ai.html, section-tech.html
- Writes data/<date>.json  (structured edition: lead + categories + items)
- Merges every story URL/headline into seen-stories.json with today's date,
  pruning entries older than 45 days so the ledger stays small.
Prints per-section item counts.
"""
import sys, os, json, re, datetime
from bs4 import BeautifulSoup

HERE = os.path.dirname(os.path.abspath(__file__))
BADGE_MAP = {'b-crit': 'crit', 'b-high': 'high', 'b-med': 'med', 'b-low': 'low'}
SLUGS = ['cyber', 'ai', 'tech']

def norm_title(t):
    return re.sub(r'[^a-z0-9]+', ' ', (t or '').lower()).strip()

def parse_section(path):
    soup = BeautifulSoup(open(path, encoding='utf-8').read(), 'html.parser')
    lead_div = soup.find('div', class_='lead')
    lead = []
    rosternote = ''
    if lead_div:
        for li in lead_div.select('ul li'):
            a = li.find('a')
            if a:
                lead.append({'text': a.get_text(strip=True), 'url': a.get('href', '')})
            else:
                lead.append({'text': li.get_text(strip=True), 'url': ''})
        rn = lead_div.find('p', class_='rosternote')
        rosternote = rn.get_text(strip=True) if rn else ''
    cats = []
    for sec in soup.find_all('section'):
        catspan = sec.find('div', class_='cat')
        cat_name = catspan.get_text(strip=True) if catspan else ''
        items = []
        for it in sec.find_all('div', class_='item'):
            badge = it.find('span', class_='badge')
            bclass = [c for c in (badge.get('class', []) if badge else []) if c in BADGE_MAP]
            sev = BADGE_MAP.get(bclass[0], 'med') if bclass else 'med'
            badge_label = badge.get_text(strip=True) if badge else 'Update'
            h3 = it.find('h3')
            h3a = h3.find('a') if h3 else None
            headline = (h3a.get_text(strip=True) if h3a else (h3.get_text(strip=True) if h3 else ''))
            url = h3a.get('href', '') if h3a else ''
            datediv = it.find('div', class_='date')
            date_txt = datediv.get_text(strip=True) if datediv else ''
            stale = 'stale' in (datediv.get('class', []) if datediv else [])
            summary = it.find('p').get_text(strip=True) if it.find('p') else ''
            why = it.find('div', class_='why')
            why_txt = why.get_text(strip=True).replace('Why it matters:', '').strip() if why else ''
            src = it.find('div', class_='src')
            src_a = src.find('a') if src else None
            if not url and src_a:
                url = src_a.get('href', '')
            items.append({'severity': sev, 'badge': badge_label, 'headline': headline,
                          'url': url, 'date': date_txt, 'stale': stale, 'summary': summary,
                          'why': why_txt, 'srcName': (src_a.get_text(strip=True) if src_a else 'Source')})
        cats.append({'name': cat_name, 'items': items})
    return {'lead': lead, 'rosternote': rosternote, 'categories': cats}

def update_seen(edition, date):
    path = os.path.join(HERE, 'seen-stories.json')
    seen = {s: [] for s in SLUGS}
    if os.path.exists(path):
        try:
            seen = json.load(open(path, encoding='utf-8'))
        except Exception:
            pass
    for s in SLUGS:
        seen.setdefault(s, [])
        existing = {e.get('url') for e in seen[s]}
        for cat in edition['sections'].get(s, {}).get('categories', []):
            for it in cat['items']:
                if it['url'] and it['url'] not in existing:
                    seen[s].append({'url': it['url'], 'title': norm_title(it['headline']), 'date': date})
                    existing.add(it['url'])
    # prune > 45 days
    cutoff = (datetime.date.fromisoformat(date) - datetime.timedelta(days=45)).isoformat()
    for s in SLUGS:
        seen[s] = [e for e in seen[s] if e.get('date', '9999') >= cutoff]
    json.dump(seen, open(path, 'w', encoding='utf-8'), indent=2, ensure_ascii=False)
    return {s: len(seen[s]) for s in SLUGS}

def main():
    date = sys.argv[1] if len(sys.argv) > 1 else datetime.date.today().isoformat()
    os.makedirs(os.path.join(HERE, 'data'), exist_ok=True)
    out = {'date': date, 'sections': {}}
    for slug in SLUGS:
        p = os.path.join(HERE, f'section-{slug}.html')
        out['sections'][slug] = parse_section(p) if os.path.exists(p) else {'lead': [], 'rosternote': '', 'categories': []}
    json.dump(out, open(os.path.join(HERE, 'data', f'{date}.json'), 'w', encoding='utf-8'), indent=2, ensure_ascii=False)
    counts = {s: sum(len(c['items']) for c in out['sections'][s]['categories']) for s in SLUGS}
    ledger = update_seen(out, date)
    print('data/%s.json written — items %s | ledger sizes %s' % (date, json.dumps(counts), json.dumps(ledger)))

if __name__ == '__main__':
    main()
