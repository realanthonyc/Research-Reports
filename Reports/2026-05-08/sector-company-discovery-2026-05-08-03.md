---
title: CPU 公司篩選報告
date: 2026-05-08
report_type: sector-company-discovery
source_skill: sector-company-discovery
folder: reports/2026-05-08
language: zh-TW
tags:
  - reports
  - reports/2026-05-08
  - Skills/research-skills/sector-company-discovery
  - research-flow/screening
  - investing/equities

aliases:
  - sector-company-discovery-2026-05-08-03
  - CPU 公司篩選 2026-05-08
related:
  - "[[Research Flow]]"
  - "[[sector-company-discovery]]"
---

## Search scope

- 主題：CPU 與 CPU-centered compute，包括 server CPU、PC CPU、Arm CPU IP、AI server CPU、製造與平台生態。
- 地理：全球公開公司，以美股或 ADR 可投資公司為主。
- 篩選條件：收入規模、技術 roadmap、資料中心 exposure、毛利與資本效率、供應鏈可得性。
- 分析日期：2026-05-08。
- 優化目標：找出 CPU 主題中最值得深研的 1-3 家公司；避免把 GPU/AI accelerator 故事誤當 CPU 投資邏輯。

## Candidate set

| 公司 | 代號 | 納入理由 |
|---|---:|---|
| AMD | AMD | EPYC server CPU 與 Ryzen client CPU 份額持續提升，AI server 也提高 CPU attach value。 |
| Intel | INTC | x86 incumbent，Client/Datacenter/Foundry 都重要，但 turnaround 與製造風險高。 |
| Arm Holdings | ARM | CPU IP 標準，smartphone、edge、cloud AI 與 data center royalty exposure；正向自有 AI server CPU 延伸。 |
| NVIDIA | NVDA | GPU 為主，但 Grace/Arm CPU 與 rack-scale AI platform 改變 server CPU 價值鏈。 |
| Qualcomm | QCOM | Snapdragon PC、edge AI、automotive 與 Arm-based compute；手機仍是主體。 |
| TSMC | TSM | CPU/AI CPU 製造瓶頸與先進製程核心，非 CPU 設計公司但價值鏈地位不可忽略。 |
| Apple | AAPL | 自研 Arm CPU 最強之一，但 CPU 並非可分拆投資主題，作排除/參考。 |

## What matters in this industry

1. Data center CPU share：AI infrastructure 仍需要 host CPU、memory bandwidth、networking 與 rack-level integration。
2. 架構遷移：x86、Arm、custom silicon 的份額變化比單代產品跑分更重要。
3. 製程與封裝取得：TSMC 3nm/5nm/CoWoS/advanced packaging 供應會限制 AMD、Arm、NVIDIA、Qualcomm 的交付。
4. Gross margin 與 operating leverage：CPU 是高 R&D、高固定成本行業，份額變動會放大利潤。
5. PC 市場週期：client CPU 仍受換機、記憶體價格與 OEM 庫存影響。
6. 估值：CPU 受 AI 敘事重估，但多數公司其實混合 GPU、IP、foundry、手機與汽車業務，不可用單一倍數粗估。

## Recent topics and narratives

