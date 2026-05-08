---
title: Electric Grid 長期複利股篩選
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
  - screening-compounders-2026-05-08-00
  - Electric Grid 複利股篩選 2026-05-08
related:
  - "[[Research Flow]]"
  - "[[screening-compounders]]"
---

## 研究範圍與篩選宇宙

參考上游報告：[Electric Grid 公司篩選報告](/Users/anthony/Git/realanthonyc/Research-Reports/Reports/2026-05-08/sector-company-discovery-2026-05-08-00.md)。

本次篩選主題是美股可投資的電網、配電設備、電氣化工程與 data center power infrastructure。初始宇宙：Quanta Services、Eaton、GE Vernova、Hubbell、nVent、Powell Industries、Schneider Electric ADR、Vertiv、Emerson、Ametek。因 skill 預設美股與直接同業，Schneider 只作商業模式參照，非最終候選。

資料期間：以 2021-2025 財年標準化財務資料為可直接核算區間；若公司上市/分拆歷史不足或重組後資料不可比，直接列為拒絕。ROCE 採 `EBIT / (Total Assets - Current Liabilities)`；EBIT 以 operating income 作 proxy。

## 步驟 1：拒絕清單

| 公司 | Pass/Fail | 觸發項目 | 證據與判斷 |
|---|---|---|---|
| Eaton | Pass to ROCE | 無立即 veto | 2026 Q1 Electrical Americas 訂單與 backlog 強，但 2025 後債務因併購/資本配置上升，需在 robustness 中扣分。 |
| Hubbell | Pass to ROCE | 無立即 veto | Utility/Electrical products 品質高，2025 firm backlog 21.59 億美元；需檢查槓桿與 ROCE。 |
| Quanta Services | Fail | 5 快速變化/低預測性；工程人力與專案風險 | 儘管 backlog 創高，工程服務本質較重人力、合約執行與大型專案風險；不是典型高 ROCE 複利模型。 |
| GE Vernova | Fail | 2 turnaround / 分拆後紀錄不足 | 2024 才獨立上市，且 Wind 與 Power/Grid 組合仍在重組，不能用長期 compounder 證據通過。 |
| nVent | Fail | 4 acquisition dependence | 電氣保護/連接組合好，但成長與組合調整受併購影響較大，不作高確定複利候選。 |
| Powell | Fail | 5 週期/專案集中 | 中壓配電受益明顯，但專案型、客戶集中與週期性太高。 |
| Vertiv | Fail | 5 快速變化且再定價後可預測性不足 | AI data center power/cooling 是強題材，但歷史上市紀錄、margin 重設與需求週期仍不足以通過嚴格複利篩選。 |
| Emerson / Ametek | Fail for theme fit | 不夠直接 | 是優質工業公司，但電網純度不足。 |

## 步驟 2：ROCE 歷史篩選

直接進入 ROCE 的只有 Eaton 與 Hubbell。兩者都是好公司，但 strict compounder bar 要求長期平均 ROCE 約 20% 以上；2021-2025 的標準化資料未達標。

| 公司 | 2025 | 2024 | 2023 | 2022 | 2021 | 平均 | 結論 |
|---|---:|---:|---:|---:|---:|---:|---|
| Eaton | 16.3% | 15.2% | 12.7% | 10.5% | 11.5% | 13.2% | Fail，ROCE 不足 20%。 |
| Hubbell | 18.0% | 19.6% | 18.4% | 16.4% | 12.6% | 17.0% | Fail，接近但仍未過 20%。 |

