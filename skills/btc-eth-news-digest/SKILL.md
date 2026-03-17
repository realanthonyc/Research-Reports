---
name: btc-eth-news-digest
description: Create detailed, trader-optimized, source-cited digests of the latest Bitcoin (BTC) and Ethereum (ETH) news, including market-moving developments, regulatory updates, protocol/ecosystem changes, ETF/flow items, and short-term macro catalysts. Include explicit analysis of how near-term macro events may affect BTC/ETH prices and provide a bilingual output (English first, then Traditional Chinese). Use when a user asks for a BTC/ETH news roundup, trading briefing, market-moving headline summary, daily/weekly crypto desk note, or latest developments with links, timing, trade relevance, and macro impact.
---

# BTC ETH News Digest

## Overview

Produce a high-signal BTC/ETH briefing for traders with source links, exact dates, market reaction context, short-term macro impact analysis, and actionable framing. Prioritize factual reporting, de-duplicate repeated headlines, and clearly separate confirmed facts from trading interpretation. Keep the report strictly BTC/ETH-focused: only include BTC/ETH-native events or macro events with explicit, sourced BTC/ETH transmission evidence. Save the final output as a Markdown report file under the repo-root `reports/crypto/` folder on every run.

## Workflow

### 1. Confirm scope and defaults

Use the user's requested timeframe and format when provided.

Default to:
- Timeframe: last 24 hours
- Audience: active trader / crypto desk
- Output: detailed trader briefing with citations, reaction framework, bilingual delivery (English + Traditional Chinese), and saved Markdown file
- Mode: full report (or delta update mode when user asks for "update only")

If the user says "latest" or "today," browse and include exact dates in the digest.

### 2. Gather market context first

Use `web.finance` for BTC and ETH spot prices to anchor the digest (price, move, and timing context). Treat price action as context, not the news itself.

Also gather recent BTC/ETH price action context from reliable market coverage when available:
- Session highs/lows and timing
- Immediate reaction after major headlines
- BTC/ETH-linked macro context (DXY, yields, risk sentiment) only when directly relevant to BTC/ETH movement

Collect short-term macro context that can move BTC/ETH over the next hours to few sessions:
- US rates and front-end yield moves (2Y/10Y, real yields if available)
- DXY / USD strength
- Major scheduled data (CPI, PPI, NFP, PMI, retail sales, jobless claims)
- Central bank communication (Fed speakers, FOMC minutes, policy decisions)
- Geopolitical or policy shocks with immediate risk-on/risk-off impact

For each macro item used, identify the transmission path to BTC/ETH (liquidity, risk sentiment, USD strength, rates sensitivity, ETF demand tone, leverage unwind risk). Exclude macro headlines with no clear BTC/ETH link.

If derivatives metrics are mentioned (funding, open interest, liquidations, options skew), cite the source and timestamp.

### 3. Collect news with browsing

Use `web.search_query` with recency filters for separate BTC and ETH searches, then open the most relevant results and cite them.

Cover these categories:
- Market structure: ETF flows, exchange/platform events, liquidity, major listings/delistings
- Policy/regulation: SEC/CFTC/DoJ/OFAC, legislation, court rulings, international regulators
- Protocol/ecosystem: upgrades, client releases, incidents, outages, major bugs, governance
- Adoption/corporate: BTC/ETH treasury activity, BTC/ETH payments, BTC/ETH enterprise integrations, BTC/ETH custody
- Macro crossover: rates, risk sentiment, USD/liquidity news only when materially affecting BTC/ETH and evidenced in BTC/ETH reaction or flows

Prefer primary sources when available (official announcements, regulator releases, project blogs, exchange notices) and use reputable reporting for context.

For macro items, prioritize primary/official sources (e.g., BLS, BEA, Federal Reserve, Treasury) and high-quality financial reporting for market reaction context.

### 4. Filter and rank

Keep only items that are:
- New within the requested window
- Material to BTC and/or ETH
- Supported by a reliable source
- Directly relevant to BTC and/or ETH (no standalone sector themes unrelated to BTC/ETH)

Combine duplicate coverage into one item with the best source(s). Rank by likely market impact, not publication volume.

For trader ranking, score each candidate mentally on:
- Time sensitivity (tradable now vs. background)
- Surprise factor (consensus vs. unexpected)
- Persistence (one headline pop vs. multi-session narrative)
- Transmission path (spot flows, derivatives positioning, regulation, protocol risk)

Also score each retained item explicitly:
- Confidence score (0-100): source quality + cross-confirmation + timestamp recency
- Market impact score (1-5): surprise + persistence + tradability + transmission strength
- Add these scores to each Top Development item in the final report

### 5. Write the digest

Use the output structure in `references/output-template.md`.

For each item, include:
- Headline
- What happened (fact summary)
- Why it matters (trader relevance)
- Affected asset(s): BTC, ETH, or both
- Confidence: confirmed / developing / speculative
- Impact horizon: immediate / 1-3 days / swing / structural
- Market reaction observed (if known)
- Bull case / bear case interpretation (brief)
- Key levels or triggers to watch (only if sourced or clearly marked as analyst inference)
- Source link(s)
- Date/time (absolute date; include timezone if relevant)

