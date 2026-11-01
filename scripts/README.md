# Scripts

先分排程與驗證，再按功能分組；在 repo 根目錄執行 Python module。每個 package 的測試和程式放一起，不建立額外工具框架。

| Package | 用途 | 入口 |
|---|---|---|
| [驗證／分工資料](驗證/分工資料/) | 唯讀檢查 R&R 分工、成員引用與 Discord ID 格式 | `python -m scripts.驗證.分工資料.validate` |
| [排程／入會權限處理](排程/入會權限處理/) | 核對已合併的入會申請、接續邀請與平台狀態 | `python -m scripts.排程.入會權限處理.process_onboarding --dry-run` |

共用 Python 依賴只維護在 [requirements.txt](requirements.txt)：

```sh
python -m pip install -r scripts/requirements.txt
python -m unittest discover -s scripts -t . -p 'test_*.py'
```

只跑個別用途的測試：

```sh
python -m unittest discover -s scripts/驗證/分工資料 -t . -p 'test_*.py'
python -m unittest discover -s scripts/排程/入會權限處理 -t . -p 'test_*.py'
```

測試使用模擬 API，不需要正式 token。入會程式的實際 dry-run 需要 GitHub API 授權；設定與操作條件見 [GitHub Setup](<../specs/05-社群基建/[規格]GitHub-Org-Setup.md>)。入會權限處理沿用分工資料驗證 的嚴格 YAML loader，不重複實作解析規則。資格裁決不由這兩個 package 執行。

排程中的程式也可手動執行；排程時間由 GitHub Actions 設定。入會權限處理只接續已核准的 Member 邀請與狀態確認，不授予 Council、Owner 或 repository 寫入權限。
