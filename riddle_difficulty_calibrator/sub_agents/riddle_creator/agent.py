"""Riddle Creator Agent - 負責創作謎語"""

import os
from google.adk import Agent

from . import prompt


riddle_creator = Agent(
    model=os.getenv("MODEL", "gemini-2.0-flash"),
    name='riddle_creator',
    description='創作謎語專家，根據主題和反饋創作適當難度的謎語',
    instruction=prompt.RIDDLE_CREATOR_PROMPT,
    output_key='riddle_and_answer',
)

