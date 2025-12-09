"""Difficulty Tester Agent - 負責測試謎語難度"""

import os
from google.adk import Agent
from google.adk.tools import FunctionTool

from . import prompt
from .tools import exit_loop


difficulty_tester = Agent(
    model=os.getenv("MODEL", "gemini-2.0-flash"),
    name='difficulty_tester',
    description='評估謎語難度，決定是否達到中等難度標準',
    instruction=prompt.DIFFICULTY_TESTER_PROMPT,
    tools=[FunctionTool(exit_loop)],
    output_key='difficulty_feedback',
)

