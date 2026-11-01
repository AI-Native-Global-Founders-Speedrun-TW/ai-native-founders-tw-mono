# Problem

正式成員需要接續取得 GitHub organization 的 Member 身分；審查人與執行邀請的人必須知道邀請誰、給哪些權限，以及何時才算完成。organization 角色、Team 與 repository 權限若混在一起，可能讓「加入組織」被誤解成取得所有 repo 的管理權，也可能把尚未接受邀請的人誤記為已加入。

# Specs

## Organization 與權限的區分

目標為 [AI-Native-Global-Founders-Speedrun-TW](https://github.com/AI-Native-Global-Founders-Speedrun-TW)。本規格記錄 GitHub org 加入方式與目前相關設定，作為[自介 PR 審查 SOP](<../03-SOP/[SOP]自介PR審查SOP.md>)的接續依據；組織資格仍依[申請制度](<../01-制度/[機制] 憲政制度.md>)。

| 對象 | 意義與接合 |
|---|---|
| 組織成員 | 依憲政制度有效取得的資格；一般申請、首屆任命及恢復的依據分開保存。 |
| GitHub org Member | 接受該 org 的 Member 邀請後生效的平台身分；不因 PR comment 或合併而自動產生。 |
| GitHub org Owner | 平台管理角色，可執行 org 邀請；不因自介通過而授予 Owner。 |
| Members team | 既有 GitHub Team；與 org Member 是不同對象。加入此 Team 會取得其 repository 權限。 |
| Council team | 既有 Members 的子 Team；平台名稱與實際權限須分開核對，不以此 Team 名單自行決定治理或審查資格。 |
| R&R 的 Leader／Contributors | 依憲政制度與 R&R 權限配置維護；Leader 具有 Council 身分，但不自動取得 org Owner、Team maintainer 或所有 repo 管理權。 |

## 維護與權限交接

[Repository Leader](<../02-R&R/[Role]基建-Repository維護.md>)承接 GitHub 技術設定與有效決定的執行；第二位接續 Leader 必須在自己的有效 R&R 中明列 GitHub 接續範圍與權限。職位本身不表示帳號已有平台權限，Org Owner 或 Team 名稱也不取代有效任職。

操作前核對共同制度的決定與生效時間，依 Repository 的權限接續步驟執行並回讀實際設定。撤任只收回已失去職責所需權限，保留其他有效職位與一般權益；不得因普通成員仍能公開讀取 repo 而宣稱撤權失敗，也不得把 org Member 當成治理票權。權限交接、緊急處置及能力不足的處理依[憲政制度](<../01-制度/[機制] 憲政制度.md>)。

## 現行設定

以下為 2026-10-27 由 GitHub 設定頁讀取的現況；這次沒有修改平台設定。此表是該日觀察，不能作為永久保留既有權限的依據。一般成員平台加入只邀請為 org Member，不加入 Members team；後續有效任免、撤權或設定變更仍依憲政制度執行。

| 設定位置 | 現行值 | 作用 |
|---|---|---|
| Org 顯示名稱 | AI-Native Founders Summit Taiwan | GitHub 平台顯示名稱；本文件不以此改寫憲法中的組織名稱。 |
| Org Base permissions | No permission | 不透過 org 基礎權限授予 repo 存取；public repo 的公開讀取不因此消失。 |
| Repository creation | Public 開啟；Private 關閉 | org Member 可建立 public repo，不能以此設定建立 private repo。 |
| Members team | mono repo：Write | Team 對指定 repo 的權限，不能由 Base permissions 的 No permission 推定沒有 Write。 |
| Council team | Members 的子 Team | 保留現行結構，不由名稱推定額外治理權或所有 repo 的 Admin。 |
| Projects base permissions | Write | 與 repository Base permissions 是不同設定。 |
| Pages creation | Public 開啟 | 允許公開 Pages；private 選項在頁面不可用。 |
| Team creation | 開啟 | org Member 可建立 Teams。 |
| 私有 repo fork | 關閉 | 不開放 private repo fork。 |
| Repository discussions | 允許 Read 使用者建立 | 在啟用 Discussions 的 repo，Read 使用者可建立及回覆討論。 |
| App access requests | Members and outside collaborators | 允許提出 app 使用申請，不表示 app 已獲安裝授權。 |
| Repo 管理員安裝 GitHub Apps | 開啟 | 依平台欄位限制，僅限不要求 org／repo administration permissions 的 App。 |
| Issue 刪除 | 不允許 repo 管理員執行 | org Owner 管理該項操作。 |
| 受 org rules 保護的分支更名 | 允許 repo 管理員執行 | 仍受 GitHub 頁面所示 rules 覆蓋或 bypass 條件限制，不表示所有規則可繞過。 |
| Repo 可見性變更 | 不允許一般 repo 管理員變更 | org Owner 管理該項變更。 |
| Repo 刪除／轉移 | 不允許一般 repo 管理員執行 | org Owner 管理該項操作。 |

設定來源：[Member privileges](https://github.com/organizations/AI-Native-Founders-TW/settings/member_privileges)、[Members team 的 repository 權限](https://github.com/orgs/AI-Native-Founders-TW/teams/members/repositories)、[Members 的子 Teams](https://github.com/orgs/AI-Native-Founders-TW/teams/members/teams)。登入管理者才能看見的設定不以公開首頁推定。

2026-11-01 API 補查：org 現址為 AI-Native-Global-Founders-Speedrun-TW，base permission 仍為 none；Members team 對 mono 已為 Triage（取代上表 Write 快照），Council parent 仍為 Members。mono 尚無 rulesets 或 main branch protection，Owner 僅 Johnny850807；App 自動化尚未配置。未重查的其他設定仍只代表上表日期。

## 審查通過後的 GitHub org 加入

自介正式通過後，邀請該申請者成為 org **Member**。邀請執行者須具有 GitHub 平台所需的權限；這項平台能力不取代組織的審查裁決權。依[審查制度](<../01-制度/[機制] 憲政制度.md>)，先由有權限的人完成 PR 合併，再由下方自動化發 Member 邀請；自動化未啟用或案件不適用時由 org Owner 接續；不選擇 Members、Council 或其他 Team，後續使用 Fork／PR。此一般加入流程不自行增減其他職責的 Team 與個別權限；另有有效權限變更決定時，依其範圍另外執行，不能以本流程為由拒絕撤權。

首屆任命及恢復資格的成員不需偽造一般審查或重做入會。平台接續由 Onboard 核對有效資格依據、本人帳號及生效時間，交 Repository 的合格操作人執行相同 Member 邀請程序：

| 資格來源 | 邀請前核對 | 紀錄位置 |
|---|---|---|
| 一般自介審查 | 正式通過結果與已合併 PR；一般新申請以 PR 合併時取得資格，合併前僅審查通過尚未生效。修訂前已有效成立的資格依憲政制度過渡規則保留，平台加入仍依本流程接續 | 原自介 PR |
| 首屆有效任命 | 公布的任命文件、本人接受、自介及 Contributors 等成立條件、共同生效時間、已核對 GitHub 帳號；不要求另外一份一般審查通過 PR | 首屆任命紀錄及相關 PR／Issue |
| 有效恢復 | 原有效資格與退出依據、原已驗證帳號、完整恢復聲明及有效 Contributors 選擇；不要求重寫自介或等待名冊合併才邀請 | 恢復案件與相關 PR／Issue |

三種來源均先確認目前 Members／Invitations；已存在不重送，缺少 Member 時才邀請，不選 Team，發送後與接受後分別記錄。首屆與恢復的歡迎訊息應如實說明資格來源，不套用「自介已審查通過並合併」的文字。資料不足時記錄待核對的具體依據，不把平台加入完成當成補足資格。

| 實際狀態 | 處理與可回報的結果 |
|---|---|
| 尚未有有效資格依據 | 不因資料初步核對或平台已有帳號就邀請。 |
| 資格已生效，尚未發邀請 | 依上表核對對應資格來源、本人 GitHub 帳號及目前 org 狀態，確保邀請正確的人。 |
| 已是 org Member | 不重複邀請，回報已確認存在；不能藉此補推歷史自介已通過。 |
| 已有相同對象的 pending invitation | 先核對邀請的角色與狀態，不盲目重送；尚未接受不能寫成加入完成。 |
| 已送出邀請 | 回報邀請已送出，請本人接受；以 GitHub 實際狀態確認後續。 |
| 已接受並出現在 Members | 才能回報 GitHub org 加入完成。 |
| 邀請失效或操作失敗 | 保留有效資格結果，如實記錄未完成原因；重試前重新核對對象與目前邀請，避免重複操作。 |

GitHub 的一般 org 邀請需本人接受，未接受的邀請七天後失效；平台要求的信箱驗證、雙因素驗證或可用席次可能影響接受與發送。這些是平台條件，不新增組織的背景或能力門檻。詳見 [GitHub 邀請說明](https://docs.github.com/en/organizations/managing-membership-in-your-organization/inviting-users-to-join-your-organization)。

邀請使用經核對的 GitHub username；不在公開 comment 放私人 email、邀請憑證或其他敏感資料。GitHub 自動發送的系統邀請與人工另寄 email 分開處理。

本規格保留人工審查與合併；合併後以 Python script、GitHub Actions 與 GitHub App 接續邀請及狀態核對。程式與 workflow 已在本地實作，尚未發布或啟用；啟用前沿用人工流程。權限不足不自動提高權限。


## 自動加入接續：Python script、GitHub Actions、GitHub App

### 範圍與來源

Onboard 需要在正式通過及合併後，免除逐人勾選 checklist、發邀請與確認接受的重複操作；例外仍由有權人接續。自動化不裁決資格、不核准或合併 PR、不接受邀請、不增減 Council、Team 或 repository 權限，也不撤銷成員資格。

第一版自動處理啟用後的一般初次申請；首屆任命、恢復、代提交、多人成員 PR、帳號變更及舊案，沿用上方資格來源的人工接續，不因此重做入會。啟用日期用環境變數保存；不把歷史自介檔案全部當成新邀請。

正式資格依據仍在原申請及制度；GitHub Members／Invitations 是平台現況來源。原 PR 中由 App 更新的一則進度 comment 只記接續狀態，不成為資格來源。不新增資料庫、後台、另一份名冊或常駐 server。

### Python script 的處理

檔案為 `scripts/排程/入會權限處理/process_onboarding.py`（入會接續程式）。提供預設唯讀的 `--dry-run` 與明確寫入的 `--apply`；兩者使用相同判斷，唯讀不發邀請、不留言。使用 GitHub REST API 與既有 YAML 解析依賴即可，不接 LLM。

1. 分頁取得啟用日期之後合併到本 repo main 的 PR，不只查當次 push 或近期幾小時。逐 PR 查 files、reviews、comments 及合併資訊；API 部分失敗不當成空資料。小型社群先完整查詢，不建立游標資料庫。
2. 一般新申請須只新增一份正式編號的 `members/` 個人 Markdown（排除 README），相關照片及本人 Contributors 變更；不可夾帶程式、設定或他人分工。新增者在合併前沒有既有自介，合併後檔案仍在 main，且目前仍有 Contributors。從自介的 GitHub 連結核對 PR 作者；username 以 GitHub API 解析為數字 user ID，對不上的轉人工，不只憑檔名或 PR 標題邀請。
3. 必須有非申請者、目前有效 Onboard Leader 的未撤銷 APPROVED review，review 的 commit_id 對上最終 PR head SHA。以現有 assignment 及其成員檔案取得帳號；檔案有值本身不是有效任命證明。啟用與交接前由 Repository 核對任職依據；職位空缺、資格不明、例外備援或 reviewer 已異動的舊案轉人工，保留原有效審查，不自動否定。審查人負責確認意圖、本人接受、利益迴避及具體異議；程式不得把一般留言解析成已裁決。一般新申請的正式通過文案放在最後 APPROVED review 正文，作為核對基準。首次邀請前存在尚未處理的 CHANGES_REQUESTED、該 review 後新增的人類留言／review 或已知資格異動時，停止該案自動邀請，由 Onboard 核對後人工接續；不讓無依據反對永久取消資格。這項保守檢查只阻擋新的寫入邀請，不阻擋已送出案件的唯讀 membership 查詢；申請者回覆「已接受」不會阻止平台完成確認。
4. 查實際 membership、pending 與 failed invitations。已加入者只更新狀態；曾確認完成但後來離開者不自動重邀。pending 邀請只回報等待，不重送；邀請 role 或 Teams 不符時交人工，不擅改既有權限。首次邀請固定 `role=direct_member`、`team_ids=[]`，用已核對的 user ID，不用私人 email。
5. 首次建立進度 comment 前由 App 自動建立／套用 `onboarding-started`（入會接續收據）label；它只表示開始處理，不是資格或人工 checklist。進度 comment 遺失時查 label 與 App 的 labeled timeline，任一存在便轉人工，即使 label 後來移除也不重邀；不得為重跑而刪除收據。發邀請前先在 App 自己的進度 comment 記錄本次準備發送，再呼叫 API，之後讀回 pending 或 active。若呼叫逾時、程序中斷或結果不明，下次先核對平台；已有準備發送紀錄但查不到可確認結果時轉人工，不盲目重送。這避免邀請已失效卻因上次中斷被當成首次發送。
6. 過期、取消或曾送出但已不在 pending／Members 的案件，保留未完成並交人工；依既有 SOP 確認本人仍想加入後由 Owner 重送。手動重跑 job 不等於批准重邀。已有效退出或資格停止案件不自動復原；目前 main／PR 資訊不足時保守停在待核對，不由程式猜測治理決定。
7. 每份 PR 最多維護一則 App 進度 comment，以固定隱藏標記和 App 作者身分共同辨識；別人貼相同標記無效。保存受邀 user ID、申請 PR 與 review 連結、發送嘗試／確認結果、已完成記錄及目前狀態；不保存 token、email 或完整 API payload。每次重新核對平台，狀態沒變不更新、不重複歡迎；人工正式 review/comment 不修改。完成時採用 SOP 歡迎文案，更新同一則 App comment。原 comment 缺失或遭刪除而無法確認既往嘗試的案件轉人工；首次上線的候選依啟用時間、完整 PR 歷史及沒有既有收據辨識。首次接管即使平台已 active 或 pending 也先查有效核准；有可信接續紀錄後才略過新增留言的首次發送阻擋，以繼續確認接受結果。
8. 單人資料問題不中斷其他案件；認證失敗、限流或平台不可用停止本輪並以非零 exit code 與 Actions summary 回報。遵循 Retry-After，重試僅限安全讀取；寫入結果不明先查回。摘要列需要 Onboard 處理的 PR 連結及原因，技術故障交 Repository。不新增另一套通知服務；原 PR 與 Actions 頁面作為入口。

### GitHub Actions 排程與 job

檔案為 `.github/workflows/sync-onboarding.yml`（入會接續工作流程）。一個 job 執行同一支 script：

- `push`：僅 main，處理新合併與既有未完成案件；不以 paths filter 漏掉設定修正後的補跑。
- `schedule`：`17 * * * *`，每小時第 17 分鐘補查；不是即時或準點承諾。
- `workflow_dispatch`：管理者手動補跑，可選 dry-run；僅允許 main 執行，不接受任意 username 直接邀請。
- 使用標準 `ubuntu-latest` runner、Python 3.12；job timeout 15 分鐘。固定 concurrency group，`cancel-in-progress: false`；只允許一個寫入 job 執行，排隊事件被取代也由下次完整查詢補齊。
- job 只從可信 main 取得程式，不 checkout／執行申請者分支、PR 中的程式或自介指令；外部字串不拼入 shell。第三方 actions 固定到審核過的完整 commit SHA。
- `GITHUB_TOKEN` 只需 `contents: read`；使用 GitHub 官方 create-github-app-token action 取得指定 org／mono installation 的短效 token，供 Python 呼叫 org 與 PR API。這不是把 Members 權限加到一般 GITHUB_TOKEN。
- 不用 pull_request_target、不接 webhook endpoint、不上傳驗證 artifacts、不建立 runner server。一般 PR 的測試不接觸 App 私鑰。

public repo 使用標準 hosted runner 的運算免費；不採付費大型 runner、付費 AI 或額外儲存。這是目前方案條件，不保證未來價格不變。排程可能延遲或漏跑，public repo 60 天沒有活動可能停用排程；Repository 接續者可手動啟用／補跑。每輪完整補查，不依賴上一輪必定成功。

### GitHub App 與環境設定

由已有權限的 Owner 在組織下註冊限本組織安裝的 GitHub App，停用 Webhook，不需要 callback server；安裝時 repository 範圍只選 mono。所需權限：Organization Members read/write（查詢與邀請）、Repository Contents read、Pull requests read/write（讀 reviews、timeline，維護 PR comment 及自動收據 label）、Metadata read。不要求 Contents write、Administration 或 Actions write。Members write 是組織層級能力，選 mono 並不把它縮成 repo 權限；程式只開放上述 Member 邀請流程。

在 mono 建立 `onboarding`（入會自動化環境），deployment branch 規則明確只允許 main，禁止同名 tag；不採「所有 protected branches」隱含放行方式。不設定每輪人工 deployment approval，以免把 checklist 換成每小時按一次同意。

環境配置：

| 名稱 | 類型 | 內容 |
|---|---|---|
| ONBOARDING_APP_CLIENT_ID | variable | GitHub App 的 Client ID |
| ONBOARDING_APP_PRIVATE_KEY | secret | Owner 產生的完整 PEM 私鑰；不進 repo、PR 或執行輸出 |
| ONBOARDING_START_AT | variable | 明確 UTC ISO 8601 啟用時間；不自動回填歷史申請 |
| ONBOARDING_ENABLED | variable | 預設 false；安全設定、測試與有權啟用確認完成才設 true |

org／repo 使用 workflow 的 repository context，必須等於本組織 mono；不讓 dispatch 任意指定目標。私鑰輪替、撤銷與 App 停用由 Repository 職責的有權操作者接續，不要求 Onboard 成為 Owner。

### 啟用與停用

1. Repository 有權者先確認有效 Onboard 任職、合併與異議處理責任、組織制度所需的有效啟用決定。使用者採納技術方案不代替 Council 等制度程序，也不任命 Chris。
2. 保護 main：要求 PR、至少一位非作者核准、核准後變更須重新審查、現有分工驗證及新增 script 測試成功，禁止 force push／刪除。自動化程式、workflow、依賴與 CODEOWNERS 的變更要求具有效 Repository 接續責任的 code owner review；實際帳號與 bypass 清單部署前核對，不直接給全部 Council。App 不列為 bypass actor。CODEOWNERS 不取代入會審查權。
3. 設定上述 App、環境與私鑰，先執行 dry-run；檢查有資格人、其他 PR、不完整資料與所有歷史案件均按範圍處理。沒有有效 Onboard Leader 時不可為了測通而指定 Owner 代替。
4. 通過測試並完成一次已授權真實申請的發送／接受核對後，再宣稱自動化已啟用；測試不得發給未授權的真實對象。若尚無適用申請，保留端到端待驗證狀態。
5. 故障時將 ONBOARDING_ENABLED 設 false 或停用 workflow，必要時撤銷 App 私鑰；不得因自動化故障撤銷已通過資格。回到 SOP 的人工接續，先查既有邀請避免重送。重啟後仍從原啟用日期補查，不重設日期掩蓋漏件。

設定的官方依據：[App 在 Actions 使用](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/making-authenticated-api-requests-with-a-github-app-in-a-github-actions-workflow)、[邀請 API](https://docs.github.com/en/rest/orgs/members#create-an-organization-invitation)、[Actions 排程](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule)、[Actions 費用](https://docs.github.com/en/actions/concepts/billing-and-usage)、[環境與 Secrets](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments)。


### 本地測試與首次設定

安裝 `scripts/requirements.txt`（驗證依賴），執行：

```sh
python -m unittest discover -s scripts -t . -p 'test_*.py'
python -m scripts.驗證.分工資料.validate
```

測試以模擬 API 執行，不需要 token，不會發邀請。Actions 的既有 Validate R&R assignments workflow 同樣執行全部 script tests。真實唯讀執行才需 GH_TOKEN、ONBOARDING_START_AT 與 ONBOARDING_BOT_LOGIN；bot login 由 token action 的 app-slug 加 `[bot]` 產生，不需使用者再維護一份帳號設定。Python 預設 dry-run；本地不要提供正式私鑰做測試。

Owner 的首次設定入口為組織 Settings → Developer settings → GitHub Apps → New GitHub App。Homepage URL 可填本 mono 首頁；Webhook Active 取消，不需 OAuth callback。按前述權限註冊並僅安裝到本 org 的 mono，產生私鑰後直接存入 repo Settings → Environments → onboarding 的 Secret，不貼在對話或 PR。

Environment 設定 Client ID、START_AT 與 ENABLED=false 後，先在 main 的 Actions → Sync onboarding → Run workflow 保留 dry_run=true。確認摘要與正式設定後，依啟用程序設 ENABLED=true。START_AT 使用實際決定的 UTC 啟用時間，例如 ISO 8601 的 `YYYY-MM-DDTHH:MM:SSZ`，不是照抄文件日期。workflow 未發布前不會出現在遠端 Actions 清單。
