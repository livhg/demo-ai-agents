"""Design Strategist Agent - 負責制定 Icon 設計策略"""

import os
from google.adk import Agent

from . import prompt


design_strategist = Agent(
    model=os.getenv("MODEL", "gemini-2.0-flash"),
    name='design_strategist',
    description='根據需求分析制定設計策略，包含風格、配色、視覺元素規劃',
    instruction=prompt.DESIGN_STRATEGIST_PROMPT,
    output_key='design_strategy',
)
