"""Icon Style Explorer - Icon 風格探索多 Agent 系統

這是一個 Parallel + Sequential（並行 + 順序）組合的多 Agent 系統，
展示如何使用 Google ADK 建立並行探索的工作流程。

系統流程：
1. Requirements Analyst: 分析設計需求
2. 並行探索三種風格：
   - Flat Designer: 扁平化設計方案
   - 3D Designer: 3D 渲染設計方案
   - Line Art Designer: 線條藝術設計方案
3. Design Integrator: 整合比較三種方案，提供推薦

使用方式：
1. 啟動 Web UI: adk web
2. 選擇 icon_style_explorer
3. 輸入要設計的 icon 需求（例如：請為一個健康追蹤 app 設計 icon）

範例輸入：
- "請為一個健康追蹤 app 設計 icon，需要探索不同的視覺風格"
- "設計一個線上學習平台的 icon，想看看不同風格的呈現"
- "為智慧家居控制 app 設計 icon，比較扁平化、3D、線條藝術哪種最適合"

特色：
- 同時產生三種完全不同的設計風格
- 節省時間，一次看到所有選項
- 專業的比較分析和推薦建議
"""

from google.adk.agents import SequentialAgent, ParallelAgent

from .sub_agents.requirements_analyst import requirements_analyst
from .sub_agents.flat_designer import flat_designer
from .sub_agents.threed_designer import threed_designer
from .sub_agents.lineart_designer import lineart_designer
from .sub_agents.design_integrator import design_integrator


# 建立並行探索團隊（三種風格同時執行）
parallel_style_exploration = ParallelAgent(
    name='parallel_style_exploration',
    description='同時探索扁平化、3D、線條藝術三種設計風格',
    sub_agents=[
        flat_designer,
        threed_designer,
        lineart_designer
    ],
)

# 組合完整流程：需求分析 → 並行探索 → 整合比較
icon_style_explorer = SequentialAgent(
    name='icon_style_explorer',
    description='Icon 風格探索系統：並行探索多種設計風格並提供專業比較',
    sub_agents=[
        requirements_analyst,
        parallel_style_exploration,
        design_integrator
    ],
)

# ADK Web UI 需要 root_agent 作為入口點
root_agent = icon_style_explorer
