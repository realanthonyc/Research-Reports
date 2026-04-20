# 財務研究分析指標與整合框架

本檔作為 `corporate-financial-research-analysis` 的細節參考。先用 SKILL.md 主流程執行；只有在需要完整定義、公式、閾值與判讀細節時載入此檔。

## A. 指標清單

### 1) 盈餘與成長性 (Earnings & Growth)

- `EPS`：每股盈餘，核心獲利指標。
- `Trailing EPS`：過去 12 個月實際 EPS。
- `Forward EPS`：未來 12 個月預估 EPS。
- `Normalized EPS`：排除一次性項目後 EPS。
- `EPS Growth Rate`：EPS 年增率。
- `EPS Guidance`：管理層 EPS 指引。

判讀要點：
- EPS 成長若不足以支撐高估值（例如高 P/E），警惕高估。
- Forward 指標高度依賴假設，需與歷史達成率交叉驗證。

### 2) 估值 (Valuation)

- `P/E`、`Forward P/E`
- `P/S`
- `P/B`
- `EV/EBITDA`、`Forward EV/EBITDA`
- `PEG Ratio = P/E ÷ EPS Growth Rate`
- `DCF Fair Value per Share`
- `DCF Fair Value Ratio = DCF Fair Value per Share ÷ 當前股價`
- `DDM`
- `Residual Income Model`

判讀要點：
- `PEG < 1` 常見於成長相對估值合理。
- `DCF Fair Value Ratio > 1` 代表理論上偏低估；`< 1` 代表可能偏高估。
- 相對估值與絕對估值需同時呈現，避免單模型偏誤。

### 3) 財務質量與效率 (Quality & Profitability)

- `FCF = CFO - CapEx`
- `ROE`
- `ROE vs WACC`
- `ROIC`
- `ROIC vs WACC`
- `Debt-to-Equity Ratio`
- `Interest Coverage Ratio = EBIT ÷ 利息費用`
- `Current Ratio = 流動資產 ÷ 流動負債`
- `Quick Ratio = (流動資產 - 存貨) ÷ 流動負債`

判讀要點：
- 長期 `ROIC > WACC` 是價值創造核心條件。
- `Interest Coverage < 1.5` 與 `Quick Ratio < 0.5` 屬顯著風險訊號。

### 4) 成長趨勢 (Growth Trend)

- `Revenue Growth`
- `Revenue Growth Trend`
- `Gross Margin`
- `Gross Margin Trend`
- `Operating Margin`
- `Operating Margin Trend`
- `Revenue Guidance`
- `Margin Guidance`
- `R&D Expense Ratio`

判讀要點：
- 最佳狀態為「營收成長 + 營業利潤率擴張」同步。
- R&D 比率需看產業特性，過度壓縮可能傷害長期競爭力。

### 5) 市場預期與情緒 (Market Expectation & Sentiment)

- `RSI`
- `MACD`
- `Institutional Holding Change`
- `Analyst Revision Rate`
- `Analyst Revision Trend`（可標準化為 0-100）

判讀要點：
- 技術指標用於時機輔助，不取代基本面估值結論。
- 分析師修正與機構持倉可視為預期轉向先行訊號。

## B. 綜合解讀框架 (Integrated Interpretation Framework)

### 1) 基本面與獲利質量

核心問題：是否持續產生高品質獲利與現金流？

重點：
- Trailing EPS 與 FCF 一致性
- Gross Margin / Operating Margin 的穩定與趨勢

### 2) 成長動能與前景

核心問題：未來 1-4 季是否具可持續成長？

重點：
- Revenue Guidance / Margin Guidance 是否支持市場預期
- 營收增長是否伴隨利潤率改善
- R&D 是否支持長期護城河

### 3) 資本效率與價值創造

核心問題：成長是否創造 EVA，而非僅擴大規模？

重點：
- `ROIC vs WACC` 為優先判斷
- `ROE vs WACC` 作為股東回報效率補充

### 4) 財務結構與風險

核心問題：是否能承受逆風與高利率壓力？

重點：
- Debt-to-Equity + Interest Coverage 看槓桿與債務壓力
- Current Ratio + Quick Ratio 看短期流動性

### 5) 估值與容錯空間

核心問題：市場定價是否過度樂觀/悲觀？

重點：
- `PEG Ratio` 看估值-成長匹配
- `Forward EV/EBITDA` 對照歷史與同業
- `DCF Fair Value Ratio` 看安全邊際

### 6) 市場預期與情緒

核心問題：短期資金與共識順風或逆風？

重點：
- Analyst Revision Trend
- Institutional Holding Change
- RSI / MACD 作為時機輔助

## C. 特殊情境與風險校正

### 1) 產業差異

- 科技：重視 Revenue Growth、R&D Ratio。
- 金融：重視 ROE、資產品質與淨息差。
- 原物料/循環：重視週期、P/S、現金流韌性。

### 2) 早期或未盈利公司

- 不以 EPS 為主，改用：
- `Burn Rate`（現金消耗）
- `Cash Runway = 現金餘額 ÷ Burn Rate`
- 融資能力與里程碑達成率

### 3) 前瞻數據風險

- Forward EPS、Guidance、Analyst Revision 皆屬假設驅動。
- 需回看管理層歷史指引達成率。

### 4) 宏觀因子

- 利率上行會提高折現率、壓縮成長股估值。
- 納入通膨、匯率、地緣政治等外生風險。

## D. 建議輸出規範

- 先結論、後證據。
- 明確標示「已驗證數據 / 估算 / 假設」。
- 必含 Bull/Base/Bear。
- 最終結論需回答：
- 目前是否具投資吸引力？
- 吸引力來自哪些可驗證因子？
- 哪些風險可能推翻結論？
