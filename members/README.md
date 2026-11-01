# 自我介紹與 PR 提交說明

加入方式依[申請制度](<../specs/01-制度/[機制] 憲政制度.md#申請與成員資格>)。一般申請以自介 PR 為基礎門檻；資格生效、首屆任命例外及退出恢復均依[憲政制度](<../specs/01-制度/[機制] 憲政制度.md>)。Discord 邀請、Star 及活動留言不取代自介審查。

## 自介參考範例

每個人都要在自介附上一張本人的真人照片。照片放在 `members/assets/`，自介以相對連結引用；命名依[照片與圖片檔名](../specs/03-SOP/[SOP]自介PR審查SOP.md#照片與圖片檔名)。

下方格式可自由調整。請寫清楚你是誰與自己的背景、為什麼加入、想要獲得什麼、想分享什麼，以及自己的 Contributions：可以幫什麼忙、想要幫什麼忙。

自介看的是參與真誠，不看背景、實力或經歷。沒有專案、仍在探索創業志向，也可以如實說明。Contributions 必須在提交前寫清楚，不能留待之後補充；寫得越清楚，未來大家有志辦活動時，越能善用 AI 找到相關可以幫忙的志工。這不表示承諾接受任何指定工作。

```markdown
# <你的名字或慣用稱呼>

![<你的名字或慣用稱呼>的真人照片](assets/pending-<小寫GitHub帳號>-<你的名字或慣用稱呼>-半身照.<副檔名>)

## 成員資料

Member ID：待配置
GitHub：<你的 GitHub 帳號>

## 我是誰

<介紹目前在做什麼、關注什麼。正在創業、做產品、工作、就學或仍在探索，都可以如實寫。>
其他聯絡方式或作品連結：<填寫你願意公開的聯絡方式或作品連結，選填。>

## 我正在 build 的產品或專案（選填）

<可以介紹自己有興趣或正在進行的專案、產品，以及想解決的問題，附上願意公開的連結。沒有專案或不想填寫，可以刪除整節；不影響申請。>

## 為什麼想加入

<是什麼讓你想加入這個組織？可以從最近遇到的問題、一次經驗，或想嘗試的事情說起。如果還不確定自己的創業志向，也可以說明目前想探索什麼。>

## 想要獲得什麼

<你目前最想釐清什麼問題、學到什麼，或認識能交流哪些事情的人？請盡量具體，讓大家知道可以跟你聊什麼、在哪裡提供協助。>

## 想分享什麼

<有哪些經驗、故事、知識、做法或正在嘗試的事情，願意和大家分享？尚未有完整成果也可以如實寫。>

## 我的 Contributions：可以幫什麼忙、想要幫什麼忙

Contributions 必須在提交前寫清楚，不能留待之後補充。寫得越清楚越好：未來大家有志要辦任何活動，都可以善用 AI，透過 Contributions 尋找相關可以幫忙的志工。

### 可以幫什麼忙

<具體寫出你目前可以協助的事情，以及能協助到什麼程度，讓發起活動的人與 AI 知道哪些事情可以找你。>

### 想要幫什麼忙

<具體寫出你有意願參與哪些活動或工作、想協助哪個部分。可以是你想一起嘗試或邊做邊學的事情，請說明清楚。>
```

## 提交 PR

1. 登入 GitHub，Fork [本 Repo](https://github.com/AI-Native-Founders-TW/ai-native-founders-tw-mono)。
2. 在自己的 Fork 建立分支，在 `members/` 新增一份 Markdown 自介。初次申請使用 `pending-<小寫GitHub帳號>.md`，Member ID 保留「待配置」，不自行選編號；已有編號者直接更新原自介。正式檔名與識別規則依[成員識別與資料](<../specs/01-制度/[規格]成員識別與資料.md>)，由合併人員在合併前配置。同時將本人的真人照片上傳至 `members/assets/`，依[照片與圖片檔名](../specs/03-SOP/[SOP]自介PR審查SOP.md#照片與圖片檔名)命名，並在自介引用相同檔名。不要修改別人的自介或照片。
3. 將範例中的 `<...>` 替換成自己的內容。可以用 AI 協助整理，但提交前務必由本人親自 review 全文：確認照片是本人的真人照片且可公開、圖片正常顯示，以及經歷、連結、動機、期待與 Contributions 真實，沒有 AI 編造的內容或參與承諾，也沒有不願公開的個資。
4. 依[成員參與制度](<../specs/01-制度/[機制] 憲政制度.md#rr-assignment>)，從 [R&R assignment](r-and-r-assignment.yml)選至少一個 R&R，將自己列入 Contributors，可選多個。在對應 role 的 contributors 清單填入從 repo 根起算的個人成員檔案路徑，不重抄 Member ID、GitHub 或資格狀態。不修改其他人的 assignment，也不在自介另抄有效分工名單。
5. Commit 後從自己的分支開啟 Pull Request，目標為本 Repo 的 `main`。確認變更只有自己的成員檔案、照片及 assignment 中與自己有關的資料，再按 **Create pull request**。不必把 PR 狀態或時間抄進自介。審查意見及結果留在該 PR。可參考 [GitHub 官方 PR 說明](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request-from-a-fork)。
6. PR 是申請，依制度審查通過並合併 PR 後才成為成員，入會時間直接看 PR 合併時間。若需要補充，依 PR 上的審查意見修正。有不熟悉的操作或問題，可以在 Discord 中發問或回覆。

審查依現行[申請制度](<../specs/01-制度/[機制] 憲政制度.md#申請與成員資格>)辦理，執行安排見[自介審查](<../specs/01-制度/[機制] 憲政制度.md#自介審查>)。Onboard Leader 依制度審查，異議交非涉案覆核人；通過後只邀請成為 GitHub org Member，不加入 Members team，後續繼續使用 Fork／PR。具體處理見[自介 PR 審查 SOP](<../specs/03-SOP/[SOP]自介PR審查SOP.md>)，收件、排隊、承接後處理目標依憲政制度；處理目標不保證任何時候都有可承接人力。

## 找成員與分工

到[本目錄](./)閱讀每人的成員檔案；檔名不等於正式資格，須核對自介申請 PR 的有效審查、合併紀錄及後續退出／恢復等有效紀錄。按分工找人讀 [R&R assignment](r-and-r-assignment.yml)，按人查分工則在 assignment YAML 搜尋該人的檔案路徑。不另維護重複名單或自介內的有效分工清單，也不從檔案存在推定成員資格。

## 資料維護

| 資料 | 唯一維護位置與更新方式 |
|---|---|
| 編號、目前帳號、本人稱呼、照片、自介與 Contributions | 個人成員檔案；照片放 assets。依[成員識別與資料](<../specs/01-制度/[規格]成員識別與資料.md>)維護。 |
| 入會是否成功與入會時間 | 自介申請 PR 的有效審查及 GitHub 合併紀錄；不另外手填狀態或時間。 |
| 入會、退出、恢復及更正的原始依據 | 該次 PR 的說明、review 或引用的有效紀錄；前後狀態由 Git 與 PR 歷史保存，不另抄流水帳。 |
| Leader | [r-and-r-assignment.yml](r-and-r-assignment.yml)；任命、本人接受與生效依據留在原 PR／Issue。 |
| Contributors | [R&R assignment](r-and-r-assignment.yml)。 |
| 各 R&R 的責任及 SOP | [R&R package](<../specs/02-R&R/README.md>)；不在成員資料重抄。 |

修改背景或 Contributions，只改自己的檔案；調整 Contributors，只改 assignment。資格變動的聲明與決定留在相關 PR／Issue，按實際情況接續 assignment 與交接，不回填自介狀態。一般入會須審查通過並合併，直接讀取 PR 合併時間；退出、恢復、首屆任命及既有資格依憲政制度各自規則核對。

## 多人編輯與識別

assignment YAML 每項 R&R 一筆 role、leader 與 contributors。新增自己時只改對應 contributors，保留其他人的行、leader 與順序。個人成員檔案一人一份，個人資料逐行維護，避免多人修改同一行。

準備合併時由有權限者依[識別規格](<../specs/01-制度/[規格]成員識別與資料.md>)配置編號並更新自介、檔名及受影響的 assignment YAML 路徑；申請者不競爭下一個號碼。改帳號請在 PR 說明前後帳號與本人對應依據，保留編號；退出恢復沿用原檔。對應尚未核對時不自行當成另一個人，也不要求預設公開私人證件。


## Council 名單與維護

直接讀 [assignment YAML](r-and-r-assignment.yml)，先依原案核對各 role 的有效任職，再將有效 leader 依同人去重為 Council；欄位有值本身不證明已生效；兼任多項職責仍只算一人。不另外手填或產生 Council 名單。

檔頭註解包含格式、欄位、範例與驗證方式。職責定義見 [R&R 入口](../specs/02-R&R/README.md)，各 Role 的人員入口指向同一份 YAML，以 role 名稱查找。任命及本人接受依據留在原 PR／Issue；leader 為 null 不表示已裁定無人具資格。詳細規則依[成員識別與資料](<../specs/01-制度/[規格]成員識別與資料.md#council-名單與維護>)。


## Discord 帳號對應

可在個人成員檔案的「成員資料」補上選填欄位；未核對時可不填，或寫：

```yaml
discord_id: null
```

取得本人或資料維護者明確提供的帳號對應後，可將 null 換成以引號包住的 Discord 使用者 ID 字串；來源留原 PR／Issue，登錄不代替操作前的本人核對。填寫與核對規則見[Discord 帳號對應](<../specs/01-制度/[規格]成員識別與資料.md#discord-帳號對應>)。Council mapping 由 assignment 的 leader 找到個人檔案，再讀取 discord_id，不在各職位重抄。不知道 ID 時不用猜，也不影響入會或任職資格。


## 執行資料驗證

在 repo 根目錄安裝 `python -m pip install -r scripts/requirements-validation.txt`，再執行 `python scripts/validate_assignments.py`。測試使用 `python -m unittest discover -s scripts -p 'test_validate_assignments.py'`。PR CI 執行相同指令，失敗時依錯誤修正格式或引用；不可為了通過而清空既有 Leader。檢查範圍與限制見[自動資料驗證](<../specs/01-制度/[規格]成員識別與資料.md#自動資料驗證>)。
