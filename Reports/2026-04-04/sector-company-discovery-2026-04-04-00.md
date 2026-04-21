---
title: AI 晶片設計與先進製造產業篩選備忘錄
date: 2026-04-04
report_type: sector-company-discovery
source_skill: sector-company-discovery
folder: Reports/2026-04-04
language: zh-TW
tags:
  - reports
  - Reports/2026-04-04
  - skills/sector-company-discovery
  - research-flow/screening
  - investing/equities
aliases:
  - AI 晶片設計與先進製造產業篩選備忘錄
  - sector-company-discovery-2026-04-04-00
  - AI 晶片設計與先進製造產業篩選備忘錄 - 2026-04-04
related:
  - "[[research-flow]]"
  - "[[sector-company-discovery]]"
---

# AI 晶片設計與先進製造產業篩選備忘錄

分析日期：2026-04-04

## Search Scope

- `產業 / 主題`：AI 相關晶片開發與生產。
- `地理`：以美股與美國投資人可直接參與的核心公司為主，納入一家關鍵非美上市 ADR。
- `本次收斂方式`：只保留真正和 `AI compute / networking / memory / leading-edge manufacturing` 直接相關的公司。
- `納入範圍`：
  - `NVDA`：AI GPU 與全棧平台龍頭。
  - `AMD`：AI GPU / CPU / rack-scale 平台第二陣營核心。
  - `AVGO`：custom AI ASIC + networking + optical DSP。
  - `MRVL`：data center connectivity + custom silicon + optical / CXL。
  - `TSM`：先進製程與先進封裝核心製造商。
  - `MU`：HBM / DRAM / NAND，AI 記憶體供應核心。
- `排除但應知道`：
  - `ASML / AMAT / LRCX / KLAC`：屬設備，不是晶片開發或生產主體。
  - `ARM`：偏 IP 授權。
  - `INTC`：目前更像 turnaround 與 foundry special situation，不適合和這 6 家用同一框架硬排。
- `優化目標`：找出最值得往下深挖的 `1-3` 家，不是寫全產業百科。

## Candidate Set

這 6 家都屬於 AI 晶片價值鏈，但站位不同：

- `NVDA`：AI 計算平台與軟硬整合標準制定者。
- `AMD`：追趕型計算平台供應商，賭的是第二供應商地位與 open stack。
- `AVGO`：吃的是 hyperscaler custom XPU、交換、光互連與基礎設施軟體現金流。
- `MRVL`：吃 AI data center 連接、custom silicon、scale-up fabric。
- `TSM`：不是設計商，但幾乎承接所有高端 AI 晶片量產與先進封裝。
- `MU`：AI 記憶體瓶頸的直接受益者，尤其是 HBM 與高頻寬記憶體供應。

## What Matters In This Industry

這個產業不能只看營收增速，真正重要的是：

1. `架構與生態位階`：誰掌握標準，誰只是參與者。
2. `先進製程 / 先進封裝控制力`：AI 晶片不是只有設計，量產能力與 CoWoS / advanced packaging 是真正瓶頸。
3. `客戶質量與訂單可見度`：hyperscaler capex 是否已從實驗走到長約與大規模部署。
4. `毛利率與現金流質量`：AI 概念很多，但真正有高經濟利潤的公司不多。
5. `估值與敘事位置`：市場已經 price in 多少，還剩多少 margin of safety。
6. `政策 / 出口 / 地緣風險`：對中國出貨限制、台海風險、供應鏈在地化都會重寫排序。

## Recent Topics And Narratives

### 1. 敘事從「訓練 GPU 稀缺」轉向「AI factory 全棧化」

- `事實`：NVIDIA 在 GTC 2026 不只推 Rubin，還把 `Dynamo`、`DSX reference design`、儲存 / 網路 / 數位分身一起推進，明顯把自己從 GPU 公司擴成 AI factory 標準制定者。[NVIDIA FY26 Q4](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Fourth-Quarter-and-Fiscal-2026/) [NVIDIA Rubin](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Vera-Rubin-Opens-Agentic-AI-Frontier/default.aspx) [NVIDIA Dynamo](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Enters-Production-With-Dynamo-the-Broadly-Adopted-Inference-Operating-System-for-AI-Factories/default.aspx)
- `市場敘事`：市場已不再只看 GPU 出貨，而是看誰能定義 AI 資料中心整體架構。
- `判斷`：這個敘事是被主文件支持的，而且對 `NVDA` 極度有利。

