---
name: upcoming-themes-discovery
description: Discover and rank underappreciated upcoming sectors or cross-industry themes that have a strong chance of becoming the next major market focus before they are fully crowded, where real demand may accelerate within 6-24 months, become genuinely large in magnitude, and persist for 1-2 years or longer, using deep web research, source-backed study, adoption-stage analysis, value-chain mapping, capital-cycle checks, and mispricing judgment. Use when the user wants to find upcoming high-demand themes early, identify sectors to research before they become consensus, build an ambush watchlist for low-price accumulation, or understand which themes are likely to become durable investment opportunities rather than short-lived market hypes.
---

# Upcoming Themes Discovery

Identify a small number of future demand regimes early enough to research deeply before the market fully prices them.
Target themes that could plausibly become the next crowded market focus later, but are not yet fully on the main stage now.
Default to public-equity relevance and write the final report in Traditional Chinese unless the user asks otherwise.

## Core Workflow

1. Define the objective and horizon
- Confirm the time horizon is `6-24 months` for demand acceleration and at least `1-2 years` for theme durability unless the user specifies otherwise.
- Clarify geography, sector scope, and whether the user wants:
  - broad theme discovery
  - discovery inside a known area
  - a watchlist for future accumulation
- Avoid reframing the task into a short-term momentum or hot-news exercise.
- Keep the target profile explicit:
  - not hot already
  - likely to become much more important later
  - demand could become forceful, not merely incremental
  - early evidence exists, but consensus is incomplete

2. Generate candidate themes from structural drivers
- Start with forces that can create non-trivial future demand:
  - regulation, legal mandates, compliance deadlines
  - defense, infrastructure, industrial policy, subsidies
  - enterprise or hyperscaler capex cycles
  - cost-curve declines that unlock adoption
  - labor shortages, resilience spending, security spending
  - energy, power, cooling, grid, water, logistics, or other bottlenecks
  - demographic or healthcare shifts
- Prefer themes where spending could become necessary rather than merely fashionable.
- Prefer themes where future demand can become `large enough to matter`, not merely incrementally positive.
- Ask explicitly:
  - can this become a board-level budget line or national-priority spend?
  - can this demand wave create a multi-quarter earnings regime for listed beneficiaries?
  - is the demand large enough to overwhelm normal cyclical noise?
  - is this still early enough that the market has not fully elevated it into a headline consensus trade?

3. Use early-positioning hints, but do not confuse them with proof
- Treat the following as helpful hints:
  - smart-money positioning starting to appear
  - specialist investor letters or niche industry commentary turning more focused
  - suppliers or industry insiders beginning to position capacity or inventory
  - subtle relative strength or volume appearing first in second-order beneficiaries
- Use these only as `early signals`, not as standalone reasons to elevate a theme.
- A theme still needs structural-demand, durability, value-chain, and mispricing support.

4. Test whether adoption is nearing an inflection
- Determine whether the theme is:
  - concept only
  - pre-inflection
  - adoption inflection
  - scaling
  - already crowded
- Look for evidence that buyers are moving from pilots or isolated projects toward budgeted deployment.
- Down-rank themes that are directionally correct but still too early to matter for earnings.

5. Map the value chain before naming winners
- Break each theme into:
  - enabling infrastructure
  - core components
  - system integrators
  - end applications
  - adjacent recurring-revenue or compliance layers
- Ask where scarcity, pricing power, switching costs, and supply discipline actually sit.
- Separate:
  - narrative beneficiaries
  - volume beneficiaries
  - high-return equity beneficiaries

6. Run durability and capital-cycle checks
- Demand must plausibly persist for `1-2 years` or longer.
- Confirm durability through one or more of:
  - multi-year budgets
  - backlog and bookings
  - deployment plans
  - compliance or reliability requirements
  - long build cycles
  - ecosystem commitments
- Reject or down-rank themes where future supply can ramp so quickly that returns may be arbitraged away.

7. Test for mispricing
- Do not stop at "this theme will grow."
- Judge whether the market has already priced the likely upside through:
  - valuation levels
  - estimate revisions
  - investor positioning
  - narrative saturation
  - whether the market is focused on the wrong part of the value chain
- Prefer themes where the thesis is becoming verifiable but remains under-modeled.

8. Produce a research-first output
- Final output should rank only `3-5` themes unless the user asks for more.
- Show the broader candidate funnel before presenting the final winners.
- State which themes were considered but not selected, and why they were rejected, deferred, or downgraded.
- Write the final memo in two layers:
  - first, a shortlist and candidate-funnel summary
  - then, one complete section per selected theme
