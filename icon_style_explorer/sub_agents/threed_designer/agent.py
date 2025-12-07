"""3D Designer Agent - 負責 3D 渲染設計方案"""

import os
from google.adk import Agent

from . import prompt


threed_designer = Agent(
    model=os.getenv("MODEL", "gemini-2.0-flash"),
    name='threed_designer',
    description='提供 3D 渲染風格的 icon 設計方案',
    instruction=prompt.THREED_DESIGNER_PROMPT,
    output_key='threed_design',
)
