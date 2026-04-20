---
name: company-valuation-analyst
description: Build a scenario-based intrinsic-value memo for any single public company across any industry or sector. Use when the user asks whether a stock is overvalued or undervalued, whether a rally is justified, whether trimming or holding is rational, what assumptions are already priced in, or how growth, margins, capital intensity, balance sheet risk, dilution, catalysts, and timing affect fair value. Best for company-specific valuation work where the goal is to translate business economics into a practical market judgment.
---

# Company Valuation Analyst

Build a disciplined valuation memo for a single company in any sector.
Prioritize explicit assumptions, scenario-based fair value, balance-sheet-aware downside, and market-implied expectations over vague opinions.

## Workflow

1. Define the economic object
- Confirm company, ticker, listing, currency, analysis date, and current price.
- Define the company's economic type, such as:
  - `compounder / mature cash flow`
  - `cyclical`
  - `asset-heavy`
  - `turnaround`
  - `single-asset or event-driven`
  - `platform or high-growth reinvestment`
- If the task requires a full institution-style research report with sector, news, peer, and scorecard coverage, prefer [`comprehensive-equity-research-analysis`](../comprehensive-equity-research-analysis/SKILL.md).

2. Separate facts from assumptions
- Label every important point as one of:
  - `Fact`: directly verified from filings, company materials, or reliable market data.
  - `Assumption`: model input chosen because the exact value is unknown.
  - `Inference`: conclusion drawn from facts and assumptions.
- Do not mix these categories in the same sentence when a clean split is possible.

3. Gather minimum valuation inputs
- Collect or estimate:
  - market cap
  - enterprise value if debt or excess cash matters
  - cash
  - debt
  - revenue, gross margin, operating margin, and free cash flow when relevant
  - capital intensity and reinvestment needs when relevant
  - basic and diluted share count if available
  - buybacks, dilution, convertibles, warrants, or financing overhang if relevant
  - key business segments or value drivers
  - next 1-3 critical catalysts with dates or windows

4. Build the valuation frame
- Use `bear / base / bull` scenarios.
- For each scenario, state:
  - revenue, volume, unit economics, or asset-value assumption
  - margin and cash-conversion assumption
  - growth duration or cycle position
  - capital intensity or reinvestment need
  - expected dilution or buyback effect if relevant
  - valuation method and multiple / discount logic
- Match the method to the business:
  - `DCF or FCF yield`: stable cash-generative businesses
  - `EV/EBITDA`, `P/E`, `EV/Sales`: comparables-driven businesses
  - `SOTP`: multi-segment or mixed-quality businesses
  - `asset value / NAV / liquidation floor`: asset-heavy or distressed situations
  - `probability-adjusted scenario value`: event-driven or binary-outcome situations
- If exact data is missing, use cautious ranges and say what would change the conclusion.

5. Stress-test the price
- Answer:
  - what does the market appear to be pricing in now
  - how much success is already embedded in the current valuation
  - whether the stock is below, near, or above reasonable base-case fair value
  - whether a sharp rally likely reflects fundamentals, sentiment, squeeze dynamics, multiple expansion, or temporary positioning

6. Translate valuation into a trading conclusion
- End with a practical conclusion about `trim / hold / wait / avoid chasing`.
- Explain what must happen for another major re-rating and what would invalidate the memo.

## Hard Rules

1. Do not call a stock cheap or expensive without a scenario table.
2. If the stock rose more than 50% in the last 20 trading days, explicitly assess:
- sentiment premium
- squeeze risk
- early pricing-in of success
- probability of opportunistic financing or insider / sponsor / shareholder supply
3. If runway is below 12-18 months or leverage is clearly stressed, include financing risk in the base case by default unless there is a clearly funded path through the next major catalyst.
4. Always discuss downside floor using net cash, asset value, normalized earnings power, or liquidation-like value where applicable.
5. State missing data clearly instead of pretending precision.
6. Use Traditional Chinese by default unless the user asks otherwise.

## Script Usage

- Use [`scripts/build_valuation_table.py`](scripts/build_valuation_table.py) when deterministic scenario math will improve reliability.
- Feed the script scenario inputs instead of doing fragile mental arithmetic for dilution-adjusted fair value.
- Read [`references/scenario-guidelines.md`](references/scenario-guidelines.md) when choosing valuation methods or setting scenario logic by company type.
- Read [`references/capital-structure-framework.md`](references/capital-structure-framework.md) when financing risk, dilution, debt, or liquidity is central to the thesis.
- Read [`references/output-template.md`](references/output-template.md) when preparing the final memo structure.
- Write the final report to `reports/research/company-valuation-analyst-{YYYY-MM-DD}-00.md`.
- If a version for the same date already exists, increment the suffix to `-01`, `-02`, and so on.
- After writing the report, stage the report file and push the commit to the current remote.

## Output

Use this section order unless the user asks for another format:

1. `Snapshot`
2. `Business model in plain language`
3. `What drives value`
4. `Balance sheet and dilution`
5. `Scenario valuation table`
6. `What the market is pricing in now`
7. `Verdict`
8. `Critical unknowns`
9. `What to watch next`

## Obsidian Knowledge Output

Make every saved report usable as an Obsidian knowledge-bank note. Before the first visible heading, add YAML frontmatter with these fields:

```yaml
---
title: <human-readable report title>
date: <YYYY-MM-DD analysis date>
report_type: company-valuation
source_skill: company-valuation-analyst
folder: reports/research
language: <en | zh-TW | bilingual>
tags:
  - reports
  - reports/research
  - skills/company-valuation-analyst
  - research-flow/study
  - investing/valuation

aliases:
  - <filename stem>
  - <short report title and date>
related:
  - "[[Research Flow]]"
  - "[[company-valuation-analyst]]"
---
```

Use Obsidian wikilinks only for internal vault relationships, and keep external citations as standard Markdown links. Preserve the report's existing section order and filename rules. Do not add prose that explains Obsidian usage inside the report body.

## Quality Bar

- Prefer simple, auditable math.
- Be analytical, not promotional.
- Make uncertainty explicit.
- Treat low-confidence news as supporting color, not core valuation evidence.
- Do not pretend a point estimate is more reliable than the inputs allow.
- Save the report as Markdown and write it in Traditional Chinese.
