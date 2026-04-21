---
name: daily-trading-insights
description: Produce a daily, source-backed U.S. trading intelligence brief that turns current news, catalysts, narratives, mega-cap stock developments, smart-money or flow hints, upcoming events, market expectations, and cross-asset signals into ranked trading insights. Use when the user asks for daily trading insights, today's market hot topics, U.S. stock or ETF hot picks, market sentiment/direction/pattern analysis, a premarket or intraday trading briefing, mega-cap watch points, or a near-term catalyst map for the next few U.S. trading sessions.
---

# Daily Trading Insights

Produce a tradeable market-intelligence brief, not a generic news roundup. Research the latest facts first, then convert them into ranked abstracts, U.S. stock/ETF hot picks, mega-cap watch points, market-regime judgment, and a final action map.

Default to two Markdown reports:
- English report first.
- Traditional Chinese report second, saved as a separate `-zh-tw` Markdown file and written as a faithful Traditional Chinese translation of the completed English report.

Keep tickers, company names, ETF names, macro acronyms, and source names in English where clarity is better. Translate surrounding prose, labels, and explanatory language into polished Traditional Chinese.

## Core Workflow

1. Lock the session date and horizon
- State the analysis date, user's timezone, and U.S. market date explicitly.
- Convert `today`, `tomorrow`, `this week`, and `next few days` into absolute dates.
- Default horizon:
  - `Today`: active U.S. trading session or next U.S. session if the market is closed.
  - `Upcoming few days`: next 1-3 U.S. trading sessions.
  - `Event horizon`: next scheduled macro, earnings, policy, product, or corporate catalyst that can move the asset.

2. Gather current evidence before forming views
- Always browse for the latest information. This skill is inherently time-sensitive.
- Build the evidence set from:
  - broad U.S. market: S&P 500, Nasdaq, Dow, Russell 2000, VIX, market breadth when available
  - rates and dollar: 2Y, 10Y, real-yield tone if relevant, DXY
  - macro calendar: inflation, labor, Fed, Treasury auctions, PMI/ISM, GDP, retail sales, jobless claims
  - earnings, guidance, analyst/institutional repricing, company announcements, filings, product launches
  - sector narratives: AI, semis, software, energy, financials, defense, biotech, crypto-linked equities, China ADRs, commodities, or whatever is driving the tape
  - smart-money and flow hints: ETF flows, options activity, 13F/filings, insider transactions, large-cap fund flows, positioning commentary
  - breaking news and important social media updates only when material and sourceable
  - upcoming catalysts over the next few days
- For the required mega-cap watch, search current news, filings, earnings/calendar items, analyst or institutional repricing, product/regulatory headlines, and relevant sector read-throughs for:
  - Google / Alphabet (`GOOGL`, `GOOG`)
  - Apple (`AAPL`)
  - Microsoft (`MSFT`)
  - Meta (`META`)
  - Nvidia (`NVDA`)
  - Amazon (`AMZN`)
  - Tesla (`TSLA`)
- Prefer primary sources for facts and high-quality financial media for market interpretation.
- Use finance/market data tools when available for live context, but do not treat price action alone as a catalyst.

3. Build a candidate pool, then filter
- Collect more candidates than needed before writing.
- De-duplicate repeated coverage into one event or theme.
- Reject low-signal items that have no plausible transmission path to U.S. equities, ETFs, volatility, rates, dollar, BTC/crypto-linked equities, commodities, or specific tradable names.
- Keep at least:
  - `20` Abstracts
  - `12` Hot Picks
- If the evidence is too thin for the minimum count, state `coverage thin` and include the best verified items instead of padding with weak claims.

4. Rank by trading usefulness
- Score mentally before ordering:
  - catalyst strength
  - surprise versus expectations
  - time sensitivity
  - breadth or sector impact
  - source quality
  - flow/positioning confirmation
  - technical or price-action confirmation
  - risk/reward and invalidation clarity
  - crowding or priced-in risk
- Rank items by decision usefulness, not headline popularity.

5. Separate fact, inference, and judgment
- Label confirmed facts, market interpretation, and your own trading judgment clearly.
- Do not overstate rumors, social-media claims, analyst opinions, or options flow.
- Treat unusual options flow and "smart money" as clues, not proof.
- Explicitly lower confidence when evidence conflicts.

## Abstract Rules

Each Abstract must include:
- `Title`
- `Signal`: Bullish / Major Bullish / Bearish / Major Bearish / Neutral
- `Signal Type`: Macro / Rates / Fed / Earnings / Guidance / AI / Tech / Crypto / Commodity / Geopolitics / Policy / Flow / Options / Social / M&A / Regulation / Sector Rotation / Other
- `Affected Assets`: tickers, ETFs, sectors, or asset classes
- `Time Horizon`: intraday / 1-3 sessions / 1-2 weeks / event-driven / structural
- `Confidence`: High / Medium / Low, with one short reason
- `Brief Summary`
- `Logics, Derivation, and Implications`
- `What To Watch / Invalidation`
- `Sources`

