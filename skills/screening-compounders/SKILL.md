---
name: screening-compounders
description: Screen a U.S. stock sector, theme, or industry for 5-10 long-term compounder candidates using a strict veto-first process. Use when the user wants a historically grounded shortlist built from recent multi-year filings and source-backed research, with one-strike eliminations for governance, leverage, acquisition addiction, fast-changing industries, or misaligned ownership; 10-year-or-longest-available ROCE analysis; financial robustness checks; convergent-evolution business-model validation; Darwin-style fact-only cross-checks; and a final ranked list with valuation context and reasons each company can remain great for a long time.
---

# Screening Compounders

Build a long-term candidate list by eliminating weak businesses first, then rewarding only companies with durable historical evidence.
Default to U.S.-listed equities and write the final report in Traditional Chinese unless the user asks otherwise.

## Core Workflow

1. Define the search universe
- Confirm `sector / theme / industry`, geography, any market-cap bias, and the report date.
- Build an initial candidate set of roughly `8-20` names so attrition is possible.
- Prefer direct peers over loose concept stocks.

2. Gather primary-source data first
- Use the most recent multi-year company filings and official disclosures first:
  - `10-K`, `20-F`, annual reports, proxy statements
  - quarterly filings only when needed to clarify the latest balance sheet or debt position
  - investor presentations only as supplements
- Use recent market data for price and valuation context only after the historical business-quality work is done.
- Record the exact fiscal years used. Prefer `10 years`; if unavailable, use the longest available history and say so explicitly.

3. Apply the veto screen before any ranking
- Run every candidate through the non-negotiable rejection checklist in [`references/veto-checklist.md`](references/veto-checklist.md).
- If any item is triggered, eliminate the company immediately.
- For every elimination, cite the evidence, the date, and the specific veto item.
- Do not "average out" a veto with a strong brand, a cheap multiple, or a charismatic CEO.

4. Calculate historical ROCE
- Use `ROCE = EBIT / (Total Assets - Current Liabilities) * 100%`.
- Build a year-by-year table for each surviving company for at least the last `10` fiscal years or the longest available period.
- Use reported `EBIT` where available. If only operating income is reported, state that it is used as the EBIT proxy.
- Use year-end `Total Assets` and `Current Liabilities` from the same fiscal year.
- Calculate:
  - annual ROCE
  - simple average ROCE across the full period
  - min / max ROCE
  - count of down years
  - whether there is any `2-year consecutive major decline`
- Treat "major decline" as a drop of about `20%+` relative from the prior year unless industry structure suggests a better threshold; if so, explain the override.
- Eliminate companies with average ROCE below `20%`, unstable long-term patterns, or repeated collapses that break the compounder case.

5. Check financial robustness
- Use [`references/financial-robustness.md`](references/financial-robustness.md) and require at least `4` passed items.
- Explicitly test:
  - net cash or near-zero net debt
  - consistently positive and strong free cash flow
  - diversified customers / suppliers
  - diversified business mix across product, customer, or geography
  - short or structurally favorable cash conversion cycle
- When a metric cannot be measured precisely from public filings, use disclosed qualitative evidence and label it as `qualitative pass/fail`.

6. Validate convergent evolution
- Ask whether the business model has already produced repeated winners in other markets, times, or adjacent geographies.
- Use [`references/convergent-evolution.md`](references/convergent-evolution.md) to frame the test.
- Reject "this company is special" narratives unless the underlying model itself is proven across multiple cases.
- State the parallel examples and why they count as the same playbook.

7. Run the Darwin cross-check
- Use only long-horizon value-creation evidence.
- Ignore near-term narrative noise unless it affects a veto item or the current balance sheet.
- Do not use DCF, TAM storytelling, or future scenario modeling.
- Look for burdensome honesty signals:
  - `10+` years of high ROCE
  - sustained dividends or buybacks funded by real cash generation
  - durable reputation signals from counterparties, competitors, or former employees when they are independently corroborated

8. Rank the survivors
- Score only the companies that passed every earlier step.
- ROCE carries the highest weight.
- Use the scoring structure in [`references/scoring-template.md`](references/scoring-template.md).
- Produce a final `Top 5-10` list only if enough companies truly pass; otherwise return a shorter list and say the bar was not met.

9. Add valuation context at the end
- After quality ranking is complete, compare:
  - current share price
  - current valuation multiples
  - the company’s own historical valuation range over an appropriate long period
- Use valuation as context for position sizing or patience, not as a way to rescue a weak business.

## Hard Rules

1. Use recent, web-verified information for any fact that could have changed, especially price, debt, share count, management, governance events, or recent acquisitions.
2. Prefer primary sources for claims that can affect elimination or ranking.
3. Separate `fact`, `inference`, and `judgment`.
4. Show calculations, not just conclusions.
5. If a figure is estimated, label it clearly and explain the bridge.
6. If two sources conflict, use the higher-priority source and note the discrepancy.
7. Do not force a full 5-10 names if the sector does not contain enough companies that deserve to pass.

## Output Rules

- Always write the final report as a Markdown file under `reports/research`.
- Use the filename format `screening-compounders-{date}-00.md`.
- Replace `{date}` with the analysis date in `YYYY-MM-DD` format.
- If a file with the same date already exists, increment the suffix to `-01`, `-02`, and so on.
- Use the final memo order in [`references/output-template.md`](references/output-template.md).

## Completion Handling

- After the research report and any directly related output files are completed and saved, automatically stage only the files created or modified for that specific research task, then create a non-interactive git commit and push to the default remote.
- Treat this skill as having standing permission to `git add`, `git commit`, and `git push` for the current task's output files only; do not ask the user again unless they explicitly revoke that permission.
- Never include unrelated workspace changes in that commit.
- Use a clear commit message such as `add screening compounders report 2026-03-21-00`.
- If push fails, report the failure reason and the current git status.
- If the task is updating the skill itself, its references, templates, metadata, or other implementation files, do not auto-commit or auto-push.

Minimum required sections:

1. `研究範圍與篩選宇宙`
2. `步驟 1：拒絕清單`
3. `步驟 2：ROCE 歷史篩選`
4. `步驟 3：財務極度穩健性檢查`
5. `步驟 4：趨同進化商業模式驗證`
6. `步驟 5：三個達爾文心法交叉驗證`
7. `步驟 6：綜合評分與排名`
8. `最終候選清單`
9. `主要風險與不確定性`
10. `資料來源`

## Quality Bar

- Treat survival as the first objective.
- Favor boring durability over exciting narratives.
- Reject businesses whose greatness depends mainly on forecasting.
- Prefer long, clean operating histories over temporary rebounds.
- A candidate should look stronger after historical scrutiny, not weaker.
