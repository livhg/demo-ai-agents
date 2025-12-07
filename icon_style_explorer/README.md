# Icon Style Explorer

Icon 風格探索系統是一個**並行型多代理系統**，展示如何使用 Google ADK 的 ParallelAgent 同時探索多種設計方向。

## 系統架構

這是一個**並行 + 順序型 (Parallel + Sequential)** 組合的多代理系統：

```
使用者輸入需求
    ↓
[1] Requirements Analyst (需求分析師)
    ↓
┌───────────────┼───────────────┐
│               │               │
▼               ▼               ▼
[2a] Flat       [2b] 3D         [2c] Line Art
Designer        Designer        Designer
│               │               │
└───────────────┼───────────────┘
                ↓
[3] Design Integrator (設計整合師)
    ↓
三種風格的比較分析與推薦
```

## 為什麼使用並行工作流？

### 創意探索的挑戰

在設計初期，很難預先知道哪種風格最適合：
- 扁平化可能太簡單？
- 3D 可能太複雜？
- 線條藝術可能不夠現代？

### 並行工作流的優勢

1. **節省時間**：三種風格同時生成，而非依序執行
2. **全面探索**：一次看到所有選項，不會錯過好的方向
3. **專業比較**：由設計總監統一比較，提供客觀建議
4. **降低風險**：避免在單一方向投入太多，最後發現不適合

## 快速開始

### 1. 啟動 ADK Web UI

```bash
adk web
```

### 2. 選擇 Agent

在 Web UI 中選擇 `icon_style_explorer`

### 3. 輸入設計需求

範例輸入：

```
請為一個健康追蹤 app 設計 icon，需要探索不同的視覺風格
```

```
設計一個線上學習平台的 icon，想看看不同風格的呈現
```

```
為智慧家居控制 app 設計 icon，比較扁平化、3D、線條藝術哪種最適合
```

### 4. 獲得設計產出

系統會產生：
1. **需求分析報告**：完整的需求拆解
2. **三種風格方案**（並行生成）：
   - 扁平化設計方案
   - 3D 渲染設計方案
   - 線條藝術設計方案
3. **整合比較報告**：專業的比較分析與推薦

## 系統特色

### 並行效率

三位設計師同時工作：
```python
parallel_style_exploration = ParallelAgent(
    sub_agents=[
        flat_designer,      # 同時執行
        threed_designer,    # 同時執行
        lineart_designer    # 同時執行
    ],
)
```

### 專業分工

每位設計師專精於自己的風格：
- **Flat Designer**：扁平化設計專家
- **3D Designer**：3D 渲染專家
- **Line Art Designer**：線條藝術專家
- **Design Integrator**：設計總監，負責整合比較

### 結構化比較

設計總監會從多個維度比較：
- 視覺表現力
- 適用場景
- 實作難度
- 品牌契合度

並提供：
- 推薦方案及理由
- 替代方案建議
- 組合策略
- 實作優先順序

## 檔案結構

```
icon_style_explorer/
├── README.md                          # 本文件
├── __init__.py                        # 模組入口
├── agent.py                           # ParallelAgent + SequentialAgent
└── sub_agents/                        # 子代理目錄
    ├── __init__.py
    ├── requirements_analyst/          # 需求分析師
    ├── flat_designer/                 # 扁平化設計師
    ├── threed_designer/               # 3D 設計師
    ├── lineart_designer/              # 線條藝術設計師
    └── design_integrator/             # 設計整合師
```