### 2. hyperscaler 正在把 AI 預算部分轉向 custom silicon

- `事實`：Broadcom FY2026 Q1 AI semiconductor revenue 達 `8.4B`、年增 `106%`，且公司預期 Q2 AI semiconductor revenue 到 `10.7B`；Marvell 也透過 `Celestial AI`、`XConn` 與 NVIDIA `NVLink Fusion` 持續強化 custom XPU 和 scale-up fabric 路線。[Broadcom FY26 Q1](https://www.prnewswire.com/news-releases/broadcom-inc-announces-first-quarter-fiscal-year-2026-financial-results-and-quarterly-dividend-302704490.html) [Marvell FY26 Q4](https://investor.marvell.com/news-events/press-releases/detail/1011/marvell-technology-inc-reports-fourth-quarter-and-fiscal-year-2026-financial-results) [Marvell Celestial AI](https://investor.marvell.com/news-events/press-releases/detail/1005/marvell-completes-acquisition-of-celestial-ai) [NVDA-Marvell](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-AI-Ecosystem-Expands-as-Marvell-Joins-Forces-Through-NVLink-Fusion/default.aspx)
- `市場敘事`：custom ASIC 會分走 GPU 經濟租。
- `判斷`：這個敘事成立，但更像重分配 `AI 基礎設施 budget`，不是直接摧毀 `NVDA`。

### 3. 真正的瓶頸正往先進封裝與記憶體移動

- `事實`：TSMC 2025 Q4 美元營收 `33.73B`、gross margin `62.3%`，3nm/5nm/7nm 合計占 wafer revenue 極高；Micron FY2026 Q2 revenue `23.86B`、operating cash flow `11.90B`，管理層直接把 AI 記憶體供需緊張寫進展望。[TSMC 4Q25](https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/3e49621566a3ca53bdf8aee2586929b666c17fd6/4Q25EarningsRelease.pdf) [TSMC U.S. expansion](https://pr.tsmc.com/system/files/newspdf/attachment/1f3cfb45dd5b56cf948833fb01a6c5c5c240a63f/TSMC%20Intends%20to%20Expand%20Its%20Investment%20in%20the%20United%20States%20to%20US%24165%20Billion%20to%20Power%20the%20Future%20of%20AI_FINAL_%28E%29_wmn.pdf) [Micron FY26 Q2](https://investors.micron.com/news-releases/news-release-details/micron-technology-inc-reports-results-second-quarter-fiscal-2026)
- `市場敘事`：下一階段 AI 競爭會卡在 `packaging + HBM + power`，不只是在 compute die。
- `判斷`：這個敘事高度可信，因此 `TSM` 和 `MU` 的戰略地位比很多人想像得更高。

## Comparison Table

| 公司 | 商業品質 | 競爭位置 | 韌性 | 估值位置 | 近期敘事解讀 | 結論 |
| --- | --- | --- | --- | --- | --- | --- |
| `TSM` | 很強 | 很強 | 很強 | 合理 | AI 幾乎全產業收租者，先進製程與封裝壁壘極高，但有地緣風險 | `綜合首選` |
| `NVDA` | 很強 | 很強 | 很強 | 偏貴但未失真 | 全棧 AI factory 定義者，平台優勢最強 | `生意最強` |
| `AVGO` | 很強 | 強 | 很強 | 大致合理 | custom ASIC 與 networking 正在變成第二主線贏家 | `第二梯隊前排` |
| `AMD` | 強 | 中上 | 強 | 偏合理 | 第二供應商敘事變強，但仍受軟體與 export control 牽制 | `可進可退的追趕者` |
| `MU` | 強 | 中上 | 中 | 不算貴 | AI 記憶體極強，但仍是資本密集且循環性更高的生意 | `高彈性但波動大` |
| `MRVL` | 中上 | 中上 | 中 | 不便宜 | AI connectivity 故事成立，但 execution 與整合風險較高 | `有潛力但不首選` |

補充市場快照：

- `NVDA`：股價約 `182.10`，市值約 `4.43T`，Forward `P/E` 約 `22.21x`。[StockAnalysis](https://stockanalysis.com/stocks/nvda/)
- `AMD`：股價約 `201.64`，市值約 `328.76B`，Forward `P/E` 約 `30.70x`。[StockAnalysis](https://stockanalysis.com/stocks/amd/)
- `AVGO`：股價約 `341.57`，市值約 `1.62T`，企業價值約 `1.67T`，Forward `P/E` 約 `25.60x`。[StockAnalysis](https://stockanalysis.com/stocks/avgo/statistics/)
- `MRVL`：股價約 `90.44`，市值約 `78.79B`，企業價值約 `81.82B`，Forward `P/E` 約 `23.70x`。[StockAnalysis](https://stockanalysis.com/stocks/mrvl/)
- `TSM`：股價約 `354.56`，市值約 `1.58T`，企業價值約 `1.52T`，Forward `P/E` 約 `24.71x`。[StockAnalysis](https://stockanalysis.com/stocks/tsm/)
- `MU`：股價約 `418.69`，市值約 `471.24B`，企業價值約 `471.72B`，Forward `P/E` 約 `9.91x`。[StockAnalysis](https://stockanalysis.com/stocks/mu/)

## Top Tier And Why

### 1. `TSM`

- `事實`：TSMC 不只是先進製程代工，而是 AI 晶片量產與先進封裝的實際 bottleneck 持有者。
- `事實`：公司已把美國投資計畫擴到 `US$165B`，並明確把 AI 客戶需求作為核心支撐之一。
- `判斷`：如果你不想押單一 GPU 架構勝負，而是想押整個 AI 晶片產業持續擴張，`TSM` 是最乾淨的收租標的。

### 2. `NVDA`

- `事實`：FY2026 revenue `215.9B`、Q4 Data Center revenue `62.3B`，規模與利潤率都遠超同業。
- `事實`：Rubin、Dynamo、DSX、NVLink、BlueField、Spectrum 等布局說明它正在把 GPU 優勢擴成資料中心作業系統與架構標準。
- `判斷`：若只論產業權力，`NVDA` 仍然第一。但它是最被市場關注、也是敘事最擁擠的一檔。

### 3. `AVGO`

- `事實`：Q1 FY2026 revenue `19.3B`，AI semiconductor revenue `8.4B`，Q2 指引 AI semiconductor revenue `10.7B`。
- `事實`：Broadcom 已經不是只有 networking，而是 hyperscaler custom XPU / switching / optical 的核心受益者。
- `判斷`：它是目前最像「NVDA 之外，真正吃到 hyperscaler AI capex 的大市值高品質公司」。

## Winner Or Preferred Shortlist

### 我的排序

1. `TSM`
2. `NVDA`
3. `AVGO`
4. `AMD`
5. `MU`
6. `MRVL`

### 為什麼 `TSM` 是綜合首選

如果只問「AI 晶片裡最強的公司是誰」，答案仍然偏向 `NVDA`。  
但如果問「這個產業裡最值得作為單一首選標的的是誰」，我會選 `TSM`，理由是：

- 它吃到 `NVDA / AMD / AVGO / MRVL` 乃至其他 custom ASIC 的共同成長。
- 它的勝負不需要建立在單一架構贏家必須一直是同一家。
- 它同時握有先進製程與 advanced packaging 的實體瓶頸。
- 以目前 forward valuation 看，並沒有比 `NVDA` 或 `AVGO` 明顯更貴。

如果你要我給 `1-3` 家 shortlist，我會給：

- `TSM`
- `NVDA`
- `AVGO`

## Main Reasons The Leading Idea Could Be Wrong

1. `TSM` 的最大風險不是基本面，而是 `台海與地緣政治`，這個風險不能被財務模型完全吸收。
2. 如果 AI 基礎設施的經濟租繼續向軟硬體全棧集中，而不是向製造端擴散，`NVDA` 可能仍會跑贏 `TSM`。
3. `AVGO` 的 AI 故事有一部分建立在 hyperscaler custom silicon 需求持續外溢，若 capex 結構改變，估值擴張可能停滯。
4. `AMD` 若在 MI 系列與 open rack-scale 方案上持續突破，現在的排名可能偏低。
5. `MU` 若 HBM 緊張周期延長，它的盈利彈性可能讓它成為報酬率黑馬，但波動也會最大。

## Next Step For Deep Research

- 第一優先：用 [`company-valuation-analyst`](/Users/anthony/Git/realanthonyc/Research-Reports/Skills/research-skills/company-valuation-analyst/SKILL.md) 深挖 `TSM`
- 問題重點：
- advanced packaging / CoWoS 收益佔比未來兩年如何體現到每股價值
- 美國擴產對回報率與資本支出的稀釋效應多大
- 在合理地緣折價下，現價是否仍低於 base-case fair value

- 第二優先：對 `NVDA` 做估值
- 問題重點：
- Rubin / Blackwell / Dynamo 對推論經濟學的提升，到底能維持多久的超額毛利
- custom ASIC 擴張會分走多少系統價值

- 第三優先：對 `AVGO` 做估值
- 問題重點：
- custom AI ASIC 的營收可持續性
- software + semiconductor 混合結構是否應享更高估值

## Sources

- [NVIDIA FY2026 Q4 results](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Fourth-Quarter-and-Fiscal-2026/)
- [NVIDIA Rubin platform](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Vera-Rubin-Opens-Agentic-AI-Frontier/default.aspx)
- [NVIDIA Dynamo](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Enters-Production-With-Dynamo-the-Broadly-Adopted-Inference-Operating-System-for-AI-Factories/default.aspx)
- [AMD FY2025 Q4 results](https://ir.amd.com/news-events/press-releases/detail/1276/amd-reports-fourth-quarter-and-full-year-2025-financial-results)
- [AMD CES 2026 AI portfolio](https://ir.amd.com/news-events/press-releases/detail/1272/amd-and-its-partners-share-their-vision-for-ai-everywhere-for-everyone-at-ces-2026)
- [AMD-Meta 6GW agreement](https://ir.amd.com/news-events/press-releases/detail/1279/amd-and-meta-announce-expanded-strategic-partnership-to-deploy-6-gigawatts-of-amd-gpus)
- [Broadcom FY2026 Q1 results](https://www.prnewswire.com/news-releases/broadcom-inc-announces-first-quarter-fiscal-year-2026-financial-results-and-quarterly-dividend-302704490.html)
- [Broadcom investor center news](https://investors.broadcom.com/financial-information/financial-news-releases)
- [Marvell FY2026 Q4 results](https://investor.marvell.com/news-events/press-releases/detail/1011/marvell-technology-inc-reports-fourth-quarter-and-fiscal-year-2026-financial-results)
- [Marvell completes Celestial AI acquisition](https://investor.marvell.com/news-events/press-releases/detail/1005/marvell-completes-acquisition-of-celestial-ai)
- [NVIDIA-Marvell NVLink Fusion partnership](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-AI-Ecosystem-Expands-as-Marvell-Joins-Forces-Through-NVLink-Fusion/default.aspx)
- [TSMC 4Q25 results](https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/3e49621566a3ca53bdf8aee2586929b666c17fd6/4Q25EarningsRelease.pdf)
- [TSMC U.S. expansion](https://pr.tsmc.com/system/files/newspdf/attachment/1f3cfb45dd5b56cf948833fb01a6c5c5c240a63f/TSMC%20Intends%20to%20Expand%20Its%20Investment%20in%20the%20United%20States%20to%20US%24165%20Billion%20to%20Power%20the%20Future%20of%20AI_FINAL_%28E%29_wmn.pdf)
- [Micron FY2026 Q2 results](https://investors.micron.com/news-releases/news-release-details/micron-technology-inc-reports-results-second-quarter-fiscal-2026)
- [NVDA market snapshot](https://stockanalysis.com/stocks/nvda/)
- [AMD market snapshot](https://stockanalysis.com/stocks/amd/)
- [AVGO market snapshot](https://stockanalysis.com/stocks/avgo/statistics/)
- [MRVL market snapshot](https://stockanalysis.com/stocks/mrvl/)
- [TSM market snapshot](https://stockanalysis.com/stocks/tsm/)
- [MU market snapshot](https://stockanalysis.com/stocks/mu/)
