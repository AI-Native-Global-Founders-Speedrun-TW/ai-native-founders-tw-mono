---
document_type: Plan
adopted: false
---

# dc infra 審視與改動提案

## 目前狀態

最新修正已恢復既有四項 Leader 對應，不因遷移清空；先前全填 null 的說法已撤回。最新採納為單一 assignment YAML：role、leader、contributors；Council 從有效 leader 去重，不另維護名單。目標為完成本地遷移、相關 SOP 與引用一致性及獨立 review，然後更新既有 PR。先前雙 YAML／產生表／工具設計均為歷史。本輪不合併 main 或更改 Discord，onboard 公開入口仍待合併後接續。

## 需求原文與範圍

> 新的session, new task
> 審視一下 dc infra
> catch up 最新進度，
> 看要做什麼改動，new plan for this

2026-11-01（Asia/Taipei）建立。已完成 Discord 入口更新；目前接續規劃 Council 角色、moderation 與協作空間，精簡角色與協作設計已採納，Council 名單與 SSoT 維護分析已通過，本地實作完成後接續 Discord 設定，見文末當期進度。以下至「初次盤點 Review」為初次盤點的歷史紀錄；已完成的平台結果見「本輪執行：Discord 更新」，目前設計採納與 SSoT 討論分列文末，不互相冒充完成。初次盤點交付為最新進度盤點、Discord 與 repo／網站的差異、可 review 的改動提案及執行順序。盤點當時文案與配置提案尚未採納；當時不修改 Discord、不發布、不 push，也不接續其他邀請工作。

