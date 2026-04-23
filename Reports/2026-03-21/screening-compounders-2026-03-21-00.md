---
title: "Screening Compounders: healthcare + biotech + medicine"
date: 2026-03-21
report_type: compounder-screen
source_skill: screening-compounders
folder: Reports/2026-03-21
language: zh-TW
tags:
  - reports
  - Reports/2026-03-21
  - skills/screening-compounders
  - research-flow/screening
  - investing/compounders
aliases:
  - "Screening Compounders: healthcare + biotech + medicine"
  - screening-compounders-2026-03-21-00
  - "Screening Compounders: healthcare + biotech + medicine - 2026-03-21"
related:
  - "[[research-workflow]]"
  - "[[screening-compounders]]"
---

# Screening Compounders: healthcare + biotech + medicine

分析日期：2026-03-21（Asia/Tokyo）  
研究範圍：美股上市、成熟醫療/醫藥/醫療設備/生命科學與部分 biotech 名單  
方法：嚴格套用 [`$screening-compounders`](/Users/anthony/Git/realanthonyc/Research-Reports/Skills/research-skills/screening-compounders/SKILL.md) 流程；若資料不足以用同一口徑重建 10 年 EBIT-based ROCE，寧可不硬塞進最終名單。

## 研究範圍與篩選宇宙

這次我把「healthcare + biotech + medicine」先收斂成 9 檔較具代表性的美股：

| 公司 | Ticker | 類型 | 納入原因 |
|---|---:|---|---|
| Johnson & Johnson | JNJ | 多元醫療/藥品/醫材 | 醫療龍頭、長期持有常見候選 |
| Merck | MRK | 大型藥廠 | 現金流強、Keytruda 壟斷敘事強 |
| Zoetis | ZTS | 動物醫療 | 高毛利、高現金流、行業結構佳 |
| IDEXX Laboratories | IDXX | 診斷/動物健康 | 高黏著、高 ROCE 類型 |
| ResMed | RMD | 呼吸睡眠醫材 | 結構性需求、軟硬體組合 |
| Intuitive Surgical | ISRG | 手術機器人 | 護城河強、但資本效率需驗證 |
| Stryker | SYK | 骨科/醫療設備 | 優質醫材龍頭，但併購頻繁 |
| Regeneron | REGN | 成熟 biotech | 高利潤，但仍屬管線驅動 |
| Vertex | VRTX | biotech | 稀有病藥王者，但集中度高 |

初步判斷：這個 cluster 的問題不是缺少好公司，而是大量候選公司一進入你的框架就會在兩個地方被殺掉：

1. `步驟 1`：純 biotech/管線驅動公司，未來贏家可預測性太差。  
2. `步驟 2`：大藥廠/多元醫療集團資產龐大，`ROCE = EBIT / (總資產 - 流動負債)` 這個口徑會把很多「好公司」打成不達標。

## 步驟 1：拒絕清單

### 一票否決結果

| 公司 | 結果 | 觸發項目 | 理由 | 資料來源 |
|---|---|---|---|---|
| JNJ | 通過 | 無 | 不是 turnaround、不是 serial acquirer、沒有明確控制人誠信崩壞證據 | 2024 年報、MacroTrends 財務頁 |
| MRK | 通過 | 無 | 大型藥廠，近年雖有收購但未達本次「連續大型併購成癮」標準 | 2024 年報、MacroTrends 財務頁 |
| ZTS | 通過 | 無 | 分拆後經營品質穩定，未見治理惡化到一票否決程度 | 2024 年報、MacroTrends 財務頁 |
| IDXX | 通過 | 無 | 沒有 turnaround 敘事，治理與商業模式相對乾淨 | 2024 年報、MacroTrends 財務頁 |
| RMD | 通過 | 無 | 不是困境反轉，也沒有明顯治理惡化 | 2024 年報、MacroTrends 財務頁 |
| ISRG | 通過 | 無 | 不靠大型併購維持成長，治理歷史乾淨 | 2024 年報、MacroTrends 財務頁 |
| SYK | 淘汰 | 4. 併購成癮 | Wright Medical、Vocera 等一連串較大交易使其更像優秀 roll-up，而不是內生複利股 | 公司公告、MacroTrends 財務頁 |
| REGN | 淘汰 | 5. 快速變化行業 | 即使已成熟，核心價值仍高度受藥物生命週期、臨床/監管與單品結構影響，對 10-20 年贏家可預測性仍偏弱 | 2024 年報、MacroTrends 公司描述 |
| VRTX | 淘汰 | 5. 快速變化行業 | 仍屬 pipeline/適應症推進驅動，且 CF franchise 集中度高 | 2024 年報、MacroTrends 公司描述 |

