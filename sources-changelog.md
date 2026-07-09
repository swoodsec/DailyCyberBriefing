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

## 2026-07-04
- +ADDED Sysdig / Threat Research Team (threatintel/strong) — its TRT published the original research behind today's lead AI story: JADEPUFFER, the first documented end-to-end LLM-driven ("agentic") ransomware operation (Langflow CVE-2025-3248 → MySQL/Nacos database extortion, 1,342 configs encrypted with an unrecoverable key, 600+ self-narrating payloads, a failed exploit fixed autonomously in 31 seconds). Full payload/IOC analysis; documented original-research track record (LLMjacking coinage, Langflow CVE-2026-33017 campaign, agentic container escape). Primary hands-on research, not aggregation; no sysdig.com domain in the roster.
- +ADDED Blackpoint Cyber (threatintel/strong) — its Adversary Pursuit Group researchers (Nevan Beal, Sam Decker) discovered and published the original analysis of today's Avalon modular malware framework and the new CrownX ransomware (legal-lure phishing → ISO/LNK → MSBuild/.NET → ETW-blinding → nine-EDR evasion → credential theft → CrownX encryption), with an AI-assisted-development assessment, ahead of broad coverage. Primary threat research, not aggregation; no blackpointcyber.com domain in the roster.
- Reviewed ~4 sources behind today's stories (Sysdig TRT, Blackpoint Cyber, Palo Alto Unit 42, PTC Trust Center). 2 added (under the 3/day cap); Unit 42 is already represented in the roster (paloaltonetworks.com) so no new domain, and PTC's advisory center is a vendor product-security page rather than an independent research source. Version bumped 11 → 12.

## 2026-07-05
- +ADDED Sekoia TDR (threatintel/strong) — its Threat Detection & Research team ran the original investigation (with YesWeHack) behind today's ChocoPoC story: seven trojanized CVE-PoC GitHub repos, a compiled/obfuscated PyPI dropper, and a Mapbox DNS-over-HTTPS dead-drop C2 with domain fronting. Long-running French threat-intel firm with consistent primary research (Aurora Stealer, GootLoader, ClickFix tracking). Primary original research, not aggregation; no sekoia.io domain in the roster.
- +ADDED Armadin (aisecurity/aifocus) — Nick McClendon's original research behind today's AI story detailed a full sandbox escape reaching root inside Claude Cowork's Hyper-V VM (USERENV.dll sideload into signed claude.exe → CoworkVMService RPC resume-flag abuse → allowlist wildcard bypass), responsibly disclosed to Anthropic (who disputes it as a vuln). AI-native offensive-security firm led by ex-Mandiant CEO Kevin Mandia and Mandiant founders. Primary offensive AI research; no armadin.com domain in the roster.
- ~CANDIDATE YesWeHack — co-authored the original ChocoPoC research with Sekoia TDR; promising original vuln-intel but primarily a bug-bounty-platform news blog. Parked to watch for sustained independent original research beyond co-published work.
- Reviewed ~4 sources behind today's stories (Sekoia TDR, Armadin, YesWeHack, Check Point Research). 2 added (under the 3/day cap); YesWeHack parked as a candidate (co-published, platform-blog cadence), and Check Point Research (behind today's browser-only-ransomware item) is credible primary research but effectively adjacent to established vendor-research roster coverage — held to stay under cap and avoid roster bloat, revisit if it recurs. Version bumped 13 → 14. (Note: the 2026-07-05 first pass had already added runZero Research and Ransom-ISAC behind the FatFs and Kairos stories; this pass adds Sekoia TDR and Armadin behind the refreshed lead stories.)

