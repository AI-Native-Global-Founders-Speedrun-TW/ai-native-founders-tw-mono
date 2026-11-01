# Council 表工具

資料規則以[成員識別與資料](<../specs/01-制度/[規格]成員識別與資料.md#council-名單與維護>)為準。本工具只彙整人工核對的來源，不判定任職效力、不連線 Discord、不發角色。

1. 先核對原案及後續事件，更新 `members/r-and-r-assignment.md` 的 Leader 欄位與共同核對截止；未能核實就如實標記，不能為了產生名單填成已生效。
2. 在 mono 根執行 `python3 scripts/render_council.py`。輸出 `members/council.md`；解析失敗不覆蓋原表。
3. 執行 `python3 scripts/render_council.py --check`，並 review 名單與來源。共同截止來自 assignment，不從產生時間自動更新。
4. 來源、產生表與必要規格在同一 PR 接續；不要直接編輯產生表。

`--check` 結束碼：0 表示一致；1 表示表缺少或不同；2 表示來源無法讀取或格式／識別衝突。任何通過都不證明外部事件已完整核對。

執行行為測試：`python3 -m unittest discover -s scripts -p 'test_*.py'`。測試使用暫存目錄，不改真實成員資料；驗證輸出不納入 Git。CI 工作流只讀檢查，無 Discord 憑證與 repo 寫入權限。

來源摘要值只包含 Council 直接使用的 Leader 欄位、共同截止及引用成員的識別與稱呼；新增一般自介、修改背景或 Contributors 不要求新人改 Council 表。所有已識別成員的編號及 GitHub 重複仍會回報衝突。