Eaton 計算例：2025 EBIT 52.09 億美元、Total Assets 412.51 億美元、Current Liabilities 93.70 億美元，ROCE = 52.09 / (412.51 - 93.70) = 16.3%。資料來源：[Eaton income statement](https://stockanalysis.com/stocks/etn/financials/)、[Eaton balance sheet](https://stockanalysis.com/stocks/etn/financials/balance-sheet/)。

Hubbell 計算例：2025 EBIT 12.09 億美元、Total Assets 82.29 億美元、Current Liabilities 15.09 億美元，ROCE = 18.0%。資料來源：[Hubbell income statement](https://stockanalysis.com/stocks/hubb/financials/)、[Hubbell balance sheet](https://stockanalysis.com/stocks/hubb/financials/balance-sheet/)。

## 步驟 3：財務極度穩健性檢查

| 公司 | Net debt | FCF | 分散度 | 業務 mix | CCC | 結論 |
|---|---:|---|---|---|---|---|
| Eaton | 2025 net debt 約 97.3 億美元；2026 Q1 TTM 淨債升至約 210.8 億美元 | 2021-2025 FCF 全為正 | 多產品/多地區 | Electrical + Aerospace + Vehicle/eMobility | 工業製造 CCC 不短 | 3/5，未達 4 項。 |
| Hubbell | 2025 net debt 約 18.3 億美元 | 2021-2025 FCF 全為正 | Utility/customer 分散度尚可 | Utility + Electrical | 存貨與應收占用資金 | 3/5，未達 4 項。 |

## 步驟 4：趨同進化商業模式驗證

Eaton/Hubbell 的模式類似高可靠度工業電氣零組件供應商，與 Rockwell、Ametek、Schneider、ABB 的工業複利模型相近：小額關鍵零組件、認證壁壘、分銷網路與 installed base。但本次不是模型失敗，而是財務門檻未達：ROCE 和淨債結構不足以支撐「嚴格 compounder」結論。

## 步驟 5：三個達爾文心法交叉驗證

- 長期高 ROCE：未通過。Eaton 與 Hubbell 近 5 年平均低於 20%。
- 現金回報：通過。兩者都有穩定 FCF、股息與回購。
- 反敘事驗證：通過但不足。AI data center 和電網升級是強需求，但 compounder 標準不獎勵題材，只獎勵長期可驗證的資本回報。

## 步驟 6：綜合評分與排名

沒有公司通過所有前置步驟，因此不做正式 compounder 排名。

觀察名單，不列入最終候選：

| 公司 | ROCE | 財務穩健 | 模型 | 估值 | 判斷 |
|---|---:|---:|---:|---:|---|
| Hubbell | 3.0/4 | 1.2/2 | 1.7/2 | 0.4/1 | 最接近，但 ROCE 不過線。 |
| Eaton | 2.5/4 | 1.0/2 | 1.8/2 | 0.3/1 | 品質高，併購後槓桿與 ROCE 拉低。 |

## 最終候選清單

無。Electric Grid 是非常好的投資主題，但在 strict compounder screen 下，最直接的電網公司不是高 ROCE、低槓桿、長期穩定複利的乾淨樣本。

## 主要風險與不確定性

- StockAnalysis 標準化資料只直接呈現 2021-2025；若用完整 10-K 重建 10 年 ROCE，可能細節不同，但目前 5 年已不足 20%，不需要靠更長資料救回。
- Eaton/Hubbell 可能仍是好投資，但更像「高品質電氣化週期股」，不是本 skill 定義的 strict compounder。
- 若電網設備價格權持續多年改善，未來 ROCE 可能上修，需年度重篩。

## 資料來源

- 上游報告：[Electric Grid 公司篩選報告](/Users/anthony/Git/realanthonyc/Research-Reports/Reports/2026-05-08/sector-company-discovery-2026-05-08-00.md)
- Eaton financials: [income statement](https://stockanalysis.com/stocks/etn/financials/), [balance sheet](https://stockanalysis.com/stocks/etn/financials/balance-sheet/)
- Hubbell financials: [income statement](https://stockanalysis.com/stocks/hubb/financials/), [balance sheet](https://stockanalysis.com/stocks/hubb/financials/balance-sheet/)
- Quanta Q1 2026: [company release](https://investors.quantaservices.com/news-events/press-releases/detail/396/quanta-services-reports-first-quarter-2026-results)
- GE Vernova 2025 annual report: [company annual report](https://www.gevernova.com/investors/annual-report)
