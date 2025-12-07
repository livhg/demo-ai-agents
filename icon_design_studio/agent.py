"""Icon Design Studio - Icon 設計多 Agent 系統

這是一個 Sequential（順序式）多 Agent 系統，展示如何使用 Google ADK
建立專業的 icon 設計工作流程。

系統流程：
1. Requirements Analyst: 分析設計需求，了解用途、受眾、技術限制
2. Design Strategist: 制定設計策略，規劃風格、配色、視覺元素
3. Prompt Engineer: 生成 AI 圖像生成 prompt，可直接用於 DALL-E/Midjourney/Stable Diffusion

使用方式：
1. 啟動 Web UI: adk web
2. 選擇 icon_design_studio
3. 輸入要設計的 icon 需求（例如：請為一個智慧家居控制 app 設計主要的 app icon）

範例輸入：
- "請為一個健康追蹤 app 設計 icon，風格要現代且專業"
- "設計一個音樂創作 app 的 icon，要有創意且吸引年輕用戶"
- "為線上學習平台設計 app icon，需要傳達知識和成長的概念"
"""

from google.adk.agents import SequentialAgent

from .sub_agents.requirements_analyst import requirements_analyst
from .sub_agents.design_strategist import design_strategist
from .sub_agents.prompt_engineer import prompt_engineer


icon_design_studio = SequentialAgent(
    name='icon_design_studio',
    description='Icon 設計工作室：從需求分析到 AI prompt 生成的完整設計流程',
    sub_agents=[
        requirements_analyst,
        design_strategist,
        prompt_engineer
    ],
)

# ADK Web UI 需要 root_agent 作為入口點
root_agent = icon_design_studio