For `Logics, Derivation, and Implications`, show the transmission chain. Example:
`softer yields -> growth multiple relief -> semis and mega-cap tech bid -> QQQ leadership improves, unless DXY rises enough to offset the rates relief`.

## Hot Pick Rules

List at least 12 U.S.-listed stocks or ETFs that are hot, worth monitoring, or tactically relevant for today and the next few sessions.

Each Hot Pick must include:
- `Name / Ticker`
- `Direction`: Bullish / Bearish / Neutral
- `Strength`: Very Strong / Strong / Normal / Weak / Unknown
- `Setup Type`: Momentum / Reversal / Breakout / Breakdown / Event / Hedge / Watch Only
- `Catalyst`
- `Why`
- `When`: Today / upcoming few days / specific date or timing
- `What To Watch If Uncertain`
- `Invalidation / Risk`

Selection rules:
- Prefer names with a fresh catalyst, active narrative, flow confirmation, sector leadership/laggard role, or clear event timing.
- Include ETFs when they express the setup better than a single stock.
- Do not force every pick to be bullish. Include bearish or hedge candidates when the tape calls for them.
- Mark `Watch Only` when a name is interesting but the setup is not actionable.

## Mega-Cap Watch Rules

Always include a dedicated section covering today's `特別注意點` and `預計走勢` for these seven mega-cap stocks:
- Google / Alphabet (`GOOGL`, `GOOG`)
- Apple (`AAPL`)
- Microsoft (`MSFT`)
- Meta (`META`)
- Nvidia (`NVDA`)
- Amazon (`AMZN`)
- Tesla (`TSLA`)

For each company, include:
- `Special Attention Point / 特別注意點`: the most important current catalyst, risk, narrative, or event to monitor today.
- `Expected Move / 預計走勢`: Bullish / Bearish / Neutral / Mixed, with the expected intraday or 1-3 session path.
- `Evidence`: source-backed facts or latest news that supports the view.
- `Trading Read-Through`: likely impact on `QQQ`, `SPY`, relevant sector ETFs, suppliers, peers, or market breadth.
- `Invalidation`: what would make the expected move wrong.

Use current related news for each name even if the final read is `Neutral` or `Watch Only`. If no fresh company-specific catalyst is found, explicitly say `no fresh company-specific catalyst found` and base the read on sector, macro, positioning, or upcoming-event context.

## Market Regime Rules

Always include a section for today's market sentiment, direction, and pattern.

Classify:
- risk-on / risk-off / mixed / rotation-led / squeeze-led / defensive
- growth-led / value-led / cyclical-led / mega-cap-led / broadening / narrowing
- volatility expanding or compressing
- dollar and yields helping or hurting equities
- breadth healthy, narrow, or deteriorating
- likely session pattern: trend day / chop / gap-and-fade / squeeze / distribution / rotation / event-waiting

Explain the current regime through cross-asset evidence, not vibes. If signals conflict, say which signal currently dominates and what would flip the read.

## Output Rules

- Follow `references/output-template.md`.
- Complete the English Markdown report first.
- After the English report is done, create a separate Traditional Chinese Markdown report as a faithful translation of the English report.
- The Traditional Chinese file must use the same filename stem with `-zh-tw` appended before `.md`.
- The English and Traditional Chinese reports must preserve the same facts, figures, directional calls, timestamps, source links, caveats, formatting (including listing and paragraph formatting), section order, item order, and ranking order.
- `Faithful translation` means no added or removed facts, but it does not mean literal word-for-word translation. Rewrite into natural, professional Taiwan-style Traditional Chinese financial prose while preserving the English report's information content.
- Use source links for every material factual claim.
- Use absolute dates and timestamps where useful.
- Keep sections compact but do not remove the reasoning chain.
- Start each report with both:
  - English: `Detailed Summary` and `Brief Summary`
  - Traditional Chinese: `詳細總結` and `總結概要`
- End with `Final Action Map` covering:
  - best bullish setups
  - best bearish or hedge setups
  - watch-only names
  - key macro/company events today and next few sessions
  - biggest hidden risk
  - what would flip the market view

## Traditional Chinese Translation Quality Rules

The `-zh-tw` file must read like a professional Traditional Chinese market note, not a machine-translated English note.

Translate these elements into Traditional Chinese:
- Section headings, table headers, bullet labels, and field labels.
- Full narrative sentences, caveats, action maps, and reasoning chains.
- Market-structure phrases such as `event-waiting`, `risk-on`, `risk-off`, `sell-the-news`, `range-bound`, `watch-only`, `gap risk`, and `breadth`.
- Time and event phrases such as `before open`, `after close`, `premarket`, `upcoming few days`, and `next 1-3 sessions`.