### 步驟 1 結論

- `淘汰`：`SYK`, `REGN`, `VRTX`
- `進入步驟 2`：`JNJ`, `MRK`, `ZTS`, `IDXX`, `RMD`, `ISRG`

## 步驟 2：ROCE 歷史篩選

公式：`ROCE = EBIT / (總資產 - 流動負債) × 100%`

本步驟的結論非常殘酷：真正明確通過的人不多。

### ROCE 摘要表

| 公司 | 可用年限 | 平均 ROCE | 穩定性 | 判定 |
|---|---:|---:|---|---|
| IDEXX | 2015-2024 | `53.4%` | 無連續 2 年大幅下滑 | 通過 |
| Zoetis | 2015-2024 | `19.7%` | 穩定，無連續 2 年大跌 | 邊界值；2016-2024 為 `20.9%`，條件式通過 |
| ResMed | 2016-2024 | `19.5%` | 穩定，無連續 2 年大跌 | 不通過，但列 watchlist |
| JNJ | 2015-2024 | `14.5%` | 穩定但偏低 | 淘汰 |
| MRK | 2015-2024 | `12.6%` | 2022→2023 崩落，波動大 | 淘汰 |
| ISRG | 2017-2024 | `14.9%` | 波動可接受，但均值不足 | 淘汰 |

### 年度 ROCE 與計算結果

#### IDEXX

- 2024: `1128 / (3293 - 1068) = 50.7%`
- 2023: `1097 / (3260 - 952) = 47.5%`
- 2022: `899 / (2747 - 1236) = 59.5%`
- 2021: `932 / (2437 - 764) = 55.7%`
- 2020: `695 / (2295 - 583) = 40.6%`
- 2019: `553 / (1832 - 725) = 50.0%`
- 2018: `491 / (1537 - 770) = 64.0%`
- 2017: `413 / (1713 - 1005) = 58.3%`
- 2016: `350 / (1531 - 935) = 58.7%`
- 2015: `300 / (1475 - 857) = 48.5%`
- `10 年平均 = 53.4%`
- 判定：`明確通過`

#### Zoetis

- 2024: `3133 / (14237 - 3412) = 28.9%`
- 2023: `2936 / (14286 - 1889) = 23.7%`
- 2022: `2656 / (14925 - 3167) = 22.6%`
- 2021: `2488 / (13900 - 1797) = 20.6%`
- 2020: `1996 / (13609 - 2170) = 17.4%`
- 2019: `1801 / (11545 - 1806) = 18.5%`
- 2018: `1690 / (10777 - 1223) = 17.7%`
- 2017: `1525 / (8586 - 1094) = 20.4%`
- 2016: `1228 / (7649 - 1117) = 18.8%`
- 2015: `545 / (7913 - 1781) = 8.9%`
- `10 年平均 = 19.7%`
- 說明：若把分拆後仍在磨合的 2015 視為結構轉換年，`2016-2024 平均 = 20.9%`
- 判定：`條件式通過`

#### ResMed

- 2024: `1320 / (6872 - 911) = 22.1%`
- 2023: `1132 / (6752 - 759) = 18.9%`
- 2022: `1000 / (5096 - 689) = 22.7%`
- 2021: `904 / (4728 - 912) = 23.7%`
- 2020: `810 / (4587 - 603) = 20.3%`
- 2019: `579 / (4108 - 556) = 16.3%`
- 2018: `542 / (3064 - 511) = 21.2%`
- 2017: `426 / (3468 - 360) = 13.7%`
- 2016: `429 / (3257 - 638) = 16.4%`
- `9 年平均 = 19.5%`
- 判定：`接近但未過線`

#### Johnson & Johnson

- 2024: `16687 / (180104 - 50321) = 12.9%`
- 2023: `15062 / (167558 - 46282) = 12.4%`
- 2022: `19359 / (187378 - 55802) = 14.7%`
- 2021: `19178 / (182018 - 45226) = 14.0%`
- 2020: `16497 / (174894 - 42493) = 12.5%`
- 2019: `17328 / (157728 - 35964) = 14.2%`
- 2018: `17999 / (152954 - 31230) = 14.8%`
- 2017: `17673 / (157303 - 30537) = 13.9%`
- 2016: `19803 / (141208 - 26287) = 17.2%`
- 2015: `19196 / (133411 - 27747) = 18.2%`
- `10 年平均 = 14.5%`
- 判定：`淘汰`