- 事實：AMD 2026 Q1 營收 102.53 億美元，年增 38%；Data Center segment revenue 57.75 億美元，年增 57%，由 EPYC CPU 與 Instinct GPU 出貨帶動；free cash flow 25.66 億美元。[AMD Q1 2026](https://www.amd.com/en/newsroom/press-releases/2026-5-5-amd-reports-first-quarter-2026-financial-results.html)
- 事實：Arm FY2026 Q4 revenue 14.9 億美元，FY2026 revenue 49.2 億美元；full-year royalty revenue 26.1 億美元，data center royalties 年增逾一倍。[Arm FY2026](https://newsroom.arm.com/news/arm-q4-fye26-results)
- 事實：NVIDIA FY2026 revenue 2,159.38 億美元，Data Center full-year revenue 1,937 億美元；Q4 Data Center revenue 623 億美元。公司同時推進 Vera Rubin、Grace/Arm CPU 與 AI rack platform。[NVIDIA FY2026](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-Fourth-Quarter-and-Fiscal-2026/)
- 事實：TSMC 2026 Q1 revenue 359 億美元，HPC 占 61%，3nm/5nm/7nm 合計 74% wafer revenue；Q2 guidance revenue 390-402 億美元、gross margin 65.5%-67.5%。[TSMC Q1 2026](https://investor.tsmc.com/english/quarterly-results/2026/q1)
- 事實：Intel 已公布 2026 Q1 results，但投資重點仍是 client/data center share、foundry losses、製程節點執行與新管理層 turnaround。[Intel Q1 2026](https://newsroom.intel.com/corporate/intel-reports-first-quarter-2026-financial-results)
- 市場敘事：AI 讓 GPU 成為核心，但 CPU 沒有消失；相反，AI data center 對 host CPU、memory coherent architecture 與 rack-scale platform 的需求提高。最大分歧在於誰拿到 incremental CPU profit pool：AMD、Arm ecosystem、NVIDIA platform，還是 Intel 反攻。

## Comparison table

| 公司 | CPU exposure 純度 | 業務品質 | 成長耐久性 | 財務/毛利 | 估值判斷 | 主要風險 | 綜合判斷 |
|---|---|---|---|---|---|---|---|
| AMD | 高，server/client CPU 核心 | 高 | 很高，EPYC share + AI attach | 改善中，FCF 強 | AI/CPU 成長已部分反映 | GPU 競爭、TSMC 供應、PC 成本 | 第一梯隊 |
| ARM | 很高，CPU IP | 很高，asset-light | 高，data center/edge royalties | 高 margin | 估值昂貴 | 客戶自研、royalty mix | 第一梯隊但估值敏感 |
| NVDA | 中，CPU 是平台一部分 | 極高 | 很高 | 極高 | AI 龍頭溢價 | GPU cycle、China、供應 | 非純 CPU 但平台勝者 |
| TSM | 間接但關鍵 | 極高 | 很高 | 極高 | 品質溢價 | 地緣、capex、客戶集中 | 供應鏈首選 |
| INTC | 很高 | 低至中，turnaround | 不確定 | 壓力大 | 便宜但價值陷阱風險 | 製程、foundry、份額流失 | 逆向候選 |
| QCOM | 中，PC/edge Arm CPU | 高 | 中高 | 高 | 手機週期折價 | 手機、PC adoption | 衛星候選 |
| AAPL | 間接 | 極高 | 中 | 高 | 非 CPU 主題 | 消費週期 | 排除 |

## Top tier and why

第一梯隊：AMD、Arm、TSMC；若允許 CPU platform 而非純 CPU，NVIDIA 也在第一梯隊。

AMD 是最直接的 server CPU share gain 標的。Q1 2026 Data Center 57% 年增，說明 EPYC 與 AI infrastructure demand 已同時推動營收。AMD 的風險是投資人往往用 GPU 願景定價，而 CPU 本身雖好，可能不足以支撐過高估值。

Arm 是 CPU 架構層最純的資產，royalty 模型資本效率高，data center royalties 翻倍顯示 cloud/AI CPU 的份額敘事正在落地。問題是估值通常提前反映很長時間的成長。

TSMC 不是 CPU 公司，但 CPU/AI chip 贏家幾乎都依賴其先進製程與封裝。若想投資整個 CPU/AI compute supply chain 而非押單一設計公司，TSMC 是最穩健的標的。

## Winner or preferred shortlist

首選：AMD。

理由：如果主題限定為 CPU，AMD 的可比性最好：server CPU、client CPU、AI platform CPU attach 和財務成長都在同一家公司內反映。Arm 更像架構 royalty，TSMC 更像製造瓶頸，NVIDIA 更像 AI platform。

Preferred shortlist：

1. AMD：CPU 主題首選。
2. Arm：CPU IP 與架構遷移首選，但等估值安全邊際。
3. TSMC：若想避開 CPU 設計勝負，買製程/封裝瓶頸。

## Main reasons the leading idea could be wrong

- AMD data center growth 中有 GPU/accelerator 成分，若把全部增長歸因於 CPU，會高估 EPYC 的獨立價值。
- Intel 若在製程、封裝或 pricing 上更積極反攻，server CPU margin 可能承壓。
- Arm 自有 AI server CPU 若與客戶利益衝突，可能傷害部分 IP 客戶關係。
- TSMC 供應限制、地緣風險或先進節點 capex 回報下降，會影響整個 CPU supply chain。

## Next step for deep research

建議用 `company-valuation-analyst` 深研 AMD，並建立 Arm/TSMC 相對情境。

待解問題：

- AMD Data Center segment 中 EPYC CPU、Instinct GPU、DPU/FPGA 的收入與 margin 拆分。
- AMD server CPU share 到 2030 的合理上限，以及每 1ppt share 對 EPS/FCF 的增量。
- Arm data center royalty doubling 的基期、客戶集中度與 AGI CPU 對 IP 模式的長期影響。
