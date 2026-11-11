---
document_type: Plan
adopted: true
---

# Cami Startup Canvas skills 與 Canvas 模組

## 使用者原文

> I created startup101-cami-skills. Package the Startup 101 skills and canvas in that repo, credit Cami and Startup 101 (see their official wesite) in the README, and add it as a submodule to ai-native-founders-tw-mono.
>
> Also Pick one License that best fit for this

## 工作與影響

三支 skills、Python runtime、YAML 範本、本地 Next app、Canvas 源碼與測試放入獨立 repository，modules/startup101-cami-skills（改名前路徑，現為 modules/startup-cami-skills）固定版本。README 署名 Cami Lu 呂緗柔及 STARTUP101，附官方網站。

原創軟體採 MIT，便於社群使用與修改並保留著作權與授權聲明。教材摘錄、第三方照片與 AllWill 私人專案資料未隨包散布。課程衍生內容及第三方權利由原權利人保有。

依 FORMULATION，module 維護實作與使用說明。這次收錄沒有組織職責、職權或對外合作承諾變更。

## 完成依據

全新暫存專案 init、setup 與 npm ci 成功。Canvas template、核心長卡、多語系與 injection checks 通過。獨立 review 發現範本教材摘錄與測試外部路徑，已移除摘錄並修正包內路徑。兩個過期的 legacy-only JS 測試未收錄，核心畫布與 Python 測試保留。

## Review

FORMULATION 獨立檢查通過，modules 路徑、gitlink、README、授權及來源一致。目標 private repo 推送由本次請求授權，mono 本地提交。

逐條憲法核對均無違反。第 1 條（組織目的）符合創業學習，第 2 條（公益署名）保留貢獻者署名且無置入，第 3 條（最高效力）無制度變動，第 4 條（成員資格）無資格變動，第 5 條（自願參與）無強制工作，第 6 條（角色權限）無任命擴權，第 7 條（決策任命）屬技術收錄且未宣稱合作承諾，第 8 條（表決效力）無表決變動，第 9 條（罷免替換）無任免，第 10 條（異議保障）無權利變動，第 11 條（利益資料）無私人資料或利益交換，第 12 條（修憲監督）無修憲或減權。

清除摘錄後 fresh init 發現 schema 將 grounding 列為必填，已改為可省略，原欄位仍相容。新模板 init 與 render 成功，評分規則保留。Next production build 通過。

## 追加的使用者原文

> 然後幫我把那幾個 skills 也直接移動進去這個 submodule(repo) 下
> README.md 要說清楚如何使用這個 Skill in zhTw

三支 skills 正式維護於 module 的 .agents/skills。CEO 原路徑改為連結，同一份實作供既有呼叫使用。README 已改繁體中文，包含安裝、對 AI 的呼叫範例、手動 init／setup／啟動、續跑、同步及重建。

## 致謝連結修正

