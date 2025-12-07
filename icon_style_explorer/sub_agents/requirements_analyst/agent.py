"""Requirements Analyst Agent - 負責分析 Icon 設計需求"""

import os
from google.adk import Agent

from . import prompt


requirements_analyst = Agent(
    model=os.getenv("MODEL", "gemini-2.0-flash"),
    name='requirements_analyst',
    description='分析 icon 設計需求，提供完整的需求分析報告',
    instruction=prompt.REQUIREMENTS_ANALYST_PROMPT,
)
