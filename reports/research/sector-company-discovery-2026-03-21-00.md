# 醫療防守型 Compounders 篩選備忘錄

分析日期：2026-03-21  
候選名單：`IDEX`、`ZTS`、`JNJ`、`MRK`、`RMD`、`ResMed`、`JNJ`

## Search Scope

- `範圍`：以使用者提供的美股候選名單為主，目標是找出最值得深挖的防守型醫療 / 健康照護 compounder。
- `地理`：美國上市公司。
- `優化目標`：不是單看便宜，而是綜合比較 `商業品質`、`成長耐久性`、`資產負債表韌性`、`近期敘事是否被基本面支持`、以及 `估值是否仍合理`。
- `清理名單`：
  - `JNJ` 重複，去重後只保留一次。
  - `ResMed` 與 `RMD` 是同一家公司，去重後只保留 `RMD`。
  - `IDEX` 若按美股常用 ticker 理解，實際對應的是 `IDEX Corporation (IEX)`，屬工業公司而非純醫療股；因此保留為 `outlier` 參考，但不納入核心同業比較。

## Candidate Set

本次真正可比的核心組合是：

- `ZTS`：動物保健龍頭，偏高品質、穩定成長、現金流與產品週期都較乾淨。
- `JNJ`：大型綜合醫療平台，兼具藥品與醫材，防守性最強但結構較複雜。
- `MRK`：大型製藥龍頭，現金流強，但中期最核心問題是 `Keytruda` 依賴與專利時鐘。
- `RMD`：睡眠呼吸與居家醫療設備龍頭，帶裝置 + mask/耗材 + 軟體資料平台屬性。

保留但排除出主排名：