#### Merck

- 2024: `20221 / (117106 - 28420) = 22.8%`
- 2023: `2954 / (106675 - 25694) = 3.6%`
- 2022: `18282 / (109160 - 24239) = 21.5%`
- 2021: `13199 / (105694 - 23872) = 16.1%`
- 2020: `5548 / (91588 - 27327) = 8.6%`
- 2019: `7926 / (84397 - 22220) = 12.7%`
- 2018: `8931 / (82637 - 22206) = 14.8%`
- 2017: `6797 / (87872 - 18614) = 9.8%`
- 2016: `5499 / (95377 - 17204) = 7.0%`
- 2015: `7547 / (101677 - 19201) = 9.2%`
- `10 年平均 = 12.6%`
- 判定：`淘汰`

#### Intuitive Surgical

- 2024: `2349 / (18743 - 1745) = 13.8%`
- 2023: `1767 / (15442 - 1659) = 12.8%`
- 2022: `1577 / (12974 - 1422) = 13.7%`
- 2021: `1821 / (13555 - 1150) = 14.7%`
- 2020: `1050 / (11169 - 965) = 10.3%`
- 2019: `1375 / (9733 - 1030) = 15.8%`
- 2018: `1199 / (7847 - 821) = 17.1%`
- 2017: `1063 / (5777 - 663) = 20.8%`
- `8 年平均 = 14.9%`
- 判定：`淘汰`

### 步驟 2 結論

- `明確通過`：`IDXX`
- `條件式通過`：`ZTS`
- `近乎通過但仍未達標`：`RMD`
- `淘汰`：`JNJ`, `MRK`, `ISRG`

## 步驟 3：財務極度穩健性檢查

我只對 `IDXX`、`ZTS`、`RMD` 做，因為其他公司已在步驟 2 出局。

| 公司 | 淨現金 | FCF 持續正向 | 客戶/供應商分散 | 業務集中度低 | 現金轉換/營運資金結構 | 結論 |
|---|---|---|---|---|---|---|
| IDXX | 失敗 | 通過 | 通過 | 通過 | 通過 | `4/5` 通過 |
| ZTS | 失敗 | 通過 | 通過 | 通過 | 通過 | `4/5` 通過 |
| RMD | 失敗 | 通過 | 通過 | 通過 | 通過 | `4/5` 通過 |

### 補充說明

#### IDEXX

- `淨現金`：不通過。公司現金部位不差，但不是幾乎零淨債務型。
- `FCF`：通過。歷史現金流與回購能力很強。
- `客戶/供應商分散`：通過。面向廣泛獸醫院所與診所。
- `業務集中度低`：通過。核心在 companion animal diagnostics，但內含檢測儀器、耗材、軟體、服務，黏著度高。
- `現金轉換`：通過。試劑/耗材/檢測服務組合使現金轉換結構優秀。

#### Zoetis

- `淨現金`：不通過。現金不大於長期負債。
- `FCF`：通過。動物醫療屬高毛利現金牛。
- `客戶/供應商分散`：通過。面向全球獸醫、養殖、寵物醫療渠道。
- `業務集中度低`：通過。寵物與 livestock、藥品/疫苗/診斷多支柱。
- `現金轉換`：通過。營運資金需求可控。

#### ResMed

- `淨現金`：不通過。2024 年現金約 `2.38 億美元`，長期債務約 `6.97 億美元`。
- `FCF`：通過。FCF/股長期為正。
- `客戶/供應商分散`：通過。全球呼吸與睡眠照護市場廣泛。
- `業務集中度低`：通過。硬體、面罩、SaaS 組合比單一設備公司更穩。
- `現金轉換`：通過。耗材與面罩補充具重複性。

## 步驟 4：趨同進化商業模式驗證

| 公司 | 商業模式 | 外部成功劇本 | 是否通過 |
|---|---|---|---|
| IDEXX | 儀器 + 耗材 + 軟體 + 檢測服務的封閉生態 | 類似 Roche Diagnostics、Danaher 旗下高黏著工具型模式；贏家吃大部分市場且現金流厚 | 通過 |
| ZTS | 動物醫療品牌藥 + 疫苗 + 診斷 | 類似成熟製藥 + 伴侶動物健康的全球寡占格局；全球多地反覆被驗證 | 通過 |
| RMD | 醫療硬體 + 面罩耗材 + SaaS/資料 | 與呼吸照護/慢性病管理的「裝機量帶耗材與服務」劇本一致 | 通過，但沒有 IDXX / ZTS 那麼強 |

