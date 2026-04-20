---
name: sector-company-discovery
description: Discover, compare, and shortlist public companies within a sector, industry, theme, or candidate set. Use when the user wants to find the most attractive company in a space, identify which company is the most undervalued, most competitive, most resilient, or best positioned, or narrow a broad universe down to 1-3 names for deeper research by combining broad data gathering, recent topic and narrative research, financial statement reading, business-quality comparison, and valuation-aware filtering.
---

# Sector Company Discovery

Screen a sector or candidate set, compare the right companies, and pick the best 1-3 names for deeper work.
Focus on narrowing the universe with evidence rather than writing a full deep-dive on every company.

## Workflow

1. Define the search universe
- Confirm the sector, industry, theme, geography, market-cap range, and date.
- If the user already has a candidate list, use it.
- If the universe is too broad, narrow it with one or more practical filters:
  - geography
  - market cap
  - business model
  - profitability
  - product category
  - customer type

2. Build the candidate set
- Identify a workable comparison set, usually `5-12` public companies.
- Exclude names that are clearly incomparable unless the user explicitly wants them included.
- State why each candidate belongs in the set.

3. Compare the right dimensions
- Evaluate each company on the dimensions that actually matter for the industry:
  - business quality
  - competitive position
  - growth durability
  - margin structure
  - balance sheet strength
  - capital intensity
  - management / capital allocation quality if relevant
  - valuation
  - resilience under stress
- Do not use the same framework blindly across every sector.

4. Read enough primary material
- Use recent filings, earnings materials, and company disclosures to confirm:
  - segment structure
  - revenue drivers
  - margin drivers
  - cash generation
  - leverage or dilution risk
  - important customer / supplier / regulatory dependencies
- Avoid relying only on summaries or secondary commentary when a core conclusion depends on a fact that can be checked in filings.

5. Research recent topics and narratives
- Identify the most relevant recent topics in the sector and for each candidate:
  - last 30-90 day earnings, guidance, or filing changes
  - major product launches, partnerships, pricing changes, or contract wins/losses
  - regulatory, policy, legal, or antitrust developments
  - management commentary that changed market expectations
  - conference, investor day, or keynote talking points
  - analyst estimate revisions, target changes, or rating shifts when they help explain market repricing
  - market narrative changes such as "AI capex", "pricing power", "China exposure", "demand normalization", or "margin reset"
- Separate:
  - what actually happened
  - what the market seems to believe happened
  - whether the narrative is supported by filings or still mostly speculative
- Prefer primary sources for the facts, then use secondary sources only to map the narrative debate.

6. Rank and reduce
- Produce a ranked list or tiered shortlist.
- Explain why the leading company wins on the criteria that matter most.
- If no company is clearly attractive, say so.

7. Hand off to deep research
- For the final 1-3 names, state what should be researched next.
- If one company clearly stands out, recommend using [`company-valuation-analyst`](../company-valuation-analyst/SKILL.md) or [`comprehensive-equity-research-analysis`](../comprehensive-equity-research-analysis/SKILL.md) for the next step.

## Hard Rules

1. Do not choose a winner based on valuation alone.
2. Do not choose a winner based on quality alone if valuation is clearly unreasonable.
3. State the comparison criteria before declaring the best company.
4. Distinguish `facts`, `assumptions`, and `judgment`.
5. If the companies serve different end-markets or use different business models, say how that reduces comparability.
6. If the evidence is mixed, give a top tier instead of forcing a single winner.
7. Use Traditional Chinese by default unless the user asks otherwise.

## Comparison Framework Selection

- Read [`references/framework-selection.md`](references/framework-selection.md) to choose the right comparison dimensions by company type.
- Read [`references/resilience-checklist.md`](references/resilience-checklist.md) when the user emphasizes defensiveness, survivability, or downside protection.
- Read [`references/output-template.md`](references/output-template.md) when preparing the final shortlist memo.
- Use [`scripts/rank_candidates.py`](scripts/rank_candidates.py) when deterministic scoring helps organize the shortlist.
- Write the final report to `Reports/research/sector-company-discovery-{YYYY-MM-DD}-00.md`.
- If a version for the same date already exists, increment the suffix to `-01`, `-02`, and so on.
- After writing the report, stage the report file and push the commit to the current remote.
- Prioritize recent topics and narrative interpretation when they materially change the sector ranking.

## Output

Use this section order unless the user asks for something else:

1. `Search scope`
2. `Candidate set`
3. `What matters in this industry`
4. `Comparison table`
5. `Top tier and why`
6. `Winner or preferred shortlist`
7. `Main reasons the leading idea could be wrong`
8. `Next step for deep research`

## Obsidian Knowledge Output

Make every saved report usable as an Obsidian knowledge-bank note. Before the first visible heading, add YAML frontmatter with these fields:

```yaml
---
title: <human-readable report title>
date: <YYYY-MM-DD analysis date>
report_type: sector-company-discovery
source_skill: sector-company-discovery
folder: Reports/research
language: <en | zh-TW | bilingual>
tags:
  - Reports
  - Reports/research
  - Skills/research-skills/sector-company-discovery
  - research-flow/screening
  - investing/equities

aliases:
  - <filename stem>
  - <short report title and date>
related:
  - "[[Research Flow]]"
  - "[[sector-company-discovery]]"
---
```

Use Obsidian wikilinks only for internal vault relationships, and keep external citations as standard Markdown links. Preserve the report's existing section order and filename rules. Do not add prose that explains Obsidian usage inside the report body.

## Quality Bar

- Compare like with like.
- Keep the shortlist small enough to be decision-useful.
- Avoid fake precision in rankings.
- If the ranking depends heavily on one uncertain assumption, say so clearly.
- Prefer direct source-backed business understanding over polished market narratives.
- Save the report as Markdown and write it in Traditional Chinese.
