#!/usr/bin/env python3
"""
Build a dilution-aware bear/base/bull valuation table from a small JSON input.

Input format:
{
  "current_price": 21.0,
  "shares_outstanding": 125000000,
  "scenarios": [
    {
      "name": "bear",
      "probability": 1.0,
      "cash": 300000000,
      "core_value": 150000000,
      "debt": 0,
      "dilution_pct": 0.25,
      "method": "ev-ebitda"
    }
  ]
}
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


def _load_input(path: str) -> dict:
    if path == "-":
        return json.load(sys.stdin)
    return json.loads(Path(path).read_text())


def _validate_payload(payload: dict) -> None:
    if "scenarios" not in payload or not isinstance(payload["scenarios"], list) or not payload["scenarios"]:
        raise ValueError("payload must include a non-empty 'scenarios' list")
    if "shares_outstanding" not in payload:
        raise ValueError("payload must include 'shares_outstanding'")


def _scenario_row(scenario: dict, shares_outstanding: float, current_price: float | None) -> dict:
    cash = float(scenario.get("cash", 0.0))
    core_value = float(scenario.get("core_value", scenario.get("asset_value", 0.0)))
    debt = float(scenario.get("debt", 0.0))
    dilution_pct = float(scenario.get("dilution_pct", 0.0))
    probability = float(scenario.get("probability", 1.0))
    method = scenario.get("method", "scenario")

    gross_equity_value = cash + (core_value * probability) - debt
    diluted_share_count = shares_outstanding * (1.0 + dilution_pct)
    per_share_value = gross_equity_value / diluted_share_count if diluted_share_count else 0.0

    row = {
        "name": scenario["name"],
        "method": method,
        "probability": probability,
        "gross_equity_value": gross_equity_value,
        "dilution_pct": dilution_pct,
        "diluted_shares": diluted_share_count,
        "per_share_value": per_share_value,
    }

    if current_price is not None and current_price > 0:
        row["upside_downside_pct"] = (per_share_value / current_price) - 1.0

    return row


def build_table(payload: dict) -> dict:
    _validate_payload(payload)

    shares_outstanding = float(payload["shares_outstanding"])
    current_price = payload.get("current_price")
    current_price = float(current_price) if current_price is not None else None

    rows = [
        _scenario_row(scenario, shares_outstanding, current_price)
        for scenario in payload["scenarios"]
    ]

    weighted_value = sum(
        row["per_share_value"] * float(scenario.get("weight", 1.0))
        for row, scenario in zip(rows, payload["scenarios"])
    )
    total_weight = sum(float(scenario.get("weight", 1.0)) for scenario in payload["scenarios"])
    weighted_value = weighted_value / total_weight if total_weight else 0.0

    result = {
        "current_price": current_price,
        "shares_outstanding": shares_outstanding,
        "weighted_per_share_value": weighted_value,
        "scenarios": rows,
    }

    if current_price is not None and current_price > 0:
        result["price_to_weighted_value"] = current_price / weighted_value if weighted_value else None

    return result


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: build_valuation_table.py <input.json|->", file=sys.stderr)
        return 1

    payload = _load_input(sys.argv[1])
    result = build_table(payload)
    json.dump(result, sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
