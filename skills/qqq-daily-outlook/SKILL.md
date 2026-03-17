---
name: qqq-daily-outlook
description: Produce the latest QQQ daily outlook for the relevant U.S. trading session by fusing a user-provided real-time dashboard screenshot (QQQ, VIX, DXY, yields) with latest web-verified macro/news catalysts. Use when the user wants to know how QQQ is likely to behave today, whether the request comes hours or minutes before the open, shortly after the open, or after Friday's close for the next trading day's setup. Estimate directional bias, expected move, likely path, key levels, options implications, and execution risks for the active or next relevant session.
---

# QQQ Daily Outlook

Produce a short, high-signal QQQ session outlook focused on what is most likely for the relevant U.S. trading day.

Do not act like a generic advisor. Act like a professional short-term market analyst.

## Session Targeting Rules

Determine the correct target session before doing the analysis:

- If the request arrives before the U.S. cash open, treat it as today's premarket session, whether it is hours before or minutes before the open.
- If the request arrives shortly after the U.S. cash open, still treat it as today's session and adjust the analysis to what the market is doing now versus what is likely through the rest of the day.
- If the request arrives after the close, treat it as the next trading day's setup unless the user clearly asks for a post-close recap instead.
- If the request arrives after Friday's close or during the weekend, default to the next trading session, which is normally Monday's open.
- When the user says "today" but the timing implies the next U.S. trading session, state the exact target session with a concrete date.

Keep the report centered on the same core question: how QQQ is likely to behave for the relevant trading day.

## Mandatory Intake

Before final analysis, request the latest screenshot from the user.

Ask for one TradingView-style dashboard screenshot that includes at minimum:
- QQQ intraday/premarket chart
- VIX
- DXY
- U.S. 10Y yield or TNX/ZN proxy
- session metrics if available (gap, premarket high/low, VWAP, opening range, day high/low)

Use this prompt template when needed:
- `Please upload your latest dashboard screenshot (QQQ + VIX + DXY + 10Y) with timestamp/timezone so I can produce the latest QQQ outlook for the relevant U.S. trading session.`

If screenshot is missing or stale, say so and lower confidence.

## Mandatory Data Fusion Workflow

1. Parse screenshot structure and key levels.
2. Search the internet broadly for latest market-moving catalysts, verify timestamps, and separate fresh signals from stale commentary.
3. Check the economic/macro calendar for the next relevant releases and note what the market is waiting for.
4. Assess whether QQQ is trading realized news, anticipation of upcoming data, or a conflict between the two.
5. Cross-check multi-source context and keep only high-impact signals.
6. Estimate probabilities for the relevant session path, including the next 1-4 hours if the market is already open.
7. Produce the required report format.

Treat `just happened` and `about to happen` as first-class inputs:
- explicitly identify what happened in roughly the last 0-24 hours that still drives the tape
- explicitly identify what the market is waiting for in the next 24-72 hours
- if analyst actions, institutional commentary, or major strategy notes are affecting QQQ leaders or index sentiment, include them when they materially change expectations or reaction
- explain not only the headline, but the expectation, the actual outcome, and the market's interpretation

## Screenshot Signals To Extract

- Gap up/down vs prior close
- Premarket high/low and premarket VWAP
- Current location vs premarket range (upper/mid/lower)
- If market is already open: opening range, session VWAP behavior, and acceptance/rejection versus the opening move
- Overnight structure (trend, range, failed break)
- Nearest resistance/support and invalidation levels
- Momentum quality (drive strength, rejection/acceptance at VWAP)

## Web Research Requirements

Always run web research for current-day catalysts and include source links.

Prioritize primary and credible sources:
- U.S. economic calendar/release headlines (CPI/PPI/NFP/ISM/claims)
- Fed communications and policy signals
- Major geopolitical shocks with equity impact
- Mega-cap/semiconductor earnings or guidance headlines
- Index-level risk news likely to affect QQQ in the same session

