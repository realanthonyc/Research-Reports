# Capital Structure Framework

Capital structure can change per-share value even when enterprise value looks unchanged.

## Core Questions

1. How much cash and near-term liquidity does the company have?
2. How much debt, lease burden, or other fixed claim exists?
3. Is the company funding itself through operations, asset sales, or external capital?
4. Is management shrinking or expanding the share count?
5. Are there convertibles, warrants, options, preferreds, or sponsor overhangs?
6. Can the company refinance on workable terms if it needs to?

## What To Model

- Net cash or net debt
- Interest burden
- Maturity wall
- Runway if the business is cash-burning
- Expected dilution if external capital is likely
- Buyback support if capital return is material

## Default Heuristics

- `Net cash + positive FCF`: dilution is usually low priority unless M&A or aggressive SBC matters.
- `Cash-burning with <18 months runway`: financing risk enters the base case.
- `Levered with major maturities inside 24 months`: refinancing risk enters the base case.
- `Convertibles / warrants / sponsor supply`: per-share value needs a dilution or supply discussion even if headline market cap looks modest.

## Scenario Treatment

- Bear: worse financing terms, weaker refinancing window, lower buyback support.
- Base: workable but unspectacular access to capital.
- Bull: stronger self-funding, cheaper capital, or accretive capital returns.

## Minimum Disclosure

When capital structure matters, state:

- timing
- scale
- mechanism
- per-share impact
