# Output Template

Use this structure for the final Daily Trading Insights reports. Write the English Markdown report first, then create a separate Traditional Chinese Markdown report as a faithful, polished Traditional Chinese translation of the English report.

Filename pair:
- English: `daily-trading-insights-<YYYY-MM-DD>-<NN>.md`
- Traditional Chinese: `daily-trading-insights-<YYYY-MM-DD>-<NN>-zh-tw.md`

Use the same `<NN>` for both files. If either file already exists, increment both to the next available pair.

## English Report

```markdown
---
title: Daily Trading Insights - <YYYY-MM-DD>
date: <YYYY-MM-DD>
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
  - daily-trading-insights-<YYYY-MM-DD>-<NN>
  - Daily Trading Insights <YYYY-MM-DD>
related:
  - "[[Research Flow]]"
  - "[[daily-trading-insights]]"
---

# Daily Trading Insights - <YYYY-MM-DD>

> [!abstract] Report Scope
> English U.S. trading intelligence note. A separate Traditional Chinese direct translation is saved as `daily-trading-insights-<YYYY-MM-DD>-<NN>-zh-tw.md`.

## Detailed Summary

<Explain the dominant drivers, likely market regime, strongest catalysts, and key uncertainty.>

## Brief Summary

- Market Bias:
- Most Important Catalyst Today:
- Strongest Bullish Setup:
- Strongest Bearish / Hedge Setup:
- Biggest Risk:
- Signals That Need Confirmation:

## Analysis Date And Scope

- User Timezone:
- U.S. Market Date:
- Analysis Scope:
- Report Status: normal / coverage-thin / event-waiting

## Today's Market Sentiment, Direction, Pattern

- Regime:
- Directional Bias:
- Leadership:
- Breadth:
- Volatility:
- Yields / DXY:
- Likely Pattern:
- What Would Flip The View:

## Abstracts

### 1. <Title>

- Signal:
- Signal Type:
- Affected Assets:
- Time Horizon:
- Confidence:
- Brief Summary:
- Logics, Derivation, and Implications:
- What To Watch / Invalidation:
- Sources:

<!-- Continue to at least 20 items. -->

## Hot Picks

### 1. <Name / Ticker>

- Direction:
- Strength:
- Setup Type:
- Catalyst:
- Why:
- When:
- What To Watch If Uncertain:
- Invalidation / Risk:

<!-- Continue to at least 12 U.S.-listed stocks or ETFs. -->

## Mega-Cap Watch: Special Attention Points And Expected Moves

| Company | Ticker | Special Attention Point | Expected Move | Evidence | Trading Read-Through | Invalidation |
|---|---:|---|---|---|---|---|
| Google / Alphabet | GOOGL / GOOG |  | Bullish / Bearish / Neutral / Mixed |  |  |  |
| Apple | AAPL |  | Bullish / Bearish / Neutral / Mixed |  |  |  |
| Microsoft | MSFT |  | Bullish / Bearish / Neutral / Mixed |  |  |  |
| Meta | META |  | Bullish / Bearish / Neutral / Mixed |  |  |  |
| Nvidia | NVDA |  | Bullish / Bearish / Neutral / Mixed |  |  |  |
| Amazon | AMZN |  | Bullish / Bearish / Neutral / Mixed |  |  |  |
| Tesla | TSLA |  | Bullish / Bearish / Neutral / Mixed |  |  |  |

## Upcoming Catalysts Radar

| Date | Event | Expected Market Focus | Assets To Watch | Risk |
|---|---|---|---|---|
| <YYYY-MM-DD> |  |  |  |  |

## Cross-Asset Confirmation Check

- Equities:
- Rates:
- DXY:
- Volatility:
- Commodities:
- Crypto / crypto-linked equities:
- Credit / liquidity if relevant:

## Final Action Map

- Best Bullish Setups:
- Best Bearish / Hedge Setups:
- Watch Only:
- Key Events Today:
- Key Events Next Few Sessions:
- Biggest Hidden Risk:
- What Would Flip The Market View:

## Caveats

- <Unresolved facts, low-confidence items, thin coverage, or contradictory evidence.>
```

## Traditional Chinese Report

Translate the completed English report faithfully into polished Traditional Chinese. Preserve every fact, number, sign, timestamp, source URL, caveat, item order, ranking order, and table row order, but do not leave English field labels or English prose fragments in the Chinese report unless they are tickers, company names, ETF names, source names, standard acronyms, or paired bilingual signal terms.

