"""Flat Designer Agent - 負責扁平化設計方案"""

import os
from google.adk import Agent

from . import prompt


flat_designer = Agent(
    model=os.getenv("MODEL", "gemini-2.0-flash"),
    name='flat_designer',
    description='提供扁平化設計風格的 icon 設計方案',
    instruction=prompt.FLAT_DESIGNER_PROMPT,
    output_key='flat_design',
)
