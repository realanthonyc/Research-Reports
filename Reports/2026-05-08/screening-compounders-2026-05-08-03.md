---
title: CPU 長期複利股篩選
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
  - screening-compounders-2026-05-08-03
  - CPU 複利股篩選 2026-05-08
related:
  - "[[Research Flow]]"
  - "[[screening-compounders]]"
---

## 研究範圍與篩選宇宙

參考上游報告：[CPU 公司篩選報告](/Users/anthony/Git/realanthonyc/Research-Reports/Reports/2026-05-08/sector-company-discovery-2026-05-08-03.md)。

宇宙：AMD、Intel、Arm、NVIDIA、Qualcomm、TSMC、Apple、Broadcom、Marvell、Micron。因主題是 CPU/compute value chain，不限純 CPU 設計；但最終必須通過 compounder 歷史證據。

資料期間：2021-2026 或 FY2022-FY2026 依公司財年可得標準化資料。對於通過者，這是「近 5 年 source-backed screen」；完整 10 年重建會是下一步，但近 5 年已足以淘汰多數弱者。

## 步驟 1：拒絕清單

| 公司 | Pass/Fail | 觸發項目 | 證據與判斷 |
|---|---|---|---|
| NVIDIA | Pass to ROCE | 無立即 veto | 產業變化快，但 CUDA/networking/rack-scale ecosystem 與財務證據足以進入 ROCE。 |
| TSMC | Pass to ROCE | 無立即 veto | 先進製程/封裝瓶頸，長期高資本回報需核算。 |
| Qualcomm | Pass to ROCE | 無立即 veto | Royalty + chipset 模式，手機週期存在但歷史 ROCE 高。 |
| AMD | Fail | 5 快速變化；ROCE 歷史不足 | 近年改善明顯，但長期複利證據仍受 turnaround、Xilinx 併購與 GPU/CPU mix 影響。 |
| Intel | Fail | 2 distressed turnaround | thesis 依賴製程/foundry turnaround。 |
| Arm | Fail | 上市紀錄不足；估值/控制複雜 | IPO 後公開歷史不足，且 SoftBank 控制與估值要求太高。 |
| Apple | Fail for theme fit | CPU 不可分拆 | 是 compounder，但 CPU exposure 不是可獨立投資 thesis。 |
| Broadcom | Fail for this pass | 4 大型併購依賴 | 高品質，但 VMware 等大型併購使本輪 CPU 主題下不作純候選。 |
| Marvell / Micron | Fail | 5 週期/低可預測性 | networking/storage/memory 週期性更高。 |

## 步驟 2：ROCE 歷史篩選

| 公司 | 2026/TTM | 2025 | 2024 | 2023 | 2022/2021 | 平均 | 2 年重大連續下滑 | 結論 |
|---|---:|---:|---:|---:|---:|---:|---|---|
| NVIDIA | 74.7% | 87.1% | 59.8% | 12.2% | 25.2% | 51.8% | 無連續兩年 | Pass，但 2023 cyclical trough 需記錄。 |
| TSMC | 34.4% TTM | 30.2% | 24.6% | 20.0% | 28.2% / 21.9% | 26.5% | 無 | Pass。 |
| Qualcomm | 24.0% TTM | 30.1% | 22.6% | 18.8% | 42.7% / 33.4% | 28.6% | 無 | Pass，2023 低於 20% 但平均與現金流通過。 |