這一步對純 biotech 最不友善。因為 biotech 常常不是「劇本被反覆驗證」，而是「單一藥物/平台是否持續贏」；這太依賴預測，不符合你的框架。

## 步驟 5：三個達爾文心法交叉驗證

### 1. 只看終極原因

- `IDXX`：真正驅動價值的是 installed base、檢測耗材、軟體工作流黏著，而不是單季新品或短期政策。
- `ZTS`：真正驅動價值的是全球寵物醫療滲透、品牌/渠道/產品組合，而不是單一季度寵物需求波動。
- `RMD`：真正驅動價值的是慢性病/睡眠呼吸障礙長期需求與耗材補充，而不是某一季裝機節奏。

### 2. 只看歷史事實

- `IDXX`：10 年 ROCE `53.4%`，這不是故事，是結果。
- `ZTS`：原始 10 年平均 `19.7%`，若看成熟期 2016-2024 則 `20.9%`，證據比敘事重要。
- `RMD`：9 年平均 `19.5%`，很接近，但你的標準不是「接近」。

### 3. 只相信累贅原則誠實信號

- `IDXX`：高 ROCE + 回購 + 產品/軟體黏著，是昂貴但誠實的信號。
- `ZTS`：長期穩定高毛利、高現金流與分紅/回購，屬誠實信號。
- `RMD`：經營品質好，但 ROCE 沒有高到足以讓我放寬標準。

## 步驟 6：綜合評分與排名

我只對 `IDXX` 與 `ZTS` 給正式分數；`RMD` 保留在 watchlist。

| 排名 | 公司 | 總分 / 10 | ROCE | 財務穩健 | 護城河/趨同進化 | 資本配置/股東一致性 | 估值脈絡 | 結論 |
|---:|---|---:|---:|---:|---:|---:|---:|---|
| 1 | IDEXX | `9.2` | 4.0 | 1.8 | 2.0 | 0.8 | 0.6 | 明確通過，質地極強，但價格不便宜 |
| 2 | Zoetis | `8.1` | 3.3 | 1.7 | 1.8 | 0.8 | 0.5 | 條件式通過，屬動物醫療寡占複利股 |
| - | ResMed | `7.4` | 3.0 | 1.6 | 1.5 | 0.8 | 0.5 | watchlist，不進最終清單 |

## 最終候選清單

### 1. IDEXX Laboratories (`IDXX`)

- `當前股價參考`：`$624.30`（GuruFocus，2026-03-05 盤中/文中價格）
- `估值脈絡`：MacroTrends 顯示其近年屬高估值醫療工具龍頭，`PE 約 53x` 水平；從商業品質看合理，但不是便宜。
- `護城河`：
  - 獸醫診斷設備 installed base
  - 耗材與檢測服務反覆消耗
  - 軟體工作流深度嵌入診所流程
  - 轉換成本高
- `為何長期保持偉大`：
  - 不是靠單一藥物，而是靠系統性工作流鎖定
  - 10 年 ROCE 極端優秀，顯示商業模式不是偶然
  - 趨同進化上，這是典型「儀器 + 耗材 + 軟體」高黏著好生意
- `我對估值的結論`：好公司，但不是撿煙屁股；更像是「等回檔買品質」。

### 2. Zoetis (`ZTS`)

- `當前股價參考`：`$126.55`（Yahoo Finance 德文站，2026-02-09 夜盤/盤後顯示）
- `估值脈絡`：
  - MacroTrends 顯示 2016-2022 多在 `30x-55x` P/E 區間
  - 以 2026 年初約 `126-127` 美元股價與 2025 指引 EPS `6.00-6.10` 粗估，市場給的倍數大約已掉到 `21x` 左右
  - 也就是說，現在的估值比它過去多數年份寬鬆不少
- `護城河`：
  - 全球動物醫療品牌、渠道與醫生習慣
  - companion animal 與 livestock 雙輪
  - 藥品/疫苗/診斷組合使競爭沒有那麼單點
- `為何長期保持偉大`：
  - 動物醫療的結構比人類 biotech 更可預測
  - 分散化比單藥 biotech 好得多
  - 2016-2024 的成熟期 ROCE 已經符合你的 20% 標準
- `我對估值的結論`：在本次清單裡，它反而是「品質不差，但估值沒有那麼誇張」的相對平衡選項。