本 Plan 回應既有 [Discord 加入、交流與活動 Problem](<../../specs/05-社群基建/[規格]Discord-社群-Setup.md#discord-加入交流與活動>)，不另建組織制度。Kickoff 的啟動歷史留在[原 Plan](../001-Kickoff/plan.md)，本次不重新啟動已完成設定，也不以歷史待辦覆蓋最新實況。

## As-Is 盤點現況

### 版本與可核對範圍

| 來源 | 2026-11-01 的實際結果 | 使用限制 |
|---|---|---|
| 本機 mono | main（目前本機分支）；HEAD 為 6fc2da0（邀請開頭官網）；fetch 後相對 origin/main（遠端主線）領先三筆、落後四筆 | 保留原有邀請日誌、招募 SOP、另一份 Plan、入口及網站未提交修改，未 pull／merge／reset／stash。 |
| 遠端 mono | dadc191（品毅自介合併），13:06:43；本次以 git show 核對最新檔案 | 遠端比本機多 Sun、Yapi、品毅自介與 Sun 活動分工更新；本機三筆邀請文件 commit 尚未在遠端主線。 |
| 網站 submodule | mono 指向 cac75de（網站文案視覺）；本機同版本上另有未提交修改 | 本機修改不是 mono 已收錄或已部署版本，未改 submodule 指標。 |
| Discord | 已登入 owner 帳號，唯讀檢查 App 與 Chrome 的 server、頻道、公告、設定頁 | owner 畫面不代表一般新人畫面；以下另列設定證據與尚待新人實測的部分。 |
| 正式網站 | https://aifounders.tw/ 與 https://aifounders.tw/join/ 均回應成功，核對其已發布 HTML 與實際 href | 沒有操作產生器送出 PR，亦未以本機 source 取代正式網站的證據。 |

版本比較基準：[本機起點](https://github.com/AI-Native-Global-Founders-Speedrun-TW/ai-native-founders-tw-mono/commit/6fc2da0)、[遠端起點](https://github.com/AI-Native-Global-Founders-Speedrun-TW/ai-native-founders-tw-mono/commit/dadc191)。盤點時間為本日約 13:13 起；交付前重新核對遠端有無新進度。這是一次盤點，並非所有後續變更的持續監控。

### 已完成、文件已有但尚未驗證、以及已變更但未更新的部分

| 對象與具體位置 | 當下內容或行為 | 對照與判定 |
|---|---|---|
| Discord 頻道列表 | 五個 category：start-here、community、get-involved、voice、management；九個公開文字／論壇頻道、meeting 語音與私有 mod-log | 結構主要已建立。語音仍叫 meeting，welcome 公告及 specs 卻寫 lounge；不能從名稱推定是同一個 channel，須先比對 ID 與原聊天。 |
| [onboard](https://discord.com/channels/1563453138810306612/1563456791050977341) topic、2026-10-26 20:29 公告及釘選系統紀錄 | topic 寫「自介審查通過後成為組織成員」。公告將「可以幫什麼忙、想要幫什麼忙」稱 R&R；檔名寫 GitHub 帳號加副檔名；「變更只有自己的自介」 | 與 [members 提交說明](../../members/README.md) 不同：真人照片、Contributions、獨立 assignment 的 Contributors 選擇及 pending 檔名均未完整帶到。該訊息有釘選紀錄，不能只另貼新訊息讓舊釘選繼續誤導。 |
| [welcome](https://discord.com/channels/1563453138810306612/1563453141641597000) 2026-10-26 公告與 topic | 有組織介紹、onboard／rules／提問／協作／活動入口，repo 用舊 org URL，語音寫 lounge | 導覽已有，保留用途，只同步實際入口與 canonical repo。另有 2026-11-01 13:11 新訊息鼓勵依組織願景辦活動；這不是替所有人完成任命或新增無限制對外授權。 |
| [rules](https://discord.com/channels/1563453138810306612/1564249902475907172) 公告及 topic | 開放交流、自願貢獻、禁止特定公司推銷／付費置入、Discord 不等於入會；repo 使用舊 org URL | 規則方向與憲法相符，更新連結即可，不另加篩選門檻。 |
| [announcements](https://discord.com/channels/1563453138810306612/1564249954266914846) topic | 寫「由既有管理者發布」；當下載入的訊息列表沒有公告正文 | 現行平台規格改為「具有效公告職責與平台能力的人」。需要更正文字，不能藉此直接給全部 Council 管理權。空頻道本身不是新增公告義務的依據。 |
| Server Settings → Onboarding | Enabled；預設模式；九個 Default Channels；Questions 顯示 Set up；Server Guide 開啟 | 這些主要設定已完成。預設頻道預覽包含九個公開文字／論壇與 meeting，不列 mod-log。無須重新建置或新增問卷。 |
| Onboarding → Server Guide | Welcome Sign 有舊「審查通過後成為成員」；三項任務為 onboard、collaborations、events；未設 Resource Pages | 第一項 Edit task 實查選中 Member visits the channel。第二、三項存在與目的頻道已確認，完成條件及 Next 串接尚未逐項實測。 |
| Server Settings → Roles → Default Permissions | 角色列表當下僅 @everyone。View、Read History、發文／論壇回覆、Connect、Speak、Create Events 開啟；Manage Events／Server／Roles／Channels、Administrator 與大量提及關閉 | 一般交流與建立本人活動的基礎權限已開，不能說尚待新增 Member 才能交流。未驗證所有 channel overwrite 或新人實際發文。 |
| start-here → Permissions | @everyone 四種發文／討論串建立權限為 Deny；View 為繼承 | 分類唯讀已配置；四個子頻道是否同步及個別覆寫仍要逐一核對。 |
| mod-log → Permissions | 與 management 同步；Private Channel 開啟；@everyone View Channel 為 Deny；可存取名單只顯示 owner | 私有管理紀錄已有保護；未證成第二位可接續者。topic 仍寫「伺服器擁有者及既有管理者」，與現行有效職責措辭不同。 |
| Community Overview／Engagement／Safety Setup | rules 為規則頻道、mod-log 為 Community 與 Safety 更新；系統訊息在 chit-chat；Only @mentions；四種系統訊息開啟；所有成員媒體過濾 | 已配置項不重做。AutoMod 詳細頁兩項規則均啟用、Block message 並警示至 mod-log；Mention Spam 限制為二十個不同提及。未實際觸發規則，也未核完信箱驗證及 timeout 選項。不能以摘要頁的計數推翻詳細設定。 |
| Server Settings → Invites | 現行網站邀請 https://discord.gg/xeWYqYaUvU 出現在 Active invite links，指向 collaborations，期限為無限 | 不需要因網址舊或入口不在 onboard 就重建邀請；設定存在不等於新帳號完整加入實測完成。 |
| events forum | 活動指南已說明所有加入者可建立本人 Events，Interested 不等於另行報名；可見「想問矽谷大佬關於創業出海的問題」活動帖 | 活動空間已有內容。網站使用該活動串網址；一般新人是否可沿網址讀取／回覆及有無已結束資訊仍待核對，不猜測活動已失效。 |
| 遠端 members 與 assignment | Sun、Yapi、品毅自介已合併，水球先前已合併。assignment 新列 Sun 活動 Leader；品毅基建 Leader 明列任命及生效依據待核對；Onboard Leader 待確認 | 合併不是所有正式資格、Leader 任命或 GitHub org 接受邀請均已成立的證據。先核資格適用規則、有效審查／任命與本人接受；不能照名單直接賦權。 |

### Repo、Agent prompt 與網站加入入口

1. [README Quick Start](../../README.md#quick-start) 已有先理解組織、再逐題引導自介的 Agent 入口；完整欄位與提交位置交 [members](../../members/README.md) 及其 SOP 維護。Discord 還在維護另一套舊手動步驟，應回到同一個現行來源。
2. 舊 org 的 repo 根網址回應成功並轉址到新 org，因此是「仍可用但應更新」。README 的 clone prompt、平台 specs、SOP 等仍有舊 org；更新有效入口，不改寫歷史原話。
3. 正式網站的 Members/README（自介說明入口）、constitution（舊憲法路徑）及舊申請制度文件三個 href 均回應找不到頁面。小寫 members 的新 org 入口已確認可讀。這是檔案路徑失效，不能只換 org 名就宣稱修好。
4. [加入頁文案 specs](<../../specs/04-Web/landing-page/[文案]加入頁.md>) 已寫真人照片、Contributors 與審查／合併的區別；正式網站仍寫「審查通過後，就是成員」，並未同步全部要求。本機網站已有 pending 檔名與部分連結修正，但未提交、未部署；不能重寫這批工作或當成已發布。
5. [憲政制度的切換條件](<../../specs/01-制度/[機制] 憲政制度.md#申請與成員資格>) 明定入會生效點修訂須有有效採納與公布時間，不能因 commit 自動生效。採納證據尚未核實，故發布文案先引用「依適用的有效制度核對資格」，不擅自回溯取消舊資格，也不以平台公告啟動新資格規則。

## 使用者目前覺得的 Problem

以下是本次審視提出、尚待 review 的具體問題；完整共通 Problem 仍由 Discord 平台規格維護。

### 新人理解組織並知道如何加入

onboard 公告、README、members 說明與已發布網站的操作內容不同；網站三個規則／提交入口失效。新人容易找不到現行要求，或照舊公告漏交照片與 assignment。對應[既有 Problem](<../../specs/05-社群基建/[規格]Discord-社群-Setup.md#新人理解組織並知道如何加入>)。

### 志工容易號召工作並找到願意一起做的人

（構思中）

平台已有協作與活動空間，但入口沒有清楚接到現行 GitHub Issue、assignment 與本人接受工作的規則；管理／公告文字仍以「既有管理者」作指涉。最新分工尚未核實任命與平台接續，不能把列名當完成。對應[既有 Problem](<../../specs/05-社群基建/[規格]Discord-社群-Setup.md#志工容易號召工作並找到願意一起做的人>)。

## To-Be 目標

1. 新人先理解組織、交流與提問，再自行決定是否申請；Discord、Server Guide、README 與網站能到達同一份現行申請來源，依 [members](../../members/README.md) 完成自己相關的自介、照片及 assignment。
2. 保留現有公開交流、協作與活動；依 [Discord 平台規格](<../../specs/05-社群基建/[規格]Discord-社群-Setup.md>) 核對一般加入者權限。導覽完成不代表入會、接受工作或報名。
3. 依[基建 Role](<../../specs/02-R&R/[Role]基建-Repository維護.md>)核對公告發布與第二人接續；未任命、無人接受或能力未驗證均如實留下，不以新增 Council Administrator 解決。

## 初次盤點工程摘要與優先順序（歷史）

先修失效入口與會讓申請者漏件的文字，再核對新人完整路徑與現行頻道引用；管理接續的證據核對可同時進行，新增權限必須等有效決定。所有外部操作仍須使用者 review 確切內容與授權後執行。

| 順序 | 改動對象、現在的問題與 impact | 建議工作、完成依據及依賴 | 執行責任與狀態 |
|---|---|---|---|
| 最先處理 | 正式網站的自介說明、憲法及制度連結失效，阻斷理解與申請 | 先沿用網站既有修改，將 links 的路徑對回現行檔案並統一新 org；所有實際 href 可開啟。網站規則差異先核適用制度，不發布未生效規則。部署後重查正式頁，不以 build 當完成。 | Hacker 與網站現有協作者核對；本 Plan 未指定人員已接受，未實作／部署。 |
| 最先處理 | onboard 舊公告缺真人照片與獨立分工，錯把 Contributions 稱 R&R，檔名及「只改自介」錯誤 | 以[候選文案](改動提案.md#onboard-釘選訊息)取代原釘選訊息；新增 README Agent 入口並保留手動入口。同步 topic、Server Guide 的資格指涉；發布前核制度適用條件。回讀原訊息與釘選，不只新增第二份。 | 公關文案、Onboard 內容核對，既有具操作能力者執行；職位空缺不冒用職權。初次盤點時僅提案；目前 Discord 範圍已授權執行。 |
| 接著處理 | welcome 語音 lounge 與實際 meeting 不同；announcements／mod-log 用舊管理者措辭 | 先核語音 channel 身分與原文聊天，再依既有 specs 將實際入口同步為 lounge，保留原聊天與邀請；若有有效新決定採 meeting，改對應規格與全部有效引用，不先任意新建或刪頻道。公告與管理 topic 改為有效職責措辭，連結改 canonical。 | 基建維護範圍；待比對語音 ID 與有效決定，不把 owner 目前能力當制度職位。 |
| 接著處理 | 目前只有設定證據，沒有一般新人端完整走查 | 不更動已符合的九頻道、問卷與三任務。用已授權的一般測試帳號／願意協助的新加入者，確認邀請→Guide→交流→README→申請；先看 role preview，再實際驗證發文／活動權限。若需建立測試訊息或活動，先授權並標示測試。 | 尚未找到已接受測試者；不為測試建立新永久 Role 或變動成員資格。 |
| 同步查證，權限操作排在有效決定後 | Roles 僅 everyone，mod-log 只有 owner；未有第二位有效 Leader 的接續證據，owner 不可用時恐無法維護 | 核對品毅、Sun 及首屆任命的原始決定／本人接受／生效；按現行制度為兩位不同有效 Leader 準備帳號、最小必要能力及恢復路徑對照。第二人 Role 必須已有明列責任，沒有則走擴權程序。分別驗證存取、操作與恢復，不分享 owner 帳密。 | 待有效任命、本人接受與權限核對；不得直接給品毅或 Sun Administrator。 |
| 上述完成後 | repo 與平台易再出現不同說明 | 同批更新有效 README prompt、Discord/GitHub setup、相關 SOP 與網站 links，保持同一來源；協作／活動指南補既有提議 SOP 入口並引用 Issue，不把日常交流全部改成開 Issue。 | 依原維護職責接續；不新增定期工作、bot 或強制參與義務。 |

### 規格差異

初次盤點階段沒有修改 specs。當時需求授權為審視與新的改動提案，尚未採納候選文案及尚未核完資格規則的適用證據；不以 Plan 取代 truth。上表是待執行工作，不是已寫入規格的 delta。

後續預定修改的 truth 位置為 [Discord Setup](<../../specs/05-社群基建/[規格]Discord-社群-Setup.md>)、[GitHub org Setup](<../../specs/05-社群基建/[規格]GitHub-Org-Setup.md>)與相應[網站文案](../../specs/04-Web/landing-page/README.md)；各項實際寫入後再列出規格差異，分別對應上方兩個 Problem。候選文案本輪只在附件供 review，採納後應放回對應文案／平台規格並改成引用，避免在 Plan 長期維護另一套規則。

## 驗收與尚未驗證處

### 本輪盤點完成依據

- [x] 已看使用者截圖，且重新唯讀核對實際 onboard 文字、頻道列表與規格差異。
- [x] 已 fetch 並分開核對本機、遠端主線、網站 submodule 與正式網站；保留既有修改。
- [x] 已讀現行基建、憲法／制度、Role、入會與協作 SOP、members／assignment 與 Plan 入口；最新 assignment 以遠端版本核對。
- [x] 已將主要設定的實際值、文案差異與未驗證處分開；這些勾選不代表平台修正完成。

### 初次盤點提出的後續驗收（歷史清單，當期結果見文末）

- [ ] 從正式首頁及加入頁開啟自介說明、憲法、制度、GitHub 與 Discord；路徑、大小寫及目的地正確。Agent clone prompt 可取得新 org 的正確 repo，保留既有本機修改。
- [ ] 從有效邀請以一般加入者身分進入；能看到九個預設公開頻道、閱讀歷史、在 chit-chat 求助及論壇發文／回覆；不能寫入口四頻道或看 mod-log。
- [ ] 逐個核對四個入口 channel、三個 forum 與語音權限覆寫；設定頁與一般帳號行為相符。@everyone 無管理全部活動、頻道、角色或 Administrator。
- [ ] Server Guide 三項任務逐一核對 visits 完成條件與 Next 的 onboard→collaborations→events；不需先完成任務才可進公開頻道，不強制發文。
- [ ] 原 onboard 釘選內容、topic 與 Guide 一致指回現行要求，自己相關的自介／真人照片／Contributors 變更都有明確來源；不以 AI 草稿或配置編號宣稱入會。
- [ ] 一般加入者可建立自己的活動；不能管理別人的活動。網站活動串可到達且可回覆；另有報名條件時 Interested 不取代報名。
- [ ] 語音 channel 身分與歷史核對完畢，再同步名稱／說明／邀請及有效引用，不遺失既有聊天。
- [ ] 信箱驗證、AutoMod response／不自動 timeout 與安全設定逐項核完；本輪未實際觸發垃圾訊息或大量提及。
- [ ] 管理接續具有效決定、兩位本人帳號、Role 接續責任與實際能力驗證；不足就保留受阻，不勾完成。

以上新人端發文／回覆／Events、全部 channel overwrite、後兩項任務完成條件、Next 實際行為、信箱驗證及第二人恢復能力均未完整實測。未以登入頁、owner 可見、文件完整或設定預覽作為實測通過。

## 初次盤點 Review 與憲法檢查（歷史）

2026-11-01，獨立 background reviewer 已讀本輪新檔全文及實際 new-file diff、Plan 入口增量、受影響引用、FORMULATION 全文與憲法全文。範圍為本 Plan、候選改動附件、決策紀錄、當時的原始需求紀錄（未納入本次提交；原話見本 Plan 開頭）及入口新增列；既有其他工作未列入本次通過結論。

### FORMULATION review

已修正 Plan 入口的表格中斷，決策紀錄以追加方式補齊可點擊引用，保留原紀錄。終版檢查沒有其餘問題：truth、候選提案及平台完成狀態分開，引用可定位，沒有將 assignment 列名或本機網站修改當成已生效任命與部署。沒有修改 specs 的原因已在規格差異說明。

本輪 git diff --check 與決策 append 檢查通過；新增文件的本機 Markdown 路徑均可定位，候選文案中的四個 GitHub 目的連結實查成功。用詞檢查只報出「審查通」這個不完整斷詞，放回原句是既有「審查通過」，未形成新名詞。交付前再次 fetch，遠端主線仍為上述盤點版本。沒有測試程式或部署改動，未將文件檢查當成新人端驗收。

### 憲法檢查

| 條文 | 終版獨立檢查結論 | 依據 |
|---|---|---|
| 第 1 條（名稱與目的） | 沒有違反 | 改善開放交流與組織理解，維持原目的。 |
| 第 2 條（公益非商業） | 沒有違反 | 未新增推銷、置入或分潤。 |
| 第 3 條（效力制度分工） | 沒有違反 | 候選保持未採納，適用制度先核實，不以公告更新啟動規則。 |
| 第 4 條（開放成員資格） | 沒有違反 | 未入會仍可交流，資格不由帳號、合併或編號單獨推定。 |
| 第 5 條（自願參與義務） | 沒有違反 | Contributors 不等於接受工作，測試須本人願意。 |
| 第 6 條（分工議會組成） | 沒有違反 | 平台能力與有效 Leader／Council 分開，第二人須有有效責任。 |
| 第 7 條（決策任命範圍） | 沒有違反 | 未任命或擴權，後續仍依有效程序。 |
| 第 8 條（平等有效表決） | 沒有違反 | 沒有改變票權、分母或門檻。 |
| 第 9 條（罷免職位替換） | 沒有違反 | 未撤任或替換職位。 |
| 第 10 條（異議資格保障） | 沒有違反 | 保留既有有效資格，不以修入口回溯改判。 |
| 第 11 條（利益緊急界線） | 沒有違反 | 不移入私人資料／憑證，不共用 owner 帳密或自批權限。 |
| 第 12 條（修憲成員監督） | 沒有違反 | 未修憲、減權或追溯改算案件。 |

此段檢查限初次盤點文件與提案。後續使用者已授權 Discord 文案與設定更新，見下方執行紀錄；不包含新增管理權。adopted 維持 false 表示尚未完成 Plan 最終交付，不表示缺少本輪執行授權。


## 本輪執行：Discord 更新

### 需求原文

> 給我 to-be 你即將 bring what changes into discord接下來就要你用 computer use 去更新囉

> ok set a goal for this and do all them
>
> onboard 記得應該可以叫大家直接去下 prompt，改一個方式就和邀請訊息類似

已建立 goal，依決策 002（授權社群更新）執行 Discord 更新。Onboard 改為直接提供可貼給 Agent 的完整 prompt，與邀請訊息相同引導意圖：先認識組織，待本人想申請後再按現行 SOP 辦理；保留手動入口與自願參與。這是對外入口與文案更新，不任命管理者、不擴大管理權，不接續 Threads 邀請，不改其他網站協作者工作。

### 本輪已寫入的規格差異

- [Discord Setup](<../../specs/05-社群基建/[規格]Discord-社群-Setup.md#onboard-釘選文案>)：直接 Agent prompt、onboard topic、Guide 歡迎與第一項導覽文字及有效 GitHub 入口已寫入。對應[新人理解組織並知道如何加入](#新人理解組織並知道如何加入)。規格已寫入不等於 Discord 已更新；實際結果在下方逐項記錄。

### Discord 實際執行結果

2026-11-01 約 13:45–14:00（Asia/Taipei），以登入 owner 的 Chrome computer use 執行，下列項目均保存後回讀。只更新原訊息與原頻道；驗證截圖、UI 快照及原內容備份只存本機 /tmp/ai-native-dc-update-20261101，不版控。

- [x] [onboard 原釘選](https://discord.com/channels/1563453138810306612/1563456791050977341/1564254596208271400)：換成完整可複製 Agent prompt，保留手動入口、自願參與與有效制度指涉。Pinned Messages 面板顯示更新內容，原訊息與釘選不變。
- [x] onboard topic：指向原釘選 prompt 與 canonical repo，移除舊的資格生效點文字。
- [x] [welcome 原公告](https://discord.com/channels/1563453138810306612/1563453141641597000/1564254698024869990)與 topic：補組織建設中、先交流與 Agent 引導，保留導覽、原回覆與聊天，更新 repo 入口。
- [x] [rules 原公告](https://discord.com/channels/1563453138810306612/1564249902475907172/1564254512342900798)與 topic：保留原規則，只更新 canonical repo。
- [x] announcements／mod-log topic：改為有效職責與平台能力的文字；未更動任何角色或權限。
- [x] Server Guide Welcome Sign 與第一項文字：已保存並由預覽回讀。三個自訂任務仍是 onboard、collaborations、events，逐項設定均為 Member visits the channel；未新增問卷、Resource Pages 或任務。
- [x] 語音 meeting 已在同一頻道更名為 lounge。Copy Channel ID 與 specs 連結相同；原用途訊息就是 lounge，原聊天、反應與歷史均保留，沒有新建或刪除頻道。
- [x] Discord「viewing the server as a new member／no roles」預覽：Guide 顯示新歡迎文案；第一項進 onboard，Next 進 collaborations，再 Next 進 events，完成計數為三項。四個入口頻道均顯示沒有發文權限；chit-chat 顯示輸入框，協作與活動顯示 New Post，mod-log 未出現在列表。此為平台預覽，不冒充真人新帳號或實際發文測試。

### 本輪範圍外與仍未實測

- 本輪未新增任何管理角色、任命或接續者，也未變動成員資格。第二人的有效職責與實際接續仍須另外核對。
- 未部署或修改網站；官網失效連結與申請頁差異仍是待處理事項。
- 未使用真人新帳號加入，未送出測試訊息、論壇帖或 Events；不能宣稱新人端完整操作測試通過。沒有實際觸發 AutoMod，安全設定的其餘歷史待核項仍未驗證。
- 更名時讀到原語音聊天有前一日的分工討論；這是新的可追溯來源，不能繼續宣稱完全沒有任命線索，但本輪未裁定它是否已完成正式程序，也未依聊天直接賦權。


### 本輪終版 Review 與憲法檢查

獨立 background reviewer 依 FORMULATION 全文、憲法全文、改動檔全文與實際 diff 複查本輪產出。歷史盤點與當期授權的衝突、附件重複維護候選文案及語音舊現況均已修正；最終沒有剩餘問題。用詞快速檢查已重建語料，沒有需裁決的自創詞。git diff --check 通過。Reviewer 檢查文件與記錄一致性，未獨立操作瀏覽器；平台保存與預覽結果由執行者回讀。

| 條文 | 終版結論與依據 |
|---|---|
| 第 1 條（名稱與目的） | 沒有違反：改善組織理解、交流與參與。 |
| 第 2 條（公益非商業） | 沒有違反：沒有推銷、置入或分潤。 |
| 第 3 條（效力制度分工） | 沒有違反：入口更新未創設資格或任命。 |
| 第 4 條（開放成員資格） | 沒有違反：先交流、依意願申請，Discord 不等於入會。 |
| 第 5 條（自願參與義務） | 沒有違反：Contributors 不等於接受指定工作。 |
| 第 6 條（分工議會組成） | 沒有違反：未新增職位或平台管理權。 |
| 第 7 條（決策任命範圍） | 沒有違反：未以維護入口替代任命或擴權。 |
| 第 8 條（平等有效表決） | 沒有違反：未改票權、分母或門檻。 |
| 第 9 條（罷免職位替換） | 沒有違反：沒有撤任或替換。 |
| 第 10 條（異議資格保障） | 沒有違反：沒有回溯取消資格或限制異議。 |
| 第 11 條（利益緊急界線） | 沒有違反：沒有公開私人憑證、自批擴權或共享帳密。 |
| 第 12 條（修憲成員監督） | 沒有違反：未修憲、減權或追溯改算案件。 |

入口更新交付當時，授權的 Discord 更新已完成，Plan 尚在延伸。其後使用者已採納精簡 Council／moderation 設計；目前整份 Plan 仍擴充名單維護設計，未作全 Plan deliver，metadata 保留 false。後續網站、真人新人操作測試與管理接續不因入口更新完成而勾選。


## 接續規劃：Council角色、moderation與協作空間

### 需求原文與範圍

> 針對 council 的部分，你覺得 dc role 設計該怎麼做， council as moderators 的 category 等等的 collaborate channels 設計等等的想一下整體

> ok 整體分析完了？和另一個帶整體觀點批判帽子的討論一遍

> 不要放 logs
> 應該進去 dc 那個 plan continue to extends it

依決策 003（延伸基建計畫），延續同一 Plan；Council 原提案、批判、撤回及修訂集中在 [Council 角色與協作空間討論](Council角色與協作空間討論.md)，不再散放 logs。原先是接續規劃授權；其後使用者依決策 004（採納精簡設計）採納修訂後整體提案，已同步 Discord Setup。未授權指定人員、賦權或任命。前一節已完成的 Discord 入口更新保持其完成狀態。

### 現況與本次要處理的 Problem

接續上方[志工容易號召工作並找到願意一起做的人](#志工容易號召工作並找到願意一起做的人)：Council 需要容易協調跨 R&R 工作，成員應能自行發起共同事項，社群維護須有人能實際接手，不因新增工具增加志工負擔。這是本次候選 Problem 摘要，不冒稱使用者已確認完整新設計。

- 現有 collaborations、announcements、lounge 與私有 mod-log 已可承接工作、通知、即時討論及平台警示；目前沒有證據顯示討論量已使 collaborations 擁擠或難找。
- 盤點時 mod-log 存取名單只有 owner；第二位接續者的有效職責、本人接受及實際平台能力尚未完成驗證。名單、遠端更新與語音討論有新線索，不能據本機待確認欄位宣稱沒有有效 Council。
- [憲法的 R&R 與 Council](../../specs/01-制度/憲法.md#第-6-條rr-與-council)、[憲政制度的職位與權限交接](<../../specs/01-制度/[機制] 憲政制度.md#職位與權限交接>)及 [Repository 職責](<../../specs/02-R&R/[Role]基建-Repository維護.md>)是現行邊界；平台技術維護不自行包含內容審查，Council 身分不自動帶入全平台管理權。

### 批判後的整體提案（設計已採納，平台待配置）

先把真人承接、現有工作與通知入口接好，再按實際需要增加頻道。原先新增公開 governance category、council-updates、proposals、私有 council-chat／mod-chat 與 Member role 的建議暫時撤回；沒有證據證明這些新增空間已比既有工具更有效率。完整理由及交鋒見[討論附件](Council角色與協作空間討論.md#整體觀點批判與交鋒)。

1. Council role 僅作有效 Leader 身分辨識與通知；Moderator 能力依本人接受的有效職責另行配置，Council 可以兼任，但不自動整批取得管理權。
2. 共同事項與具體工作沿用 collaborations，一件工作一帖，以 tags 區分；正式案件連回 repo 原案。announcements 整理重要通知與結果，不成為成員提案必須等管理者代發的關卡。
3. 非敏感跨 R&R 協調留在原工作帖或既有語音；影響下一步的結論回到原案。暫不新增公開或私有協調頻道，後續依具體漏案、難找或協調需求重新比較。
4. 邀請擴大前預備 moderation，不等待第一個受害事件：先確認警示接收人、敏感私訊聯絡人與非涉案備援，明定必要暫時處置及覆核。敏感正文不丟進公開 Forum／Issue，也不因 Council 身分全面開放原始證據；不先給廣泛 Timeout／Kick／Ban 或角色管理能力。

### 後續順序、未決與驗收

先核有效 Council 與帳號對應，再核兩位不同有效 Leader 的技術接續與實際能力；接著明定 moderation 的承接者、日常範圍與非涉案覆核，依適用程序確認職責及權限後，才準備確切 Discord 改動。技術接續與 moderation 不是同一項資格，不能以其中一項完成代替另一項。

仍須確認的事項包括完整有效任職依據、接續者本人接受、誰實際接警示及敏感訊息，以及新 moderation 職責應由哪個 R&R 承接與適用決定程序。沒有在本輪指定人員、裁定任命或把候選補成 truth。

- [x] 使用者確認修訂後整體提案，依決策 004（採納精簡設計）同步 specs；未勾選後續人員與平台操作。
- [ ] 有效任職、本人接受與實際平台能力分別核對，不能只看 Discord role 名稱。
- [ ] 準備的設定讓正式成員可自行通知原案，沒有增加 Council 背書或管理者代發門檻。
- [ ] 已接受的聯絡人實際收到警示、可接案，原聯絡人涉案時有合格非涉案接續；缺少時明列未完成。
- [ ] 若後續執行權限變更，逐角色預覽公開交流、四入口唯讀、私有資料存取及管理能力，保留現有討論。

初次延伸僅改 Plan 與附件；本輪已依使用者採納同步 Discord Setup 的 Council 身分、Moderator 能力、既有協作入口與接續設計，平台仍未改動。

初次搬移的歷史 review：獨立 reviewer 當時回讀 Plan、討論附件、決策紀錄、入口與原 log：搬移完整、引用可接續，FORMULATION 沒有剩餘問題；憲法第 1 條（名稱與目的）、第 2 條（公益非商業）、第 3 條（效力制度分工）、第 4 條（開放成員資格）、第 5 條（自願參與義務）、第 6 條（分工議會組成）、第 7 條（決策任命範圍）、第 8 條（平等有效表決）、第 9 條（罷免職位替換）、第 10 條（異議資格保障）、第 11 條（利益緊急界線）及第 12 條（修憲成員監督）均沒有違反。該次檢查限初次文件搬移與接續規劃，不代替本輪採納同步及新 SSoT 設計的 review，也不代表已核定任職或完成平台操作。


### 本輪採納的 To-Be 與規格差異

前輪精簡設計已依決策 004（採納精簡設計）寫入 [Discord Setup 的 Council 與 Moderator](<../../specs/05-社群基建/[規格]Discord-社群-Setup.md#council-身分與-moderator-能力>)、[技術接續與敏感事件處理](<../../specs/05-社群基建/[規格]Discord-社群-Setup.md#技術接續與敏感事件處理>)及[共同事項與跨 R&R 協作](<../../specs/05-社群基建/[規格]Discord-社群-Setup.md#共同事項與跨-rr-協作>)：以有效分工辨識 Council，治理身分不自動帶入 moderation／技術能力；沿用現有協作入口，技術接續與敏感事件須有真人承接。對應[志工容易號召工作並找到願意一起做的人](#志工容易號召工作並找到願意一起做的人)。這是組織規格的設計同步，不證明正式程序、任職或平台操作完成。

## Council list 與 SSoT 維護的接續討論

以下保留本輪授權前的調查與候選設計脈絡；最新採納範圍、分析與實作狀態見[本輪分析與本地實作](#本輪分析與本地實作)，不將歷史的「尚未採納」視為當期狀態。

### 需求原文

> ok go adopt them
>
> /sf-ai 然後啊 council list 在本專案中，是不是也沒有 maintain 好
>
> 這樣很難對應管理，請給一些 SSOT 的設計來讓這一切 maintainable?

前輪整體設計已採納；本次接續同一分工與平台對應管理情境，補查名單維護的實際困難。既有[成員識別與資料](<../../specs/01-制度/[規格]成員識別與資料.md>)已將個人資料、資格證據與分工分開；本次不先把它們合併成另一張手填總表。新 SSoT 資料結構及衍生名單仍為提案，未修改 assignment、個人資料或資格規則。

### 已查到的現況

獨立盤點以 GitHub 即時 main 與 origin/main 核對，兩者同為 dadc191（品毅自介合併）；本機 HEAD 仍是較早的 6fc2da0（邀請開頭官網）。未 pull 或覆蓋工作樹。以下遠端證據連結固定到查核版本，避免把本機舊 assignment 當成最新現況。

- [遠端 assignment](https://github.com/AI-Native-Global-Founders-Speedrun-TW/ai-native-founders-tw-mono/blob/dadc191085ffdb2f23a993233953f0d0c4e678b8/members/r-and-r-assignment.md)已有 Sun 活動 Leader 與品毅 Repository Leader 的安排；後者明列任命及生效依據待核對。原規格已要求 Leader 附有效決定、本人接受與生效時間，並非沒有 SSoT 規則。
- [Sun 活動 Leader 更新](https://github.com/AI-Native-Global-Founders-Speedrun-TW/ai-native-founders-tw-mono/pull/9)已合併；[Sun 自介](https://github.com/AI-Native-Global-Founders-Speedrun-TW/ai-native-founders-tw-mono/pull/8)區分本人願意接受與尚未具備共同生效依據。不能把表格列名或 PR 合併當成完成全部任職條件。
- [Kickoff 的首次建立與首屆任命](../001-Kickoff/plan.md#首次建立與首屆任命)仍須完整首屆名單、本人接受及共同生效條件的核對。repo 尚未承接完整依據，不等於外部完全沒有證據，也不等於可自行取消既有資格。
- 目前身分規格有 Member ID 與 GitHub 帳號，沒有穩定的 Discord 帳號對應；平台能力的既有觀察也不是現行 Council 名冊。

### 本輪位置與待確認內容

名單與帳號對應的維護仍在構思中。要解決的是：接續管理者在任職、分工或帳號改變時，應容易確認有效負責人、依據及平台操作差異；同時避免再手填 Council 名單、從缺少資料推定失去資格、或讓自動報告直接執行任免。這些限制來自現行制度，不新增資格條件。

[Council 名單與平台對應 SSoT 設計](Council名單與平台對應SSoT設計.md)保存本輪可比較的資料維護方案、推薦與未決；方案尚未採納。下一步確認其範圍及取捨，再同步適用 specs，不能把本輪調查或候選設計當成已維護完成的 Council list。


### sf-ai 本輪接續狀態

前輪精簡 Council／moderation 設計已有使用者明確採納且已同步 specs；名單與平台對應是在同一管理情境下繼續討論的維護設計，仍為候選，不由此新增角色、資料欄位或自動賦權。尚未宣告整 Plan 需求就緒或 deliver，adopted 保留 false。

Auto-sync status 沒有既有待收輪次。啟動器 dry-run 辨識的是 CEO 外層 HEAD（aec120b（外層工作版本）），不是本子 repo HEAD；其內建 truth 範圍也以 SpecFormula 為對象，未將此預覽當成本專案的有效檢驗。未實際派送 Auto-sync，沒有 ready 或整 Plan 通過結論。本 repo 要求的獨立 FORMULATION 與逐條憲法檢查另按實際文件執行，不冒稱已取代 Auto-sync。

### 前版採納與 SSoT 設計的歷史 Review

獨立 reviewer 已讀本輪 Discord Setup 增量、Plan 與全部相關附件、決策紀錄、入口及適用成員資料規格。已修正歷史與當期狀態混用；FORMULATION 沒有剩餘問題。憲法第 1 條（名稱與目的）、第 2 條（公益非商業）、第 3 條（效力制度分工）、第 4 條（開放成員資格）、第 5 條（自願參與義務）、第 6 條（分工議會組成）、第 7 條（決策任命範圍）、第 8 條（平等有效表決）、第 9 條（罷免職位替換）、第 10 條（異議資格保障）、第 11 條（利益緊急界線）及第 12 條（修憲成員監督）逐條均沒有違反。檢查確認已採納設計與候選 SSoT 分開、資料缺漏不等於撤任、兼任不加票、敏感資料與已開票名冊保護未變。這是文件 review，未操作平台、未核定真人任職，也不是 Auto-sync 或整 Plan ready 的結論。


### Council 維護設計的完整修訂

使用者要求「please peer to peer review and give me the best complete proposal」，完整原話及修訂方案在 [Council 名單與平台對應 SSoT 設計](Council名單與平台對應SSoT設計.md)。前版的文件合規檢查沒有證明維護流程完整；本輪獨立 peer 指出入口、有效性輸入、格式、承接者、私人對應、過期處理、首屆成立、撤權失敗與固定名冊使用九項不足，已據此重寫候選提案。

推薦採用 members/council.md 作公開產生的入口，既有 assignment 用固定 Leader 欄位引用人工核對的原案，renderer 與 CI 只檢查彙整一致；平台操作按次核對本人與當下設定，不建第二份人工 Council 名單或未受控的私人對應庫。完整變更檔案、資料責任、首次建立、失敗接續及 how to test 都在附件。本輪只改候選設計與本 Plan，未同步新規則至 specs、未建立真實名冊或配置權限；先前已採納的精簡 Discord 設計仍有效。

本輪最終全文已由同一位獨立 peer 複查，候選提案完整性及 FORMULATION 通過，沒有剩餘阻擋問題。攻防後補上「撤除已明確對應的失效權限不要求離任者再同意」，以及「共同核對截止須精確相同，不同時點進待更新區」，避免撤權被卡住或把不同日期當完整名冊。最後四區呈現與時間欄位也已讀回確認。前版 review 不代替本輪結論。

憲法檢查逐條結論：

- 第 1 條（名稱與目的）：沒有違反；改善協作與責任查找，未改目的。
- 第 2 條（公益非商業）：沒有違反；無推銷、分潤或移除歷史署名。
- 第 3 條（效力制度分工）：沒有違反；候選、採納、原案與實作分開，程式不裁定效力。
- 第 4 條（開放成員資格）：沒有違反；缺欄位或帳號不取消既有資格。
- 第 5 條（自願參與義務）：沒有違反；工作須本人接受，不強迫接任或續任。
- 第 6 條（分工議會組成）：沒有違反；依有效 Leader 彙整去重，不以 Council 身分廣泛賦權。
- 第 7 條（決策任命範圍）：沒有違反；沿原程序，不以 CI 或文件任命、擴權。
- 第 8 條（平等有效表決）：沒有違反；表不直接決定分母，案件固定名冊依原案。
- 第 9 條（罷免職位替換）：沒有違反；保留其他有效職位，未來接任不提前覆蓋現任。
- 第 10 條（異議資格保障）：沒有違反；資料疑義依既有覆核，不自動撤資格。
- 第 11 條（利益緊急界線）：沒有違反；本人利益案迴避，私人證據受控，技術操作不代替永久任免。
- 第 12 條（修憲成員監督）：沒有違反；未改憲或追溯改算案件，新共同義務仍須有效採納。

檢查的是候選設計，沒有核定真人資格、實作工具或配置權限。名單維護設計仍在整體設計思考，未獲完整採納，不宣告 Auto-sync 通過、需求就緒或全 Plan deliver。


### Council 變更的分析與執行順序

> ok do gap analysis and consistency analysis for your plan
> after all agree, set a goal to work on this change, first local repo change then discord setup changed

依本次授權，先獨立執行兩項分析並處理發現，再設定 Council 變更的執行 goal。當時執行順序如下（新版名單維護與平台接續見 [目前設計](Council名單與平台對應SSoT設計.md)）：本地來源、Council 表與工具先完成，再處理 Council role、協作 tags 與入口接合。發布後才加入新 Council 網址，尚未核實的真人任職不賦權。既有 moderation 職責歸屬、精確能力與人員接續仍未完成，不宣稱整份 dc Plan 已就緒。


### 本輪任職來源核對

2026-11-01 本輪重新讀取 GitHub 原案與遠端 main，查核截止記為 2026-11-01T14:50:00+08:00。這是 AI 協助來源整理，不是正式資格、原案效力或首屆成立的裁決；沒有取得全部外部事件的完整證據，不能以未找到判定不存在。

- Sun：原申請明記願意承擔活動 Leader，但缺公開任命及共同生效；後續 Johnny 合併 Leader 安排。來源：[Sun 自介申請](https://github.com/AI-Native-Global-Founders-Speedrun-TW/ai-native-founders-tw-mono/pull/8)、[Leader 安排](https://github.com/AI-Native-Global-Founders-Speedrun-TW/ai-native-founders-tw-mono/pull/9)。
- 品毅：遠端 assignment 已記本人接受 Repository Leader，但任命及生效依據待核對。來源：[自介申請](https://github.com/AI-Native-Global-Founders-Speedrun-TW/ai-native-founders-tw-mono/pull/5)、[當時 assignment](https://github.com/AI-Native-Global-Founders-Speedrun-TW/ai-native-founders-tw-mono/blob/dadc191085ffdb2f23a993233953f0d0c4e678b8/members/r-and-r-assignment.md)。
- 水球：網域及司法與覆核兩項本人指定並接受的安排，原案仍記首屆共同生效待完成；自介編號為本人指定的起始個案，不用一般正整數檢查撤銷原識別。來源：[水球自介與制度整理](https://github.com/AI-Native-Global-Founders-Speedrun-TW/ai-native-founders-tw-mono/pull/7)。

assignment 先保留四項安排為依據待核對；Council 表不得呈現為已核定的有效 Council。其他待確認職位亦未由資料整理宣告空缺已核實。完整首屆依據及共同生效仍回 [Kickoff](../001-Kickoff/plan.md#首次建立與首屆任命) 接續。


### 本輪分析與本地實作

依決策 005（分析後順序執行），兩位獨立 reviewer 分別執行 gap analysis 與 consistency analysis，並於修訂後複讀同一版本。已補明新網址的發布與可讀前提、Council role 自身可被提及但無管理能力、協作 tags 的確切名稱與可選性，以及本次範圍與整份舊 Plan 的未完成事項。兩份分析均無本次範圍的剩餘阻擋問題，據此建立執行 goal；沒有宣告整 Plan ready。

本地已合併本次查核的最新遠端 main，保留其他工作。四項 Leader 安排仍為「依據待核對」；沒有核定任職、撤任或發角色。已建立 Council Markdown 表與產生／檢查工具（前版檔案，本輪已移除）及只讀 CI。16 項行為測試通過，包含兼任去重、同名不同人、最後職位終止、保留另一有效職位、時間不一致、未來生效不自動轉正、重複身分、缺依據、產生失敗保留舊表與偵測手改／來源變動；本地 `--check` 通過，遠端 CI 尚未執行。

規格變化以[成員識別與資料的 Council 維護](<../../specs/01-制度/[規格]成員識別與資料.md#council-名單與維護>)為主要維護位置；[Repository 技術維護](<../../specs/02-R&R/[Role]基建-Repository維護.md#council-檢視的技術維護>)與[Discord 帳號核對與操作](<../../specs/05-社群基建/[規格]Discord-社群-Setup.md#council-帳號核對與操作>)引用接續。此變更回應[志工容易號召工作並找到願意一起做的人](#志工容易號召工作並找到願意一起做的人)：先讓人找到分工及依據，再按有效職責完成平台操作。

本地實作已經獨立 reviewer 檢查實際檔案全文與 diff。FORMULATION 通過；review 發現一般新人修改自介及 Contributors 不應被迫重產 Council 表，已將摘要限於 Council 使用的資料，加入測試後複查通過。當期狀態與歷史段落亦已分開。Discord 設定接續中；新 Council 網址須等獲授權發布並實際讀取後才加入，真人掛名須另有有效任職與帳號依據。


#### 本地實作憲法檢查

獨立 reviewer 讀取憲法全文與實作，逐條結論：

- 第 1 條（名稱與目的）：沒有違反；改善組織協作與責任查找。
- 第 2 條（公益非商業）：沒有違反；未新增商業交換或移除署名。
- 第 3 條（效力制度分工）：沒有違反；程式不取代原案決定。
- 第 4 條（開放成員資格）：沒有違反；缺資料不視為喪失資格。
- 第 5 條（自願參與義務）：沒有違反；保留本人接受，不強迫任職。
- 第 6 條（分工議會組成）：沒有違反；有效 Leader 兼任去重，不自帶管理權。
- 第 7 條（決策任命範圍）：沒有違反；CI 與編輯不能完成任命。
- 第 8 條（平等有效表決）：沒有違反；產生表不直接決定投票分母。
- 第 9 條（罷免職位替換）：沒有違反；終止一職保留其他有效職位。
- 第 10 條（異議資格保障）：沒有違反；疑義保持待核對，不自動除名。
- 第 11 條（利益緊急界線）：沒有違反；私人證據受控、利益案件迴避。
- 第 12 條（修憲成員監督）：沒有違反；未改憲、削減監督或追溯改算案件。

此結論限本地實作，不證明真人任職、遠端 CI 或 Discord 操作完成。


### 本輪 Discord 執行結果

本地實作與獨立 review 完成後，以已登入 owner 帳號的瀏覽器操作，2026-11-01 完成以下設定並回讀：

- Council role 已建立，Manage Members 為零；角色全部 Permissions 關閉，僅 Display 中「Allow anyone to @mention this role」開啟。不為任何真人掛名，未新增私有頻道存取。
- collaborations 原無 tags，已加入「共同事項」「工作協作」；兩個 tag 的「Only allow moderators to apply tag」皆未啟用，「Require people to select tags when posting」保持關閉。原帖保留。
- 原 Post Guidelines 已更新為[現行協作文案](<../../specs/05-社群基建/[規格]Discord-社群-Setup.md#collaborations-文案>)，明示可以自行通知並連回 repo 原案；沒有新增頻道或代發關卡。
- collaborations 權限仍同步 get-involved，Create Posts 與 Send Messages in Posts 均沿用原本權限。四個入口 welcome、onboard、rules、announcements 逐一回讀：皆同步 start-here，對 @everyone 的發文、討論串回覆、公開及私人討論串建立皆為 Deny。此次未改頻道權限。

Council 新公開網址尚未加入 onboard：本地變更尚未獲授權 push，canonical main 尚無此頁。待發布並確認實際可讀後，只補原 onboard 的入口，不複製人員清單。真人任職／帳號掛名、moderation 職責／能力／人員、第二位技術接續與網站／真人測試仍各自未完成，不宣稱整 Plan 完成。驗證截圖只存在本機暫存位置，不進版控。

本輪執行結果與新增協作文案已由獨立 reviewer 複讀，FORMULATION 及前述十二條憲法均無新增問題；平台結果由實際操作與回讀負責。


### 本輪 PR 發布

使用者原話：「發 pr for this」。本次僅發布 Council SSoT 與 Discord 設定變更的 PR，不直接 push main、不合併 PR。PR 以最新遠端 main 為基底，排除本機先前三筆邀請與 Agent 申請引導 commit，保留原工作目錄的其他未提交修改。

隔離分支再次執行 16 項行為測試及 Council `--check`，全部通過。前述「尚未獲授權 push」是當時狀態；目前授權限於本次 PR 分支。Council 入口仍待 PR 合併到 canonical main 並確認可讀後加入 onboard，不以 PR 分支頁面替代正式入口。

PR 基底複查修正原始需求的可點擊引用，改指向本 Plan 保留的原話；members README 明確區分 Contributors 每人一行與 Leader 固定欄位，並保留其他人的區塊。Discord 文案與 Threads 引導僅共用先理解再申請的順序，不宣稱兩處 prompt 相同。

隔離 PR 的最終全文與新基底已由獨立 reviewer 複查，FORMULATION 無剩餘問題；憲法第 1 條（名稱與目的）、第 2 條（公益非商業）、第 3 條（效力制度分工）、第 4 條（開放成員資格）、第 5 條（自願參與義務）、第 6 條（分工議會組成）、第 7 條（決策任命範圍）、第 8 條（平等有效表決）、第 9 條（罷免職位替換）、第 10 條（異議資格保障）、第 11 條（利益緊急界線）、第 12 條（修憲成員監督）逐條均沒有違反。此結論允許發布本次 PR 分支，不涵蓋合併或直接推 main。


## 2026-11-01：Council simple structure data 本地修訂

### 使用者原話

> 如果他要被 parse，why not use yml ?
>
> 舉例一下這 yml 你怎麼列？
> 另外我覺得 council 也該是yml?
>
> 但我希望不要 over-engineering！！！
> 能不能一切就從簡啊，不要一堆奇怪的 prone
> 而是 simple structure data
>
> 本地先大幅更新我看看？

### 本輪修訂

前版讓 assignment 固定欄位經 parser 產生 Council Markdown，並增加專用 CI；後續 YAML 提案仍帶過多欄位。使用者要求從簡，因此改為直接手動維護 `members/council.yml`，每人只有 member 與 roles。Contributors 保留在原 assignment，Leader 入口統一指向 YAML；任職依據留原案。移除產生器、相關測試、工具說明、專用 workflow 與產生表，同步 README、制度與 SOP。

本輪任職來源核對仍有效：未確認的安排留在本 Plan，不因格式改動就自動轉為現任。真實 YAML 暫為空清單，不能解讀為已裁定無人有資格。此輪只做本地修訂供 review，不推送、不更新 Discord。

### 本輪 review 與憲法檢查

獨立 peer 已全文檢查實際 diff、受影響文件與 FORMULATION。發現志工協作 SOP 的按人搜尋仍只查 assignment，已改為同查 Council YAML 與 assignment，複查通過，無剩餘阻擋。YAML 成功解析；Contributors 區塊與修改前一致；git diff --check 通過。未發布、未操作 Discord。

- 第 1 條（名稱與目的）：沒有違反；保留協作及責任查找。
- 第 2 條（公益非商業）：沒有違反；未新增商業交換或移除署名。
- 第 3 條（效力制度分工）：沒有違反；名單維護不取代有效原案。
- 第 4 條（開放成員資格）：沒有違反；未確認或空清單不取消資格。
- 第 5 條（自願參與義務）：沒有違反；保留本人接受及自願參與。
- 第 6 條（分工議會組成）：沒有違反；每人一筆多職位，保留有效 Leader 條件。
- 第 7 條（決策任命範圍）：沒有違反；編輯 YAML 不構成任命。
- 第 8 條（平等有效表決）：沒有違反；名單不代替案件固定投票名冊。
- 第 9 條（罷免職位替換）：沒有違反；終止個別職位保留其他有效職位。
- 第 10 條（異議資格保障）：沒有違反；未透過格式遷移撤任或除名。
- 第 11 條（利益緊急界線）：沒有違反；私人資料與平台權限界線保持。
- 第 12 條（修憲成員監督）：沒有違反；未改門檻、削減監督或追溯改算。


## 2026-11-01：Plan 單向依賴與 YAML 格式說明

### 使用者原話

> 不要在那些 truth 或者是 members 裡面去提到 plan 好不好？
>
> plan 這個東西應該是單向依賴，永遠都是 plan 依賴出去，而不是外面的人依賴進來 plan，這個可以在 formulation 裡面加強嗎？
>
> 然後這個 YAML 上面應該要有一個很大的註解格式，去說明這個 YAML 的規範、整個格式與欄位是什麼，應該要有一個很 standard 的 structured expression，to let anyone know what to write and how to validate if the format is valid in the YAML's content.

### 本輪變更

[FORMULATION](../../FORMULATION.md#plan-的單向依賴) 明定單向依賴；移除 truth 與 members 對特定 Plan 的引用。原先只有 Kickoff 寫明的首屆任命與共同生效條件，移入[憲政制度](<../../specs/01-制度/[機制] 憲政制度.md#首屆任命與生效>)，保留既有條件，不新授予權力；Kickoff 中原文視為歷史，現行條件以制度為準。已移除的候選與進度引用不轉成已生效 truth。

[Council YAML](../../members/r-and-r-assignment.yml) 以頂部註解說明 purpose、structure、example、validation 與 maintenance；正文仍只有 council 清單及 member／roles。語法、資料格式及任職有效性分開核對，不新增工具或 CI。本輪維持本地 review，未 push、未更新 Discord。

### 本輪單向依賴 review 與憲法檢查

獨立 peer 完整檢查後，修正問題文件仍以 Kickoff 追蹤證據的句子及 Verify note 拼寫不一致；最終複查通過。truth 與 members 無特定 Plan 引用；首屆條件與原文對照一致。YAML 可解析，格式註解不增加資料欄位或自動化工具。

- 第 1 條（名稱與目的）：沒有違反；維持協作目的。
- 第 2 條（公益非商業）：沒有違反；未改商業限制或署名保障。
- 第 3 條（效力制度分工）：沒有違反；制度承載既有規則，格式不取代效力。
- 第 4 條（開放成員資格）：沒有違反；空清單不裁定資格，既有資格保留。
- 第 5 條（自願參與義務）：沒有違反；本人接受條件完整保留。
- 第 6 條（分工議會組成）：沒有違反；有效 Leader 組成及兼任規則不變。
- 第 7 條（決策任命範圍）：沒有違反；一次性安排未擴張，一般任命程序保留。
- 第 8 條（平等有效表決）：沒有違反；YAML 不替代案件資格核對及固定名冊。
- 第 9 條（罷免職位替換）：沒有違反；未改罷免及替換門檻。
- 第 10 條（異議資格保障）：沒有違反；未以格式或資料缺漏取消資格。
- 第 11 條（利益緊急界線）：沒有違反；利益迴避、私人證據及權限界線未變。
- 第 12 條（修憲成員監督）：沒有違反；未新設常設權力、削減監督或追溯改算。


### 本地檔案讀回與同步修正

使用者指出：「I still didn't see you update the console or relevant YAMLs with the new rules.」「不對啊，這也根本沒符合規範啊」。讀回實際 YAML 確認仍為舊三行註解且引用 Plan；已恢復完整格式說明並移除反向引用，同步至原 mono checkout。兩處 YAML 位元組一致，解析成功；members 與 specs 無特定 Plan 引用。獨立 peer 重新檢查實際原 checkout，FORMULATION 通過；憲法第 1 條（名稱與目的）、第 2 條（公益非商業）、第 3 條（效力制度分工）、第 4 條（開放成員資格）、第 5 條（自願參與義務）、第 6 條（分工議會組成）、第 7 條（決策任命範圍）、第 8 條（平等有效表決）、第 9 條（罷免職位替換）、第 10 條（異議資格保障）、第 11 條（利益緊急界線）、第 12 條（修憲成員監督）逐條皆沒有違反。本輪未 commit、未 push。

## R&R assignment YAML 提案（尚未採納）

使用者要求：「ok deep analyze and propose」。本輪只提案，不改現行 assignment 或 truth。

### 現況與要保留的意思

現有 assignment 包含 11 項 R&R、16 筆 Contributors 關係；21 份 README、members 或 specs 文件引用其 Markdown 路徑。Leader 已改由 Council YAML 維護，assignment 內重複的 Leader 段落只提供入口。規格要求正式成員至少選一項 Contributors，Leader 也一樣；加入分工不等於接受該分工所有工作，更不自動取得管理權。pending 檔名不等於未入會，不能只憑檔名移除既有分工。

### 建議結構

以 members/r-and-r-assignment.yml 取代 Markdown 名單，每項 role 一筆，只放 role 與 contributors。Council 維持每人一筆 member 與 roles。兩者表達的是不同關係，不因同一人出現在兩處就算重複資料；不得從 Council 自動推導 Contributors。

以下路徑為格式示意，不是真實人選或任命：

```yaml
assignments:
  - role: Hacker
    contributors:
      - members/example.md
  - role: 活動籌辦與協助
    contributors: []
```

role 及 Council 的 roles 沿用 specs/02-R&R/README.md 文件入口中的既有 R&R 名稱。該入口已提供名稱與 Role 文件對應，不另建 role ID、registry 或重抄職責路徑。名稱調整時在同一變更更新該入口、兩份 YAML 及受影響引用。

個人只使用 repo 根目錄起算的 members 檔案路徑，不另存姓名、Member ID、GitHub 或狀態。個人檔案改名時同步兩份 YAML，歷史不重寫。

### 格式規範與驗證

YAML 頂部沿用 Council 的 purpose、structure、example、validation、maintenance 註解分節。root 只允許 assignments；其值為 sequence。每筆只允許必填的 role（非空 string）與 contributors（string sequence）。同一 role 只能一筆，同一 role 內不得重複個人；同一人可出現在不同 role。同一人不得用不同路徑重複表示。

保留目前全部 11 項角色，包括沒有人加入者；無人時明寫 contributors: []，不用 null 或省略。所有現行 Role 均須列出，停止的 Role 按有效決定移除；新增 Role 即使沒人也列空清單。這是分工清單，不另外包含 Leader、狀態、日期或證據欄位。

格式驗證檢查 YAML 語法、重複 key、必填與型別、role 唯一、role 與既有入口一致、個人路徑存在且唯一。制度核對另檢查本人選擇、有效資格及每位正式成員至少一項 Contributors；檔案存在或格式正確都不能證明資格有效。尚未合併的自介 PR 可提出 assignment 變更，不因此把人列成已生效；合併仍依有效審查與制度處理。不新增專用 parser、schema、CI、產生表或平台同步服務。

### 文件與操作影響

刪除舊 Markdown 名單，避免兩份都能改。原填寫規範整理至 members/README.md 及 YAML 檔頭；治理規則維持 specs，歷史紀錄維持既有來源。更新所有指向舊檔及其章節 anchor 的有效引用；YAML 不保留 Markdown anchors，Role 文件改連到 YAML 並明說查找同名 role。從 GitHub 看 YAML 會失去原 Markdown 的可點擊人名與章節跳轉，接受以簡單結構與搜尋查找取代，不額外生成閱讀頁。

主要影響：新增 assignment YAML、移除 assignment Markdown；更新 Council 的 role 名稱來源註解、members README、根 README、成員識別規格、憲政制度、R&R README、各 Role 的人員入口及受影響 SOP。沿用本 Plan 記錄過程；truth 與 members 不回連本 Plan。子 module 不在本輪直接修改，正式遷移前需確認是否有讀取舊檔或 anchors 的消費端，存在時列入必要同步範圍後再交付。

### 遷移與 how to test

先逐項轉換現有 11 項／16 筆關係，不趁格式遷移重新判定資格或變更人選。對照轉換前後的 role/member 關係完全相同，確認零漏列與零新增；對資格疑義沿原案處理，不以 pending 檔名自動撤除。再核對新路徑與引用、檔頭範例可解析、正文符合格式、有效文件無舊檔或 anchor 依賴。修正引用後刪除舊檔；不推送、不改 Discord，直到獲得相應授權。

### 取捨

不合併兩份名單：在 assignment 同時放 leader，再手填 Council 會重複維護；改用產生 Council 又回到使用者拒絕的工具。Council 按人適合看議會組成，Contributors 按 role 適合新人選分工，兩份都保持兩個欄位即可。人員及職責名稱仍需隨改名同步，這是選擇簡單檔案引用的成本，不宣稱免維護。


### R&R YAML 提案 review

獨立 peer 依 FORMULATION 複查通過，無阻擋提案交付的問題。實作前仍須查消費端，不宣稱已完成遷移。憲法逐條結論：

- 第 1 條（名稱與目的）：沒有違反；本輪僅提案，不更動資格、任職、權限或既有制度。
- 第 2 條（公益非商業）：沒有違反；本輪僅提案，不更動資格、任職、權限或既有制度。
- 第 3 條（效力制度分工）：沒有違反；本輪僅提案，不更動資格、任職、權限或既有制度。
- 第 4 條（開放成員資格）：沒有違反；本輪僅提案，不更動資格、任職、權限或既有制度。
- 第 5 條（自願參與義務）：沒有違反；本輪僅提案，不更動資格、任職、權限或既有制度。
- 第 6 條（分工議會組成）：沒有違反；本輪僅提案，不更動資格、任職、權限或既有制度。
- 第 7 條（決策任命範圍）：沒有違反；本輪僅提案，不更動資格、任職、權限或既有制度。
- 第 8 條（平等有效表決）：沒有違反；本輪僅提案，不更動資格、任職、權限或既有制度。
- 第 9 條（罷免職位替換）：沒有違反；本輪僅提案，不更動資格、任職、權限或既有制度。
- 第 10 條（異議資格保障）：沒有違反；本輪僅提案，不更動資格、任職、權限或既有制度。
- 第 11 條（利益緊急界線）：沒有違反；本輪僅提案，不更動資格、任職、權限或既有制度。
- 第 12 條（修憲成員監督）：沒有違反；本輪僅提案，不更動資格、任職、權限或既有制度。


## 單一 assignment YAML 採納與 PR 更新

使用者原話：「leader 咧」「好，整體相關 SOP 都改動了？最後一次檢查, update goal 確定一切都自洽後更新 PR」。採納把 role、leader、contributors 放在同一 YAML 的提案，Council 為非空 leader 去重集合，取代前版兩份名單。

本輪 goal：完成單一資料遷移、全部相關 SOP 和有效引用更新，保持 11 項／16 筆 Contributors 關係不變，通過格式、引用、消費端及獨立 FORMULATION／逐條憲法檢查後更新既有 PR。先前 goal 所述 renderer 與 Council 產生表已被撤回；Discord main 公開入口及真人任職仍不冒稱完成。

已查網站現有 build-graph 的 members 來源只掃 .md，舊檔名為排除項，新 .yml 不會被當自介；測試舊字串為排除測試樣本，不需變更網站。任職仍待原案證據核對，各 leader 為 null，不擅自填名。


### 單一 YAML 最終檢查

獨立 peer 已核對實際 diff 與受影響全文，FORMULATION 通過，無剩餘阻擋。11 項職責及 16 筆 Contributors 與原 Markdown 完全一致，leader null 不裁定資格；相關 SOP 與有效引用已同步。網站消費端僅掃 Markdown 自介，新 YAML 不會混入。YAML 解析、檔案引用與 git diff --check 通過；未初始化 submodule 的來源連結已於原 checkout 核對。可依本次授權更新既有 PR，合併及 Discord 入口更新仍不屬本次完成範圍。

- 第 1 條（名稱與目的）：沒有違反；保持既有資格、本人選擇、任命條件與權限界線，格式遷移不改制度效力。
- 第 2 條（公益非商業）：沒有違反；保持既有資格、本人選擇、任命條件與權限界線，格式遷移不改制度效力。
- 第 3 條（效力制度分工）：沒有違反；保持既有資格、本人選擇、任命條件與權限界線，格式遷移不改制度效力。
- 第 4 條（開放成員資格）：沒有違反；保持既有資格、本人選擇、任命條件與權限界線，格式遷移不改制度效力。
- 第 5 條（自願參與義務）：沒有違反；保持既有資格、本人選擇、任命條件與權限界線，格式遷移不改制度效力。
- 第 6 條（分工議會組成）：沒有違反；保持既有資格、本人選擇、任命條件與權限界線，格式遷移不改制度效力。
- 第 7 條（決策任命範圍）：沒有違反；保持既有資格、本人選擇、任命條件與權限界線，格式遷移不改制度效力。
- 第 8 條（平等有效表決）：沒有違反；保持既有資格、本人選擇、任命條件與權限界線，格式遷移不改制度效力。
- 第 9 條（罷免職位替換）：沒有違反；保持既有資格、本人選擇、任命條件與權限界線，格式遷移不改制度效力。
- 第 10 條（異議資格保障）：沒有違反；保持既有資格、本人選擇、任命條件與權限界線，格式遷移不改制度效力。
- 第 11 條（利益緊急界線）：沒有違反；保持既有資格、本人選擇、任命條件與權限界線，格式遷移不改制度效力。
- 第 12 條（修憲成員監督）：沒有違反；保持既有資格、本人選擇、任命條件與權限界線，格式遷移不改制度效力。


## Discord member ID mapping 接續

使用者要求：「然後啊 council 和 discord member id 要做 mapping council member 的 object 可以多這欄位」。單一 assignment 沒有獨立 Council member object；採用成員資料選填 discord_id，leader 路徑連到本人資料，避免兼任職位重複填 ID。現階段補格式及操作規則，未填任何猜測的真人 ID，亦未派發角色。缺少 mapping 不撤除資格或任職。

本輪查回既有 PR 仍為 OPEN、尚未合併；因此 main 的新 assignment URL 尚不能視為已發布，不更新 onboard 至尚不存在的新路徑。舊 goal 的 renderer 與產生表已由後續單一 YAML 決策取代，不恢復被撤回設計。


### Discord mapping review

獨立 peer 依五檔實際變更及 FORMULATION 全文 review 通過，沒有剩餘阻擋；未填真人 ID 或更新 Discord。

- 第 1 條（名稱與目的）：沒有違反；欄位選填及本人核對不改變資格、權限或治理條件。
- 第 2 條（公益非商業）：沒有違反；欄位選填及本人核對不改變資格、權限或治理條件。
- 第 3 條（效力制度分工）：沒有違反；欄位選填及本人核對不改變資格、權限或治理條件。
- 第 4 條（開放成員資格）：沒有違反；欄位選填及本人核對不改變資格、權限或治理條件。
- 第 5 條（自願參與義務）：沒有違反；欄位選填及本人核對不改變資格、權限或治理條件。
- 第 6 條（分工議會組成）：沒有違反；欄位選填及本人核對不改變資格、權限或治理條件。
- 第 7 條（決策任命範圍）：沒有違反；欄位選填及本人核對不改變資格、權限或治理條件。
- 第 8 條（平等有效表決）：沒有違反；欄位選填及本人核對不改變資格、權限或治理條件。
- 第 9 條（罷免職位替換）：沒有違反；欄位選填及本人核對不改變資格、權限或治理條件。
- 第 10 條（異議資格保障）：沒有違反；欄位選填及本人核對不改變資格、權限或治理條件。
- 第 11 條（利益緊急界線）：沒有違反；欄位選填及本人核對不改變資格、權限或治理條件。
- 第 12 條（修憲成員監督）：沒有違反；欄位選填及本人核對不改變資格、權限或治理條件。


## 恢復既有 Leader 對應

使用者原話：「leader 怎麼為空，之前我和 sun 都是某些 leaders 啊」「去啊」。先前格式遷移保留 Contributors，卻把既有 Leader 清空，是錯誤；前述全填 null 的檢查結論不能作為保留完整分工的證明。

對照遠端原 Markdown，恢復 Sun 的活動籌辦與協助、品毅的基建-Repository 維護、水球的基建-Domain-Name 維護及司法與覆核。這是恢復原有資料，不新增任命；原案的生效條件與待核對事項維持，不據此自動派發 Discord 權限。YAML 與資料規則明定：不能因本輪未完成核對而把既有 Leader 清空。


### Leader 還原複查

獨立 peer 對照 origin/main 的全部 Leader 對應與 Contributors，確認四項 Leader 與十六筆 Contributors 完全保留；前次接受清空 Leader 的 review 結論撤回。已同步修正「非空即有效 Council」敘述，原案有效性與保留對應分開。FORMULATION 與 diff 檢查通過。

- 第 1 條（名稱與目的）：沒有違反；恢復既有對應，不新增任命、授權或宣告原案程序完成。
- 第 2 條（公益非商業）：沒有違反；恢復既有對應，不新增任命、授權或宣告原案程序完成。
- 第 3 條（效力制度分工）：沒有違反；恢復既有對應，不新增任命、授權或宣告原案程序完成。
- 第 4 條（開放成員資格）：沒有違反；恢復既有對應，不新增任命、授權或宣告原案程序完成。
- 第 5 條（自願參與義務）：沒有違反；恢復既有對應，不新增任命、授權或宣告原案程序完成。
- 第 6 條（分工議會組成）：沒有違反；恢復既有對應，不新增任命、授權或宣告原案程序完成。
- 第 7 條（決策任命範圍）：沒有違反；恢復既有對應，不新增任命、授權或宣告原案程序完成。
- 第 8 條（平等有效表決）：沒有違反；恢復既有對應，不新增任命、授權或宣告原案程序完成。
- 第 9 條（罷免職位替換）：沒有違反；恢復既有對應，不新增任命、授權或宣告原案程序完成。
- 第 10 條（異議資格保障）：沒有違反；恢復既有對應，不新增任命、授權或宣告原案程序完成。
- 第 11 條（利益緊急界線）：沒有違反；恢復既有對應，不新增任命、授權或宣告原案程序完成。
- 第 12 條（修憲成員監督）：沒有違反；恢復既有對應，不新增任命、授權或宣告原案程序完成。


## 加入 validation script 與 CI

使用者原話：「最後一樣可以寫 validation script runs in CI 啊」「你 validate 了什麼？scripts 在哪，沒從 PR 中看見啊」。前輪僅提出檢查範圍，沒有建立 script／workflow；本輪補上實作，不恢復產生器。

新增 scripts/validate_assignments.py、其回歸測試與固定 PyYAML 依賴、PR／main 的 validation workflow。現有 11 項職責、16 筆 Contributors 通過，無已填 Discord ID。測試涵蓋合法/null 資料、重複 key／role、漏職責、錯誤欄位型別、失效或越界路徑、Contributors 重複、Discord ID 型別與跨人重複、非成員資料範例忽略。CI 不裁決任命、不修改任何名單。


### Validation 實作 review

獨立 peer 讀實際程式與變更並執行八項測試，全數通過；真實資料驗證 11 項／16 筆／0 ID 通過。FORMULATION 一致，CI 僅 contents: read，不提供 Discord 憑證。遠端結果待 push 後核對。

- 第 1 條（名稱與目的）：沒有違反；驗證唯讀，不改資料、任命、資格或權限。
- 第 2 條（公益非商業）：沒有違反；驗證唯讀，不改資料、任命、資格或權限。
- 第 3 條（效力制度分工）：沒有違反；驗證唯讀，不改資料、任命、資格或權限。
- 第 4 條（開放成員資格）：沒有違反；驗證唯讀，不改資料、任命、資格或權限。
- 第 5 條（自願參與義務）：沒有違反；驗證唯讀，不改資料、任命、資格或權限。
- 第 6 條（分工議會組成）：沒有違反；驗證唯讀，不改資料、任命、資格或權限。
- 第 7 條（決策任命範圍）：沒有違反；驗證唯讀，不改資料、任命、資格或權限。
- 第 8 條（平等有效表決）：沒有違反；驗證唯讀，不改資料、任命、資格或權限。
- 第 9 條（罷免職位替換）：沒有違反；驗證唯讀，不改資料、任命、資格或權限。
- 第 10 條（異議資格保障）：沒有違反；驗證唯讀，不改資料、任命、資格或權限。
- 第 11 條（利益緊急界線）：沒有違反；驗證唯讀，不改資料、任命、資格或權限。
- 第 12 條（修憲成員監督）：沒有違反；驗證唯讀，不改資料、任命、資格或權限。
