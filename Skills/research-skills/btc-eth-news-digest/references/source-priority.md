# Source Priority

## Priority Order

Use the highest-quality source available for each item.

1. Primary sources
- Regulators/courts/government releases
- Official project blogs / foundation posts
- Client team release notes
- Exchange/platform status pages and announcements
- Public company filings / investor relations releases
- Official macro/economic sources (BLS, BEA, Federal Reserve, U.S. Treasury, ECB, BoE, etc.)

2. High-quality reporting (for synthesis/context)
- Established financial press
- Established crypto industry reporters with named sources and direct quotes

3. Aggregators / social posts
- Use only as discovery signals, then trace back to a primary source

## Search Heuristics

Run separate searches for BTC and ETH to avoid mixed, low-signal results.

Useful query patterns:
- `"Bitcoin OR BTC" latest news ETF regulation upgrade`
- `"Ethereum OR ETH" latest news upgrade validator SEC ETF`
- `site:sec.gov bitcoin ethereum` (regulatory filings/releases)
- `site:blog.ethereum.org OR site:ethereum.org ethereum` (official ecosystem posts)
- `site:bitcoin.org OR site:bitcoincore.org bitcoin core release`
- `site:bls.gov CPI PPI release`
- `site:federalreserve.gov FOMC minutes statement speech`
- `US Treasury auction results yields` (or equivalent official source query)

Use recency filters in `web.search_query` and verify timestamps on the opened pages.

For trader reports, run at least one macro-focused search and one market-reaction search when macro is likely relevant.

## Freshness and Coverage SLA

- Target: at least 70% of cited items should be published within the requested window.
- If the SLA is not met, mark the report as `coverage-thin` and explain which categories were sparse.
- Prefer fewer high-quality in-window items over padding with stale low-signal headlines.

## Short-Term Macro Checklist (Trader Reports)

Check these before finalizing the report:
- Was there a major economic release in the report window?
- Did yields or DXY move meaningfully after a release/headline?
- Did BTC/ETH react in the same window?
- Is the observed move likely headline-driven, macro-driven, or mixed?
- Is the effect likely intraday only or multi-session?

If no meaningful macro catalyst is present, say "No clear short-term macro driver identified in the requested window" rather than forcing a macro narrative.

## Data Consistency Gate

Before final output:
- Ensure each key metric (price, ETF flow, funding, OI, liquidations, yields, DXY) has an explicit `as-of` timestamp and timezone.
- Avoid mixing stale and fresh datapoints without stating the timing mismatch.
- Do not compare metrics from different windows as if they are synchronous.

## Primary-Source Backfill Rule

- For material claims sourced from secondary media, attach the primary source link when available.
- If the primary source cannot be found, label explicitly: `primary source unavailable at time of writing`.

## Deduping Guidance

- Merge multiple articles covering the same event.
- Keep the strongest source as the main citation.
- Add one secondary source only if it materially improves context.
- Assign an event key: `asset + event-type + date`.
- Remove duplicate headlines that resolve to the same event key.

## Materiality Heuristic

Prefer items that can change:
- Market access (ETF, exchange, custody)
- Legal/regulatory risk
- Network security/reliability
- Token supply/demand expectations
- Institutional adoption or capital flows

## Source Budget (Efficiency)

- Keep headline citations concise: usually 1 primary source + up to 1 high-quality contextual source.
- Avoid over-citing multiple near-identical articles for the same event.
