# Output Structure

Follow this structure exactly unless the user explicitly asks for a shorter or custom format.

## 1. 標題與日期

- `Cross-Asset Weekly Outlook`
- `分析日期：YYYY-MM-DD`
- `分析範圍：` one line matching the weekday scope

## 2. 核心判斷

- 3 to 6 bullets.
- State the dominant market regime first.
- State the most important near-term driver.
- State whether equities, BTC, and gold are aligned or diverging.
- State overall confidence: `高 / 中 / 低`.

## 3. 市場現在在交易什麼

- Explain what the market is actually pricing now.
- Use 2 to 5 bullets with explicit cause-and-effect reasoning.
- Separate `已實現催化`, `市場等待中的事件`, and `背景脈絡`.

## 4. 大市

- Cover `S&P 500`, `Nasdaq`, `Dow`, `Russell 2000`, `VIX`, rates, and `DXY`.
- Explain not just the move, but the mechanism behind the move.
- End with a short judgment on breadth, leadership, and fragility.

## 5. 焦點個股

- Analyze either user-specified names or your own selected tape drivers.
- For each stock:
  - what happened
  - why it matters
  - implication for the broader market or sector

## 6. BTC

- Explain current structure and macro linkage.
- If the weekday scope includes the weekend, explicitly discuss:
  - weekend liquidity
  - gap risk into Monday
  - whether BTC is more likely to lead or follow macro risk appetite

## 7. 金價

- Explain the move through real yields, dollar, and safe-haven or reserve demand.
- Note whether gold is confirming or contradicting the broader macro regime.

## 8. 分日 / 分階段路徑推演

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

## 9. 關鍵監測清單

- 5 to 10 bullets.
- Include the next macro releases, policy events, earnings, flows, or technical markers that could change the view.

## 10. Bottom Line

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
- Use the filename format `Cross-Asset-Weekly-Outlook-{YYYY-MM-DD}-{NN}.md`.
- The first report generated on a given date must use `-00`.
- Later reports on the same date must increment: `-01`, `-02`, `-03`, and so on.