Allowed to remain in English:
- Tickers, ETF names, company names, source names, proper product names, and macro acronyms when they are standard market usage: `QQQ`, `SPY`, `DXY`, `VIX`, `FCF`, `EPS`, `AWS`, `Azure`, `Copilot`, `Google Cloud`, `Strait of Hormuz`.
- Direction and signal values only if paired with Chinese on first use or in compact table cells, for example `看多 (Bullish)`, `中性 (Neutral)`, `事件驅動 (event-driven)`.
- Source link labels when they are official outlet names.

Use Taiwan-market phrasing:
- `盤前`, `盤後`, `收盤後`, `未來幾個交易日`, `事件驅動`, `觀望`, `偏多`, `偏空`, `中性`, `震盪`, `防禦`, `輪動`, `風險偏好`, `殖利率`, `美元指數`, `通膨風險溢價`, `估值壓力`, `上行空間`, `下行風險`.

Reasoning chains may keep the arrow format, but each node must be translated into Chinese except tickers and standard acronyms. Example:
`油價走高 -> 通膨風險溢價上升 -> 殖利率承壓 -> 高估值成長股受壓 -> QQQ 領漲力道轉弱`.

Before saving the `-zh-tw` file, run a manual translation QA pass:
- No untranslated English field labels such as `Signal`, `Brief Summary`, `What To Watch`, `Sources`, `Why`, or `When`.
- No long English fragments in prose unless they are tickers, names, acronyms, source names, or quoted terms that are clearer in English.
- Headings may keep company names and tickers in English, but report structure labels must be Chinese.
- The Chinese report must preserve all links and numbers exactly.
- The Chinese report must be readable as a standalone Traditional Chinese report.

## File Output

Default to saving the report as Markdown under the repo-root `Reports/outlooks/` folder unless the user asks for chat-only output.

Filename:
- English: `daily-trading-insights-{YYYY-MM-DD}-{NN}.md`
- Traditional Chinese: `daily-trading-insights-{YYYY-MM-DD}-{NN}-zh-tw.md`
- Start each date at `00`.
- If either file for the date exists, increment both reports to the next shared `NN` pair (`01`, `02`, and so on).

Add Obsidian-compatible YAML frontmatter before the first visible heading:

```yaml
---
title: <human-readable report title>
date: <YYYY-MM-DD analysis date>
report_type: daily-trading-insights
source_skill: daily-trading-insights
folder: Reports/outlooks
language: en
tags:
  - Reports
  - Reports/outlooks
  - Skills/research-skills/daily-trading-insights
  - asset-class/equities
  - cadence/daily
  - language/en
aliases:
  - <filename stem>
  - <short report title and date>
related:
  - "[[Research Flow]]"
  - "[[daily-trading-insights]]"
---
```

For the Traditional Chinese file, use the same frontmatter structure but set:
- `title`: translated report title
- `language: zh-TW`
- language tag: `language/zh-TW`
- aliases based on the `-zh-tw` filename stem

Do not automatically commit or push skill-generated reports unless the user explicitly asks for git actions or grants standing permission for this skill.

## Obsidian Rules

- Optimize every saved report as an Obsidian note.
- Use YAML properties at the top of each file only once, before the visible report heading.
- Use Obsidian wikilinks only for internal vault relationships such as `[[Research Flow]]` and `[[daily-trading-insights]]`.
- Use standard Markdown links for all external sources.
- Use clear headings so Obsidian outline navigation works:
  - English file: `# Daily Trading Insights - <YYYY-MM-DD>`
  - Traditional Chinese file: `# 每日交易洞察 - <YYYY-MM-DD>`
- Add tags only in frontmatter; avoid noisy inline tags inside the report body unless the user asks.
- Do not embed external sources or images by default.
- Preserve source URLs in both language files.

## Research Integrity Gates

Before finalizing, verify:
- At least 70% of cited abstracts are from today, the latest available trading session, or explicitly relevant upcoming events.
- Every material item has a source link.
- Each directional judgment has a time horizon.
- Rumors, social media, and unconfirmed flow items are labeled as Low confidence or developing.
- Abstracts are de-duplicated by event/theme.
- Hot Picks are U.S.-listed stocks or ETFs.
- Mega-Cap Watch includes Google/Alphabet, Apple, Microsoft, Meta, Nvidia, Amazon, and Tesla with `Special Attention Point / 特別注意點` and `Expected Move / 預計走勢`.
- The report includes both bullish and bearish risk framing.
- The final action map is consistent with the market-regime section.
- Translation QA confirms the English and Traditional Chinese files have identical facts, numbers, signs, links, caveats, section order, and ranking order.
- Traditional Chinese QA confirms the `-zh-tw` file uses natural Traditional Chinese prose and translated labels, with English retained only for tickers, company names, ETF names, source names, standard acronyms, or paired bilingual signal terms.

## References

- Read `references/source-priority.md` when choosing sources and confidence labels.
- Read `references/output-template.md` when writing the final report.
