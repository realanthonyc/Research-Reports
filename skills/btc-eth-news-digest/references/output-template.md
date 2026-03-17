# Output Template

## Default Structure (Trader-Optimized, Bilingual)

Use this structure unless the user requests a different format.

Always produce:
1. English version
2. Traditional Chinese (繁體中文) version
3. A saved Markdown file in `reports/` at the repo root

## File Output Requirement (required)

- Save every report as Markdown: `reports/<report-name>-<YYYY-MM-DD>.md`
- Create `reports/` if missing
- Use a sanitized lowercase hyphenated report name
- If filename exists, append `-2`, `-3`, etc.
- Include both the English and Traditional Chinese sections in the same file

### BTC & ETH News Digest (time window)
- Generated at: `<absolute date/time + timezone>`
- Scope: `BTC`, `ETH`, and cross-market items
- Audience: `Active trader / crypto desk`
- Mode: `Full report | Delta update`
- Data quality: `Pass | coverage-thin`
- Executive setup (3-6 bullets):
  - `<highest-impact takeaway>`
  - `<what changed vs prior session>`
  - `<what matters next>`
- Market context:
  - BTC: `<spot price, % change, session range, notable reaction timing>`
  - ETH: `<spot price, % change, session range, notable reaction timing>`
  - Cross-market: `<DXY / yields / equities / ETF flows / risk tone if relevant>`
  - Macro setup (short-term): `<which macro issues matter now and why>`

### Top Developments

1. `<headline>`
- Asset(s): `BTC | ETH | Both`
- Confidence: `Confirmed | Developing | Speculative`
- Confidence score: `<0-100>`
- Market impact score: `<1-5>`
- Impact horizon: `Immediate | 1-3 days | Swing | Structural`
- Event key: `<asset + event-type + date>`
- What happened: `<fact summary with exact figures/dates when available>`
- Why it matters (trader): `<positioning/liquidity/flow/regulatory/protocol impact>`
- Market reaction observed: `<price/vol/liquidation/funding reaction if known>`
- Trade framing (inference): `<bull case / bear case in 1-3 bullets total>`
- Key triggers / levels to monitor: `<sourced levels or clearly-marked analyst inference>`
- Sources: `<markdown links>`
- Timing: `<absolute date/time>`

2. `<headline>`
- Asset(s): `...`
- Confidence: `...`
- Confidence score: `...`
- Market impact score: `...`
- Impact horizon: `...`
- Event key: `...`
- What happened: `...`
- Why it matters (trader): `...`
- Market reaction observed: `...`
- Trade framing (inference): `...`
- Key triggers / levels to monitor: `...`
- Sources: `...`
- Timing: `...`

### Short-Term Macro Impact Analysis (required)

1. `<macro issue / event>`
- Type: `Scheduled data | Central bank | Rates move | USD move | Geopolitical | Policy`
- What changed: `<actual print / speaker tone / yields / DXY / equities move>`
- BTC impact pathway (analysis / inference): `<liquidity, risk sentiment, ETF flow sensitivity, leverage>`
- ETH impact pathway (analysis / inference): `<beta/risk sensitivity, ecosystem-specific exposure if any>`
- Time horizon: `Intraday | Next 24h | 1-3 sessions`
- Bias: `Bullish | Bearish | Mixed | Neutral`
- Invalidation / confirmation signals: `<what to monitor next>`
- Sources: `<markdown links>`
- Timing: `<absolute date/time>`

2. `<macro issue / event>`
- Type: `...`
- What changed: `...`
- BTC impact pathway (analysis / inference): `...`
- ETH impact pathway (analysis / inference): `...`
- Time horizon: `...`
- Bias: `...`
- Invalidation / confirmation signals: `...`
- Sources: `...`
- Timing: `...`

### Watchlist (optional)
- `<emerging item to monitor and what confirms/invalidates it>`

### Catalyst Calendar (recommended)
- `<date/time>` — `<event>` — `Why it matters for BTC/ETH`

### Positioning / Flow Notes (optional, only if sourced)
- `<ETF flows / funding / OI / liquidations / options skew item>` — `<interpretation>`

### Data Integrity Checks (required)
- Freshness SLA: `<% of cited items within requested window>`
- Timestamp hygiene: `<all key metrics include as-of time + timezone>`
- Primary-source backfill: `<pass/fail + exceptions>`
- Duplicate suppression: `<event keys used and duplicates removed>`

### Notable Noise / Unconfirmed (optional)
- `<rumor or low-confidence claim>` — explain why it is not included in the main list

### Desk Summary (recommended)
- Base case (inference): `<1-2 lines>`
- Risk to base case: `<1-2 lines>`
- What to re-check next update: `<specific datapoints / sources>`

### Risk Disclosure (required)
- `This report is market analysis for informational purposes and is not investment advice.`

### Traditional Chinese Translation (繁體中文)
- Repeat the full report in Traditional Chinese with identical structure and facts.
- Preserve source links and absolute timestamps.
- Keep key acronyms/tickers in original form where helpful (BTC, ETH, ETF, CPI, FOMC, DXY).

## Style Rules

- Be detailed but scan-friendly.
- Put the takeaway before background detail.
- Use absolute dates (e.g., `February 22, 2026`) when the user says "today/latest."
- Keep each main item self-contained.
- Label sourced facts vs inference explicitly.
- Include macro analysis even on slow crypto-news days if macro is the main driver.
- The final deliverable is the saved Markdown report file; provide the file path in the response.
