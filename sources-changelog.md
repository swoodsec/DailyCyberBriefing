# Source Roster Changelog

This log records how the Daily Cyber Briefing's source roster evolves. The 6 AM task runs a discovery pass each day and appends any newly vetted sources here, so you can see — and prune — what the system has learned.

Format: `YYYY-MM-DD — [+ADDED | ~CANDIDATE | -REMOVED] Source Name (category/tier) — rationale`

---

## 2026-06-09 — Seed roster established
Initial 40 sources curated from a dedicated research project across general news, investigative, threat-intel, vulnerability feeds, and AI/LLM security. See `sources.json` for the full list. All seeded sources are marked `"seed": true` and are not auto-removed.

<!-- The daily task appends new entries below this line. -->

## 2026-06-15
- +ADDED The CyberWire (breaking/core) — long-running, credible daily cyber news network with original reporting; notable gap in the seed roster.
- +ADDED Help Net Security (breaking/strong) — original source on the LiteLLM PyPI backdoor and OWASP prompt-injection coverage; consistent original reporting.
- +ADDED NVIDIA AI Red Team (aisecurity/aifocus) — primary, hands-on LLM security research (garak, NeMo Guardrails); fills an AI attack/defense gap.
- ~CANDIDATE Security Affairs — strong original-reporting blog (Paganini); held back only by the 3/day cap, promote next run.
- ~CANDIDATE CyberGeoDigest — daily cyber+geopolitics digest; more curation than original reporting, watch before promoting.
- Reviewed ~6 candidates; 3 added (at the daily cap), 2 parked, rest were SEO listicles/aggregators that didn't meet the bar.

## 2026-06-16
- +ADDED Security Affairs (breaking/strong) — promoted from candidate; original/early source on the Aflac 22.7M notification and the Iran-linked Handala Cal Water breach. Paganini's long-running original reporting.
- +ADDED Obsidian Security (aisecurity/aifocus) — primary research team that disclosed the LiteLLM CVSS 9.9 priv-esc/RCE chain (CVE-2026-47101/47102/40217); credible hands-on AI-gateway vuln research.
- ~CANDIDATE Aikido Security — its AI pentesting tool found the decade-old phpBB auth-bypass (CVE-2026-48611); promising original vuln research but a vendor product blog, watching cadence/independence before promoting.
- Reviewed ~5 candidates; 2 added (Security Affairs promoted, Obsidian new), 1 parked, rest were aggregators/SEO listicles that didn't meet the bar.

## 2026-06-17
- +ADDED CERT Polska / CERT.PL (threatintel/strong) — Poland's national CERT; original source for the Ghostwriter/UNC1151 Gmail 2FA-phishing campaign with primary technical writeups and IOCs.
- +ADDED OX Security (aisecurity/aifocus) — disclosed the systemic MCP arbitrary-command-execution vulnerability class (150M+ downloads affected); original hands-on AI supply-chain research.
- +ADDED Adversa AI (aisecurity/aifocus) — primary adversarial-AI / red-teaming research; surfaced June MCP exposure data (Censys counts, VIPER-MCP 67 CVEs).
- ~CANDIDATE S-RM — weekly cyber-intelligence briefing with some original incident framing (law-firm helpdesk-impersonation campaign); largely curated, watch for sustained original reporting.
- ~CANDIDATE Halcyon — original ransomware tracking (INC Ransom law-firm campaign, 200+ legal incidents); credible but a vendor alert feed, monitor independence/cadence.
- Reviewed ~6 candidates; 3 added (at the daily cap), 2 parked, rest were aggregators/SEO listicles that didn't meet the bar.

## 2026-06-20

- +ADDED Arctic Wolf Labs (threatintel/strong) — published original technical analysis of the actively-exploited Oracle PeopleSoft CVE-2026-35273 (ShinyHunters) campaign ahead of broad coverage; credible IR/threat research with IOCs.
- Reviewed ~4 candidate sources behind today's stories (Arctic Wolf, The Register Cyber, Pathlock, Black Kite). 1 added (Arctic Wolf); The Register parked informally as established but aggregation-heavy; vendor blogs (Pathlock, Black Kite) did not clearly clear the original-research bar. Version bumped 4 → 5.

## 2026-06-23
- +ADDED ReliaQuest (threatintel/strong) — GreyMatter threat-research team; published the original Threat Spotlight tying the Klue/"Icarus" OAuth integration abuse to Salesforce CRM data theft ahead of broad coverage; consistent original research (SAP NetWeaver zero-day, annual threat report).
- +ADDED Huntress (threatintel/strong) — MDR provider with hands-on intrusion analysis; published its own primary investigation of the Klue breach (as responder and victim) plus consistent original writeups (Nightmare-Eclipse, Railway.com device-code phishing).
- +ADDED Orca Security (aisecurity/aifocus) — cloud/AI security research; published the primary technical breakdown of the Mastra npm scope takeover (144 packages, easy-day-js typosquat, postinstall RAT) used by AI-agent builders.
- Reviewed ~5 sources behind today's stories (ReliaQuest, Huntress, Orca, PointGuard AI, Rescana). 3 added (at the daily cap); PointGuard AI and Rescana parked informally as more incident-summary/aggregation than sustained original reporting. Version bumped 5 → 6.

