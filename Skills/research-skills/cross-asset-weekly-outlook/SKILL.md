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
- Determine the weekday in both the user's timezone and `America/New_York`.
- In the output header, explicitly write the U.S. market weekday, for example:
  - `分析日期：2026-03-17`
  - `分析範圍：2026-03-17 至 2026-03-20（美東週一收盤資料；美東週二至週五展望）`
- Follow the correct scope ladder in `references/output-structure.md`, but anchor the horizon wording to the U.S. market calendar rather than only the local calendar.

2. Gather current market evidence first
- Always verify unstable facts with fresh web research before forming a view.
- Cover, at minimum:
  - broad U.S. market action: `S&P 500`, `Nasdaq`, `Dow`, `Russell 2000`, `VIX`
  - rates and dollar: `2Y`, `10Y`, curve tone, `DXY`
  - focus stocks explicitly named by the user; if none are named, select the most relevant market leaders or current tape drivers and say why
  - `BTC`
  - gold
- Also gather a ranked list of the most valuable current and near-term market news items that must later feed the `今日熱點新聞` section.
- Build an `important happenings radar` every run:
- `just happened`: what changed in the last 0-24 hours and is still driving the tape
- `recent`: what from the last few days still matters
- `upcoming`: what the market is now waiting for over the next several days
- Include analyst / institutional repricing or rating changes when they help explain expectations, sector leadership, or market reaction.
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
- Treat `DXY` as a required analytical pillar, not a side datapoint. Do not merely quote the level:
  - state the latest level or recent directional move
  - explain what is driving it: rate differentials, oil shock, safe-haven demand, growth divergence, or policy repricing
  - explain what the current DXY behavior implies for equities, BTC, and gold
  - state whether DXY is confirming or contradicting the broader regime
- Separate what already happened from what the market is waiting for next.
- If the evidence is conflicting, say so directly and lower confidence instead of forcing a false narrative.

## Focus-Stock Rules

- If the user provides a list of focus stocks, analyze those exact names.
- If the user provides fewer than 6 names, you may add more relevant names so that the section is not too thin, but keep the user-specified names first.
- If the user does not provide names, choose at least 6 current drivers.
- Prefer names that materially influence index tone, sector leadership, AI / semiconductor sentiment, consumer risk appetite, or macro sensitivity.
- For each stock, answer:
  - what happened
  - why it matters beyond the single name
  - whether it confirms or contradicts the broader market regime
- When no names are specified, prefer a diversified basket across at least 3 distinct market roles, for example:
  - index-heavy AI / semis
  - mega-cap platforms or software
  - macro-sensitive cyclicals / financials / consumer
  - crypto-linked or commodity-linked expressions when relevant

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
- Start the report with two summary layers:
- `詳細總結`：更完整地解釋最近/即將發生的重要動態、推導邏輯、你的理解與判斷。
- `總結概要`：快速、直接、可掃讀地講清楚結論、偏向、關鍵風險與最重要催化。
- Do not number the first-level output section titles. Use plain markdown headings such as `## 標題與日期`, `## 核心判斷`, `## 大市`, and so on.
- Whenever you make a directional or structural judgment, explicitly state the applicable time span, for example:
  - `對未來 1 到 3 個美股交易日的判斷`
  - `對本週剩餘交易日的判斷`
  - `對未來 1 到 4 週的中短線判斷`
- Do not write vague lines such as `可以反彈，但結構仍脆` without specifying whether that refers to the next session, the rest of the week, or a multi-week horizon.
- In the `大市` section, always include a distinct `DXY` bullet or paragraph and a final judgment block that specifies:
  - the time span of the judgment
  - directional bias
  - breadth / leadership condition
  - fragility or invalidation trigger
- In section `分日 / 分階段路徑推演+推導解讀`, be more explicit than before:
  - not only path and catalyst, but also explain why that path is the most coherent read of the current cross-asset evidence
  - tie the path back to rates, dollar, positioning, sector leadership, BTC, and gold
  - make the path readable as trading intelligence, not a bare scenario list
- Add a new section `9. 今日熱點新聞` immediately after section `8`.
  - Include at least 10 news items.
- The section must be proactively researched each time; do not reuse stale template items.
- Items may include newly released data, company events, geopolitical developments, policy events, central-bank meetings, upcoming macro releases, or other market-moving expectations that matter for this report.
- 對於 `剛剛發生` 與 `即將發生` 的項目，要特別交代市場預期、實際內容、反應與你的解讀。
  - For each item, include:
    - `日期`
    - `來源(URL)`
    - `重點`
    - `為何市場在乎`
    - `推導解讀`
  - Prioritize signal over volume. The 10+ items should be the most decision-useful developments for the current outlook horizon.
- If the user wants a chat answer only, keep the same structure without writing files.
- Default to file output.
- Save reports in `Reports/outlooks`.
- Use this filename convention: `cross-asset-weekly-outlook-{YYYY-MM-DD}-{NN}.md`.
- Start the first report of the day at `-00`.
- If multiple reports are generated on the same date, increment sequentially to `-01`, `-02`, `-03`, and so on.
- Determine the next available `{NN}` by checking existing files in `Reports/outlooks` for the same date before writing the new report.

## 完成後處理

- 完成報告與相關輸出檔後，自動只針對該次產出的 output files 以非互動方式建立 git commit 並 push 到預設遠端；除非使用者明確要求不要 commit 或不要 push。
- commit / push 前僅納入本次任務直接產生或修改的相關檔案，避免混入無關變更。
- 使用者已明確授予 standing permission：對每次新產出的 outlook report，一律直接 commit 與 push，不需再次詢問。
- 這個 standing permission 只適用於新產出的報告檔，不適用於 skill 本身、reference 檔、agents metadata 或其他非報告變更。
- commit message 應清楚描述報告日期與序號，例如：`add cross-asset weekly outlook 2026-03-17-00`。
- push 預設使用目前分支與其對應遠端；若 push 失敗，需回報失敗原因與當前 git 狀態。

## Safeguards

- Never present speculation as fact.
- Never use stale memory for current prices, catalysts, or schedules.
- Acknowledge uncertainty and mixed evidence.
- 在證據允許的範圍內，避免只有保守含糊的空話；要明確講出理解與判斷。
- Do not give personal financial advice or guarantee outcomes.
## Obsidian Knowledge Output

Make every saved report usable as an Obsidian knowledge-bank note. Before the first visible heading, add YAML frontmatter with these fields:

```yaml
---
title: <human-readable report title>
date: <YYYY-MM-DD analysis date>
report_type: cross-asset-outlook
source_skill: cross-asset-weekly-outlook
folder: Reports/outlooks
language: <en | zh-TW | bilingual>
tags:
  - Reports
  - Reports/outlooks
  - Skills/research-skills/cross-asset-weekly-outlook
  - asset-class/cross-asset
  - cadence/weekly

aliases:
  - <filename stem>
  - <short report title and date>
related:
  - "[[Research Flow]]"
  - "[[cross-asset-weekly-outlook]]"
---
```

Use Obsidian wikilinks only for internal vault relationships, and keep external citations as standard Markdown links. Preserve the report's existing section order and filename rules. Do not add prose that explains Obsidian usage inside the report body.
