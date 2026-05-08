---
title: New Energy（含核能）長期複利股篩選
date: 2026-05-08
report_type: compounder-screen
source_skill: screening-compounders
folder: reports/2026-05-08
language: zh-TW
tags:
  - reports
  - reports/2026-05-08
  - Skills/research-skills/screening-compounders
  - research-flow/screening
  - investing/compounders

aliases:
  - screening-compounders-2026-05-08-02
  - New Energy 含核能複利股篩選 2026-05-08
related:
  - "[[Research Flow]]"
  - "[[screening-compounders]]"
---

## 研究範圍與篩選宇宙

參考上游報告：[New Energy（含核能）公司篩選報告](/Users/anthony/Git/realanthonyc/Research-Reports/Reports/2026-05-08/sector-company-discovery-2026-05-08-02.md)。

宇宙：Constellation、Vistra、NextEra、First Solar、Cameco、BWX Technologies、GE Vernova、Enphase、SolarEdge、Fluence。這是題材強但財務模型差異極大的集合，因此本次特別嚴格處理 leverage、merchant power、政策補貼與短歷史問題。

## 步驟 1：拒絕清單

| 公司 | Pass/Fail | 觸發項目 | 證據與判斷 |
|---|---|---|---|
| Constellation | Fail | 3 槓桿；4 大型併購 | Calpine 交易後變成更好平台，但槓桿與整合使 strict compounder 不通過。 |
| Vistra | Fail | 3 槓桿；5 merchant power | 電價/容量市場 beta 太高。 |
| NextEra | Fail | 3 資本密集槓桿；ROCE 結構低 | Utility/renewables 是資產重模型，不是高 ROCE 複利模型。 |
| First Solar | Fail | 5 政策/價格週期 | backlog 強，但太陽能製造受政策、價格與產能週期影響。 |
| Cameco | Fail | 5 commodity cycle | 鈾價與礦山供應週期支配獲利。 |
| BWX Technologies | Pass to ROCE | 無立即 veto | 核供應鏈與海軍核推進品質高，值得核算。 |
| GE Vernova | Fail | 2 分拆/turnaround | 獨立上市歷史不足且 Wind 重組仍影響可比性。 |
| Enphase / SolarEdge / Fluence | Fail | 5 快速變化/低可預測性 | 住宅太陽能、inverter、儲能競爭與價格壓力太高。 |

## 步驟 2：ROCE 歷史篩選

BWXT 是核能供應鏈最接近 compounder 的公司，但 ROCE 仍遠低於 20%。

| 公司 | 2025 | 2024 | 2023 | 2022 | 2021 | 平均 | 結論 |
|---|---:|---:|---:|---:|---:|---:|---|
| BWXT | 9.2% | 13.5% | 14.0% | 13.4% | 15.3% | 13.1% | Fail，ROCE 不足。 |

計算例：2025 EBIT 3.296 億美元、Total Assets 42.72 億美元、Current Liabilities 6.720 億美元，ROCE = 9.2%。資料來源：[BWXT income statement](https://stockanalysis.com/stocks/bwxt/financials/)、[BWXT balance sheet](https://stockanalysis.com/stocks/bwxt/financials/balance-sheet/)。

## 步驟 3：財務極度穩健性檢查

| 公司 | Net debt | FCF | 分散度 | 業務 mix | CCC | 結論 |
|---|---:|---|---|---|---|---|
| BWXT | 2025 net debt 約 15.1 億美元 | FCF 連續為正，但 2021-2022 偏弱 | 政府/海軍核需求穩定但客戶集中 | Government + Commercial + Medical | 合約製造/庫存占用資金 | 3/5，未達 4 項。 |

## 步驟 4：趨同進化商業模式驗證

BWXT 的模式接近「高認證、國防/核能 mission-critical 零組件」，可類比 TransDigm、HEICO、Ametek 某些工業品線與國防 prime supplier 的供應鏈地位。模型本身可產生長期現金流，但 BWXT 的資產強度與政府合約結構，使 ROCE 沒有達到本 skill 的高門檻。

## 步驟 5：三個達爾文心法交叉驗證

- 長期高 ROCE：不通過。近 5 年平均約 13.1%。
- 現金回報：部分通過。FCF 為正且 dividend 穩定，但 FCF margin 不高。
- 反敘事驗證：通過。核能題材不用預測也能看到供應鏈稀缺；但稀缺不等於高 ROCE compounder。

## 步驟 6：綜合評分與排名

沒有公司通過所有前置步驟。

| 公司 | ROCE | 財務穩健 | 模型 | 資本配置 | 估值 | 判斷 |
|---|---:|---:|---:|---:|---:|---|
| BWXT | 1.8/4 | 1.2/2 | 1.7/2 | 0.7/1 | 0.2/1 | 5.6，不列入。 |

## 最終候選清單

無。New Energy 是強長期主題，但多數公司是 regulated utility、merchant power、commodity、政策週期或早期技術，不符合 strict compounder。

## 主要風險與不確定性

- BWXT 可能是好品質核能供應鏈標的，但 current valuation 很高，ROCE 不足以支撐 compounder 入選。
- CEG/VST 可能因 AI power 價格重估而繼續上漲，但這屬於電力價格/資產重估，不是本報告的穩定複利框架。
- 如果 Calpine 整合後 CEG 快速降槓桿且 ROCE 顯著提升，需重新篩選。

## 資料來源

- 上游報告：[New Energy（含核能）公司篩選報告](/Users/anthony/Git/realanthonyc/Research-Reports/Reports/2026-05-08/sector-company-discovery-2026-05-08-02.md)
- BWXT financials: [income statement](https://stockanalysis.com/stocks/bwxt/financials/), [balance sheet](https://stockanalysis.com/stocks/bwxt/financials/balance-sheet/)
- BWXT Q1 2026: [company release](https://www.bwxt.com/bwx-technologies-reports-first-quarter-2026-results/)
- Constellation FY2025: [company release](https://www.constellationenergy.com/content/constellationenergy/en/news/2026/02/constellation-reports-fourth-quarter-and-full-year-2025-results)
- NextEra Q1 2026: [company release](https://www.investor.nexteraenergy.com/~/media/Files/N/NEE-IR/reports-and-fillings/quarterly-earnings/2026/Q1%202026/2026-0423%20NEEQ12026News%20Release%20vF.pdf)
