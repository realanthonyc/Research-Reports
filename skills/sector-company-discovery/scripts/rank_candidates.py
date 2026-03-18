#!/usr/bin/env python3
"""
Rank candidate companies from a small JSON scorecard.

Input:
{
  "weights": {
    "business_quality": 0.3,
    "valuation": 0.25,
    "resilience": 0.25,
    "balance_sheet": 0.2
  },
  "companies": [
    {
      "name": "Company A",
      "scores": {
        "business_quality": 8,
        "valuation": 6,
        "resilience": 9,
        "balance_sheet": 8
      }
    }
  ]
}
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


def _load_payload(path: str) -> dict:
    if path == "-":
        return json.load(sys.stdin)
    return json.loads(Path(path).read_text())


def _validate(payload: dict) -> None:
    if "weights" not in payload or not isinstance(payload["weights"], dict) or not payload["weights"]:
        raise ValueError("payload must include a non-empty 'weights' object")
    if "companies" not in payload or not isinstance(payload["companies"], list) or not payload["companies"]:
        raise ValueError("payload must include a non-empty 'companies' list")


def rank_companies(payload: dict) -> dict:
    _validate(payload)
    weights = {k: float(v) for k, v in payload["weights"].items()}
    total_weight = sum(weights.values())
    if total_weight <= 0:
        raise ValueError("weights must sum to a positive number")

    ranked = []
    for company in payload["companies"]:
        scores = company.get("scores", {})
        weighted_score = 0.0
        missing = []
        for key, weight in weights.items():
            if key not in scores:
                missing.append(key)
                continue
            weighted_score += float(scores[key]) * weight
        normalized_score = weighted_score / total_weight
        ranked.append(
            {
                "name": company["name"],
                "weighted_score": normalized_score,
                "missing_metrics": missing,
                "scores": scores,
            }
        )

    ranked.sort(key=lambda item: item["weighted_score"], reverse=True)
    return {"weights": weights, "ranked_companies": ranked}


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: rank_candidates.py <input.json|->", file=sys.stderr)
        return 1

    payload = _load_payload(sys.argv[1])
    result = rank_companies(payload)
    json.dump(result, sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