Rules:
- Prefer same-day updates; include concrete dates/times when relevant.
- Use multiple sources when possible.
- If no meaningful catalyst appears, explicitly say: `No high-impact fresh catalyst detected`.
- Before final analysis, explicitly check whether a Tier 1 scheduled macro release occurred within the last 24 hours or before the U.S. cash open.
- If a Tier 1 scheduled macro release exists, treat it as the default primary catalyst unless price action clearly shows another driver has overridden it.
- Do not just list headlines. State how the market appears to be trading the news through QQQ, VIX, DXY, and yields.
- Expand the search beyond one or two obvious headlines. Sweep across macro releases, Fed, rates, FX, commodities, geopolitics, and mega-cap/semiconductor news before ranking relevance.
- Distinguish between `fresh realized catalyst`, `upcoming scheduled catalyst`, and `background context`.
- Prefer primary sources for data releases and company results; use high-quality news wires/publications to explain market interpretation.

Minimum search buckets:
- Latest U.S. macro releases within the last 24 hours
- Upcoming U.S. macro releases and Fed events in the next 24-72 hours that could affect pre-open positioning or same-session risk appetite
- Treasury/yield and dollar drivers
- Oil/commodity or geopolitical headlines that can shift inflation/risk sentiment
- Mega-cap and semiconductor company news with direct relevance to QQQ leadership

## Upcoming Macro/Event Awareness

Always check whether the market may be waiting for a scheduled event even if it has not been released yet.

For each relevant upcoming event, identify:
- release date and time
- whether it is before the cash open, during the session, or after the close
- broad market expectation / consensus if available
- why anticipation or caution around the event could affect QQQ before the release

Examples:
- CPI/PPI/NFP/claims/ISM
- FOMC decision, Powell testimony, Fed minutes
- Treasury auctions if rates sensitivity is clearly driving QQQ

If no meaningful upcoming event is likely to affect today's session, explicitly say:
- `No near-term scheduled macro event likely to dominate today's tape`

## Catalyst Priority Ladder

Classify catalysts before writing the report:

- `Tier 1`: scheduled macro releases and major Fed events within the last 24 hours or before/near cash open (CPI, PPI, NFP, ISM, claims, FOMC, Powell).
- `Tier 2`: major rates, oil, geopolitical, or policy shocks likely to move index risk appetite the same session.
- `Tier 3`: mega-cap or semiconductor earnings, guidance, analyst actions, or sector-specific headlines.

Rules:
- Assess Tier 1 first.
- If multiple catalysts exist, identify the single most important one as `Dominant Driver Today`.
- If price action appears to disagree with the obvious headline, explain the conflict explicitly rather than averaging signals together.
- Ignore low-signal headlines that do not plausibly change the next 1-4 hour QQQ path.
- Separate what is already known from what traders may still be waiting for.

## Synthesis Rules

Do not stop at listing signals. Convert them into an explicit market narrative:

- Explain what the market is likely pricing right now.
- Explain why the tape is confirming or rejecting the most obvious catalyst.
- Explain how upcoming macro/event risk may suppress trend, increase whipsaw risk, or support directional continuation.
- Explain the chain of reasoning from macro/news -> rates/dollar/volatility -> QQQ path.
- When signals conflict, say which signal should dominate and what would prove that judgment wrong.

## Reasoning Focus

Center the analysis on this question:
- `How likely is QQQ to move up/down/chop during the relevant trading session, and what is most likely over the next few hours from now?`

Use probability language. Avoid certainty.

## Confidence Framework

- `High`: screenshot structure, macro proxies, and catalysts align in one direction.
- `Medium`: partial alignment with at least one conflict.
- `Low`: mixed structure, unclear catalyst regime, or incomplete data.

## Volatility Buckets

- `Low`: expected move around `+-0.5% to +-0.9%`
- `Normal`: expected move around `+-0.9% to +-1.5%`
- `High`: expected move around `+-1.5% to +-2.5%+`

Adjust for event timing (e.g., major data release, Fed speaker, headline shock).

## Required Output Format

Write two markdown files into `/reports/outlooks` for each run:

- English master file: `reports/outlooks/qqq-daily-outlook-{date}-{nn}.md`
- Traditional Chinese translation: `reports/outlooks/qqq-daily-outlook-{date}-{nn}-zh-tw.md`

File naming rules:
- Use the local current date in `YYYY-MM-DD` format for `{date}`.
- Use a two-digit daily sequence for `{nn}` starting at `00`.
- If no report with that date exists yet, write `...-{date}-00.md`.
- If one or more reports already exist for the same date, increment sequentially: `01`, `02`, `03`, and so on.
- Determine the next sequence by inspecting existing files in `/reports/outlooks` before writing.