```markdown
---
title: 每日交易洞察 - <YYYY-MM-DD>
date: <YYYY-MM-DD>
report_type: daily-trading-insights
source_skill: daily-trading-insights
folder: Reports/outlooks
language: zh-TW
tags:
  - Reports
  - Reports/outlooks
  - Skills/research-skills/daily-trading-insights
  - asset-class/equities
  - cadence/daily
  - language/zh-TW
aliases:
  - daily-trading-insights-<YYYY-MM-DD>-<NN>-zh-tw
  - 每日交易洞察 <YYYY-MM-DD>
related:
  - "[[Research Flow]]"
  - "[[daily-trading-insights]]"
---

# 每日交易洞察 - <YYYY-MM-DD>

> [!abstract] 報告範圍
> 美股交易情報筆記的繁體中文直譯版。英文原文另存為 `daily-trading-insights-<YYYY-MM-DD>-<NN>.md`。

## 詳細總結

<Translate Detailed Summary into Traditional Chinese. Preserve facts, numbers, directional calls, timestamps, and source links.>

## 總結概要

- 大市偏向：
- 今日最重要催化：
- 最強 bullish setup：
- 最強 bearish / hedge setup：
- 最大風險：
- 需要等確認的訊號：

## 分析日期與範圍

- 使用者時區：
- 美股交易日期：
- 分析範圍：
- 報告狀態：normal / coverage-thin / event-waiting

## 今日市場情緒、方向與型態

- 市場狀態：
- 方向偏向：
- 領漲主線：
- 市場廣度：
- 波動率：
- 殖利率 / DXY：
- 可能盤型：
- 什麼情況會扭轉觀點：

## 摘要

### 1. <Title>

- 訊號：
- 訊號類型：
- 受影響資產：
- 時間範圍：
- 信心程度：
- 簡要說明：
- 邏輯、推導與影響：
- 觀察重點 / 失效條件：
- 來源：

<!-- Continue to at least 20 items in the same order as English. -->

## Hot Picks

### 1. <Name / Ticker>

- 方向：
- 強度：
- 型態：
- 催化因素：
- 理由：
- 時點：
- 不確定時的觀察重點：
- 失效條件 / 風險：

<!-- Continue to at least 12 U.S.-listed stocks or ETFs in the same order as English. -->

## Mega-Cap Watch：特別注意點與預計走勢

| 公司 | Ticker | 特別注意點 | 預計走勢 | 證據 | 交易連動影響 | 失效條件 |
|---|---:|---|---|---|---|---|
| Google / Alphabet | GOOGL / GOOG |  | 看多 / 看空 / 中性 / 混合 |  |  |  |
| Apple | AAPL |  | 看多 / 看空 / 中性 / 混合 |  |  |  |
| Microsoft | MSFT |  | 看多 / 看空 / 中性 / 混合 |  |  |  |
| Meta | META |  | 看多 / 看空 / 中性 / 混合 |  |  |  |
| Nvidia | NVDA |  | 看多 / 看空 / 中性 / 混合 |  |  |  |
| Amazon | AMZN |  | 看多 / 看空 / 中性 / 混合 |  |  |  |
| Tesla | TSLA |  | 看多 / 看空 / 中性 / 混合 |  |  |  |

## Upcoming Catalysts Radar

| 日期 | 事件 | 預期市場焦點 | 觀察資產 | 風險 |
|---|---|---|---|---|
| <YYYY-MM-DD> |  |  |  |  |

## Cross-Asset Confirmation Check

- 股票：
- 利率：
- DXY：
- 波動率：
- 商品：
- Crypto / crypto-linked equities：
- 信用 / 流動性（如相關）：

## Final Action Map

- 最佳看多設定：
- 最佳看空 / 避險設定：
- 僅觀察：
- 今日關鍵事件：
- 未來幾個交易日關鍵事件：
- 最大隱藏風險：
- 什麼情況會扭轉市場觀點：

## Caveats

- <Translate unresolved facts, low-confidence items, thin coverage, or contradictory evidence.>
```

Chinese QA before saving:
- Replace English field labels with the Chinese labels above.
- Translate prose into natural Taiwan-style Traditional Chinese.
- Preserve tickers, company names, ETF names, source names, URLs, numbers, dates, and timestamps.
- Keep English signal terms only when paired with Chinese, for example `看多 (Bullish)` or `事件驅動 (event-driven)`.
- Translate reasoning-chain nodes into Chinese while preserving the arrow structure.
