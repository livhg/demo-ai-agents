"""Prompt Engineer Agent - 負責生成 AI 圖像生成 Prompt"""

import os
from google.adk import Agent

from . import prompt


prompt_engineer = Agent(
    model=os.getenv("MODEL", "gemini-2.0-flash"),
    name='prompt_engineer',
    description='將設計策略轉換為精確的 AI 圖像生成 prompt',
    instruction=prompt.PROMPT_ENGINEER_PROMPT,
)
