"""Icon Design with Approval - 人工確認的 Icon 設計系統

這是一個 Sequential + Human-in-the-Loop 的多 Agent 系統，
展示如何在關鍵決策點加入人工確認流程。

系統流程：
1. Requirements Analyst: 分析設計需求
2. Design Strategist: 制定設計策略
3. [暫停] Approval Coordinator: 等待人工確認設計策略
4. Final Prompt Generator: 根據人工反饋生成最終 prompt

使用方式：
1. 啟動 Web UI: adk web
2. 選擇 icon_design_with_approval
3. 輸入設計需求
4. 審核設計策略並提供反饋
5. 獲得最終 prompt

範例輸入：
- "請為音樂創作 app 設計 icon，風格要有創意且吸引年輕用戶"
- "設計一個健康追蹤 app 的 icon"
- "為線上學習平台設計 app icon"

特色：
- 在生成 prompt 前確認設計方向
- 避免在錯誤方向上浪費資源
- 讓使用者參與設計決策
- 可以提供修改建議或完全拒絕
"""

from google.adk.agents import SequentialAgent

from .sub_agents.requirements_analyst import requirements_analyst
from .sub_agents.design_strategist import design_strategist
from .sub_agents.approval_coordinator import approval_coordinator
from .sub_agents.final_prompt_generator import final_prompt_generator


icon_design_with_approval = SequentialAgent(
    name='icon_design_with_approval',
    description='Icon 設計系統（含人工確認）：在關鍵決策點等待人類反饋',
    sub_agents=[
        requirements_analyst,      # 1. 分析需求
        design_strategist,         # 2. 制定策略
        approval_coordinator,      # 3. 等待人工確認
        final_prompt_generator     # 4. 生成最終 prompt
    ],
)

# ADK Web UI 需要 root_agent 作為入口點
root_agent = icon_design_with_approval
