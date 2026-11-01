# Council 與 R&R assignment SSoT 設計

使用者已同意單一 assignment YAML，並要求完成一致性檢查後更新既有 PR。此版取代前版雙 YAML 及產生表設計；歷史保留在同 Plan 與 Git。

唯一資料為 [members/r-and-r-assignment.yml](../../members/r-and-r-assignment.yml)。每項職責一筆 role、leader、contributors，完整格式與驗證說明在 YAML 檔頭。Leader 與 Contributors 同處閱讀；Council 先依原案核對有效任職，再將有效 leader 依同人去重；欄位有值本身不證明已生效，不另手填或產生名單。

規則由[成員識別與資料](<../../specs/01-制度/[規格]成員識別與資料.md#council-名單與維護>)及[憲政制度](<../../specs/01-制度/[機制] 憲政制度.md>)維護，職責由既有 Role 文件定義。任命、本人接受與生效證據留原 PR／Issue；格式遷移不核定真人資格。

本輪保留 11 項職責及 16 筆 Contributors 關係；恢復既有四項 Leader 對應：Sun 的活動、品毅的 Repository、水球的 Domain-Name 與司法覆核；保留對應不另宣告原案生效程序完成。移除舊 Markdown 名單與前版 Council YAML，更新 README、Role 入口、SOP 與資料引用。不新增 parser、schema、CI 或同步服務。

網站實際來源只掃 members 下 Markdown 自介，排除舊 assignment 檔名；新 YAML 不會被讀成自介。該舊檔名在測試中用作排除樣本，不是讀取依賴，無需改網站程式。

Discord 仍等 PR 合併且 main 上 YAML 可讀後再補 onboard 入口；本輪更新 PR 不等於合併、部署或派發角色。
