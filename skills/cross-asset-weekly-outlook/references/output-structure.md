# Output Structure

Follow this structure exactly unless the user explicitly asks for a shorter or custom format.

## 標題與日期

- `Cross-Asset Weekly Outlook`
- `分析日期：YYYY-MM-DD`
- `分析範圍：` one line matching the weekday scope, explicitly naming the U.S. market weekday in `America/New_York`
- Prefer wording like:
  - `分析範圍：2026-03-17 至 2026-03-20（美東週二至週五）`
  - if the latest usable market tape is from the prior U.S. session, say so directly in the same line or immediately below it

## 核心判斷

- 3 to 6 bullets.
- State the dominant market regime first.
- State the most important near-term driver.
- State whether equities, BTC, and gold are aligned or diverging.
- State overall confidence: `高 / 中 / 低`.

## 市場現在在交易什麼

- Explain what the market is actually pricing now.
- Use 2 to 5 bullets with explicit cause-and-effect reasoning.
- Separate `已實現催化`, `市場等待中的事件`, and `背景脈絡`.

## 大市

- Cover `S&P 500`, `Nasdaq`, `Dow`, `Russell 2000`, `VIX`, rates, and `DXY`.
- Explain not just the move, but the mechanism behind the move.
- Give `DXY` dedicated analytical treatment, not just a passing mention.
- End with a judgment block that explicitly states:
  - the time span of the judgment
  - directional bias
  - breadth
  - leadership
  - fragility / invalidation trigger

## 焦點個股

- Analyze either user-specified names or your own selected tape drivers.
- If the user does not specify names, analyze at least 6 stocks.
- For each stock:
  - what happened
  - why it matters
  - implication for the broader market or sector

## BTC

- Explain current structure and macro linkage.
- If the weekday scope includes the weekend, explicitly discuss:
  - weekend liquidity
  - gap risk into Monday
  - whether BTC is more likely to lead or follow macro risk appetite

## 金價

- Explain the move through real yields, dollar, and safe-haven or reserve demand.
- Note whether gold is confirming or contradicting the broader macro regime.

## 分日 / 分階段路徑推演+推導解讀

- Build the path according to the weekday:
  - Monday: `週一至週五`
  - Tuesday: `週二至週五`
  - Wednesday: `週三至週五`
  - Thursday: `週四至週五` + `BTC 週末` + `來週`
  - Friday: `週五` + `BTC 週末` + `來週`
  - Saturday or Sunday: `BTC 週末` + `來週` + `特別是週一`
- For each required horizon, provide:
  - base case
  - upside path
  - downside path
  - main catalyst to watch
- Add a short `推導解讀` block for each required horizon that explains why the path follows from the current evidence across rates, dollar, oil, volatility, leadership, BTC, and gold.

## 今日熱點新聞

- Include at least 10 items.
- Each item must include:
  - `日期`
  - `來源(URL)`
  - `重點`
  - `為何市場在乎`
  - `推導解讀`
- Mix already-released and upcoming items when that improves the report's usefulness, but every item must be directly relevant to the report horizon.
- Prefer the highest-value macro, policy, geopolitical, earnings, sector, and flow catalysts rather than generic headlines.

## 關鍵監測清單

- 5 to 10 bullets.
- Include the next macro releases, policy events, earnings, flows, or technical markers that could change the view.

## Bottom Line

- 4 to 8 bullets.
- State:
  - dominant directional bias
  - which asset has the cleanest setup
  - what would most likely prove the base case wrong
  - what matters most next

## Source Use

- Inline-link material sources wherever factual claims depend on fresh information.
- Prefer primary sources; use strong secondary sources for interpretation.

## File Output

- Save the completed report to `/reports/outlooks`.
- Use the filename format `cross-asset-weekly-outlook-{YYYY-MM-DD}-{NN}.md`.
- The first report generated on a given date must use `-00`.
- Later reports on the same date must increment: `-01`, `-02`, `-03`, and so on.
