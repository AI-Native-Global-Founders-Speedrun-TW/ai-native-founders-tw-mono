---
document_type: Plan
adopted: true
---

# GitHub setup

## 需求原文

> new task 回 main
> /sf-ai 接下來想要聊的事情是 GitHub 的 setup。
>
> 目前 GitHub 的權限設計還可以更精確。目前每個 member 在 PR 被 approved 之後，我們其實沒有辦法自動將他變成 member。這可能會是一個 SOP，要請 onboard 的 leader（未來可能是 Chris）來負責這件事情。
>
> 那整體你覺得需要什麼基建來輔助嗎？

## As-Is

2026-11-01 唯讀核對：本地 main 與 origin/main 一致；既有未提交內容保留。

- [GitHub 平台規格](../../specs/05-社群基建/[規格]GitHub-Org-Setup.md)與[自介審查 SOP](../../specs/03-SOP/[SOP]自介PR審查SOP.md)已規定正式審查、合併、Member 邀請、本人接受及回讀確認；目前採人工操作。
- [Onboard Role](../../specs/02-R&R/[Role]Onboard-篩選與加入接續.md)已負責加入接續；[assignment](../../members/r-and-r-assignment.yml)尚無該職責 Leader。Chris 僅為使用者提出的可能人選，未任命。
- GitHub API 查得 organization 為 Free，base permission 為 none，Owner 僅 Johnny850807；目前 pending invitations 為空。此查詢不證明所有正式成員已完成平台加入。
- mono 的 rulesets 回傳空清單，main branch protection 回傳 Branch not protected。
- Members team 對 mono 的實際權限為 Triage；Council 的 parent 為 Members。平台規格記錄的是 2026-10-27 的 Write 舊快照，不能沿用為今日實況。
- org 允許成員建立 repository；未要求全體成員開啟雙因素驗證。本輪未修改設定。

## 使用者目前覺得的 Problem

### GitHub 的權限設計還可以更精確

已採納自動接續方向，詳見[決策紀錄](decisions.md)。Onboard 在審查及合併後，需要免除逐人勾 checklist、邀請與查接受的操作，同時維持資格裁決和平台能力分離。Problem 與設計見[GitHub 平台規格](../../specs/05-社群基建/[規格]GitHub-Org-Setup.md)。

## To-Be

