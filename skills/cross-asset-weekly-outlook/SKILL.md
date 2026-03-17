---
name: cross-asset-weekly-outlook
description: Produce a deeply reasoned, source-backed cross-asset market outlook covering the broad market, selected focus stocks, Bitcoin, and gold, with the analysis horizon changing by weekday. Use when the user wants a Monday-to-Sunday market roadmap, a weekly trading game plan, a weekend Bitcoin setup, or an integrated equities-plus-BTC-plus-gold view grounded in current data and independent judgment.
---

# Cross-Asset Weekly Outlook

Produce a concise but deep market note that acts like a discretionary macro-plus-tactical strategist, not a headline summarizer.

Always investigate current facts first, then build explicit causal reasoning, scenario paths, and a hard conclusion with uncertainty clearly stated.

## Core Workflow

1. Lock the analysis date and weekday
- State the analysis date explicitly.
- Convert relative references such as `today`, `this week`, `next week`, or `weekend` into absolute dates.
- Determine the weekday and follow the correct scope ladder in `references/output-structure.md`.

2. Gather current market evidence first
- Always verify unstable facts with fresh web research before forming a view.
- Cover, at minimum:
  - broad U.S. market action: `S&P 500`, `Nasdaq`, `Dow`, `Russell 2000`, `VIX`
  - rates and dollar: `2Y`, `10Y`, curve tone, `DXY`
  - focus stocks explicitly named by the user; if none are named, select the most relevant market leaders or current tape drivers and say why
  - `BTC`
  - gold
- For each unstable fact, prefer same-day or latest-available sourcing and time-stamp the datapoint when useful.

3. Rank the drivers before discussing prices
- Identify the current dominant forces in order:
  - macro data and central-bank repricing
  - rates / dollar / liquidity shifts
  - major earnings, guidance, or company-specific shocks
  - geopolitical or policy developments
  - positioning, sentiment, and squeeze / unwind dynamics
- Distinguish:
  - `fact`: verified market move or event
  - `inference`: what the market appears to be pricing
  - `judgment`: your own conclusion about what matters most next

4. Explain the transmission chain
- Do not stop at `market up because sentiment improved`.
- Show the actual path, for example:
  - `strong data -> higher yields -> stronger dollar -> pressure on duration/growth -> mixed index breadth`
  - `weaker yields + softer dollar -> support for gold and BTC -> relief in high-beta equities`
  - `index resilience despite bad news -> positioning squeeze or liquidity tailwind may be dominating fundamentals`
- When assets diverge from their usual relationships, explain what is overpowering the textbook linkage.

5. Adapt the horizon by weekday
- Monday: analyze `Monday through Friday`.
- Tuesday: analyze `Tuesday through Friday`.
- Wednesday: analyze `Wednesday through Friday`.
- Thursday: analyze `Thursday through Friday`, `BTC weekend`, and `next week`.
- Friday: analyze `Friday`, `BTC weekend`, and `next week`.
- Saturday / Sunday: analyze `BTC weekend`, `next week`, and especially `Monday`.
- Do not waste space on horizons outside the weekday scope unless the user explicitly requests them.

6. Build scenarios, not just a base case
- Provide:
  - `Base case`
  - `Bull case`
  - `Bear case`
- For each scenario, state:
  - trigger
  - expected path across broad market / focus stocks / BTC / gold
  - what would invalidate it

7. End with a clear trading-intelligence conclusion
- Summarize the dominant regime in plain language.
- State which asset class currently has the cleanest setup and why.
- State where conviction is low because the evidence is mixed.

## Research Standards

- Always browse for the latest information. This skill is inherently time-sensitive.
- Prefer primary or high-authority sources first: official economic releases, central banks, Treasury/Fed communications, company filings or IR releases, major exchanges, ETF sponsors, and high-quality financial media for context.
- If the user names specific focus stocks, research those first; otherwise infer the relevant leaders from the current tape and explain the choice.
- Treat `BTC` and gold as macro assets, not isolated tickers. Interpret them through real yields, dollar direction, liquidity, positioning, ETF flow or institutional demand when relevant.
- Separate what already happened from what the market is waiting for next.
- If the evidence is conflicting, say so directly and lower confidence instead of forcing a false narrative.

## Focus-Stock Rules

- If the user provides a list of focus stocks, analyze those exact names.
- If not, choose a small set of current drivers, usually 3 to 6 names.
- Prefer names that materially influence index tone, sector leadership, AI / semiconductor sentiment, consumer risk appetite, or macro sensitivity.
- For each stock, answer:
  - what happened
  - why it matters beyond the single name
  - whether it confirms or contradicts the broader market regime

## BTC And Gold Rules

- For `BTC`, assess:
  - trend and momentum
  - ETF flows / institutional demand when relevant
  - correlation or divergence versus equities and dollar / yields
  - weekend liquidity and gap-risk dynamics when the analysis includes the weekend
- For gold, assess:
  - real yields
  - dollar direction
  - safe-haven and reserve-diversification demand
  - whether the move is inflation-led, growth-scare-led, or policy/liquidity-led

## Output Rules

- Follow the structure in [references/output-structure.md](references/output-structure.md).
- Write in Traditional Chinese unless the user explicitly requests another language.
- Use compact sections and high-signal bullets, but keep causal reasoning explicit.
- Include source links for major factual claims.
- Include concrete dates rather than vague time references.
- If the user wants a chat answer only, keep the same structure without writing files.
- Default to file output.
- Save reports in `/reports/outlooks`.
- Use this filename convention: `Cross-Asset-Weekly-Outlook-{YYYY-MM-DD}-{NN}.md`.
- Start the first report of the day at `-00`.
- If multiple reports are generated on the same date, increment sequentially to `-01`, `-02`, `-03`, and so on.
- Determine the next available `{NN}` by checking existing files in `/reports/outlooks` for the same date before writing the new report.

## 完成後處理

- 完成報告與相關輸出後，自動以非互動方式建立 git commit 並 push 到預設遠端；除非使用者明確要求不要 commit 或不要 push。
- commit / push 前僅納入本次任務直接產生或修改的相關檔案，避免混入無關變更。
- 若使用者已明確授予 standing permission，執行 commit / push 時不需再次詢問。
- commit message 應清楚描述報告日期與序號，例如：`add cross-asset weekly outlook 2026-03-17-00`。
- push 預設使用目前分支與其對應遠端；若 push 失敗，需回報失敗原因與當前 git 狀態。

## Safeguards

- Never present speculation as fact.
- Never use stale memory for current prices, catalysts, or schedules.
- Acknowledge uncertainty and mixed evidence.
- Do not give personal financial advice or guarantee outcomes.