- `IDEX / IEX`：雖然有 `Health & Science Technologies` 部門，但本質仍是多元工業解決方案公司，終端市場與盈利框架和上面四家差異太大，不適合硬排在同一張 shortlist 裡。[IDEX profile](https://stockanalysis.com/stocks/iex/company/) [IDEX site](https://www.idexcorp.com/)

## What Matters In This Industry

這組公司不是同一條產品線，因此不能只用 `P/E` 或單一成長率硬排。這裡真正重要的是五件事：

1. `需求韌性`：產品是不是高必要性、低可選消費、能穿越景氣。
2. `護城河品質`：品牌、臨床地位、網路效應、通路、法規門檻、替換成本。
3. `成長耐久性`：未來 3-5 年成長靠的是可複製平台，還是單一 blockbuster / 單一療法。
4. `資本結構與現金流`：能不能自己供養成長、回購或併購，而不是被融資條件綁住。
5. `估值與敘事位置`：市場現在到底是在低估、合理定價，還是提前把太多好消息寫進股價。

## Recent Topics And Narratives

### 1. 醫療防守股重新被分層

- `事實`：`JNJ`、`MRK`、`ZTS`、`RMD` 最近的財報都還能交出成長，但市場給估值的方式明顯不同。
- `市場敘事`：資金不再把所有 defensive healthcare 一視同仁，而是更願意把高品質、低專利懸崖、低訴訟噪音、可持續成長的平台股拉開估值。
- `判斷`：這個敘事是被基本面支持的，不是純風格漂移。

### 2. 大藥廠的「專利時鐘」重新被市場計價

- `事實`：Merck 2025 全年營收 `65.0B`，其中 `KEYTRUDA / KEYTRUDA QLEX` 就有 `31.7B`，而 `GARDASIL / GARDASIL 9` 年減 `39%` 到 `5.2B`；2026 指引也偏保守。[Merck FY2025](https://www.merck.com/news/merck-highlights-progress-advancing-broad-diverse-pipeline/)
- `市場敘事`：MRK 便宜，是因為市場在折價 `Keytruda` 專利懸崖與中國 HPV 壓力，而不是沒看到現金流。
- `判斷`：這個折價邏輯是合理的，因此 MRK 的低估值不能直接等同高品質勝出。

### 3. 居家醫療與動物保健仍在吃結構性成長

- `事實`：ResMed FY2026 Q2 營收年增 `11%` 至 `1.4B`，毛利率提升到 `61.8%`，營運現金流 `340M`；Zoetis FY2025 營收 `9.5B`，2026 指引仍有 `3%-5%` organic operational growth，且長效 OA 疼痛產品 `Lenivia` 與 `Portela` 已在加拿大和歐盟獲批。[ResMed FY2026 Q2](https://investor.resmed.com/news-events/press-releases/detail/416/resmed-inc-announces-results-for-the-second-quarter-of-fiscal-year-2026) [Zoetis FY2025](https://investor.zoetis.com/news/news-details/2026/Zoetis-Reports-Fourth-Quarter-and-Full-Year-2025-Results/default.aspx)
- `市場敘事`：
  - `RMD`：市場已逐步接受 GLP-1 不會破壞 CPAP 長期需求，反而更關注診斷到治療的數位閉環與居家醫療滲透。
  - `ZTS`：市場重新把它當成高品質動物保健平台，而不是只看單季 OA mAb 雜訊。
- `判斷`：兩個敘事都大致被主文件支持，其中 `ZTS` 的可預測性比 `RMD` 更高。

## Comparison Table

| 公司 | 商業品質 | 成長耐久性 | 資產負債表 / 韌性 | 估值位置 | 近期敘事解讀 | 結論 |
| --- | --- | --- | --- | --- | --- | --- |
| `ZTS` | 很強 | 很強 | 很強 | 合理偏吸引 | 單季增速不炸裂，但產品組合與 pipeline 仍穩，市場開始重新認可品質 | `首選` |
| `RMD` | 很強 | 強 | 很強 | 大致合理 | 睡眠呼吸需求、耗材與 SaaS / 數據平台屬性支撐高品質溢價 | `次選` |
| `JNJ` | 很強 | 中上 | 很強 | 偏貴 | 兼具藥品與醫材，防守性高，但市場已給足安全溢價且仍有法律噪音 | `穩健但非最佳` |
| `MRK` | 強 | 中 | 很強 | 看似便宜 | 便宜主要因為 `Keytruda` 集中度與 `Gardasil` 壓力，折價有原因 | `價值型候選，不是品質冠軍` |
| `IDEX / IEX` | 不可比 | 不可比 | 不可比 | 不作主判斷 | 工業平台含醫療部門，不適合和四家醫療公司同排 | `排除` |

補充市場快照：

- `ZTS`：股價約 `119.79`，Forward `P/E` 約 `17.05x`，市值約 `50.57B`。[StockAnalysis](https://stockanalysis.com/stocks/zts/)
- `JNJ`：股價約 `242.99`，Forward `P/E` 約 `21.07x`，市值約 `585.58B`。[StockAnalysis](https://stockanalysis.com/stocks/jnj/)
- `MRK`：股價約 `116.21`，Forward `P/E` 約 `22.69x`，市值約 `287.32B`。[StockAnalysis](https://stockanalysis.com/stocks/mrk/)
- `RMD`：股價約 `240.15`，Forward `P/E` 約 `20.61x`，市值約 `34.83B`。[StockAnalysis](https://stockanalysis.com/stocks/rmd/)

## Top Tier And Why

### 1. `ZTS`

- `事實`：Zoetis 2025 全年營收 `9.5B`，調整後 EPS `6.41`，2026 指引仍有 `3%-5%` organic operational growth。
- `事實`：`Lenivia`、`Portela` 等新一代 OA 痛症產品已取得重要批准，代表不只是成熟品牌吃尾勁，而是 pipeline 正在接棒。
- `判斷`：它在這組名單裡同時擁有 `最乾淨的產業結構`、`最少的專利懸崖風險`、`高毛利/高現金流特性`、以及相對沒有被過度抬價的估值。

### 2. `RMD`

- `事實`：ResMed Q2 FY2026 收入、毛利、EPS、營運現金流都在擴張，且仍持續回購。
- `事實`：VirtuOx 收購把它從治療端往診斷端再延伸一步，商業模式更接近 `device + recurring supply + data workflow`。[VirtuOx](https://investor.resmed.com/news-events/press-releases/detail/402/resmed-acquires-virtuox)
- `判斷`：如果你更偏好 `醫療設備 + 軟體化 + 居家醫療長趨勢`，RMD 幾乎一定在前二。

### 3. `JNJ`

- `事實`：JNJ 2025 全年營收 `94.2B`，其中 Innovative Medicine `60.4B`、MedTech `33.8B`，兩大支柱都在成長。[JNJ FY2025](https://www.investor.jnj.com/investor-news/news-details/2026/Johnson--Johnson-reports-Q4-and-Full-Year-2025-results/default.aspx)
- `事實`：Intra-Cellular Therapies 併購進一步加強神經科學產品線，但短期也帶來融資與整合稀釋。[Intra-Cellular close](https://www.investor.jnj.com/investor-news/news-details/2025/Johnson--Johnson-Closes-Landmark-Intra-Cellular-Therapies-Inc--Acquisition-to-Solidify-Neuroscience-Leadership/default.aspx)
- `判斷`：它是最穩的大平台，但不是這組裡 risk/reward 最好的那一個。

## Winner Or Preferred Shortlist

### 我的排序

1. `ZTS`
2. `RMD`
3. `JNJ`
4. `MRK`
5. `IDEX / IEX`：排除出主比較

### 為什麼 `ZTS` 贏

`ZTS` 是這組裡最平衡的一檔：

- 它不像 `MRK` 那樣被單一 mega-blockbuster 專利懸崖主導。
- 它不像 `JNJ` 那樣已被市場給了太多純防守溢價，且還帶著法律與大型整合噪音。
- 它不像 `RMD` 那樣仍需要市場持續買單居家醫療數位化與 GLP-1 無害化敘事。

如果只選一檔做下一步深挖，我會選 `ZTS`。  
如果選兩檔，我會選 `ZTS + RMD`。  
如果你追求的是最保守的大市值防守，而不是最好的綜合 risk/reward，才考慮把 `JNJ` 放回首位。

## Main Reasons The Leading Idea Could Be Wrong

1. `ZTS` 的 2025 年底國際業務有一次性 timing 影響，若市場之後更嚴格調整這部分，短期成長感知可能再下修。[Zoetis FY2025](https://investor.zoetis.com/news/news-details/2026/Zoetis-Reports-Fourth-Quarter-and-Full-Year-2025-Results/default.aspx)
2. `RMD` 若後續需求增速繼續超預期，市場可能更願意給它高於 ZTS 的品質溢價。
3. `JNJ` 若法律噪音淡化、MedTech 再加速，現在看似偏貴的問題可能沒那麼重要。
4. `MRK` 若 pipeline 轉化速度快於市場預期，現在的折價可能反而提供更高報酬。
5. 如果你原本寫的不是 `IDEX`，而是 `IDXX`，那整個排名會明顯改寫，因為 `IDEXX` 會和 `ZTS` 高度可比，甚至可能直接進入第一梯隊。

## Next Step For Deep Research

- 第一優先：用 [`company-valuation-analyst`](/Users/anthony/Git/realanthonyc/Research-Reports/skills/company-valuation-analyst/SKILL.md) 深挖 `ZTS`
  - 問題重點：
  - `Lenivia / Portela` 的中長期峰值收入與對整體動物保健組合的拉動
  - OA mAb 產品波動是否只是短期庫存與節奏問題
  - 現價是否低於合理 base-case fair value

- 第二優先：對 `RMD` 做同樣的單公司估值
  - 問題重點：
  - VirtuOx 與診斷閉環對長期增速的意義
  - GLP-1 對 OSA 治療需求的真實中期影響
  - 耗材 / mask / SaaS 混合模式是否值得更高估值倍數

## Sources

- [Zoetis FY2025 results](https://investor.zoetis.com/news/news-details/2026/Zoetis-Reports-Fourth-Quarter-and-Full-Year-2025-Results/default.aspx)
- [JNJ FY2025 results](https://www.investor.jnj.com/investor-news/news-details/2026/Johnson--Johnson-reports-Q4-and-Full-Year-2025-results/default.aspx)
- [JNJ closes Intra-Cellular acquisition](https://www.investor.jnj.com/investor-news/news-details/2025/Johnson--Johnson-Closes-Landmark-Intra-Cellular-Therapies-Inc--Acquisition-to-Solidify-Neuroscience-Leadership/default.aspx)
- [Merck FY2025 results](https://www.merck.com/news/merck-highlights-progress-advancing-broad-diverse-pipeline/)
- [ResMed FY2026 Q2 results](https://investor.resmed.com/news-events/press-releases/detail/416/resmed-inc-announces-results-for-the-second-quarter-of-fiscal-year-2026)
- [ResMed acquires VirtuOx](https://investor.resmed.com/news-events/press-releases/detail/402/resmed-acquires-virtuox)
- [ZTS market snapshot](https://stockanalysis.com/stocks/zts/)
- [JNJ market snapshot](https://stockanalysis.com/stocks/jnj/)
- [MRK market snapshot](https://stockanalysis.com/stocks/mrk/)
- [RMD market snapshot](https://stockanalysis.com/stocks/rmd/)
- [IDEX company profile](https://stockanalysis.com/stocks/iex/company/)
- [IDEX corporate overview](https://www.idexcorp.com/)