> 欸欸 [https://www.cami.works/](https://www.cami.works/) 這連結無法存取啊

舊連結回傳 502。README 的 Cami 署名改連政大商學院專訪，Canvas 介紹頁保留同一專訪入口，移除失效的個人網站入口。STARTUP101 官網連結保留。

### 改用 LinkedIn

> 然後我覺得不如放 Linkedin 吧？？？
>
> [https://www.linkedin.com/in/camillialu/](https://www.linkedin.com/in/camillialu/)

致謝連結改用指定的 LinkedIn，供本地 review。

## 合併提交紀錄

> squash these commits ，讓整個 repo 只有一個 commit
>
> push force this repo
> and make adjustment to the commit record of this submodule from mono repo

技能與畫布 repo 的 main 合併成一筆提交，保留 LinkedIn 致謝。社群 mono 將四筆本地模組提交合併成一筆，直接固定該版本。這次推送範圍是技能與畫布 repo 的 main。

獨立 review 核對 FORMULATION 與憲法各條，確認模組版本、致謝與授權範圍一致。推送後回讀 GitHub 的 main，與 mono 固定的版本相同，該版本只有一筆提交。

## 社群 mono 交付

> 發 PR 而不是直接合併

邀請紀錄提交排在模組提交之前。當時模組 repository 為私人，初始化這個 submodule 需要該 repository 的讀取權限；2026-11-11 改名時 repository 已是公開。

獨立 review 逐條核對憲法與 FORMULATION。公開 PR 的邀請進度以確認送出的總數記錄，逐人紀錄留在原工作區。模組路徑與版本、署名和使用說明通過檢查。

## README 影片預覽

使用者要求加入 YouTube 影片，並授權直接推送及更新 submodule 指標。README 介紹下方加入影片縮圖與觀看連結，縮圖請求回傳 HTTP 200，點擊前往 YouTube。這次只調整 README 與模組版本，無規格變更。

獨立 review 通過 FORMULATION 與憲法逐條檢查。第 1 條（名稱與目的）、第 2 條（公益非商業）、第 3 條（最高規範效力）、第 4 條（開放成員資格）、第 5 條（自願貢獻義務）、第 6 條（分工與議事會）、第 7 條（決策範圍任命）、第 8 條（平等有效表決）、第 9 條（罷免職位替換）、第 10 條（異議資格保障）、第 11 條（利益緊急處置）、第 12 條（修憲成員監督）均無違反。

## 因商標改名為 startup-cami

> 因為商標的問題，我們不能把名字命名成 Startup101，那是不行的。所以提到時也不要秀 Startup101 的商標，都不要，秀 Cammy 就好了。

> 另外有一件事情：repository 裡面我們有個 side project 是 AI native，它底下 model repo 裡面有把這個 skill 收錄進去，所以收錄這個 skill 的那個 repo 名稱要改，你盤一下 impact

> https://github.com/AI-Native-Global-Founders-Speedrun-TW/startup-cami-skills
>
> 裡面的 readme 就沒改
> 幫忙都大改掉吧，

> 改完就 push 吧

> 記得這個也要 commit and push both repo!!

使用者先前指定 skill 名稱為「/startup-cami-xxxx」，影片中念 `startup-cami-office`。使用者轉述 Cami 在群組的原話：

> startup101 可以改成 Cami嗎
>
> 可以說Cami做投資同時也做加速器
>
> 把STARTUP101 作為我的產出之一
>
> STARTUP101 <<<我們全部都是大寫而且數字連載一起

GitHub repository 已由使用者改名為 `startup-cami-skills`。模組內三支 skills 改為 `startup-cami-office`、`startup-cami-facilitation`、`startup-cami-evaluate`。runtime、範本、專案資料檔與本地 view 設定隨之改名，專案資料檔為 `startup-cami.yaml`。只有舊檔名 `startup101.yaml` 的既有專案仍可讀寫，`migrate-name` 預設預覽，`--apply` 才改成新檔名並保留舊檔。已存進使用者資料的識別碼維持原值，改動會讓既有資料失效。

README 改以 Cami Startup Canvas 為名，更新 clone 網址、指令與檔名，並說明改名前建立的專案如何沿用。README 致謝與 About 頁的 Cami 介紹改用上述原話：「Cami 做投資，同時也做加速器，STARTUP101 是她的產出之一」。STARTUP101 只作為 Cami 的產出與照片來源標示，不作產品或 skill 名稱，也不再放推介 STARTUP101 服務的延伸閱讀區塊。Cami 照片原本可見麥克風牌上的 STARTUP101 logo，已換成修去 logo 的版本，Canvas 範本與離線介紹頁的內嵌照片同步更換。README 拿掉仍顯示舊產品名的 YouTube 縮圖，保留影片文字連結。

mono 的 submodule 路徑改為 `modules/startup-cami-skills`，`.gitmodules` 改為新網址，本 Plan 目錄同步改名。這次沒有 specs 變更：改名屬於模組實作與使用說明，組織職責、職權與合作承諾不變。

### 完成依據

改名後的 Python（runtime、setup、migration、decision review、language、sync core、YAML runtime、名稱相容）、Node（canvas cache、core canvas、About 語系）、template 與 Next HTTP 測試通過。改名前已失敗的三支舊測試（`test_clusters.py`、`test_integration.py`、`test_next_client.cjs`）在改名前版本上失敗原因相同，未納入本次修正。暫存目錄端到端實測：新專案 init 產生 `startup-cami.yaml`，setup、production build 與 `/api/canvas` 正常；以改名前 runtime 建立的舊專案可由新 runtime、setup `--upgrade` 與 Next app 讀取，`migrate-name --apply` 後內容雜湊不變。

### Review

獨立 subagent 依 FORMULATION 全文審查兩輪。第一輪擋下四項：Cami 照片仍可見麥克風牌上的 STARTUP101 logo；README 的 YouTube 縮圖仍顯示舊產品名；About 頁的 STARTUP101 推介區塊與 Cami 介紹和 README、Plan 的說法不一致；Plan 缺 Cami 原話與過時描述。四項修正後複審通過，另修英文 Cami 介紹用字並刪除不再使用的樣式。

尚未處理：照片來源標示沒有註明照片經修改。GitHub repository 說明欄仍寫舊產品名並誤拼 Cami 的名字，推送後以 repository 設定修正。

### 憲法檢查

複審逐條結論均為沒有違反。第 1 條（名稱與目的）、第 2 條（公益與非商業性：STARTUP101 服務推介區塊已刪，只保留 Cami 要求的署名與照片來源）、第 3 條（最高效力與制度分工）、第 4 條（開放與成員資格）、第 5 條（自願貢獻與參與義務）、第 6 條（R&R 與 Council）、第 7 條（決策範圍與任命）、第 8 條（平等表決與有效決定）、第 9 條（罷免與 Leader 替換）、第 10 條（異議與資格保障）、第 11 條（利益衝突與緊急處置）、第 12 條（修憲與成員監督）。第一輪曾判第 2、3 條違反（推介區塊），已隨刪除解除。
