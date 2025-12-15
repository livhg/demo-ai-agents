# Multi-Agent System -- 使用 ADK 框架

使用 Google Agent Development Kit (ADK) 建立的多代理系統範例集，展示四種不同的多代理工作流模式。

## 環境設置

### 安裝說明

請參考 [SETUP.md](./SETUP.md) 完成以下步驟：

1. 安裝 Python 3.14 與 uv（可選）
2. 建立虛擬環境
3. 安裝 Google ADK

### 設定 API Key

在各 Agent 目錄內建立 `.env` 檔案，填入你的 API Key：

```
GOOGLE_API_KEY=your-api-key-here
```

需要設定的目錄：

- `icon_design_studio/.env`
- `icon_style_explorer/.env`
- `riddle_difficulty_calibrator/.env`
- `design_with_approval/.env`

### 啟動 Web UI

```bash
adk web
```

在瀏覽器中開啟後，選擇想要體驗的 Agent 即可開始互動。

---

## 🎯 體驗不同模式的多代理系統

本專案包含四種經典的多代理工作流模式，每種模式都有其獨特的應用場景：

| 模式                  | 範例專案                     | 特色               | 適用場景             |
| --------------------- | ---------------------------- | ------------------ | -------------------- |
| **Sequential**        | Icon Design Studio           | 順序執行，層層推進 | 有明確先後順序的任務 |
| **Parallel**          | Icon Style Explorer          | 並行執行，同時探索 | 需要同時比較多種方案 |
| **Loop**              | Riddle Difficulty Calibrator | 循環迭代，直到達標 | 需要反覆優化的任務   |
| **Human-in-the-Loop** | Design with Approval         | 關鍵節點人工確認   | 高風險決策需人工介入 |

---

### 1️⃣ Sequential 順序型 — Icon Design Studio

**路徑**：[`icon_design_studio/`](./icon_design_studio/README.md)

專業的 Icon 設計工作流，三個 Agent 依序協作：

```
需求分析師 → 設計策略師 → Prompt 工程師
```

**試試看**：

```
請為一個智慧家居控制 app 設計主要的 app icon
```

**特色**：

- 每個 Agent 專注單一職責
- 輸出層層遞進、邏輯清晰
- 適合有明確先後順序的工作流

---

### 2️⃣ Parallel 並行型 — Icon Style Explorer

**路徑**：[`icon_style_explorer/`](./icon_style_explorer/README.md)

同時探索三種不同的設計風格：

```
需求分析師
    ↓
┌───┼───┐
↓   ↓   ↓
扁平化  3D  線條藝術  ← 並行執行
└───┼───┘
    ↓
設計整合師
```

**試試看**：

```
請為一個健康追蹤 app 設計 icon，需要探索不同的視覺風格
```

**特色**：

- 三種風格同時生成，節省時間
- 由設計總監統一比較分析
- 適合創意探索、需要多方案比較的場景

---

### 3️⃣ Loop 循環型 — Riddle Difficulty Calibrator

**路徑**：[`riddle_difficulty_calibrator/`](./riddle_difficulty_calibrator/README.md)

自動迭代改進謎語，直到難度恰到好處：

```
┌──────────────────────┐
│    謎語創作者         │
│        ↓             │
│    難度測試員         │
│        ↓             │
│  太簡單/太難 → 繼續   │
│  剛剛好 → 結束循環    │
└──────────────────────┘
```

**試試看**：

```
狗狗
```

**特色**：

- 自動迭代，無需人工介入
- 達標才結束，確保輸出品質
- 適合有明確評估標準的優化任務

---

### 4️⃣ Human-in-the-Loop 人機協作型 — Design with Approval

**路徑**：[`design_with_approval/`](./design_with_approval/README.md)

在關鍵決策點暫停，等待人工確認：

```
需求分析 → 設計策略 → ⏸️ 人工確認 → 生成 Prompt
                          ↑
                     你可以：
                     • 批准
                     • 修改
                     • 拒絕
```

**試試看**：

```
請為音樂創作 app 設計 icon，風格要有創意且吸引年輕用戶
```

⚠️ **注意**：系統暫停時，請在**啟動 `adk web` 的 Terminal** 中輸入你的決定。

**特色**：

- 關鍵節點保留人類決策權
- 可融入人類的創意和專業判斷
- 適合高成本、高風險的決策場景

---

## 📂 專案結構

```
demo-ai-agents/
├── README.md                      # 本文件
├── SETUP.md                       # 環境設置指南
├── icon_design_studio/            # Sequential 順序型範例
├── icon_style_explorer/           # Parallel 並行型範例
├── riddle_difficulty_calibrator/  # Loop 循環型範例
└── design_with_approval/          # Human-in-the-Loop 範例
```

---

## 🧠 選擇合適的工作流模式

| 你的需求             | 推薦模式          |
| -------------------- | ----------------- |
| 任務有明確的先後順序 | Sequential        |
| 需要同時探索多種方案 | Parallel          |
| 需要反覆優化直到達標 | Loop              |
| 關鍵決策需要人工介入 | Human-in-the-Loop |
| 複雜流程需要組合使用 | 混合模式          |

---

## 📚 延伸學習

- [Google ADK 官方文件](https://google.github.io/adk-docs/)
- [ADK GitHub](https://github.com/google/adk-python)

---

**Happy Building! 🤖✨**
