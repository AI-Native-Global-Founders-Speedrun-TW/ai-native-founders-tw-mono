# Problem

## Discord 加入、交流與活動

Discord 需要支援新人開始、創業交流、志工號召工作，以及線上與實體活動的發起及參與。參與者各有工作與生活，投入時間有限；組織需要讓這些行為容易發生，也需要讓重要資訊可以被找到。

### 新人理解組織並知道如何加入

收到邀請的人需要理解組織目的、知道如何加入，以及遇到問題時能在哪裡詢問。

1. Discord 身分與組織成員資格需要分清楚；具體資格及加入方式依[申請制度](<../01-制度/[機制] 憲政制度.md>)，交流工具不自行增加加入條件。
2. 新人需要找得到目的、加入說明與提問位置；重要內容不能只靠逐一私訊說明或翻找大量聊天。

### 創業者容易討論問題、分享經驗與認識彼此

創業者需要能提出具體問題、分享經驗並認識彼此，也需要在自己的時間能投入時接續討論。

1. 交流需要容納不同創業階段與背景，不將特定背景當作參與條件；開放原則依[憲法第 4 條（開放成員資格）](<../01-制度/憲法.md#第-4-條開放與成員資格>)。
2. 日常對話與值得深入、持續參考的內容都需要空間；重要內容不能一直被聊天洗掉。知識整理仍承接[志工協作與開源知識](<../03-SOP/[SOP]志工協作與開源知識.md#開源知識如何被使用>)。
3. 主動參與不等於要求每天發言；具體參與安排依[成員參與制度](<../01-制度/[機制] 憲政制度.md>)。

### 志工容易號召工作並找到願意一起做的人

志工需要能讓其他人知道正在發起什麼工作、需要哪些幫忙，以及如何參與，讓願意一起做的人可以接續。

1. 參與者時間有限，需要容易理解工作內容與參與方式，不以持續盯著聊天作為協作前提。
2. 號召不能變成強制幫忙；能力與意願不等於已接受工作。認領及決策的關係依[協作工作流](<../03-SOP/[SOP]志工協作與開源知識.md#認領與拍板>)與[憲法第 5 條（自願貢獻參與）](<../01-制度/憲法.md#第-5-條自願貢獻與參與義務>)及[第 7 條（決策範圍任命）](<../01-制度/憲法.md#第-7-條決策範圍與任命>)。
3. Council 需要容易協調跨 R&R 工作，正式成員需要能自行提出共同事項；不能以私下受理或等待管理者代發作為前提。頻道與角色的增加應回應具體協作需要，不增加志工不必要的維護負擔。

### 線上與實體活動容易發起及參與

參與者需要能發起線上或實體活動、號召有興趣的人，並讓有興趣的人容易找到活動及參與方式。

1. 辦活動與號召工作、日常討論是不同情境；討論容易，不代表活動的發起與參與就容易。
2. 活動資訊與接續討論需要能找到，避免參與者必須持續讀取日常聊天才能知道如何參與。
3. 讓活動容易發起不等於規定固定頻率或強制出席；尚未決定的頻率及參與標準仍依[成員參與制度](<../01-制度/[機制] 憲政制度.md#長期不參與與成員資格處理>)。

# Specs

## Discord 社群的適用範圍

本機制以頻道分工、權限與新人導覽，支援上方 [Discord 加入、交流與活動](#discord-加入交流與活動)的四種情境。Server Guide 帶新人找到加入方式、協作與活動；實際申請由 repo 的制度承接。

目標 server 為 [AI-Native Global Founders Speedrun Taiwan](https://discord.com/channels/1563453138810306612/1563453141641597000)。頻道與 category 名稱均使用英文，描述及新人說明使用繁體中文；既有訊息與論壇討論串保留。

Discord 身分與組織成員資格分開。申請與審查依[申請制度](<../01-制度/[機制] 憲政制度.md>)，自介放在公開 repo 的 [members](<../../members/README.md>) 資料夾，以 PR 提交；具體參與安排依[成員參與制度](<../01-制度/[機制] 憲政制度.md>)。進入 server、新人導覽與活動權限不另設組織加入條件。

## 頻道整體配置

分類與頻道依下表排列。Text 是文字頻道、Forum 是論壇、Voice 是語音；括號說明可見及發文限制。

| Category | Channel | Type | 描述 |
|---|---|---|---|
| start-here | [welcome](https://discord.com/channels/1563453138810306612/1563453141641597000) | Text（唯讀） | 歡迎加入 AI-Native Global Founders Speedrun Taiwan！組織目前還在建設中，歡迎先交流、參與活動，也一起做些什麼。先看 <#1563456791050977341> 的 Agent prompt，認識組織後再依意願申請；現行規範看 <#1564249902475907172>，有問題到 <#1563454007605723186>。 |
| start-here | [onboard](https://discord.com/channels/1563453138810306612/1563456791050977341) | Text（唯讀） | 從這裡開始：把釘選中的 prompt 貼給 Agent，先認識組織，再依意願申請；也可依 members 說明手動準備自介、真人照片與 Contributors 選擇。進入 Discord 不等於已入會。Repo：https://github.com/AI-Native-Global-Founders-Speedrun-TW/ai-native-founders-tw-mono |
| start-here | [rules](https://discord.com/channels/1563453138810306612/1564249902475907172) | Text（唯讀） | 交流請遵守組織憲法與現行制度：開放學習、尊重彼此、自願貢獻；不得以本組織名義、筆記或活動為特定公司推銷產品、服務或提供收費置入。規範以 repo 為準：https://github.com/AI-Native-Global-Founders-Speedrun-TW/ai-native-founders-tw-mono |
| start-here | [announcements](https://discord.com/channels/1563453138810306612/1564249954266914846) | Text（唯讀） | 重要公告、組織更新與已確認活動，由具有效公告職責與平台能力的人發布。日常討論請到 #chit-chat；活動詳情與接續討論請到 #events。 |
| community | [chit-chat](https://discord.com/channels/1563453138810306612/1563454007605723186) | Text | 打招呼、閒聊、即時問答與新人求助。想深入討論創業問題或分享經驗，請到 #discussions 開一篇，讓大家能在自己的時間接續。 |
| community | [funding](https://discord.com/channels/1563453138810306612/1564236090770984970) | Text | 交流募資問題、經驗與資源。請交代創業階段、具體問題與需要的幫忙；仍須遵守不得以組織名義推銷產品、服務或提供收費置入的規定。 |
| community | [discussions](https://discord.com/channels/1563453138810306612/1564250031706607657) | Forum | 一個創業問題或一份經驗分享開一篇。請說明背景、具體問題、已嘗試的方法與希望得到的幫忙；相關討論留在同篇，長期有用的知識再整理到 repo。 |
| get-involved | [collaborations](https://discord.com/channels/1563453138810306612/1563454194541658122) | Forum | 見下方 [collaborations 文案](#collaborations-文案)。 |
| get-involved | [events](https://discord.com/channels/1563453138810306612/1563454084168814612) | Forum | 一場線上或實體活動開一篇，說明目的、時間、地點或會議連結及參與方式；活動討論留在同篇。所有加入者都可建立自己的 Events 排程；Interested 表示興趣，不取代另有要求的報名程序。 |
| voice | [lounge](https://discord.com/channels/1563453138810306612/1563453141641597001) | Voice | 即時交流、Coffee Chat、工作討論與小型線上活動共用語音空間。活動目的、時間與參與方式請放 #events，工作號召請放 #collaborations。 |
| management | [mod-log](https://discord.com/channels/1563453138810306612/1564250087775932556) | Text（私有） | 私有管理紀錄：接收 Community 更新與 AutoMod 警示，僅供具有必要管理職責與平台能力的人查看；不在此新增組織決策權或管理授權。 |

文字頻道的描述填入 Channel Topic，論壇填入 Post Guidelines。lounge 的設定頁沒有描述欄位，使用語音頻道的[文字聊天用途說明](https://discord.com/channels/1563453138810306612/1563453141641597001/1564251491944898581)。announcements 使用一般 Text；原生 Events 是活動排程功能，不是額外頻道。

<a id="管理與公告發布"></a>

## 維護責任與制度接合

[Repository Leader](<../02-R&R/[Role]基建-Repository維護.md>)承接 Discord 技術設定、權限與事故處理。第二位接續 Leader 須在自己的有效 R&R 明列 Discord 接續範圍與必要權限；Council 身分不代表取得 Administrator，伺服器 Role 也不代表有效任命。

變更依有效決定核對分類、頻道與帳號，操作後回讀確認，保留不含秘密的證據。任免交接、備援、緊急限制與非本人覆核依[憲政制度](<../01-制度/[機制] 憲政制度.md>)，具體操作接續依 Repository 職責文件。不得以封鎖平台存取代替永久取消組織成員資格；制度有效變更與平台實際完成分開記錄。

### Council 身分與 Moderator 能力

Council role 用來辨識有效 R&R Leader 及通知，不自動授予訊息管理、內容裁決或技術管理權。掛名須核對有效任職與本人平台帳號，不以熟人關係、歷史認領、名單編輯或已有平台權限代替任命依據。Council 可兼任 Moderator，但 Moderator 能力僅依本人已接受的有效職責配置；Repository 的技術維護不自行包含內容審查。

目前不新增沒有實際用途的 Member role，也不新增 governance category、council-updates、proposals、council-chat、mod-chat 或按每個 R&R 建立永久頻道。後續有具體漏案、難找或協調需要時再比較調整，不將本次取捨視為永久禁止。

本節記錄已採納的設計方向，不表示已完成組織正式程序、任命、賦權或 Discord 配置。新增 moderation 職責、擴權及任命仍依[憲政制度的制度修改與執行調整](<../01-制度/[機制] 憲政制度.md#制度修改與執行調整>)辦理；未有有效職責及決定前不發放相應管理能力。

### 技術接續與敏感事件處理

優先依[職位與權限交接](<../01-制度/[機制] 憲政制度.md#職位與權限交接>)核對兩位不同有效 Leader 的技術接續範圍、本人接受、實際帳號與操作或恢復能力。技術接續、Council 身分與 moderation 分別核對，不以其中一項代替另一項。第二人的有效職責與實際能力尚未完成驗證時，如實列為未完成，不直接判定該人沒有資格或能力。

邀請擴大前預備最小 moderation，不等待第一個受害事件才找承接者。準備範圍包括可辨識濫發、明確釣魚或惡意連結、洩露憑證等正在發生傷害的必要暫時處置；不以此授予一般內容爭議的任意裁決權，也不預設給予廣泛 Timeout、Kick、Ban 或角色管理能力。處置、必要紀錄與非涉案覆核依[緊急處置](<../01-制度/[機制] 憲政制度.md#緊急處置>)接續，不代替永久成員資格處理。

mod-log 須有實際接受警示與接案的人。welcome／rules 應能找到已接受職責且有實際能力的敏感事件聯絡人，以及原聯絡人涉案時的合格非涉案接續者；未有人接受或未有合格者時明列受阻，不以抽象角色名稱假裝已有聯絡人。敏感正文不放公開 Forum／Issue，原始證據僅供有權且非涉案者受控查核，不因 Council 身分全面開放。

moderation 由哪項有效 R&R 承接、本人接受的具體範圍、聯絡人與非涉案備援、必要能力清單及實際配置仍待核實與確認。本節未指定人名；正式公告聯絡方式與配置能力前，須完成適用程序、本人接受與實際驗證。

## 公開、唯讀與管理權限

權限分成 server 的 @everyone 預設權限、分類限制及頻道覆寫。@everyone 提供一般交流能力，start-here 再限制入口頻道發文，management 再限制管理紀錄可見性。

| 設定位置 | 權限 | 設定值與作用 |
|---|---|---|
| @everyone | View Channels、Read Message History、Send Messages and Create Posts | 開啟，提供公開交流與讀取歷史的基礎權限。 |
| @everyone | Connect、Speak | 開啟，允許進入 lounge 與發言。 |
| @everyone | Create Events | 開啟，允許建立自己的活動。 |
| @everyone | Manage Events、Manage Server、Manage Roles、Manage Channels、Administrator | 關閉，不因加入 server 取得管理權。 |
| @everyone | Mention @everyone, @here, and All Roles | 關閉。 |
| start-here | Send Messages and Create Posts、Send Messages in Threads and Posts、Create Public Threads、Create Private Threads | 對 @everyone 設 Deny。 |
| welcome | 發訊息、討論串發文、建立公開與私人討論串 | 頻道本身也對 @everyone 設 Deny。 |
| onboard、rules、announcements | 分類權限 | 與 start-here 同步。 |
| management | View Channel | 對 @everyone 設 Deny。 |
| mod-log | 分類權限 | 與 management 同步，保持私有。 |

公開交流頻道允許一般加入者查看、發文、回覆及讀取歷史，lounge 允許進入與發言。start-here 的四個入口頻道不允許一般加入者發訊息、在討論串發文或建立公開、私人討論串；公告由具有效職責與平台能力的人發布，依 Repository 的技術維護安排接續。

management 與 mod-log 對 @everyone 拒絕 View Channel。管理者、角色及公告發布能力依憲政制度與有效 R&R 配置核對及交接，既有平台權限不構成永久職權；不將管理伺服器、管理角色、管理頻道、管理全部活動或 Administrator 開給一般加入者。一般加入者不能使用 @everyone、@here 或大量角色提及。

## 共同事項與跨 R&R 協作

共同事項與具體工作沿用 collaborations，一案一帖，以 tags 區分共同事項與具體協作；tags 採「共同事項」「工作協作」，保留既有 tags，不要求發帖必選 tag，不將用途說明當成平台已配置的字串。一帖交代要做什麼、需要哪些幫忙、如何參與、由誰負責決策及 repo 原案；具體工作由本人自願認領。

提案人可自行在 collaborations 通知並連回 repo 原案，不必先取得 Council 背書或等待 announcements 管理者代發。正式案件、討論與表決依[提案、紀錄與投票程序](<../01-制度/[機制] 憲政制度.md#提案紀錄與投票程序>)，不在 Discord 建第二份正式票數；announcements 整理重要通知與結果，不成為受理關卡。一般號召依[提出提議或活動與號召討論 SOP](<../03-SOP/[SOP]提出提議或活動與號召討論.md>)，不把所有日常交流升級為正式治理案件。

非敏感跨 R&R 協調留在原工作帖，需即時討論時可使用既有 lounge；影響下一步的重要結論與本人接受的工作補回 repo 原案，不要求逐句搬運。敏感事件改依上方[技術接續與敏感事件處理](#技術接續與敏感事件處理)，不因方便協調而公開敏感證據。

<a id="活動建立與管理權限"></a>

## 活動建立與參與

每場活動從籌備、公告、舉辦到同篇 forum 的會後摘要，依[活動籌備、舉辦與會後整理 SOP](<../03-SOP/[SOP]活動籌備、舉辦與會後整理.md>)接續；本節維護平台能力與頻道分工，不另訂第二套辦理流程。

所有 server 加入者均可建立自己的原生 Events 活動排程；不以組織成員資格或管理者身分作為條件。管理全部活動仍限具有效職責及對應平台能力的人，不增加出席或辦活動義務。

活動詳情與討論放 events，籌備工作號召放 collaborations。每場活動說明目的、時間、地點或會議連結及參與方式；若另有名額、審核或報名要求，須在該活動說清楚，Interested 不等於完成另行要求的報名。尚未發起的活動不填入虛構日期、地點或出席承諾。活動遵守[憲法](<../01-制度/憲法.md>)。

<a id="community-與安全設定"></a>

## Community、通知與安全設定

Community 及安全設定保護公開交流；平台驗證不取代組織申請與審查。

| 設定 | 採用值 |
|---|---|
| Community | 啟用。 |
| Rules or Guidelines Channel | rules。 |
| Community Updates Channel | mod-log。 |
| Safety Notifications Channel | mod-log。 |
| 發訊息驗證 | 要求已驗證信箱。 |
| 敏感媒體檢查 | 所有成員。 |
| Default Notification Settings | Only @mentions。 |
| System Messages Channel | chit-chat。 |
| 自動歡迎、歡迎貼圖提示、Boost 通知、server setup 提示 | 開啟，均使用系統訊息頻道。 |

AutoMod 採用下表設定；這些規則不自動禁言。

| 規則 | 狀態 | 阻擋條件／範圍 | 動作 | 警示目的地 |
|---|---|---|---|---|
| Block Mention Spam | 啟用 | 每則訊息最多提及二十個不同對象。 | Block message、Send alert。 | mod-log。 |
| Block Suspected Spam Content | 啟用 | 平台判定的可疑垃圾內容；此規則僅支援英文。 | Block message、Send alert。 | mod-log。 |

## 新人引導與 Next 接續

### Onboarding 的入口與預設頻道

Onboarding 與 Server Guide 均啟用，使用預設模式，不設定加入前或加入後的角色問卷。加入者不必先回答問卷才能找到公開頻道，也不會透過問卷自動取得組織成員資格。

| 設定 | 採用值 |
|---|---|
| Default Channels：文字與論壇 | welcome、onboard、rules、announcements、chit-chat、funding、discussions、collaborations、events，共九個。 |
| 語音入口 | lounge。 |
| 私有頻道 | mod-log 不列入新人預設入口。 |
| Resource Pages | 不設定；入口頻道保留在頻道列表。 |
| Server Guide 自訂 Banner、任務自訂縮圖 | 不設定。 |

### 歡迎訊息

Server Guide 的 Welcome Sign 由 waterball.pan 顯示，使用下列文字；[@username] 是平台代入新人名稱的位置：

> 歡迎 [@username]！這裡是 AI-Native Global Founders Speedrun Taiwan。組織目前還在建設中，歡迎先交流、參與活動，也一起做些什麼。先看 welcome、onboard 與 rules；有問題到 chit-chat。onboard 有可直接貼給 Agent 的 prompt，帶你認識組織，再依意願申請。下方是入門導覽，不是額外入會門檻。

### New Member To Do 與完成條件

三個自訂任務依下表排列。每項都使用 **Member visits the channel** 作為完成條件；不採用傳送訊息或在論壇發文、回覆作為完成條件。

| 順序 | 任務文字 | 目的頻道 | 完成條件 | 依序瀏覽時的接續 |
|---|---|---|---|---|
| 第一項 | 認識組織，使用 Agent 引導或閱讀加入說明 | onboard | 進入 onboard。 | Next：看看正在號召的協作工作，導向 collaborations。 |
| 第二項 | 看看正在號召的協作工作 | collaborations | 進入 collaborations。 | Next：看看線上與實體活動及參與方式，導向 events。 |
| 第三項 | 看看線上與實體活動及參與方式 | events | 進入 events。 | 自訂任務至此結束，沒有第四個自訂任務。 |

Read the rules 是平台另提供的規則入口，對應 Community 的 rules 頻道，不是第四個自訂任務。Next 是 Discord 原生新人導覽按鈕，不是發在頻道中的訊息或自建 bot。

依序瀏覽的路徑為：Server Guide → onboard → Next → collaborations → Next → events。導覽任務可以從 Server Guide 直接選取，並不把前一個任務完成當成開放下一個公開頻道的權限門檻。

導覽完成只代表到過對應頻道，不代表已讀完文字、提出自介 PR、通過審查、認領工作或報名活動。這些行為依各自制度與活動說明辦理；導覽也不強制發言或出席。

### onboard SOP 與頻道說明的接合

onboard 以[釘選訊息](https://discord.com/channels/1563453138810306612/1563456791050977341/1564254596208271400)承接第一項導覽，直接提供可複製給 Agent 的 prompt：先引導理解組織，待本人確認想申請後，再依現行 members 說明及 SOP 逐題完成自介、本人真人照片、Contributions、獨立 assignment 的 Contributors 選擇與 PR 申請。不使用 Agent 仍可依 [members 提交說明](../../members/README.md)手動完成；資格判定依[申請制度](<../01-制度/[機制] 憲政制度.md>)。不在 Discord 建立第二套加入規則。

### onboard 釘選文案

下列文案使用 Discord Markdown；頻道提及指向本 server 已存在的頻道。此 Agent prompt 延續 [Threads 邀請公版](<../03-SOP/[SOP]Threads引流招募客服SOP.md>)先理解組織、再依意願申請的順序；兩處不要求使用同一段 prompt，Discord 不帶入私訊客服或發送規則。

````markdown
**Onboard｜從這裡開始**

歡迎來到 AI-Native Global Founders Speedrun Taiwan！目前組織還在建設中，歡迎先進來交流、參與活動，也一起做些什麼。
進入 Discord 不等於已成為組織成員；你可以先認識我們，再決定是否申請。

**把這段 prompt 貼給你的 Agent**
```text
我想了解並考慮加入 AI-Native Global Founders Speedrun Taiwan：
https://github.com/AI-Native-Global-Founders-Speedrun-TW/ai-native-founders-tw-mono

請先 git clone 這個 repo；如果本機已有，使用既有目錄並保留未提交的修改。讀取 AGENTS.md、README.md，沿引用閱讀組織願景、憲法與制度，用清楚的中文引導我了解組織想做什麼、如何運作、成員的權利與義務，以及如何參與分工。不要只列文件名稱或貼整份制度，一次只問一個問題，依我想深入的部分繼續說明。

等我了解並確認想申請加入後，再讀 members/README.md 與相關 SOP，引導我完成自介 PR 申請。一次只問一個問題，依我的回答逐步更新草稿；已有答案不重問，不編造經歷或承諾。依 SOP 核對自介內容、本人真人照片與命名、分工及提交範圍。提交前讓我確認全文與公開資料，再依 SOP 完成 Fork、分支與 PR 提交，回報實際結果及下一步；不代替正式審查。
```

**不使用 Agent，也可以手動申請**
依 repo 的 [members 提交說明](https://github.com/AI-Native-Global-Founders-Speedrun-TW/ai-native-founders-tw-mono/blob/main/members/README.md)，準備自己的自介、真人照片與 Contributors 分工選擇。Contributions（可以幫什麼忙、想要幫什麼忙）與 R&R 分工分開；選擇分工不代表接受指定工作。
提交前請本人確認全文與公開資料；申請及資格依現行制度與有效審查紀錄核對。

**先交流、提問或一起做事**
有問題到 <#1563454007605723186>；創業討論到 <#1564250031706607657>，募資交流到 <#1564236090770984970>，志工協作到 <#1563454194541658122>，活動到 <#1563454084168814612>。參與自願，導覽完成不等於入會、接受工作或活動報名。
````

| 頻道 | 固定說明與接續 |
|---|---|
| welcome | 組織介紹、onboard 與 rules 入口，以及交流、募資、協作、活動、語音與公告的導覽。 |
| onboard | 釘選上述 SOP；操作有疑問到 chit-chat。 |
| rules | 現行交流規範與 repo 的憲法、制度入口。 |
| announcements | 由具有效公告職責與平台能力的人發布重要公告與已確認活動。 |
| lounge | 用語音頻道文字聊天的用途說明承接即時交流，活動詳情回 events、工作號召回 collaborations。 |

welcome 保留組織與頻道導覽；自動加入與其他系統訊息使用前述 chit-chat 設定。

### welcome 公告文案

保留[原歡迎公告](https://discord.com/channels/1563453138810306612/1563453141641597000/1564254698024869990)的訊息與回覆，使用下列文案：

````markdown
**歡迎加入 AI-Native Global Founders Speedrun Taiwan！**

我們共享創業知識、交流經驗與認識彼此，讓志工容易一起做事，也讓線上與實體活動容易發起及參與。目前組織還在建設中，歡迎先進來交流、參與活動，也一起做些什麼。

先看 <#1563456791050977341>：裡面有可以直接貼給 Agent 的 prompt，帶你認識組織，再依意願申請；也保留手動申請入口。現行規範看 <#1564249902475907172>；有問題到 <#1563454007605723186>。

• 創業問題與經驗分享：<#1564250031706607657>
• 募資交流：<#1564236090770984970>
• 號召志工、找人一起做事：<#1563454194541658122>
• 線上與實體活動：<#1563454084168814612>
• 即時語音交流：lounge
• 重要公告：<#1564249954266914846>

公開 repo：https://github.com/AI-Native-Global-Founders-Speedrun-TW/ai-native-founders-tw-mono
Discord 身分與組織成員資格分開，入會依 repo 的現行制度與有效審查紀錄核對。歡迎依自己的時間與意願參與。
````

### rules 公告文案

保留[原規則公告](https://discord.com/channels/1563453138810306612/1564249902475907172/1564254512342900798)的交流規則，只更新有效 repo 入口：

````markdown
**交流規則與現行制度**

這裡維持開放的交流與學習環境，不因背景限制接觸創業知識與參與交流。

• 志工自願參與，認領工作不代表必須獨自完成。
• 不得以本組織名義、筆記或活動為特定公司推銷產品或服務，也不得以收款為條件提供廣告、置入或推薦。
• 進入 Discord 不等於取得組織成員資格；申請方式、自介審查與參與安排依 repo 的現行制度。
• 頻道說明用來幫助找到交流位置，不另外制定入會門檻。

完整憲法與制度：https://github.com/AI-Native-Global-Founders-Speedrun-TW/ai-native-founders-tw-mono
有問題請到 <#1563454007605723186> 詢問。
````

### collaborations 文案

Post Guidelines 使用以下文案；分類與提案程序依[共同事項與跨 R&R 協作](#共同事項與跨-rr-協作)。

```text
號召志工與協作，一件工作、活動籌備或共同事項開一篇。請說明要做什麼、需要哪些幫忙、如何參與、由誰負責決策，以及相關 repo 原案；參與自願，認領不代表必須獨自完成。

可選「共同事項」或「工作協作」分類，不必選 tag 才能發帖。提案人可以自行通知，不必先取得 Council 背書或等待管理者代發。

正式共同事項請連回 repo 的原 Issue／PR；正式討論、決定與表決依 repo 現行制度，Discord 用於通知與協調，不另外統計正式票數。一般交流與工作號召不必變成正式治理案件。

Repo：https://github.com/AI-Native-Global-Founders-Speedrun-TW/ai-native-founders-tw-mono
```

## 邀請與伺服器介紹

| 設定 | 採用值 |
|---|---|
| 現行邀請 | https://discord.gg/xeWYqYaUvU |
| 邀請所屬頻道 | collaborations。 |
| 到期 | 不到期。 |
| Server Description | 共享創業知識、交流經驗與認識彼此，讓志工容易一起做事，也讓線上與實體活動容易發起及參與。 |
| Private Profile | 開啟。 |

邀請所屬頻道與 Server Guide 的導覽任務是不同設定；不將邀請指向 collaborations 解讀成略過 onboard SOP 或完成組織申請。


## Council 帳號核對與操作

Council role 只提供辨識與通知，所有管理能力關閉，不因此開放 management 或 mod-log。允許任何參與者提及 Council role 本身，不為此開啟 @everyone 的 Mention Everyone／All Roles 權限。尚未核實真人任職時可先建立空角色，但不能據此宣布 Council 已成立。

[Council 閱讀入口](../../members/r-and-r-assignment.yml)須等 canonical repo 的 main 已發布且實際可讀後，才在原 onboard 說明加入網址；本機完成不等於已發布，不貼尚不存在的公開網址。角色掛名須另外核對有效任職與本人帳號，名單、合併 PR 或已持有平台權限均不能代替。

新增權限或換綁時，從已可核對的 GitHub 本人及 Discord 互動雙向確認，讀取 Discord User ID，不以暱稱、頭像或同名猜測。可用本次一次性確認或雙向原對話核對控制權，不要求私人證件。公開原案只記核對者、對象、時間及結果；私人訊息及未同意公開的帳號證據不入 public repo。尚未建立共享的私人綁定資料庫；下次新增或換綁時重新核對，不能假稱私人對話可永遠供其他管理者讀取。

撤除已明確對應且職責已終止的能力時，使用原核對依據、既有配置及當下不可變帳號識別，不等待離任者再次同意。身份確有疑義、缺乏合法可查核依據或平台操作能力時，記錄該項受阻並接既有備援／恢復程序，不猜測撤權；可核實的其他項目繼續。交接須真的驗證必要依據可供合格接續者查核，否則仍是接續不足。

操作前核對原案、後續事件、本人利益迴避、已有角色、角色層級與頻道覆寫，列出具體加撤差異；只改本次有效職責所需能力，保留其他有效職位與一般權益。操作後回讀，部分成功逐項記錄；重試先讀當下狀態。誤改只恢復仍有有效依據的能力，不為回復舊狀態重授已失效權限。公開原案保存非敏感結果與未完成接續；截圖與原始驗證輸出不版控。期限與非涉案覆核沿用憲政制度，不另創任命或管理權。
