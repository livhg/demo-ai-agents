"""Design Integrator Agent - 負責整合並比較設計方案"""

import os
from google.adk import Agent

from . import prompt


design_integrator = Agent(
    model=os.getenv("MODEL", "gemini-2.0-flash"),
    name='design_integrator',
    description='整合並比較不同風格的設計方案，提供專業推薦',
    instruction=prompt.DESIGN_INTEGRATOR_PROMPT,
)
