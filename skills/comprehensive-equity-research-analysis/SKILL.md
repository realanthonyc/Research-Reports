---
name: comprehensive-equity-research-analysis
description: 以機構級標準進行公司投資研究，整合事實查核、最新動向追蹤、財務推導、相對估值與DCF三情境、量化評分卡、風險/催化分析與交易-配置策略，輸出繁體中文且附來源連結與訊息確定性標註的完整研究報告。Use when the user asks for company valuation, stock research, investment attractiveness judgment, latest company/sector developments with reliability assessment, buy/hold/sell (or buy/hold/avoid) recommendations, peer comparison, catalyst/risk mapping, swing-to-mid-term strategy, or institution-style equity reports with source-backed conclusions.
---

# 綜合股權投資研究分析 (Comprehensive Equity Research Analysis)

使用一致且可追溯的流程，輸出「可驗證事實 + 最新動向評估 + 估值模型 + 量化評分 + 策略建議」的一體化研究報告。

## 核心流程

1. 定義任務邊界
- 確認公司名稱、Ticker、交易所、幣別、分析日期、投資週期。
- 若未提供標的，先要求補充標的再開始。

2. 鎖定時間與資料新鮮度
- 強制標示：`分析日期`、`股價時間（含時區）`、`最新財報期別`。
- 將 `today/latest/近期` 轉為絕對日期後再輸出。

3. 蒐集與事實查核（依優先級）
- 來源優先級：`監管文件/法定申報 > 公司公告/法說資料 > 交易所或官方市場資料 > 一線資料商 > 財經媒體`。
- 核心結論至少附 1-2 個來源。
- 數字衝突時採高優先級來源，並註記差異。

4. 最新動向、消息與重要動態判讀（必做）
- 蒐集近 30-90 天重大消息（財報、指引、監管、併購、供應鏈、產品、政策、資金流）。
- 額外建立 `重要動態雷達`：主動且積極搜尋未來 14-30 天的 upcoming happenings 與過去 14-30 天的 recent happenings，不限於正式 event，也包含重要新聞流、客戶/供應鏈動作、產品節點、監管變化、資本支出訊號、競爭者動態、產業敘事轉折。
- 把 `機構調研評價 / 分析師重估 / rating change / target-price revision / buy-side debate` 視為重要動態的一部分，但只有在它們能幫助理解市場預期、預期差或估值中樞變化時才納入。
- 判斷標準不是「是不是 event」，而是「是否可能顯著影響營收、毛利、CapEx、競爭格局、估值中樞或市場預期」。
- 若未來 14 天內有高重要性 upcoming happenings，必須在報告中說明：`市場目前在期待什麼`、`爭議焦點是什麼`、`哪些內容屬於已反映`、`什麼結果才算超預期/低於預期`。
- 若過去 14 天內剛發生高重要性 recent happenings，必須做 `重要動態深讀`：不只列出名稱，而要拆解 `實際發生了什麼`、`沒有發生什麼`、`市場如何解讀`、`你是否同意這種解讀`、`對 Bull/Base/Bear 哪個情境影響最大`。
- 對 event-driven 或 narrative-driven 標的，必須主動找出「市場現在最在意的 1-3 個 happenings」，即使使用者未明示要求。
- 每則消息必須標示：事件日期、來源、`確定性等級`、`市場影響方向`、`你的評價`。
- 僅可驗證消息可納入核心論點；低確定性消息僅列為觀察，不可作為主要估值依據。
- 若情報僅來自單一網路來源（單一媒體/社群/轉述），預設降級為 `C` 或 `D`，並標註 `需二次驗證`。
- 若消息情報來自網頁或社群貼文（例如 X.com 推文），必須附上原始來源 URL。
- 詳細規格使用 [references/news-intelligence-framework.md](references/news-intelligence-framework.md)。

5. 財務推導與口徑統一
- 優先使用可直接驗證數值，再補算缺失值。
- 禁止混用年度與季度口徑。
- 至少計算：`Debt-to-Equity`、`Interest Coverage`、`Current Ratio`、`Quick Ratio`、`FCF/Revenue`。

6. 分析模組與估值
- 執行六模組分析（基本面、成長、資本效率、財務風險、估值、市場預期）。
- 相對估值至少 2 種倍數（如 `Forward P/E`、`Forward EV/EBITDA`）。
- DCF 使用 `Bull/Base/Bear` 三情境（參數按 [references/modeling-standards.md](references/modeling-standards.md)）。

7. 量化評分與覆核
- 使用 [references/scoring-rubric.md](references/scoring-rubric.md) 產出 0-100 分、分項權重與等級。
- 出現重大紅旗（治理、流動性、ROIC 長期低於 WACC 等）時下修結論。

