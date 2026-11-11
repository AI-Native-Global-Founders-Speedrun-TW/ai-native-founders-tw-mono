---
document_type: Plan
adopted: true
---

# Startup 101 skills 與 Canvas 模組

## 使用者原文

> I created startup101-cami-skills. Package the Startup 101 skills and canvas in that repo, credit Cami and Startup 101 (see their official wesite) in the README, and add it as a submodule to ai-native-founders-tw-mono.
>
> Also Pick one License that best fit for this

## 工作與影響

三支 skills、Python runtime、YAML 範本、本地 Next app、Canvas 源碼與測試放入獨立 repository，modules/startup101-cami-skills 固定版本。README 署名 Cami Lu 呂緗柔及 STARTUP101，附官方網站。

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

邀請紀錄提交排在模組提交之前。模組 repository 為私人，初始化這個 submodule 時需要該 repository 的讀取權限。

獨立 review 逐條核對憲法與 FORMULATION。公開 PR 的邀請進度以確認送出的總數記錄，逐人紀錄留在原工作區。模組路徑與版本、署名和使用說明通過檢查。
