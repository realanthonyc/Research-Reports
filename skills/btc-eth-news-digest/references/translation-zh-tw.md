# Traditional Chinese Translation Conventions (繁體中文)

## Goal

Translate the completed English report into Traditional Chinese while preserving trading precision, timestamps, links, and factual caveats.

## Rules

- Output the English report first, then the Traditional Chinese report.
- Preserve structure, numbering, and section order exactly.
- Preserve all source links unchanged.
- Preserve absolute dates/times and timezone labels unchanged unless the user requests localized formatting.
- Keep tickers/acronyms in original form when standard in trading context:
  - BTC, ETH, ETF, SEC, CFTC, CPI, PPI, NFP, PMI, FOMC, DXY, OI
- Translate surrounding prose and labels into Traditional Chinese.
- Preserve fact vs inference labels explicitly (e.g., `事實 / 推論` or equivalent clear labels).
- Do not add new claims or remove caveats during translation.

## Suggested Terminology

- trader briefing: `交易員簡報`
- market reaction: `市場反應`
- impact horizon: `影響時程`
- catalyst calendar: `催化劑行事曆`
- watchlist: `觀察清單`
- confirmed / developing / speculative: `已確認 / 進展中 / 推測性`
- bullish / bearish / neutral / mixed: `偏多 / 偏空 / 中性 / 偏中性（或分歧）`
- risk-on / risk-off: `風險偏好 / 風險趨避`
- yields: `殖利率`
- liquidity: `流動性`

## Consistency Check

Before finalizing:
- Ensure every English bullet/item has a Chinese counterpart.
- Ensure numbers, percentages, and signs (`+/-`) match exactly.
- Ensure caveats and uncertainty wording are preserved.

## Translation QA Gate (required)

Run a final pass and verify:
- All URLs in Chinese section are identical to English section.
- All timestamps and timezone labels are identical to English section.
- Confidence labels and confidence scores are preserved exactly.
- Market impact scores and event keys are preserved exactly.
- Any `coverage-thin` or `primary source unavailable` flags are preserved in Chinese.
