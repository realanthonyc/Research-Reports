---
name: global-macro-intelligence
description: Produce institutional-style macroeconomic intelligence reports that explain the current US-led global macro regime, recent catalysts, and cross-asset implications across equities, rates, FX, commodities, crypto, credit, liquidity, and positioning, and save them as Markdown deliverables. Use when the user asks for a macro outlook, global market strategy note, cross-asset regime analysis, Fed/liquidity/yields/dollar interpretation, risk-on versus risk-off assessment, or a professional macro research report based on the latest data and news.
---

# Global Macro Intelligence

Produce a current macro research note with explicit cause-and-effect reasoning, recent verified developments, and clear market implications. Default to a US-first framework, but always integrate China, Japan, Europe, commodities, and geopolitics when they matter for global flows or risk pricing.

## Workflow

1. Define the report date and scope
- State the analysis date explicitly.
- Convert relative time references such as "today" or "this week" into absolute dates.
- If the user does not narrow the scope, produce a full cross-asset macro report.

2. Gather current evidence first
- Actively search for the latest macro data, central-bank signals, market moves, and geopolitical developments before drawing conclusions.
- Prefer primary and high-authority sources: official economic releases, central banks, Treasury/Fed/ECB/BOJ/PBOC communications, exchange or government data, then high-quality financial media for context.
- Time-stamp unstable facts such as yields, DXY, futures pricing, ETF flows, and policy probabilities.
- Build an `important happenings radar` every run:
- `just happened`: what was released or said in the last 0-24 hours
- `recent`: what still matters from the last 1-7 days
- `upcoming`: what the market is waiting for in the next few days
- Include analyst / strategist repricing or institutional debate only when it helps explain market expectation, reaction, or positioning.

3. Diagnose the macro regime
- Explicitly classify the environment across these axes:
  - `risk-on` vs `risk-off`
  - `inflationary` vs `disinflationary`
  - `growth-accelerating` vs `growth-slowing`
  - `liquidity-expanding` vs `liquidity-contracting`
- Support each regime label with evidence rather than adjectives.

4. Explain the transmission chain
- Use stepwise macro logic instead of shallow summaries.
- Make the links explicit, for example:
  - `inflation -> Fed pricing -> front-end yields -> DXY -> liquidity -> equity multiples`
  - `growth scare -> long-end yields -> curve shape -> credit spreads -> cyclicals/defensives`
  - `China stimulus or weakness -> commodities -> global manufacturing -> EM FX -> risk appetite`
- Distinguish facts, inference, and judgment.

5. Connect macro to markets
- Cover, at minimum:
  - US equities: `S&P 500`, `Nasdaq`, and growth vs value
  - US rates: `2Y`, `10Y`, curve shape, and real yields
  - Fed expectations and liquidity conditions
  - `DXY` and major FX
  - Gold, silver, copper, oil
  - Bitcoin and crypto beta
  - Credit conditions, volatility, and capital flows
- For each asset bucket, explain why it is moving, not just how much it moved.
- Treat liquidity as a first-order driver, not a side note. When possible, interpret reserves, reverse repo usage, Treasury General Account shifts, Fed balance-sheet change, bank-funding conditions, credit creation, and financial-conditions indexes together rather than discussing only QE/QT headlines.
- Separate `market liquidity`, `policy liquidity`, and `funding stress`. Explain whether assets are reacting to easier financial conditions, balance-sheet expansion, reduced collateral stress, or merely lower rate expectations.
- Strengthen gold analysis specifically. Do not stop at "safe haven" or "inflation hedge"; explain gold through the interaction of real yields, dollar direction, central-bank buying, geopolitical hedging demand, reserve diversification, and growth scare dynamics.
- When gold and real yields move in the same direction, explicitly explain the non-rate driver that is overpowering the usual relationship.

6. Build forward scenarios
- Identify the main regime-change risks over the next days to weeks.
- For each risk, describe the likely asset-market response path.
- Emphasize what would falsify the base case.

## Analysis Standards

- Write as a sell-side or hedge-fund macro desk note: clear, dense, and evidence-based.
- Focus primarily on the United States, then incorporate global influences that alter the US outlook or cross-asset pricing.
- Do not rely on stale memory for current facts; verify anything time-sensitive.
- Keep causal reasoning explicit and educational.
- Avoid unsupported certainty. If the evidence is mixed, say so and explain why.
- When data is missing or conflicting, note the gap and how it affects confidence.