- Do not alternate by discussion dimension across all selected themes. Finish one theme fully before moving to the next.
- For each theme, explain:
  - why it won against other candidates
  - why demand should accelerate
  - why the theme should last
  - where value capture is likely to occur
  - whether the demand can become truly large in scale
  - what could invalidate the thesis
  - what evidence to monitor next
  - what type of pullback would create an attractive ambush entry

## Minimum Research Bar

- Do not finalize a report after a shallow scan.
- For each serious candidate theme, try to verify the thesis with multiple source categories.
- Prefer using at least `3` of the following source types, and preferably `4+` for the final selected themes:
  - official policy, regulatory, or budget documents
  - company filings, investor materials, or earnings-call commentary
  - credible industry research or trade-group data
  - primary market or supply-chain evidence such as backlog, capacity, lead-time, or procurement signals
  - market evidence such as positioning, relative strength, or smart-money hints
- If the evidence base is thin, say so and down-rank the theme instead of filling gaps with narrative confidence.
- For every selected theme, explicitly note which evidence types support it.

## Hard Rules

1. Do not confuse price momentum with future demand.
2. Do not promote a theme unless demand timing and durability are both addressed.
3. Do not treat a theme as investable until value-chain economics are discussed.
4. Do not ignore supply response; future demand without supply discipline is often a trap.
5. Distinguish `fact`, `inference`, and `judgment`.
6. Research must involve deep web search, not a shallow scan of a few articles.
7. Use recent, source-backed information for claims that could have changed.
8. Prefer primary sources for facts that materially affect the thesis, then use secondary sources to map interpretation or debate.
9. If the theme is real but too early, say `too early` instead of forcing a bullish setup.
10. If the theme is real but already consensus, say `priced in / crowded` instead of forcing an idea.
11. If the demand opportunity is not likely to become meaningfully large, do not elevate it into the final list.
12. Use Traditional Chinese by default unless the user asks otherwise.
13. Do not present final themes without showing the selection logic and the rejected or deferred candidates.
14. Do not rely on obvious top-down narratives alone; include at least one non-obvious or second-order angle when possible.
15. Treat smart-money or early industry positioning as a hint, not as sufficient proof by itself.
16. A selected theme should usually be supported by multiple independent evidence types, not one article or one narrative lane.

## Research Lenses

- Read [`references/methodology.md`](references/methodology.md) to apply the full demand-regime framework and intellectual foundations.
- Read [`references/output-template.md`](references/output-template.md) when writing the final memo.

## Output Rules

- Always write the final report as a Markdown file under `reports/research`.
- Use the filename format `upcoming-themes-discovery-{date}-00.md`.
- Replace `{date}` with the analysis date in `YYYY-MM-DD` format.
- If a file with the same date already exists, increment the suffix to `-01`, `-02`, and so on.
- Use the report order in [`references/output-template.md`](references/output-template.md) unless the user requests a different structure.

## Obsidian Knowledge Output

Make every saved report usable as an Obsidian knowledge-bank note. Before the first visible heading, add YAML frontmatter with these fields:

```yaml
---
title: <human-readable report title>
date: <YYYY-MM-DD analysis date>
report_type: theme-discovery
source_skill: upcoming-themes-discovery
folder: reports/research
language: <en | zh-TW | bilingual>
tags:
  - reports
  - reports/research
  - skills/upcoming-themes-discovery
  - research-flow/discovery
  - investing/themes

aliases:
  - <filename stem>
  - <short report title and date>
related:
  - "[[Research Flow]]"
  - "[[upcoming-themes-discovery]]"
---
```

Use Obsidian wikilinks only for internal vault relationships, and keep external citations as standard Markdown links. Preserve the report's existing section order and filename rules. Do not add prose that explains Obsidian usage inside the report body.

## Completion Handling

- If the task is to produce a research report, save the report file, then automatically stage only the files created or modified for that specific research task, create a non-interactive git commit, and push to the default remote without asking the user again.
- Treat this skill as having standing permission to `git add`, `git commit`, and `git push` for the current task's report files only.
- Never include unrelated workspace changes in that commit.
- Use a clear commit message such as `add upcoming themes discovery report 2026-03-22-00`.
- If push fails, report the failure reason and the current git status.
- If the task is to update the skill itself, references, templates, or metadata, do not auto-commit or auto-push.

## Quality Bar

- Prefer forced or necessary spending over fashionable storytelling.
- Prefer huge, budget-moving demand regimes over modest niche growth.
- Prefer themes where adoption, economics, and timing line up.
- Prefer underappreciated bottlenecks over obvious concept stocks.
- Prefer themes where the best angle may sit in a second-order enabler rather than the headline winner.
- Prefer themes that are early enough to be under-owned, but far enough along to be researchable and verifiable.
- Prefer a smaller list of high-conviction themes over a long list of weak ideas.
- The final output should help the user research early and wait patiently, not encourage impulsive chasing.
