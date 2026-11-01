# 自介審查通過後自動處理 GitHub 入會權限 決策

## 2026-11-01：水球採用 Python script、GitHub Actions 與 GitHub App

原話：「有辦法自動化這個流程嗎？」「來取代 checklist」「then how to host???」「所以如果是要設計的話，是完全免費嗎？然後可能要寫什麼邏輯的程式嗎？那個排程+job的邏輯是什麼？」「所以基本上就是寫一個 python script for this?」

採納原話：「好，就用這個方案，更新 plan 和相關 specs，把 Python script、GitHub Actions 跟 GitHub App 要怎麼設定規劃清楚，保持簡單不要 over-engineering。」

確認對象：人工審查與合併後，一支 Python script 以 GitHub App 權限接續邀請、核對接受及更新進度；Actions 由 main 更新、每小時排程及手動啟動。不另設 server、網站或資料庫，以自動核對取代 checklist。這輪授權規劃與文件更新，未要求部署、發邀請、任命或 push。技術設定細節是本輪依此方向展開的規劃，組織啟用仍依有效制度決定。

## 2026-11-01：水球授權本地實作與測試

原話：「好，接著實作 Python script 和 GitHub Actions，先在本地測試好，GitHub App 要我設定什麼再跟我說。」

範圍：完成本地 Python script、Actions 與離線測試，再交付 GitHub App 設定步驟；不含遠端啟用或真實邀請。

## 2026-11-01：按用途整理 scripts

使用者原話：「scripts 底下能否做好 packaging by purposes」。按 assignments 與 onboarding 分組，測試與各用途程式放在一起，保留一份共用依賴；同步 module 執行入口、CI 與有效文件引用。

## 2026-11-01：用途名稱使用繁體中文

使用者原話：「purpose in zhtw」。用途資料夾改為 scripts/分工驗證 與 scripts/入會接續，Python module、測試與有效引用同步。

## 2026-11-01：先按排程與驗證，再按功能分組

使用者原話：「要不要先分成 scripts/排程 scripts/驗證 底下再 package by feature」、「入會接續 -> 入會權限處理」。採兩層目錄，功能為排程／入會權限處理及驗證／分工資料；排程入口命名 process_onboarding.py，權限處理範圍不因此擴大。

## 2026-11-01：保持停用，下一筆入會申請再測試

水球原話：「好，直接跑 dry-run 驗證一下，先保持 ONBOARDING_ENABLED=false」「還是等其他 members 要合併時再來測試？」「ok 那本地還有什麼相關檔案還沒 commit 嗎」「不然這 plan 就要結束了」。

本次建置收尾；保持 false，下一筆入會申請合併後再執行適用案件的 dry-run，正式邀請與接受流程尚未驗證。不是現在啟用，也不把未執行的驗收勾成完成。

## 2026-11-01：Plan 名稱表達意圖

水球原話：「plan 不要叫 github setup，把意圖講清楚」。Plan 改名為「自介審查通過後自動處理 GitHub 入會權限」，同步目錄與索引；原始需求引用保留原話。