8. 形成結論與策略
- 同時輸出 `Bull / Base / Bear` 觀點與反證。
- 提供兩段策略：`Swing（數天到1個月）`、`中短期（1-6個月）`。
- 結論必須對應證據與可追蹤觸發條件。

## 報告輸出規格

- 優先使用 [references/report-presentation-template.md](references/report-presentation-template.md)；若使用者要求完整機構版章節，搭配 [references/comprehensive-report-outline.md](references/comprehensive-report-outline.md)。
- 預設將最終報告寫入 `reports/research/comprehensive-research-<ticker>-<YYYY-MM-DD>-00.md`；除非使用者另行指定路徑或檔名。
- 同一 `ticker` 與 `YYYY-MM-DD` 若當日已存在先前版本，依序改用 `-01`、`-02`、`-03`...；寫檔前先檢查現有檔名並選擇下一個可用序號，序號固定為兩位數。
- 涉及新聞/社群來源時，表格內使用來源代號，完整 URL 置於表格下方「來源 URL」區塊。
- 必須先給 `Investment Verdict`，再展開證據鏈。
- 報告開頭的總結必須拆成兩部分：
- 1) `詳細總結`：較完整地解釋證據鏈、推導、判斷與預測；對較難理解的概念要放慢並簡化說明。
- 2) `總結概要`：快速、直接、可掃讀地說清楚結論、偏向、關鍵風險與最重要的觀察點。
- 表格欄位至少含：`數值`、`期間`、`來源`、`是否估算`。
- 最新消息段落必須使用 `確定性等級 + 你的評價 + 對估值影響`。
- 若 14 天內有即將發生或剛發生的重要 happenings，報告必須加入專節，明確回答：
- 1) `市場原本在期待什麼 / 爭論什麼`
- 2) `實際發生了什麼 / 沒發生什麼`
- 3) `市場如何解讀`
- 4) `你是否同意市場解讀，以及理由`
- 5) `對營收、毛利、CapEx、競爭格局、估值中樞的潛在傳導`
- 估算值一律標註 `（為估算值）` 並說明假設。
- 全文使用繁體中文；專有術語可保留英文。

## 完成後處理

- 完成報告與相關輸出檔後，自動只針對該次產出的 output files 以非互動方式建立 git commit 並 push 到預設遠端；除非使用者明確要求不要 commit 或不要 push。
- commit / push 前僅納入本次任務直接產生或修改的相關檔案，避免混入無關變更。
- commit message 應清楚描述標的與日期，例如：`add TSM comprehensive research report 2026-03-17-00`。
- 若使用者已明確授予 standing permission，執行 commit / push 時不需再次詢問。
- 若任務是更新 skill 本身、references、templates、metadata 或其他 skill implementation files，則不自動 commit / push。
- push 預設使用目前分支與其對應遠端；若 push 失敗，需回報失敗原因與當前 git 狀態。

## 最低內容要求

1. 公司概要與商業模式（含收入結構/地區）
2. 客戶與供應商集中度
3. 最新動向與消息評級（含確定性、重要動態雷達、分析師評價與市場預期）
4. 財務三表重點與比率趨勢（歷史 + 前瞻）
5. 估值（相對估值 + DCF 三情境）
6. 風險與催化（機率/影響/監測指標）
7. 同業比較與關聯標的
8. 投資論點與策略建議（Swing + 中短期）
9. 雙層總結（詳細總結 + 總結概要）

## 品質門檻

- 明確區分：`已驗證事實`、`模型假設`、`推論`、`主觀判斷`。
- 不使用情緒化措辭，不以單一指標下定論。
- 明示資料缺口、模型限制與結論脆弱點。
- 對低確定性消息加註「需二次驗證」，並降低其在結論中的權重。
- 不可只列出事件名稱或新聞標題；對重大 happenings 必須交代 `市場預期`、`實際內容`、`落差`、`市場解讀`、`你的判斷`。
- 若公司所屬產業高度受事件、新聞流或敘事轉折驅動（例如 GTC、WWDC、AI Day、FDA、資本市場日、監管政策、雲端 CapEx 趨勢），漏掉近期待發生或剛發生的重要 happenings 視為報告缺陷。
- 總結不可只有保守、模糊、兩面兼顧的空話；在證據允許的範圍內，必須明確寫出理解、判斷與預測。
- 結尾加入「非投資建議」聲明。

## 參考檔案

- 指標與框架： [references/metrics-framework.md](references/metrics-framework.md)
- 建模參數： [references/modeling-standards.md](references/modeling-standards.md)
- 評分卡： [references/scoring-rubric.md](references/scoring-rubric.md)
- 報告模板： [references/report-presentation-template.md](references/report-presentation-template.md)
- 最新消息框架： [references/news-intelligence-framework.md](references/news-intelligence-framework.md)
