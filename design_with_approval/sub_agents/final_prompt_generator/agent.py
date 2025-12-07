"""Final Prompt Generator Agent - 負責生成最終 Prompt"""

import os
from google.adk import Agent

from . import prompt


final_prompt_generator = Agent(
    model=os.getenv("MODEL", "gemini-2.0-flash"),
    name='final_prompt_generator',
    description='根據設計策略和人工反饋生成最終的 AI 圖像生成 prompt',
    instruction=prompt.PROMPT_ENGINEER_PROMPT,
)