## Output Rules

- Follow the structure in [references/report-outline.md](references/report-outline.md).
- Start with a two-part summary:
- `Detailed Summary`: slower and clearer reasoning, with explicit judgment, forecast, and explanation of harder concepts in simpler language.
- `Brief Summary`: fast-read version that states the bottom-line regime, market message, and key judgment directly.
- Use short paragraphs and selective bullets; do not turn the note into disconnected headline fragments.
- Include absolute dates for recent events and data prints.
- Include source links for material factual claims when the task expects a fully sourced note.
- If the user requests a shorter product, compress the depth but preserve the same causal structure.
- Default to file output, not chat-only output.
- Write the original English report to `reports/macro/macro-intelligence-report-{YYYY-MM-DD}-{NN}.md`.
- After the English report is complete, translate that English report into Traditional Chinese and write it to `reports/macro/macro-intelligence-report-{YYYY-MM-DD}-{NN}-zh-tw.md`.
- Use a zero-padded daily sequence for `{NN}`.
- For the first report generated on a given analysis date, use `00`.
- If multiple reports are generated for the same analysis date, increment the suffix to `01`, `02`, `03`, and so on for both the English and Traditional Chinese files.
- Keep the Chinese file as a faithful translation of the English report rather than a newly re-authored variant.
- When saving files, use the analysis date for `{YYYY-MM-DD}` unless the user explicitly requests a different report date.
- Determine the next available `{NN}` by checking existing files for that date before writing new ones, so the English and Traditional Chinese pair always share the same sequence number.
- In the final response, mention both file paths and summarize the macro regime briefly.
- After writing the English and Traditional Chinese files, automatically stage only the files created or updated by this run, create a non-interactive git commit, and push to the default remote/branch.
- If the user has already granted standing permission for commit/push, do not ask again before doing so.
- If commit or push fails, report the failure reason and current git status briefly.
- Use a clear commit message that includes the report date and sequence, for example: `add macro intelligence report 2026-03-17-00`.
- The summary sections must explicitly cover:
- what just happened
- what the market is now waiting for
- how current pricing reflects or misreads those developments
- your own forward judgment, not only balanced caveats

## Evidence Priorities

1. Official macro data and policy sources
- `BLS`, `BEA`, `Census`, `Treasury`, `Federal Reserve`, `ECB`, `BOJ`, `PBOC`, `Eurostat`, government ministries, official energy agencies.

2. Market-implied pricing and exchange-quality data
- Treasury yields, futures-implied policy expectations, major index and commodity pricing, FX benchmarks, ETF flow data, credit-spread proxies, volatility indices.

3. High-quality contextual reporting
- Use reputable financial media and research summaries to connect events, but do not let them substitute for primary facts.

## Global Coverage Rules

- Always assess:
  - China: growth, stimulus, property, credit, yuan, commodity demand.
  - Japan: BOJ policy, JGB yields, yen, repatriation/global liquidity implications.
  - Europe: growth, ECB stance, fiscal or energy shocks, euro impact.
  - Commodities: oil and industrial metals as macro signal transmitters.
  - Geopolitics: conflicts, sanctions, trade tensions, and shipping/supply disruptions.
- Include these regions only to the depth required by current market relevance, but never omit a major external driver if it is moving US markets.
- For liquidity interpretation, also check whether non-US policy or reserve behavior is influencing global dollar liquidity, Treasury demand, or official-sector gold accumulation.

## Positioning And Sentiment

- Incorporate positioning when it changes the market response function.
- Relevant inputs include `VIX`, options skew, CTA or trend-following dynamics if observable, ETF flows, speculative futures positioning, and credit-spread behavior.
- Explain whether positioning is reinforcing or dampening the macro impulse.

## Deliverable Checklist

- Regime identified and justified
- Recent developments tied to market impact
- US macro and Fed path explained
- Global spillovers covered
- Rates, liquidity, FX, commodities, crypto, and credit connected
- Forward risks and monitoring dashboard included
- Positioning discussed
- Causal chains made explicit
- English Markdown report saved in `reports/macro/`
- Traditional Chinese Markdown translation saved in `reports/macro/`
