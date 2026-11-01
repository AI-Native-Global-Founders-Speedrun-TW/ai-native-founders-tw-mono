# decisions

本檔只 append。每一筆是使用者在本 plan 的一個決策，舊紀錄不改寫；推翻或更正時新增一筆並寫明是哪一筆。目前有效的承諾以 specs truth 為準。格式見 /sf-plan 的 `formats/decisions.md`。

## 決策 001（新建基建計畫）

- 使用者：Johnny Pan <johnny850807@gmail.com>（git author）
- 時間：2026-11-01T13:23:24+08:00
- 互動：新建或沿用 Plan
- 完整語意：使用者要求在新的 session 審視 dc infra、追上最新進度，並為需要的改動建立新的 Plan；此筆只記錄新建 Plan 的需求，不表示採納 AI 提出的文案、設定或人員權限。
- 推翻：無
- 落點：plan.md 的需求原文與範圍；原話保存在 ../../logs/20261101-dc-infra審視原始需求.md

## 引用補充

決策 001（新建基建計畫）的落點見 [Plan 需求](plan.md#需求原文與範圍)與[原始需求](plan.md#需求原文與範圍)。原紀錄保留當時的 log 落點；本次 PR 不包含該 log，可讀原話以 Plan 開頭為準，不增加使用者決策。

## 決策 002（授權社群更新）

- 使用者：Johnny Pan <johnny850807@gmail.com>（git author）
- 時間：2026-11-01T13:43:40+08:00
- 互動：寫入授權
- 完整語意：使用者確認本 chat 所列 Discord To-Be，要求設立 goal 並完成各項更新；onboard 改為與邀請訊息類似，直接提供可複製給 Agent 的 prompt，帶新人認識組織後再按本人意願申請。本次包括 welcome、onboard釘選/topic、Server Guide、有效GitHub入口、announcements/mod-log topic及核實後語音名稱；不擴大為任命管理者或授予管理權，也不接續Threads邀請。
- 推翻：無
- 落點：plan.md、Discord Setup specs及實際Discord入口

## 決策 003（延伸基建計畫）

- 使用者：Johnny Pan <johnny850807@gmail.com>（git author）
- 時間：2026-11-01T14:16:32+08:00
- 互動：新建或沿用 Plan
- 完整語意：使用者要求 Council 角色、moderation、category 與協作頻道的提案及批判討論，移入既有 dc infra Plan 並繼續延伸，不放 logs。這是文件落點與沿用 Plan 的要求，不表示採納候選設計、任命人員或授權平台賦權。
- 推翻：無
- 落點：[plan.md 接續規劃](plan.md#接續規劃council角色moderation與協作空間)與[Council 討論附件](Council角色與協作空間討論.md)；移除原 log 的追加二、追加三。

## 決策 004（採納精簡設計）

- 使用者：Johnny Pan <johnny850807@gmail.com>（git author）
- 時間：2026-11-01T14:25:38+08:00
- 互動：confirm 整體提案
- 確認對象：[Council 角色與協作空間討論的修訂後整體建議](Council角色與協作空間討論.md#修訂後整體建議未採納未實作)，採納前檔案 SHA-256：9d84f381ac54713c3775c9d90748dab1d93215777a3caf9d2b12c4a6998b2b62
- 完整語意：使用者以「ok go adopt them」採納前輪經獨立批判後的精簡 Council／Moderator 整體方案：身分與能力分開，暫不新增冗餘角色與頻道，沿用 collaborations／announcements／lounge，優先核對技術接續、警示接收、敏感聯絡與非涉案備援，再依有效程序配置必要 moderation 能力。採納設計不代表已完成任命、組織程序或 Discord 配置；使用者同時要求接續 Council 名單與 SSoT 維護設計，不把整份仍在擴充的 Plan 標為已 deliver。
- 推翻：無
- 落點：[Discord Setup](<../../specs/05-社群基建/[規格]Discord-社群-Setup.md#council-身分與-moderator-能力>)；plan.md 的接續規劃、To-Be 與規格差異。

## 決策 005（分析後順序執行）

- 使用者：Johnny Pan <johnny850807@gmail.com>（git author）
- 時間：2026-11-01T14:48:33+08:00
- 互動：寫入授權
- 完整語意：使用者要求對 Council 提案進行 gap analysis 與 consistency analysis；分析達成一致後設定執行 goal，先完成本地 repo 變更，再更新 Discord。Council 表保留一行 Verify note：Council 必須至少擔任一項有效的 R&R Leader。此授權不代替真人任職或組織決定，不將缺少原案依據補造為有效，也未要求 push。
- 推翻：無
- 落點：plans/004-dc-infra/plan.md 的分析與執行順序；Council名單與平台對應SSoT設計.md；後續本地 sources、工具、specs 與 Discord 設定


## 決策 006（名單結構從簡）

- 使用者：Johnny Pan
- 日期：2026-11-01
- 完整語意：使用者要求 Council 使用 simple structure data，避免 over-engineering，並授權先在本地大幅更新供 review。採用手動 YAML 的 member 與 roles，移除前版產生表、parser 與專用 CI；不因此確認真人任職，也不授權本輪 push 或 Discord 更新。
- 推翻：前版 Council 名單產生與專用工具設計；既有憲政資格、表決與平台權限規則不變。
- 落點：本 Plan 最新本地修訂節、Council SSoT 設計及 members/council.yml。


## 決策 007（單向依賴規範）

- 使用者：Johnny Pan
- 日期：2026-11-01
- 完整語意：Plan 永遠向外依賴，truth 與 members 不得依賴 Plan；在 FORMULATION 明定。Council YAML 頂部以完整結構化註解說明規範、格式、欄位與驗證方式，讓讀者知道如何填寫及判定有效格式。
- 推翻：前版由 members 與 truth 連回 Plan 補足任職狀態或規則的設計。
- 落點：FORMULATION、Council YAML、受影響 truth 與 members；原話見本 Plan 最新段落。


## 決策 008（單一分工資料）

- 使用者：Johnny Pan
- 日期：2026-11-01
- 完整語意：同意單一 assignment YAML 同列 role、leader、contributors，Council 由非空 leader 去重；要求最後一次一致性檢查並更新既有 PR。
- 推翻：Council 與 Contributors 分別手填兩份 YAML 的前版設計。
- 落點：assignment YAML、相關 SOP／specs 與本 Plan 最新執行目標。
