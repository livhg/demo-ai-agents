# Riddle Difficulty Calibrator

謎語難度校準系統是一個 **Loop（循環式）** 多代理系統，展示如何使用 Google ADK 建立迭代改進的工作流程。

## 系統架構

這是一個 **Loop（循環迭代）** 的多代理系統：

```
使用者輸入主題
    ↓
┌─────────────────────────────────┐
│           迭代循環               │
│                                 │
│  [1] Riddle Creator             │
│      (創作謎語)                  │
│          ↓                      │
│  [2] Difficulty Tester          │
│      (測試難度)                  │
│          ↓                      │
│      ┌───────┴───────┐          │
│      │               │          │
│   太簡單/太難      剛剛好         │
│      │               │          │
│      ↓               ↓          │
│   返回步驟 1      呼叫 exit_loop │
│   (附帶反饋)      結束循環        │
│                                 │
└─────────────────────────────────┘
    ↓
最終難度適中的謎語
```

## 為什麼使用 LoopAgent？

### 一次性生成的問題

如果只讓 AI 一次性創作：

- 難度難以掌控，可能太簡單或太難
- 無法根據評估結果調整
- 缺乏品質保證機制
- 結果不穩定

### LoopAgent 的優勢

1. **迭代改進**：根據反饋不斷優化
2. **品質控制**：達標才結束，確保輸出品質
3. **自動化**：無需人工介入，全自動完成
4. **靈活終止**：可設定最大迭代次數，避免無限循環

## 快速開始

### 1. 啟動 ADK Web UI

```bash
adk web
```

### 2. 選擇 Agent

在 Web UI 中選擇 `riddle_difficulty_calibrator`

### 3. 輸入謎語主題

範例輸入：

```
狗狗
```

```
交通工具
```

```
水果
```

### 4. 觀察迭代過程

系統會自動：

1. **第一輪**：Riddle Creator 創作初始謎語
2. **評估**：Difficulty Tester 評估難度
3. **決策**：
   - 如果難度適中 → 呼叫 `exit_loop`，結束
   - 如果太簡單/太難 → 提供反饋，進入下一輪
4. **後續輪次**：Riddle Creator 根據反饋調整，重複評估

### 5. 獲得最終產出

當難度達標時，你會得到：

- 難度適中的謎語
- 謎語的答案
- 通過評估的理由

## 系統特色

### 循環迭代機制

```python
riddle_difficulty_calibrator = LoopAgent(
    sub_agents=[
        riddle_creator,      # 創作謎語
        difficulty_tester    # 測試難度（達標時呼叫 exit_loop）
    ],
    max_iterations=3,  # 最多嘗試 3 次
)
```

### exit_loop 工具

使用 `exit_loop` 函式作為終止信號：

```python
def exit_loop():
    """當謎語達到理想難度時呼叫此函式，結束迭代循環。"""
    return "✅ 循環完成：謎語難度已達標，無需繼續改進。"
```

### 智能難度評估

Difficulty Tester 會分析：

- **線索直接度**：是否太明顯或太抽象
- **推理時間**：預估 10-30 秒為適中
- **唯一性**：答案是否唯一
- **趣味性**：是否有巧思和成就感

### 反饋驅動改進

Riddle Creator 會根據反饋調整：

- **太簡單**：移除直接線索、增加抽象描述
- **太困難**：增加具體線索、減少過度抽象

## 檔案結構

```
riddle_difficulty_calibrator/
├── README.md                      # 本文件
├── __init__.py                    # 模組入口
├── agent.py                       # LoopAgent（主循環）
└── sub_agents/                    # 子代理目錄
    ├── __init__.py
    ├── riddle_creator/            # 謎語創作者
    │   ├── __init__.py
    │   ├── agent.py
    │   └── prompt.py
    └── difficulty_tester/         # 難度測試員
        ├── __init__.py
        ├── agent.py
        ├── prompt.py
        └── tools.py               # exit_loop 工具
```

## 設計理念

### 為什麼選擇謎語難度校準？

1. **清晰的評估標準**：

   - 難度有明確的判斷依據
   - AI 可以有效評估和改進
   - 結果可驗證

2. **展示迭代價值**：

   - 一次創作難以達標
   - 迭代改進效果明顯
   - 學習反饋整合機制

3. **實用性**：
   - 可應用於遊戲、教育等場景
   - 輸出結果有實際用途
   - 容易理解和擴展

### LoopAgent vs 其他模式

| 模式                | 適用場景             | 本專案為何選擇 LoopAgent |
| ------------------- | -------------------- | ------------------------ |
| **SequentialAgent** | 固定步驟的線性流程   | 需要動態迭代次數         |
| **ParallelAgent**   | 可同時執行的獨立任務 | 評估依賴創作結果         |
| **LoopAgent**       | 需要迭代改進直到達標 | ✅ 完美符合需求          |

### 何時使用 LoopAgent？

適合的場景：

- 輸出品質需要達到特定標準
- 一次性生成難以保證品質
- 有明確的評估標準
- 可以根據反饋改進

不適合的場景：

- 沒有明確的完成標準
- 每次迭代成本很高
- 任務本質上不可迭代改進
- 需要人工判斷是否達標（考慮 Human-in-the-Loop）

## 進階應用

### 調整最大迭代次數

```python
riddle_difficulty_calibrator = LoopAgent(
    sub_agents=[riddle_creator, difficulty_tester],
    max_iterations=5,  # 增加到 5 次
)
```

### 自訂難度標準

修改 `sub_agents/difficulty_tester/prompt.py` 中的評估標準，例如：

- 調整為「簡單」難度
- 針對特定年齡層
- 加入特殊創作要求

### 擴展應用

這個模式可以應用於：

- 文案優化：迭代改進直到達到行銷標準
- 程式碼審查：自動改進直到通過檢查
- 翻譯品質：反覆優化直到流暢自然
