# Icon Design with Approval

人工確認的 Icon 設計系統是一個 **Human-in-the-Loop** 多代理系統，展示如何在關鍵決策點加入人工確認流程。

## 系統架構

這是一個 **Sequential + Human-in-the-Loop** 的多代理系統：

```
使用者輸入需求
    ↓
[1] Requirements Analyst
    (分析需求)
    ↓
[2] Design Strategist
    (制定設計策略)
    ↓
    ┌─────────────────────────┐
    │ [暫停] 等待人工確認      │
    │                         │
    │ 您可以：                 │
    │ • 批准 (approved)       │
    │ • 修改 (提供建議)        │
    │ • 拒絕 (reject)         │
    └─────────────────────────┘
    ↓
[3] Final Prompt Generator
    (根據反饋生成 prompt)
    ↓
最終 AI 圖像生成 Prompt
```

## 為什麼需要 Human-in-the-Loop？

### 完全自動化的風險

如果沒有人工確認：
- 可能在錯誤的設計方向上浪費資源
- AI 的理解可能與人類期望不符
- 無法融入人類的創意和專業判斷
- 缺乏靈活性和控制感

### Human-in-the-Loop 的優勢

1. **風險控制**：在投入資源前確認方向正確
2. **創意參與**：融入人類的創意想法
3. **靈活調整**：可以根據實際情況調整策略
4. **信任建立**：使用者保有最終決策權

## 快速開始

### 1. 啟動 ADK Web UI

```bash
adk web
```

### 2. 選擇 Agent

在 Web UI 中選擇 `icon_design_with_approval`

### 3. 輸入設計需求

範例輸入：

```
請為音樂創作 app 設計 icon，風格要有創意且吸引年輕用戶
```

```
設計一個健康追蹤 app 的 icon
```

### 4. 審核設計策略

系統會：
1. 分析需求
2. 制定設計策略
3. **暫停並等待您的確認**

您會看到設計策略的總結，然後可以：

#### 選項 1：批准策略
```
輸入：approved
或：同意
```
系統會按照原策略生成 prompt

#### 選項 2：提供修改建議
```
輸入：請改用藍綠色配色
或：增加科技感的元素
```
系統會整合您的建議，調整設計策略

#### 選項 3：拒絕策略
```
輸入：reject
或：重新設計
```
系統會知道需要完全重新思考

### 5. 獲得最終產出

根據您的反饋，系統會生成：
- 整合了您的意見的最終 prompt
- 可直接用於 AI 圖像生成

## 系統特色

### 關鍵決策點的暫停機制

```python
icon_design_with_approval = SequentialAgent(
    sub_agents=[
        requirements_analyst,      # 自動執行
        design_strategist,         # 自動執行
        approval_coordinator,      # ⏸️ 暫停等待
        final_prompt_generator     # 根據反饋執行
    ],
)
```

### 人工確認工具

使用 Python 的 `input()` 函式：

```python
def request_human_approval():
    user_feedback = input("你的決定：").strip()
    return user_feedback
```

### 智能反饋處理

Approval Coordinator 會分析人工輸入：
- 識別批准信號："approved", "同意", "ok"
- 識別拒絕信號："reject", "重新設計", "不行"
- 提取修改建議：其他具體的文字輸入

Final Prompt Generator 會根據反饋調整：
- `APPROVED`：按照原策略生成
- `MODIFY: [建議]`：整合修改建議
- `REJECTED`：提示需要重新設計

## 檔案結構

```
icon_design_with_approval/
├── README.md                          # 本文件
├── __init__.py                        # 模組入口
├── agent.py                           # SequentialAgent（含暫停點）
└── sub_agents/                        # 子代理目錄
    ├── __init__.py
    ├── requirements_analyst/          # 需求分析師
    ├── design_strategist/             # 設計策略師
    ├── approval_coordinator/          # 人工確認協調員
    └── final_prompt_generator/        # 最終 Prompt 生成器
```

## 設計理念

### 為什麼在設計策略階段暫停？

1. **成本效益**：
   - 設計策略是關鍵決策點
   - 此時修正成本最低
   - 避免後續浪費

2. **人類價值**：
   - 設計策略需要創意判斷
   - AI 可能不理解品牌細微差異
   - 人類可提供業界洞察

3. **流程效率**：
   - 不是每個步驟都需要確認
   - 選擇最關鍵的一個點
   - 平衡自動化與控制

### 何時使用 Human-in-the-Loop？

適合的場景：
- 高成本操作（如：實際生成圖像需付費）
- 需要專業判斷（如：品牌設計）
- 探索性工作（如：尋找最佳方案）
- 訓練和微調（收集人類偏好）

不適合的場景：
- 低成本、可重複的任務
- 已有明確標準的任務
- 需要快速大量處理的任務
