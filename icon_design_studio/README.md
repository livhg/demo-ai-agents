# Icon Design Studio

Icon 設計工作室是一個多代理系統，展示如何使用 Google ADK 建立專業的 icon 設計工作流程。

## 系統架構

這是一個**順序型 (Sequential)** 多代理系統，由三個專業化的 Agent 協作完成 icon 設計流程：

```
使用者輸入需求
    ↓
[1] Requirements Analyst (需求分析師)
    - 分析用途與場景
    - 識別目標受眾
    - 理解核心訊息
    - 評估技術限制
    ↓
[2] Design Strategist (設計策略師)
    - 選擇設計風格
    - 規劃配色方案
    - 設計視覺元素
    - 制定差異化策略
    ↓
[3] Prompt Engineer (Prompt 工程師)
    - 生成主要 Prompt
    - 設定負面 Prompt
    - 建議技術參數
    - 提供設計規格書
    ↓
完整的 AI 圖像生成 Prompt
```

## 快速開始

### 1. 啟動 ADK Web UI

```bash
cd sessions/ai-agents/example/adk-project
adk web
```

### 2. 選擇 Agent

在 Web UI 中選擇 `icon_design_studio`

### 3. 輸入設計需求

範例輸入：

```
請為一個智慧家居控制 app 設計主要的 app icon
```

```
設計一個健康追蹤 app 的 icon，風格要現代且專業
```

```
為音樂創作 app 設計 icon，要有創意且吸引年輕用戶
```

### 4. 獲得設計產出

系統會依序產生：
1. **需求分析報告**：完整的需求拆解和分析
2. **設計策略規劃**：風格、配色、視覺元素的詳細規劃
3. **AI Prompt 規格書**：可直接用於圖像生成的 prompt

## 系統特色

### 專業分工

每個 Agent 專注於自己的專業領域：
- **Requirements Analyst**：UI/UX 需求分析專家
- **Design Strategist**：視覺設計策略師
- **Prompt Engineer**：AI 圖像生成專家

### 結構化輸出

每個階段都提供結構化的報告：
- 清晰的分析框架
- 完整的設計邏輯
- 可執行的技術規格

### 實務應用

產出的 Prompt 可直接用於：
- DALL-E 3
- Midjourney v6
- Stable Diffusion XL
- 其他 AI 圖像生成工具

## 檔案結構

```
icon_design_studio/
├── README.md                          # 本文件
├── __init__.py                        # 模組入口
├── agent.py                           # 主要的 SequentialAgent
└── sub_agents/                        # 子代理目錄
    ├── __init__.py
    ├── requirements_analyst/          # 需求分析師
    │   ├── __init__.py
    │   ├── agent.py
    │   └── prompt.py
    ├── design_strategist/             # 設計策略師
    │   ├── __init__.py
    │   ├── agent.py
    │   └── prompt.py
    └── prompt_engineer/               # Prompt 工程師
        ├── __init__.py
        ├── agent.py
        └── prompt.py
```

## 設計理念

### 為什麼使用順序工作流？

Icon 設計是一個需要**層層推進**的過程：

1. **需求先行**：必須先理解需求，才能制定策略
2. **策略指導實作**：設計策略決定了 prompt 的內容
3. **清晰的資料流**：每個階段的輸出是下一階段的輸入

順序工作流確保：
- 設計決策有明確的依據
- 過程可追溯、可重現
- 每個階段專注於自己的職責

### Agent 設計原則

每個 Agent 遵循以下原則：

1. **單一職責**：每個 Agent 只做一件事，做好一件事
2. **明確輸入輸出**：清楚定義需要什麼資訊、產出什麼結果
3. **專業化**：使用專業術語和框架，提供專業級的產出

## 擴展性

### 加入更多 Agent

可以輕鬆加入新的 Agent，例如：

- **Design Reviewer**：評估設計品質
- **Brand Consultant**：確保品牌一致性
- **Accessibility Checker**：檢查無障礙性

### 改變工作流模式

可以將系統改為：

- **並行工作流 (ParallelAgent)**：同時探索多種設計風格
- **循環工作流 (LoopAgent)**：反覆優化直到達到品質標準
- **Human-in-the-Loop**：在關鍵決策點加入人工確認
