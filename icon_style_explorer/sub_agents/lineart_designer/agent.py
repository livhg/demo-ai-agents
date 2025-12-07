"""Line Art Designer Agent - 負責線條藝術設計方案"""

import os
from google.adk import Agent

from . import prompt


lineart_designer = Agent(
    model=os.getenv("MODEL", "gemini-2.0-flash"),
    name='lineart_designer',
    description='提供線條藝術風格的 icon 設計方案',
    instruction=prompt.LINEART_DESIGNER_PROMPT,
    output_key='lineart_design',
)