NVIDIA 計算例：FY2026 operating income 1,303.87 億美元、assets 2,068.03 億美元、current liabilities 321.63 億美元，ROCE = 74.7%。資料來源：[NVIDIA income statement](https://stockanalysis.com/stocks/nvda/financials/)、[NVIDIA balance sheet](https://stockanalysis.com/stocks/nvda/financials/balance-sheet/)。

TSMC 計算例：FY2025 operating income 1.936 兆新台幣、assets 7.933 兆、current liabilities 1.522 兆，ROCE = 30.2%。資料來源：[TSMC income statement](https://stockanalysis.com/stocks/tsm/financials/)、[TSMC balance sheet](https://stockanalysis.com/stocks/tsm/financials/balance-sheet/)。

Qualcomm 計算例：FY2025 operating income 123.55 億美元、assets 501.43 億美元、current liabilities 91.44 億美元，ROCE = 30.1%。資料來源：[Qualcomm income statement](https://stockanalysis.com/stocks/qcom/financials/)、[Qualcomm balance sheet](https://stockanalysis.com/stocks/qcom/financials/balance-sheet/)。

## 步驟 3：財務極度穩健性檢查

| 公司 | Net debt/cash | FCF | 分散度 | 業務 mix | CCC | 結論 |
|---|---:|---|---|---|---|---|
| NVIDIA | FY2026 net cash 約 515 億美元 | FY2022-FY2026 FCF 全正且快速放大 | hyperscaler 集中是風險，但平台需求廣 | data center、gaming、networking、software | 預收/供應鏈議價能力強 | 4/5，通過。 |
| TSMC | 2025 cash/ST investments 約 3.13 兆新台幣，高於總債務 | FCF 長期為正但 capex 重 | 客戶集中於大型 fabless，但技術壟斷抵消部分風險 | HPC、smartphone、auto、IoT | foundry working capital 可控 | 4/5，通過。 |
| Qualcomm | 2025 net debt 約 46.6 億美元，低於 EBITDA | FCF margin 長期高，2021-2025 全正 | Apple/手機集中風險仍在 | QCT + QTL，汽車/IoT 擴張 | fabless 模式有利 | 4/5，通過。 |

## 步驟 4：趨同進化商業模式驗證

- NVIDIA：模式是高 switching cost 的開發者平台 + 硬體加速 + networking fabric。可類比 Microsoft Windows/Office developer ecosystem、ASML 製程瓶頸、Cisco 早期 networking stack；歷史上這類平台能長期賺取高 ROCE，但也容易遭遇技術週期重估。
- TSMC：模式是先進製程雙邊平台：客戶設計依賴、設備/製程 know-how、良率學習曲線。可類比 ASML、台灣/韓國半導體 foundry 的集中化路徑、航空引擎供應鏈的長期認證壁壘。
- Qualcomm：模式是 IP royalty + fabless chipset。可類比 ARM IP royalty、Dolby/QNX 類授權模式、部分 EDA/IP 模型；QTL 是高品質，QCT 則較週期。

## 步驟 5：三個達爾文心法交叉驗證

- 長期高 ROCE：NVIDIA、TSMC、Qualcomm 近 5 年通過；TSMC/Qualcomm 更平滑，NVIDIA 2023 有 trough 但後續躍升極強。
- 現金回報：三者通過。NVIDIA 與 Qualcomm 有 buyback/dividend，TSMC 有穩定股息與巨額再投資。
- 反敘事驗證：TSMC 最不依賴「AI 預測」，因為所有 CPU/AI chip winner 都需要先進製程；NVIDIA 依賴 AI capex 持續，Qualcomm 依賴手機以外的 diversification 成功。

## 步驟 6：綜合評分與排名

| 排名 | 公司 | ROCE 4 | 財務 2 | 模型 2 | 資本配置 1 | 估值 1 | 總分 | 判斷 |
|---:|---|---:|---:|---:|---:|---:|---:|---|
| 1 | TSMC | 3.4 | 1.7 | 1.9 | 0.8 | 0.5 | 8.3 | 最穩健 CPU/compute supply-chain compounder。 |
| 2 | NVIDIA | 3.8 | 1.7 | 1.8 | 0.8 | 0.1 | 8.2 | 最強 ROCE，但估值與 AI capex 週期風險高。 |
| 3 | Qualcomm | 3.2 | 1.6 | 1.5 | 0.8 | 0.6 | 7.7 | 合格但手機/Apple/競爭折價仍在。 |

## 最終候選清單

1. TSMC：首選。它不是 CPU 設計公司，但在 CPU/AI compute 價值鏈中最接近「不押單一架構贏家」的複利資產。
2. NVIDIA：品質最高、ROCE 最強，但目前估值留下的錯誤空間最小。
3. Qualcomm：合格但較低順位；適合等待手機週期與汽車/PC/IoT diversification 被低估時再研究。

## 主要風險與不確定性

- 本報告使用標準化 5 年資料，完整 10 年逐年 ROCE 重建仍應在深研階段完成。
- NVIDIA 可能因 AI capex 週期、China restrictions、ASIC 競爭或毛利正常化而被重估。
- TSMC 的地緣風險是最大單一風險；ROCE 再好也不能忽略 Taiwan risk。
- Qualcomm 的 QTL 很好，但 QCT 面臨手機週期、Apple 自研 modem 與 Arm PC 不確定性。

## 資料來源

- 上游報告：[CPU 公司篩選報告](/Users/anthony/Git/realanthonyc/Research-Reports/Reports/2026-05-08/sector-company-discovery-2026-05-08-03.md)
- NVIDIA financials: [income statement](https://stockanalysis.com/stocks/nvda/financials/), [balance sheet](https://stockanalysis.com/stocks/nvda/financials/balance-sheet/)
- TSMC financials: [income statement](https://stockanalysis.com/stocks/tsm/financials/), [balance sheet](https://stockanalysis.com/stocks/tsm/financials/balance-sheet/)
- Qualcomm financials: [income statement](https://stockanalysis.com/stocks/qcom/financials/), [balance sheet](https://stockanalysis.com/stocks/qcom/financials/balance-sheet/)
- AMD Q1 2026: [company release](https://www.amd.com/en/newsroom/press-releases/2026-5-5-amd-reports-first-quarter-2026-financial-results.html)
- Arm FY2026: [company release](https://newsroom.arm.com/news/arm-q4-fye26-results)