## 2026-06-25
- +ADDED Cybernews (investigative/strong) — its own research team discovered and published today's lead story, the 24-billion-record / 8.3 TB infostealer leak (exposed Elasticsearch cluster, 36 sources); documented track record of original breach-discovery research (4B-record China leak, IDMerit 3B KYC exposure). Primary investigative research, not aggregation.
- Reviewed ~4 sources behind today's stories (Cybernews, Morphisec, Qualys ThreatPROTECT, Cloud Security Alliance Labs). 1 added (Cybernews); Morphisec and Qualys parked informally as credible but vendor product blogs (RoguePlanet analysis) — watch for sustained independent cadence; CSA Labs is a strong research note source but more advisory/standards than breaking original reporting. Version bumped 6 → 7.

## 2026-06-25 (refresh)
- +ADDED JFrog Security Research (vulnfeeds/strong) — published the first public root exploit walkthrough for the DirtyClone Linux kernel LPE (CVE-2026-43503) behind today's vuln story; strong original-research track record (PixelSmash FFmpeg RCE, Redis RCE, 183+ disclosed CVEs, malicious Hugging Face models). Primary technical research, not aggregation.
- +ADDED Pillar Security (aisecurity/aifocus) — published the original "Agent Security Paradox" research disclosing the Cursor allowlist-bypass RCE (CVE-2026-22708) behind today's AI story; offensive-security team with consistent original agentic-AI attack-surface research.
- Reviewed ~4 sources behind the refreshed stories (JFrog Security Research, Pillar Security, Symantec/Security.com Threat Intelligence, The Register Security). 2 added (under the 3/day cap); Symantec's security.com is credible primary intel but parked informally to stay under cap and avoid roster bloat — revisit if it recurs; The Register parked again as established but aggregation-heavy. Version bumped 7 → 8.

## 2026-07-01
- +ADDED watchTowr Labs (vulnfeeds/strong) — published the original patch-diff analysis and working pre-auth PoC for today's lead vuln, Progress Kemp LoadMaster CVE-2026-8037, ahead of broad coverage; documented offensive-research track record on Citrix NetScaler and MOVEit-class edge bugs. Primary technical research, not aggregation; no watchtowr.com domain in the roster.
- +ADDED XLab (QiAnXin) (threatintel/strong) — discovered and published the original research on today's RustDuck botnet; renowned botnet-hunting team that has exposed 30+ globally impactful botnets (Zergeca, Vo1d, AISURU, AIRASHI, Kimwolf) with hands-on C2/honeypot telemetry. Primary original research; no qianxin.com domain in the roster.
- Reviewed ~4 sources behind today's stories (watchTowr Labs, XLab/QiAnXin, Phoenix Security, Upwind). 2 added (under the 3/day cap); Phoenix Security and Upwind parked informally as credible but vendor supply-chain feeds that lean toward roundup/aggregation of others' campaigns — watch for sustained first-party original research before promoting. Version bumped 8 → 9.

## 2026-07-02
- +ADDED SentinelOne / SentinelLABS (threatintel/strong) — published the original technical analysis and attribution of today's macOS.Gaslight DPRK backdoor (Phil Stokes), the first malware observed prompt-injecting AI-assisted triage agents to abort analysis; consistent primary macOS/DPRK research (NimDoor, BONZAI signature family). Primary research, not aggregation; no sentinelone.com domain in the roster.
- +ADDED Calif.io (vulnfeeds/strong) — discovered and published the original disclosure + PoC for today's "Squidbleed" (CVE-2026-47729), a 29-year-old Squid proxy heap over-read leaking cleartext HTTP credentials, found with AI assistance (Claude Mythos Preview) and responsibly coordinated with the Squid project. Primary vuln research; no calif.io domain in the roster.
- Reviewed ~4 sources behind today's stories (SentinelLABS, Calif.io, Microsoft AutoJack coverage, Huntress). 2 added (under the 3/day cap); Microsoft's Security Blog is already effectively represented via Microsoft Threat Intelligence in the roster, and Huntress was added 2026-06-23 (behind today's Azure ROPC spray) so no new domain to add. Version bumped 9 → 10.

## 2026-07-03
- +ADDED SOCRadar (threatintel/strong) — its Threat Research Unit (STRU) ran the original FortiBleed investigation behind today's lead story: analyzed the full 86,644-firewall dataset, first tied the campaign to INC and Lynx ransomware, notified affected orgs and pushed data to CERTs, and shipped a free exposure checker. Primary original research, not aggregation; no socradar.io domain in the roster.
- +ADDED Security Discovery / Bob Diachenko (investigative/strong) — first flagged the exposed FortiBleed attacker server behind today's ransomware-pipeline story; long documented track record of first-hand exposed-database discovery (MOAB 26B records, 8.7B-record Chinese leak, 4.3B database). Primary investigative discovery, not aggregation; no securitydiscovery.com domain in the roster.
- Reviewed ~4 sources behind today's stories (SOCRadar, Security Discovery, Morphisec/RoguePlanet, Malwarebytes Labs). 2 added (under the 3/day cap); Morphisec parked again informally as a credible but vendor product blog (revisit if cadence sustains), and Malwarebytes Labs is solid but leans toward summarizing others' research (e.g. Cybernews' 24B-record find) rather than first-party discovery. Version bumped 10 → 11.
