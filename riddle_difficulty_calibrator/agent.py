"""Riddle Difficulty Calibrator - 謎語難度校準系統

這是一個 LoopAgent（循環式）多 Agent 系統，展示如何使用 Google ADK
建立迭代改進的工作流程。

系統流程：
1. Riddle Creator: 創作一個謎語
2. Difficulty Tester: 測試難度是否適中
3. 如果不適中：根據反饋回到 Riddle Creator 重新創作
4. 如果適中：呼叫 exit_loop 工具，結束循環

使用方式：
1. 啟動 Web UI: adk web
2. 選擇 riddle_difficulty_calibrator
3. 輸入謎語主題（例如：日常用品）
4. 系統會自動迭代改進，直到達到適中難度

範例輸入：
- "請為「水果」創作一個謎語"
- "以「交通工具」為主題出謎語"
- "幫我想一個關於「文具」的謎語"

特色：
- 自動迭代改進，無需人工介入
- 展示 LoopAgent 的循環改進機制
- 學習 LLM 如何根據反饋調整輸出
"""

from google.adk.agents import LoopAgent

from .sub_agents.riddle_creator import riddle_creator
from .sub_agents.difficulty_tester import difficulty_tester


riddle_difficulty_calibrator = LoopAgent(
    name='riddle_difficulty_calibrator',
    description='謎語難度校準器：透過迭代改進創作出難度適中的謎語',
    sub_agents=[
        riddle_creator,      # 1. 創作謎語
        difficulty_tester    # 2. 測試難度（達標時會呼叫 exit_loop）
    ],
    max_iterations=3,  # 最多嘗試 3 次
)

# ADK Web UI 需要 root_agent 作為入口點
root_agent = riddle_difficulty_calibrator