## 2026-07-07
- +ADDED Zscaler ThreatLabz (aisecurity/aifocus) — published the original indirect-prompt-injection research behind today's lead AI story: CSS-hidden and JSON-LD-buried web prompts that tricked 4 of 26 tested LLM agents (including Llama and Gemini variants) into autonomous cryptocurrency payments and DeBank-typosquat trust, tested with its own in-house multi-model agent harness against SEO-poisoned sites. Large, well-resourced threat-research org with a documented track record of zero-day discoveries and annual ransomware/AI-security reports. Primary original research, not aggregation; no zscaler.com domain in the roster.
- +ADDED Synacktiv (vulnfeeds/strong) — discovered and published the original unauthenticated-RCE research behind today's lead vuln story: an unpatched, un-CVE'd Argo CD repo-server flaw that can lead to full Kubernetes cluster takeover, disclosed to maintainers in January 2025 and published after 18 months without a fix. French offensive-security/pentest firm with 300+ public vulnerability disclosures (Livewire, BizTalk360, Snipe-IT, Citrix Provisioning Services) and Pwn2Own research history. Primary technical research, not aggregation; no synacktiv.com domain in the roster.
- Reviewed ~5 sources behind today's stories (Zscaler ThreatLabz, Synacktiv, Sysdig [already in roster], SOCRadar [already in roster], SecureWorld). 2 added (under the 3/day cap); SecureWorld's Momentum Cyber M&A recap is a solid industry-news writeup but is itself summarizing Momentum Cyber's own report rather than original research, so it wasn't added — the Vendor & Tooling item cites it directly as the outlet that carried the report. Version bumped 14 → 15.

## 2026-07-08
- +ADDED Aikido Security (vulnfeeds/strong) — promoted from candidate (parked 2026-06-16). A month after its original decade-old phpBB auth-bypass discovery (CVE-2026-48611), published a full technical write-up plus a second related CVE (CVE-2026-48612) on July 3, honoring phpBB's requested 4-week embargo — sustained cadence and disclosure discipline resolves the earlier "watch for independence" concern. Primary vuln research, not aggregation.
- Reviewed ~5 sources behind today's stories (Krebs on Security's NetNut/Popa reporting [already in roster], Google Threat Intelligence Group [already represented via Google/Mandiant TI], theopscon.com's HSIN follow-up, Lupovis's Citrix NetScaler exploitation data, Aikido Security). 1 added (Aikido, promoted from candidate); theopscon.com and Lupovis are credible but this is their first appearance with no sustained track record yet — parked informally, watch for recurrence before adding as candidates. No new candidates parked today. Version bumped 15 → 16.

## 2026-07-09
- +ADDED Proofpoint (threatintel/strong) — its Threat Research team has tracked UNK_MassTraction, a suspected China-aligned cluster exploiting Roundcube n-day flaws (CVE-2024-42009, CVE-2025-49113) against US/Canadian university physics and national-security researchers, since May 2026; original campaign research (IceCube stealer, VShell backdoor) behind today's lead breach story, ahead of broad coverage. Long-established threat-intel vendor with a deep original-research track record; no proofpoint.com domain in the roster.
- +ADDED Varonis Threat Labs (aisecurity/aifocus) — published the original "Rogue Agent" research disclosing a shared-execution-environment flaw in Google Dialogflow CX (reported Nov 2025, fixed Jun 2026) that could let one edit permission compromise every AI chatbot agent in a GCP project, behind today's AI story. Consistent original AI-security disclosure cadence (SearchLeak in Microsoft 365 Copilot, Reprompt in Copilot Personal, Cookie Bite Azure MFA bypass). Primary hands-on research, not aggregation; no varonis.com domain in the roster.
- Reviewed ~6 sources behind today's stories (Proofpoint, Varonis Threat Labs, Cisco Talos [already in roster], Sysdig [already in roster], GalaxyWarden ransomware-leak tracker, Businesswire/Forescout NATO press release). 2 added (under the 3/day cap); GalaxyWarden is a useful leak-site aggregator but not original research, and the Forescout/NATO item is a vendor press release rather than independent reporting — neither meets the originality bar, so both were cited directly in the briefing without adding as sources. No new candidates parked today. Version bumped 16 → 17.
