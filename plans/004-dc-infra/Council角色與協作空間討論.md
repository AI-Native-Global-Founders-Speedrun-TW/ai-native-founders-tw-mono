# Council 角色與協作空間討論

本檔保存 [dc infra Plan](plan.md#接續規劃council角色moderation與協作空間) 的原候選提案及批判歷史。使用者已於 2026-11-01 採納下方「修訂後整體建議」，原提案及「未採納」字樣保留為當時狀態；採納後設計維護於 [Discord Setup](<../../specs/05-社群基建/[規格]Discord-社群-Setup.md#council-身分與-moderator-能力>)，本附件不另當現行規格。採納不等於平台已實作。

## 原提案：Council、moderation 與協作空間

### 原文（逐字未加工）

> 針對 council 的部分，你覺得 dc role 設計該怎麼做， council as moderators 的 category 等等的 collaborate channels 設計等等的想一下整體

### 加工後的提案（尚未採納、未修改 Discord）

建議 Council role 顯示有效治理身分、提供 Council 協調空間；Moderator role 只給已接受 moderation 職責且有有效依據的人。Council 可兼任 Moderator，但不因 Council 身分自動取得全部平台管理能力。依憲法第 6 條（分工議會組成）與第 7 條（決策任命範圍），新增 moderation 職責或擴大 R&R 職權須走適用程序，不能以 Discord role 操作代替。

建議角色包括：@everyone 保留公開交流與本人活動；Member 識別有效正式成員；Council 識別有效 Leader；Moderator 管公開交流區訊息與討論串；既有 Repository 維護者按有效職責接續技術設定。活動及公告能力按實際職責在需要範圍另給，Council 不直接取得 Administrator、Manage Roles、Manage Channels、全站公告發布或全部活動管理。角色掛名依有效證據核對；不在本提案指定現任者。

建議新增公開 governance category：council-updates 唯讀，提供正式案件、進度與結果連結；proposals 用 Forum，正式成員可自行發起，不需 Council 私下受理，其他加入者可閱讀並提問。正式提案與投票仍以現行 repo Issue／必要 PR 為準，不把 Discord poll 或反應當正式票。Council 內部協調放 management 的 council-chat，不能以私有討論代替公開程序或否決成員提案權。

management 保留私有，按頻道分別設 council-chat（Council）、mod-chat（實際 Moderator）、mod-log（必要管理職責者）。敏感案件不因 Council 身分全面開放，只給必要且非涉案者；公開必要程序、理由與結果，私人證據受控查核。

get-involved 的 collaborations Forum 繼續一件具體工作一帖，以 R&R 與進度 tags 協助找人及接續，不按每個 R&R 先新增永久頻道。每帖帶目的、負責決策的 R&R／Leader、需要幫忙、成果與 repo Issue／Plan 入口，具體工作由本人認領。R&R 通知角色若有實際通知需要再建立，不以多個身分取代 assignment。events 繼續負責活動資訊，日常社群區維持開放。

Moderator 候選能力先限公開交流與工作區的 Manage Messages、Manage Threads、必要語音移動／靜音；不在治理紀錄區授予刪文能力。Timeout Members 涉及全 server，不把它當只限某個頻道的工具；先不授予 Kick／Ban 或角色管理。任何暫時限制與案件處理須有明確職責、依據、必要性、紀錄及非涉案覆核，不等於取消正式資格，禁止用 moderation 處理不同意見或自身案件。Discord 權限無法完整限制每次操作目的，仍須靠明定職責、紀錄與覆核。

以上是整體候選設計；角色名稱、公開／私有配置及 moderation 職責尚未獲使用者採納，不是現行 specs。

## 整體觀點批判與交鋒

### 原文（逐字未加工）

> ok 整體分析完了？和另一個帶整體觀點批判帽子的討論一遍

### 獨立批判與回應（討論紀錄，尚未採納）

另一位 agent 讀取實際憲法、制度、Discord 規格、Repository 職責、Plan 與上方原提案後，從整體運作提出反對。以下區分批評、主 agent 回應與收斂，不將討論視為有效採納。

- 批判：新增 council-updates 與現有 announcements 重複；新增 proposals 又以 GitHub Issue 為正式原案，會增加入口與搬運。主 agent 接受精簡，但指出唯讀 announcements 不能成為提案的唯一入口。批判者進一步指出制度明定提案人可自行發布；因此保留 collaborations 的本人發帖入口，以共同事項／治理 tag 分類，通知連回 repo 原案，不能等管理者代發才開始程序。
- 批判：沒有資料證明 collaborations 已擁擠，跨 R&R 協調本來就是工作，不應先建新的 operations forum 或每組永久頻道。主 agent 接受：非敏感協調可一案一帖，急事使用原帖提及 Council 或既有語音；影響後續工作的語音結論回到原案，不要求逐字搬運。
- 批判：Member role 若無實際權益或查核用途，只增加人工同步；council-chat／mod-chat 若同一批人使用，未必值得立即建立。主 agent 接受先不建立，包含原提案的公開 governance category 也先撤回；後續若有具體漏案、難找或協調問題再比較。
- 批判：先核完整有效 Council 與平台帳號對應。不能以熟人、歷史認領或本機待確認欄位推定有效與無效；遠端更新與語音聊天有新線索，但未完成全部資格核定。主 agent 接受，不在討論中指定現任人員。
- 批判：盤點時已核到 mod-log 的存取名單只有 owner；第二人有效職責與實際技術接續能力尚未完成驗證。先完成兩位不同有效 Leader 的接續範圍、本人接受、實際帳號與能力驗證，比新增多個頻道有直接價值。Council 身分與技術操作、內容 moderation 三者不可互相代替。
- 交鋒：批判者初步主張先證明實際 moderation 事件與承接需要；主 agent 反對等受害事件出現才準備，因為組織正在邀請新人。批判者接受並撤回等待事件的要求：可以預先設計可辨識濫發、明確釣魚／惡意連結、洩露憑證等正在發生傷害的最小處置，但須有承接者、有效職責、必要紀錄與非涉案覆核；真偽未明或爭議意見不由 Moderator 自行裁決，不先給廣泛 Timeout／Kick／Ban。
- 補完：需要的是實際敏感事件聯繫入口，不一定是私有 Council 房間。welcome／rules 應能找到已接受且有實際能力的聯絡人與備援；當事人涉案時須有合格非涉案接續者，沒有就如實受阻。申訴正文不丟進公共 collaborations 或 Issue，不因 Council 身分開放原始敏感證據。mod-log 必須有人實際接收警示與接案。後續若兩位操作者確有快速協調需求，再考慮僅必要管理職責者可見的 mod-chat；共用聊天室不取代個案迴避。

### 修訂後整體建議（未採納、未實作）

先不增加 category 或公開／私有聊天頻道，也先不增加無實際用途的 Member role。Council role 僅依有效任職對應，作身分辨識與通知；不自動取得 moderation 或技術管理權。共同事項與工作沿用 collaborations，正式案仍在 repo，announcements 整理重要通知及結果但不是受理關卡。優先核實第二位技術接續者、警示接收與敏感事件聯絡／非涉案備援；moderation 的必要日常職責與最小操作能力先設計並依適用程序成立，不等待第一個受害事件，也不先把所有 Council 掛成完整 moderators。

本輪沒有修改 Discord、R&R 或 specs；上方原提案保留為被批判前版本。

### 批判討論的終版檢查

獨立批判 agent 回讀實際批判討論後，FORMULATION 檢查沒有剩餘問題；憲法第 1 條（名稱與目的）、第 2 條（公益非商業）、第 3 條（效力制度分工）、第 4 條（開放成員資格）、第 5 條（自願參與義務）、第 6 條（分工議會組成）、第 7 條（決策任命範圍）、第 8 條（平等有效表決）、第 9 條（罷免職位替換）、第 10 條（異議資格保障）、第 11 條（利益緊急界線）及第 12 條（修憲成員監督）均沒有違反。這是候選討論與對話忠實性檢查，沒有重新操作 Discord 或裁定任職資格。