## 主要風險與不確定性

1. 這個框架對醫療大藥廠非常苛刻。`JNJ`、`MRK` 不是壞公司，只是用這個 `ROCE` 口徑不夠漂亮。
2. `ZTS` 的通過帶有一個明確判斷：我把 2015 分拆後轉型年視為失真點；若你要求絕對機械化，`ZTS` 應該列為未達標。
3. `IDXX` 的最大風險不是商業模式，而是估值。
4. `RMD` 很接近，但嚴格說仍未達標；如果你願意把門檻從 `20%` 放寬到 `18%-19%`，它會重新進入名單。
5. 純 biotech 在這套框架下先天吃虧。這不是說它們不能漲，而是它們更像預測遊戲，不是「不用預測也能長抱」。

## 資料來源

### 候選與財務歷史

- Johnson & Johnson total assets: <https://www.macrotrends.net/stocks/charts/JNJ/johnson-johnson/total-assets>
- Johnson & Johnson operating income: <https://www.macrotrends.net/stocks/charts/JNJ/johnson-johnson/operating-income>
- Johnson & Johnson total current liabilities: <https://www.macrotrends.net/stocks/charts/JNJ/johnson-johnson/total-current-liabilities>
- Merck total assets: <https://www.macrotrends.net/stocks/charts/MRK/merck/total-assets>
- Merck operating income: <https://www.macrotrends.net/stocks/charts/MRK/merck/operating-income>
- Merck total current liabilities: <https://www.macrotrends.net/stocks/charts/MRK/merck/total-current-liabilities>
- Zoetis total assets: <https://www.macrotrends.net/stocks/charts/ZTS/zoetis/total-assets>
- Zoetis operating income: <https://www.macrotrends.net/stocks/charts/ZTS/zoetis/operating-income>
- Zoetis total current liabilities: <https://www.macrotrends.net/stocks/charts/ZTS/zoetis/total-current-liabilities>
- IDEXX total assets: <https://www.macrotrends.net/stocks/charts/IDXX/idexx-laboratories/total-assets>
- IDEXX operating income: <https://www.macrotrends.net/stocks/charts/IDXX/idexx-laboratories/operating-income>
- IDEXX total current liabilities: <https://www.macrotrends.net/stocks/charts/IDXX/idexx-laboratories/total-current-liabilities>
- ResMed total assets: <https://www.macrotrends.net/stocks/charts/RMD/resmed/total-assets>
- ResMed operating income: <https://www.macrotrends.net/stocks/charts/RMD/resmed/operating-income>
- ResMed total current liabilities: <https://www.macrotrends.net/stocks/charts/RMD/resmed/total-current-liabilities>
- Intuitive Surgical total assets: <https://www.macrotrends.net/stocks/charts/ISRG/intuitive-surgical/total-assets>
- Intuitive Surgical operating income: <https://www.macrotrends.net/stocks/charts/ISRG/intuitive-surgical/operating-income>
- Intuitive Surgical total current liabilities: <https://www.macrotrends.net/stocks/charts/ISRG/intuitive-surgical/total-current-liabilities>

### 財務穩健與估值

- Zoetis P/E history: <https://www.macrotrends.net/stocks/charts/ZTS/ZTS/pe-ratio>
- IDEXX P/E page: <https://www.macrotrends.net/stocks/charts/IDXX/IDXX/pe-ratio>
- ResMed cash on hand: <https://www.macrotrends.net/stocks/charts/RMD/resmed/cash-on-hand>
- ResMed long-term debt: <https://www.macrotrends.net/stocks/charts/RMD/resmed/long-term-debt>
- ResMed free cash flow per share: <https://www.macrotrends.net/stocks/charts/RMD/resmed/free-cash-flow-per-share>
- Zoetis quote page (price reference): <https://de.finance.yahoo.com/quote/ZTS/>
- IDEXX price reference: <https://www.gurufocus.com/news/8681858/idexx-laboratories-inc-idxx-shares-down-376-on-mar-5>
- Zoetis 2025 guidance context: <https://www.investors.com/news/technology/zoetis-stock-zoetis-earnings-q4-2024/>

### 方法與限制

- 本報告優先使用 MacroTrends 的多年歷史財務表來維持口徑一致，再輔以公司年報與即時報價頁補 valuation context。
- 若某家公司無法在同一來源系統下重建一致的 `EBIT / 總資產 / 流動負債` 長序列，我寧可不把它硬塞進最終名單。

非投資建議。
