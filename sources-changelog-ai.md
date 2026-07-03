# AI Sources — Changelog

This file logs how the **AI news** source roster (`sources-ai.json`) evolves over time. Each morning the briefing task vets candidate outlets against the discovery rules (reputable, original reporting or authoritative primary announcements, actively publishing in 2026, clearly about general AI news rather than cybersecurity, deduped by domain) and appends what it added, promoted, or flagged here. Seeded core sources are never removed.

## 2026-06-17 — Seed roster established

Initial roster seeded with **16 sources** across five categories (models, research, products, business, policy) and three tiers (core, strong, newsletter). These were selected for editorial credibility, original reporting or primary-announcement value, and active 2026 publishing. Includes the major lab blogs (OpenAI, Google DeepMind, Anthropic, Microsoft, Meta, NVIDIA) as primary sources, leading tech-news AI desks (TechCrunch, The Verge, Ars Technica, CNBC, Reuters, Axios), research-focused outlets (MIT Technology Review, ScienceDaily), and two respected newsletters (Import AI, The Batch). No candidates carried over; the `candidates` list starts empty.

<!-- The daily task appends new entries below this line. -->

## 2026-06-20

- No new sources met the bar today (≈3 reviewed). Today's stories traced back to outlets already in the roster (CNBC, TechCrunch, OpenAI/White House primary pages, LLM-Stats, ScienceDaily). Roster unchanged at 16 sources.

## 2026-06-23

Reviewed ~6 outlets surfaced behind today's stories. Added 3, parked 2, for a roster of 19 sources. Bumped roster version to 2.