Add a dedicated section for short-term macro impact analysis that covers:
- Macro issue/event
- Current market signal (what changed)
- BTC impact pathway (bullish/bearish/neutral and why)
- ETH impact pathway (bullish/bearish/neutral and why)
- Time horizon (intraday / next 24h / 1-3 sessions)
- What would invalidate the macro read

### 6. Add caveats and follow-ups

Call out unresolved facts, missing official confirmation, or contradictory reporting. If coverage is thin, say so explicitly instead of padding with low-signal items.
Do not include AI, EV, or general equity-sector stories unless there is explicit, sourced BTC/ETH impact evidence.

If no meaningful catalyst exists in-window, explicitly state:
- "No clear short-term macro driver identified in the requested window."
- "Coverage thin for new BTC/ETH-specific headlines in the requested window."

Do not force directional bias in this case.

### 7. Close with a trader watchlist

End with a forward-looking section that helps a trader monitor risk over the next session(s):
- Upcoming catalysts (scheduled releases, decisions, unlocks, upgrade milestones)
- Invalidations / what would change the bias
- "Need confirmation" items to re-check

### 8. Translate to Traditional Chinese after the English report

Always output:
1. Full English version first
2. Full Traditional Chinese translation second

Translation requirements:
- Preserve structure, ordering, timestamps, and source links
- Translate prose and labels into Traditional Chinese (繁體中文)
- Keep tickers, metric names, and key financial acronyms in original form where clarity matters (e.g., BTC, ETH, ETF, CPI, FOMC, DXY)
- Preserve "confirmed / developing / speculative" semantics accurately
- Preserve any explicit "inference" labels

### 9. Save the output as a Markdown file in `/reports/crypto`

Always save the final report as a Markdown file at the repo root:
- Folder: `reports/crypto/` (create it if it does not exist)
- Format: Markdown (`.md`)
- Filename: `<report-name>-<YYYY-MM-DD>-<NN>.md`

Filename rules:
- Use a short descriptive report name (default: `btc-eth-news-digest`)
- Lowercase
- Hyphen-separated (sanitize spaces/special characters to `-`)
- Include the report date in absolute format as `YYYY-MM-DD`
- Always append a zero-padded daily sequence suffix as `NN`
- Start the first report for a given report name and date at `00`
- If multiple reports are generated for the same report name on the same date, increment the suffix to `01`, `02`, `03`, and so on
- When selecting the next filename, scan existing files for the same `<report-name>` and `<YYYY-MM-DD>` prefix and choose the next available zero-padded suffix

Examples:
- `reports/crypto/btc-eth-news-digest-2026-02-23-00.md`
- `reports/crypto/btc-eth-news-digest-2026-02-23-01.md`
- `reports/crypto/btc-eth-news-digest-2026-02-23-02.md`

### 10. Enforce data integrity gates before final output

Before finalizing, verify:
- Freshness SLA: at least 70% of cited items are published within the requested window; otherwise mark the report `coverage-thin`.
- Timestamp hygiene: all prices/flows/metrics include explicit "as-of" time and timezone.
- Source backfill: each material secondary-media claim includes a primary source link unless explicitly unavailable.
- Duplicate suppression: assign event key `asset + event-type + date` and remove duplicate headlines.
- Translation QA: English and Traditional Chinese sections have identical facts, numbers, signs, links, and caveats.
- Scope gate: every included item must pass `BTC-only`, `ETH-only`, `Both`, or `BTC/ETH-linked macro` classification.

### 11. Complete with git commit and push

After writing the final report file:
- Stage only the report file(s) created or updated by this run.
- Create a non-interactive git commit automatically.
- Push automatically to the default remote/branch for the current repo.
- Do not ask the user again for commit/push confirmation if the user has already granted standing permission.
- If commit or push fails, report the failure reason and current git status briefly.
- Use a clear commit message that includes the report name and date, for example: `add btc-eth-news-digest 2026-03-17-00`.

## Quality Rules

- Cite every material claim with links.
- Do not present rumors as confirmed news.
- Do not infer causation from price moves without evidence.
- Prefer exact numbers and dates over vague phrases.
- Distinguish BTC-specific, ETH-specific, both, and BTC/ETH-linked macro items.
- Mark analysis as inference when it goes beyond sourced facts.
- Separate "observed reaction" from "proposed trade framing."
- Avoid fake precision on levels, flows, or positioning data; cite or omit.
- In macro analysis, distinguish observed correlations from claimed causation.
- If macro relevance is uncertain, state uncertainty explicitly instead of forcing a directional call.
- Exclude non-BTC/ETH thematic news unless direct BTC/ETH impact is demonstrated with sources.
- Ensure the Traditional Chinese version matches the English version in facts and caveats.
- Ensure the saved Markdown file contains both English and Traditional Chinese sections.
- Do not return only inline text when the task is executed; write the report file under `reports/crypto/` first, then provide/quote the path.
- Use a short risk disclosure block: this is market analysis, not investment advice.
- When reporting "observed reaction," include the reaction timestamp.

## References

- Source selection and search heuristics: `references/source-priority.md`
- Digest format and output template: `references/output-template.md`
- Translation conventions (Traditional Chinese): `references/translation-zh-tw.md`