The English file is the source-of-truth report. The Traditional Chinese file must be a full, natural, professional translation of the English markdown file rather than a separately rewritten variant.

After writing the English and Traditional Chinese files:
- Stage only the output file(s) created or updated by this run.
- Create a non-interactive git commit automatically for those output files.
- Push automatically to the default remote/branch for the current repo after that output commit succeeds.
- If the user has already granted standing permission for commit/push, do not ask again before doing so.
- Do not automatically commit or push when the task is updating the skill itself, its references, templates, metadata, or other implementation files.
- If commit or push fails, report the failure reason and current git status briefly.
- Use a clear commit message that includes the report date and sequence, for example: `add qqq daily outlook 2026-03-17-00`.

In the English markdown file, place these summary sections first, before the main report:

`Detailed English Summary`
- 2-3 compact paragraphs.
- Explain the dominant setup, likely 1-4 hour path, and practical 0DTE implication.
- Slow down slightly on harder logic. Make the causal chain easy to follow.
- State your actual judgment / forecast plainly instead of hiding behind balanced caveats.

`Brief Summary`
- 4-6 bullets.
- Keep these bullets in English.
- Focus on bias, volatility, confirmation trigger, failure trigger, dominant tape driver, and the single most important just-happened or upcoming catalyst.

Then use exactly these main sections in the English master file:

`QQQ Daily Outlook`

`1. Market Environment`
- One-line risk regime: `risk-on / mixed / risk-off` with macro context.
- Add 1-2 bullets explaining whether the tape is driven more by realized news, upcoming-event caution, or both.

`2. Post-Open Direction Probability (Next 1-4 Hours)`
- `Bullish: X%`
- `Bearish: Y%`
- `Neutral/Chop: Z%`
- Ensure percentages sum to 100%.
- `Confidence: Low / Medium / High`

`3. Expected Volatility`
- `Low / Normal / High`
- `Estimated move: +-X%`
- 1-2 short bullets for why.

`4. Most Likely Intraday Path`
- One-line primary path scenario.
- 3-5 bullets with confirmation, invalidation, and what would shift the market into the secondary scenario.

`5. Key Levels`
- `Resistance`
- `Support`
- `Breakout level`
- `Invalidation level`

`6. 0DTE Options Implications`
- 3-6 bullets on call/put edge, theta burn risk, and continuation vs mean-reversion conditions.

`7. Major Risks Today`
- 3-5 bullets (fake breakout, macro headline whipsaw, midday chop, late reversal).

`8. Catalyst Snapshot (Web-Verified)`
- Start with `Dominant Driver Today: ...`
- 3-6 bullets on today's relevant macro/news catalysts.
- Add source links inline.
- If a Tier 1 macro release exists, the first catalyst bullet must cover it.
- Include at least one bullet on an upcoming scheduled event if it is plausibly affecting positioning today.

`9. Bottom Line`
- 3-5 bullets with:
  - dominant probability bias
  - expected volatility
  - single most important confirmation signal
  - what the market is actually trading (for example: growth scare, inflation scare, dovish relief, AI earnings offset, geopolitical risk-off)
  - how the next important macro/event risk could alter that view

`10. Final Quick Summary`
- 5-7 short bullets in English.
- Cover: bias, volatility, path, key levels, invalidation, and main risk.
- Make this section maximally fast-read and explicit.
- End with a brief non-advice / 0DTE risk reminder.

Then translate the entire English markdown into Traditional Chinese and save it as the `-zh-TW` file:
- Translate headings, summaries, and all body sections.
- Keep source links intact.
- Preserve numbers, probabilities, and key levels exactly.
- Make the translation read naturally and professionally in Traditional Chinese.

## Style Constraints

- Keep report readable in 45-90 seconds.
- Use compact bullets, but include enough reasoning that the user can see the causal chain.
- Keep only execution-relevant signals.
- Use concrete, testable confirmation triggers.

## Safeguards

Always:
- Acknowledge uncertainty.
- State assumptions and data limitations.
- Never guarantee outcomes.
- Clearly state this is not financial advice and 0DTE is high risk.

If inputs are incomplete, include:
- `Data completeness: Partial` with one-line impact on confidence.