- **Added — Fortune** (`fortune.com`, business, strong). Broke the detail on Anthropic's confidential IPO filing and $965B valuation (Jun 1, 2026). Reputable, original business reporting, actively publishing in 2026, AI-relevant and not cybersecurity-focused. Not previously in roster (deduped by domain).
- **Added — Crunchbase News** (`news.crunchbase.com`, business, strong). Primary source for AI funding-round data and weekly megaround roundups (e.g., Flourish's $500M Bezos-backed round). Original reporting backed by Crunchbase's deal database; clearly AI/business relevant.
- **Added — SemiAnalysis** (`semianalysis.com`, research, strong). Influential original AI/semiconductor and compute-economics research firm and newsletter (250k+ subscribers, cited by Nvidia/AMD leadership). Rigorous primary analysis of the AI buildout, not aggregation.
- **Candidate — SiliconANGLE** (`siliconangle.com`, business). Solid enterprise-AI coverage (Flourish raise, DeepMind robotics) but skews event/vendor-driven; parked pending a stronger original-reporting track record.
- **Candidate — The New Stack** (`thenewstack.io`, products). Credible developer/AI-tooling outlet but narrower scope and partly analysis/opinion; monitoring for original-reporting cadence before adding.

## 2026-06-25

Reviewed ~5 outlets surfaced behind today's stories (OpenAI/Broadcom, Bloomberg, The Decoder, Engadget already in roster, BusinessWire). Added 2, for a roster of 22 sources. Bumped roster version to 4.

- **Added — Bloomberg** (`bloomberg.com`, business, strong). Broke today's Google-to-Anthropic researcher departures (Jonas Adler, Alexander Pritzel; Jun 24, 2026) and consistently breaks AI business, deal, and talent scoops. Top-tier reputable original reporting, actively publishing in 2026, AI/business relevant and not cybersecurity-focused. Not previously in roster (deduped by domain).
- **Added — The Decoder** (`the-decoder.com`, research, strong). Editorially independent AI desk by DEEP CONTENT, part of heise medien (Europe's largest tech publisher); 1,700+ original AI articles/yr spanning model releases, research, and policy. Surfaced the "65% of internal code" detail behind today's Claude Tag story (Jun 23). Reputable, actively publishing in 2026, clearly AI-relevant.
- Not added — Broadcom investor relations and BusinessWire are primary IR/press-release wires rather than original-reporting outlets; the OpenAI/Broadcom Jalapeño story is already covered by the OpenAI Blog (in roster). WIRED remains parked as a candidate (overlap with existing Verge/Ars/MIT Tech Review desks).

## 2026-06-25 (refresh)

Refreshed the briefing with the latest 24–72h stories (OpenAI/Broadcom Jalapeño verified on the OpenAI primary page; Gemini 3.5 Flash now default in Search/Gemini app; US export-control shutdown of Claude Fable 5 & Mythos 5; Meta Muse Spark; Assort Health and Taktile rounds). Reviewed ~4 outlets behind today's stories (VentureBeat, PR Newswire, Fortune already in roster, The Information). Added 1, parked 1, for a roster of 23 sources. Bumped roster version to 5.

- **Added — VentureBeat** (`venturebeat.com`, products, strong). Long-established, editorially credible enterprise-AI desk doing original reporting and proprietary (VB Pulse) survey research on models, agents, and infrastructure; surfaced primary detail behind today's OpenAI/Broadcom Jalapeño dev-acceleration and Meta Muse Spark naming stories. Actively publishing in 2026, clearly AI-relevant, not cybersecurity-focused, deduped by domain (not previously in roster).
- **Candidate — The Information** (`theinformation.com`, business). Top-tier original AI-business scoops, but a hard paywall limits link usability for a daily briefing and coverage overlaps existing Bloomberg/Reuters/CNBC entries; parked pending a clearly citable, non-gated scoop.
- Not added — PR Newswire and BusinessWire (Assort Health, Taktile releases) are press-release wires, not original-reporting outlets; the underlying funding stories are already covered by roster outlets (TechCrunch, Crunchbase News).

## 2026-07-01

Refreshed the briefing with the latest 24–72h stories (OpenAI's GPT-5.6 Sol/Terra/Luna preview and its US-government-mandated trusted-partner-only rollout, Jun 26; Anthropic's Claude Science launch and internal drug-discovery program, Jun 30; Commerce lifting export controls on Claude Fable 5 & Mythos 5, Jun 30; Gemini 3.5 Pro's GA slipping to July, Jun 29; Baseten's $1.5B Series F; Odyssey's $310M world-model round; the ~400K Claude Code sessions study). Reviewed ~7 outlets surfaced behind today's stories plus 1 discovery search. Added 1, parked 2, for a roster of 24 sources. Bumped roster version to 6.

- **Added — Latent Space** (`latent.space`, research, newsletter). The definitive AI-engineering publication (swyx and Alessio Fanelli), pairing a widely followed podcast with original written deep dives on inference economics, agent frameworks, and the tooling layer; covered today's GPT-5.6 Sol/Terra/Luna trusted-partner release with original framing. Editorially independent, actively publishing in 2026, clearly AI-relevant (research/tooling) and not cybersecurity-focused, deduped by domain (not previously in roster).
- **Candidate — STAT News** (`statnews.com`, research). Top-tier original health/biotech journalism that interviewed Dario Amodei for its Claude Science coverage (Jun 30), but primarily a health/pharma desk rather than a general-AI outlet; parked pending recurring general-AI relevance.
- **Candidate — The Next Web** (`thenextweb.com`, products). Credible European tech outlet with original AI product coverage (framed Claude Science as an "AI workbench for the lab"), but overlaps existing Verge/Ars/VentureBeat/Engadget product desks; parked pending a clearly differentiated original scoop.
- Not added — CNBC, MIT Technology Review, TechCrunch, Bloomberg and OpenAI/Anthropic primary pages behind today's stories are already in the roster. BusinessWire (Baseten) is a press-release wire, not an original-reporting outlet. The EU Commission's `digital-strategy.ec.europa.eu` is an authoritative primary regulator page used directly for the AI Act item but is a government portal rather than a news outlet, so not added as a roster "source."

## 2026-07-02

Refreshed the briefing with the latest 24–72h stories (Anthropic's Claude Sonnet 5 launch as the new Free/Pro default, Jun 30; the July 1 redeployment of Fable 5 and Mythos 5 after export controls were lifted, plus the new cross-industry jailbreak-severity framework with Amazon/Microsoft/Google; Gov. Newsom's first-of-its-kind California/Anthropic 50%-discount deal, Jun 29; Gemini 3.5 Pro's GA slipping to July; Zhipu's MIT-licensed GLM-5.2; the Google/Microsoft Agentic Resource Discovery spec). Reviewed ~5 outlets surfaced behind today's stories plus 1 discovery search on emerging AI-research newsletters. Added 1, for a roster of 25 sources. Bumped roster version to 7.

- **Added — Interconnects (Nathan Lambert)** (`interconnects.ai`, research, newsletter). Widely regarded as the newsletter of record for frontier-lab research analysis in 2026: original, technically rigorous essays and model reviews on RL/post-training and the open-model ecosystem from a practicing AI researcher, published 1–3x/week. Editorially independent, actively publishing in 2026, clearly AI-relevant (research), not cybersecurity-focused, and distinct from Latent Space's AI-engineering angle. Deduped by domain (not previously in roster).
- Not added — Anthropic and Google Developers primary pages behind today's Sonnet 5, Fable 5 and ARD stories are already covered (Anthropic News in roster; Google DeepMind Blog in roster). TechCrunch (Newsom/Anthropic deal), Crunchbase News (Baseten) and Latent Space (GLM-5.2) are already in the roster. The California Governor's `gov.ca.gov` press release and `whitehouse.gov` executive-order page are authoritative primary government portals used directly for citations but are not news outlets, so not added as roster "sources."

## 2026-07-03

Refreshed the briefing with the latest 24–72h stories (Meta Compute's launch to resell surplus AI capacity, Jul 1; the ~6% Philadelphia Semiconductor Index slump on Jul 2 driven by Meta and a report that OpenAI more than halved inference costs; MGX's $49B AI fund close, Jul 1; Together AI's $800M Series C at $8.3B led by Aramco Ventures, Jul 1; Google's Nano Banana 2 Lite image model, Jun 30; Willow's Atlas 1 speech-to-text; plus Gemini 3.5 Pro's July GA target and GPT-5.6's trusted-partner gating as background). Reviewed ~6 outlets surfaced behind today's stories plus 1 discovery search on emerging AI-research newsletters. Added 1, for a roster of 26 sources. Bumped roster version to 8.

- **Added — AlphaSignal** (`alphasignal.ai`, research, newsletter). Technical "by researchers, for researchers" AI newsletter (180k+ subscribers) covering ML and hardware developments, trending research/repos, and original analysis of emerging models and techniques. Original curation and analysis rather than pure link aggregation; distinct from The Batch's applied-digest angle and Interconnects' post-training focus by leaning ML-engineering/research-trend. Editorially credible, actively publishing in 2026, clearly AI-relevant (research), not cybersecurity-focused, deduped by domain (not previously in roster).
- Not added — CNBC/Bloomberg (MGX), TechCrunch (Together AI), Seeking Alpha and Yahoo Finance (chip-stock/Meta coverage), and Google DeepMind, OpenAI and Anthropic primary pages behind today's stories are already in the roster or are aggregating wires. **Quartz** (`qz.com`) covered MGX but was rejected on the "original reporting" criterion after TechCrunch (Jan 2025) documented Quartz quietly publishing AI-generated news articles. **The Rundown** and **TLDR AI** surfaced in the discovery search but are daily-digest aggregators that distill others' reporting rather than produce original reporting/research, so they fail the criteria. **The Information** (OpenAI inference-cost scoop) remains a parked candidate (hard paywall limits link usability).