1. 一支 Python script 執行加入接續；人工只處理審查、合併及例外。
2. 一份 GitHub Actions workflow 處理 main 更新、每小時補查與手動補跑；GitHub App 提供必要權限，不另設 server 或資料庫。
3. 原 PR 呈現平台實際狀態，避免重送邀請、重複留言與假完成。規則統一見[自動化規格](../../specs/05-社群基建/[規格]GitHub-Org-Setup.md#自動加入接續python-scriptgithub-actionsgithub-app)。

## 工程摘要

先實作 script 與 mock API 測試，再接 workflow；完成 main 保護及 App 環境設定後 dry-run，最後依有效授權實際驗證。細部設定只維護在平台規格；Python script、離線測試及 workflow 已在本地建立，平台配置尚未執行。

本地程式產物：`scripts/排程/入會權限處理/process_onboarding.py`（入會接續程式）、`scripts/排程/入會權限處理/test_process_onboarding.py`（入會接續測試）、`.github/workflows/sync-onboarding.yml`（入會接續工作流程）；必要依賴沿用現有 Python requirements。不新增通用工作流框架。

### 規格差異

- [成員識別與資料](../../specs/01-制度/[規格]成員識別與資料.md)：驗證程式引用更新到 分工驗證 package；members 說明與 YAML 頂部驗證指令同步，行為不變。對應 [GitHub 的權限設計還可以更精確](#github-的權限設計還可以更精確)。

- [憲政制度](<../../specs/01-制度/[機制] 憲政制度.md>)：平台邀請由 Owner 人工執行擴充為已授權 App 接續，保留原資格與裁決條件。對應 [GitHub 的權限設計還可以更精確](#github-的權限設計還可以更精確)。
- [社群基建入口](../../specs/05-社群基建/README.md)：更新 GitHub 設定的內容導覽。對應 [GitHub 的權限設計還可以更精確](#github-的權限設計還可以更精確)。

- [GitHub org Setup](../../specs/05-社群基建/[規格]GitHub-Org-Setup.md)：以 App 自動邀請及定時查詢取代一般案件的人工平台接續，定義 script、job、設定與安全啟用。對應 [GitHub 的權限設計還可以更精確](#github-的權限設計還可以更精確)。
- [自介審查 SOP](../../specs/03-SOP/[SOP]自介PR審查SOP.md)：審查與合併保留人工，加入自動接續、故障及重邀的人工處理。對應 [GitHub 的權限設計還可以更精確](#github-的權限設計還可以更精確)。
- [Onboard Role](../../specs/02-R&R/[Role]Onboard-篩選與加入接續.md)：一般查詢由自動化執行，Leader 接續例外。對應 [GitHub 的權限設計還可以更精確](#github-的權限設計還可以更精確)。
- [Repository Role](../../specs/02-R&R/[Role]基建-Repository維護.md)：維護 App、Actions、私鑰及故障接續。對應 [GitHub 的權限設計還可以更精確](#github-的權限設計還可以更精確)。

## 驗收：待實作後執行

- [ ] 一般新申請有效核准且合併後送出 Member 邀請；無有效審查、未合併、其他 PR、歷史及不適用案件不自動邀請。
- [ ] 已有 pending 或 active 不重送；本人接受後下輪查詢更新原 PR，沒有重複歡迎。
- [ ] 核准過期、核准後異議、職位空缺／異動及帳號不符交人工，不推翻既有資格。
- [ ] 寫入前後中斷、comment 更新失敗、邀請過期／取消、成員後續離開、API 限流與部分回傳均不造成盲目重送或假完成。
- [ ] 多個觸發只跑一個寫入 job；漏掉前輪後仍可補齊；dry-run 無外部寫入。
- [ ] 非 main、fork PR 或改動 workflow 的未受信內容取不到私鑰；script 不執行自介內容。
- [ ] 人工接續與自動化停用／恢復可行；真實邀請及接受尚待有授權的適用案件驗證。

## 進度與限制

方案已採納；script 與 workflow 已在本地實作。未建立 App／Secrets／ruleset、未部署、未發邀請。本 Plan adopted 為 true，表示使用者已明確採納方案，不表示實作或部署完成。Chris 仍未任命；目前有效 Onboard 任職、Repository code owner 帳號、bypass 與有效啟用決定均須在部署前核對，不以規劃完成代替。

本輪需文件獨立 review；尚未宣稱整 Plan Auto-sync 檢驗通過或工程就緒。

## 規劃階段文件審查與憲法檢查

獨立 reviewer 完整讀取本輪 diff、文件及憲法後複查通過。已修正 adopted 與實作完成的混淆，以及正式通過留言阻擋自身自動接續的問題。FORMULATION 核對結果：設定由平台規格維護，SOP／Role／制度同步承接，沒有 truth 反向依賴 Plan；單一 script、workflow、App，沒有新增資料庫或服務。相對連結與 git diff whitespace 檢查通過；沒有程式或平台驗證，未宣稱整 Plan Auto-sync 通過。

憲法逐條結論：
- 第 1 條（名稱與目的）：沒有違反；改善成員加入協作。
- 第 2 條（公益非商業）：沒有違反；無商業交換。
- 第 3 條（效力制度分工）：沒有違反；啟用仍須有效制度依據。
- 第 4 條（開放成員資格）：沒有違反；程式不裁決資格，例外轉人工。
- 第 5 條（自願參與義務）：沒有違反；未強迫任職或追加工作承諾。
- 第 6 條（分工議會組成）：沒有違反；權限按職責，不自動授予 Council 或 Owner。
- 第 7 條（決策任命範圍）：沒有違反；Chris 未被視為已任命。
- 第 8 條（平等有效表決）：沒有違反；資料與 App 不代替有效決定。
- 第 9 條（罷免職位替換）：沒有違反；未新增撤任或替換途徑。
- 第 10 條（異議資格保障）：沒有違反；不因故障或無依據反對取消資格。
- 第 11 條（利益緊急界線）：沒有違反；保留迴避與秘密保護，不藉故障擴權。
- 第 12 條（修憲成員監督）：沒有違反；未削減監督或改變門檻。


## 本地實作與驗證

使用者原話：「好，接著實作 Python script 和 GitHub Actions，先在本地測試好，GitHub App 要我設定什麼再跟我說。」

已建立程式、mock API tests、main／排程／手動 workflow，並將既有 CI 改為執行全部 script tests。App 首次接續自動加一個收據 label 並保留 timeline，供進度留言遺失時停止重邀；不新增人工 checklist 或資料庫。設定步驟仍只在平台規格維護。

本地執行 unittest discover 共 34 項通過（22 項入會接續／HTTP 測試及 12 項分工測試）；分工 validator 通過。actionlint 驗證兩份 workflow 通過，git diff --check 通過。所有 API 測試均使用模擬資料，無真實邀請或外部留言。真實 installation token 權限、GitHub App 邀請及接受驗證仍未執行；不能以離線測試取代平台驗收。

### 實作獨立 review

最終複查通過，reviewer 亦執行 34 項測試通過。先前發現並修正：進度留言遺失導致重邀、首次既有 active 未查核准、單人 YAML／邀請拒絕中斷整輪、review 依據與 SOP 歡迎文案未完整承接。FORMULATION 核對通過；本地實作不等於已發布或已啟用。

憲法逐條檢查：
- 第 1 條（名稱與目的）：沒有違反；協助成員加入協作。
- 第 2 條（公益非商業）：沒有違反；無商業交換。
- 第 3 條（效力制度分工）：沒有違反；首次接管核對有效核准。
- 第 4 條（開放成員資格）：沒有違反；平台 active 不代替審查依據。
- 第 5 條（自願參與義務）：沒有違反；無額外工作承諾。
- 第 6 條（分工議會組成）：沒有違反；未自動授予治理職位或管理權。
- 第 7 條（決策任命範圍）：沒有違反；啟用與任職仍需原有效依據。
- 第 8 條（平等有效表決）：沒有違反；不以程式取代表決。
- 第 9 條（罷免職位替換）：沒有違反；未新增撤任或替換途徑。
- 第 10 條（異議資格保障）：沒有違反；問題轉人工，不撤銷資格。
- 第 11 條（利益緊急界線）：沒有違反；保留自審阻擋與秘密保護。
- 第 12 條（修憲成員監督）：沒有違反；未改變監督權利或門檻。

## Scripts 按用途整理

按分工驗證與入會接續 分成 Python packages，各自包含測試；scripts/README.md 提供用途與執行入口，共用 requirements.txt。Actions、成員資料說明與平台規格同步 module 路徑；既有歷史紀錄不改寫。移動後重新執行全部測試與 workflow 檢查。

用途分組後獨立 review 通過：module imports、mock 路徑、repo root、兩份 workflow 與有效文件引用均已核對；34 項測試、validator、CLI、actionlint 與 diff 檢查通過。FORMULATION 無阻擋，未改治理或平台行為。憲法逐條複查：
- 第 1 條（名稱與目的）：沒有違反；本輪只調整程式用途分組與引用，既有保障及權限不變。
- 第 2 條（公益非商業）：沒有違反；本輪只調整程式用途分組與引用，既有保障及權限不變。
- 第 3 條（效力制度分工）：沒有違反；本輪只調整程式用途分組與引用，既有保障及權限不變。
- 第 4 條（開放成員資格）：沒有違反；本輪只調整程式用途分組與引用，既有保障及權限不變。
- 第 5 條（自願參與義務）：沒有違反；本輪只調整程式用途分組與引用，既有保障及權限不變。
- 第 6 條（分工議會組成）：沒有違反；本輪只調整程式用途分組與引用，既有保障及權限不變。
- 第 7 條（決策任命範圍）：沒有違反；本輪只調整程式用途分組與引用，既有保障及權限不變。
- 第 8 條（平等有效表決）：沒有違反；本輪只調整程式用途分組與引用，既有保障及權限不變。
- 第 9 條（罷免職位替換）：沒有違反；本輪只調整程式用途分組與引用，既有保障及權限不變。
- 第 10 條（異議資格保障）：沒有違反；本輪只調整程式用途分組與引用，既有保障及權限不變。
- 第 11 條（利益緊急界線）：沒有違反；本輪只調整程式用途分組與引用，既有保障及權限不變。
- 第 12 條（修憲成員監督）：沒有違反；本輪只調整程式用途分組與引用，既有保障及權限不變。

繁體中文用途更名複查：imports、mock、CI、有效引用已同步，34 項測試、validator、module CLI、actionlint 與 diff 檢查通過。獨立 FORMULATION review 通過。憲法逐條結論如下，皆沿用前版保障，未改行為或部署：
- 第 1 條（名稱與目的）：沒有違反。
- 第 2 條（公益非商業）：沒有違反。
- 第 3 條（效力制度分工）：沒有違反。
- 第 4 條（開放成員資格）：沒有違反。
- 第 5 條（自願參與義務）：沒有違反。
- 第 6 條（分工議會組成）：沒有違反。
- 第 7 條（決策任命範圍）：沒有違反。
- 第 8 條（平等有效表決）：沒有違反。
- 第 9 條（罷免職位替換）：沒有違反。
- 第 10 條（異議資格保障）：沒有違反。
- 第 11 條（利益緊急界線）：沒有違反。
- 第 12 條（修憲成員監督）：沒有違反。

排程／驗證兩層結構最終複查通過：imports、mock、CI、文件與 repo root 深度均符合新位置。34 項測試、validator、CLI、actionlint 與 diff 檢查通過；FORMULATION 無阻擋，未擴大權限。憲法逐條複查：
- 第 1 條（名稱與目的）：沒有違反；既有行為及保障保留。
- 第 2 條（公益非商業）：沒有違反；既有行為及保障保留。
- 第 3 條（效力制度分工）：沒有違反；既有行為及保障保留。
- 第 4 條（開放成員資格）：沒有違反；既有行為及保障保留。
- 第 5 條（自願參與義務）：沒有違反；既有行為及保障保留。
- 第 6 條（分工議會組成）：沒有違反；既有行為及保障保留。
- 第 7 條（決策任命範圍）：沒有違反；既有行為及保障保留。
- 第 8 條（平等有效表決）：沒有違反；既有行為及保障保留。
- 第 9 條（罷免職位替換）：沒有違反；既有行為及保障保留。
- 第 10 條（異議資格保障）：沒有違反；既有行為及保障保留。
- 第 11 條（利益緊急界線）：沒有違反；既有行為及保障保留。
- 第 12 條（修憲成員監督）：沒有違反；既有行為及保障保留。


### 發 PR 前最終檢查（2026-11-01）

使用者要求最後 review、確認後 commit 並發 PR，並提供 GitHub App 設定方式。本輪在獨立 worktree 檢查實際程式、workflow、規格與引用；34 項模擬 API／資料測試、分工驗證、actionlint 與 diff 檢查通過。獨立 reviewer 的 FORMULATION 與程式檢查無阻擋，憲法逐條檢查十二條均沒有違反，前述逐條結論仍適用。Python 快取已排除版控。未配置 App、未發送真實邀請、未啟用排程寫入；Onboard Leader 及正式啟用條件仍待確認。
