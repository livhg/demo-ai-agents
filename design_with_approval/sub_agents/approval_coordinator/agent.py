"""Approval Coordinator Agent - 負責請求人工確認"""

import os
from google.adk import Agent
from google.adk.tools import FunctionTool

from . import prompt


def request_human_approval():
    """請求人工審核設計策略。

    這個函式會暫停 agent 執行，等待人工輸入確認訊息。

    Returns:
        str: 人工的反饋訊息
    """
    print("\n" + "="*60)
    print("[暫停] 系統暫停：等待人工確認")
    print("="*60)
    print("\n請審核上述的設計策略。")
    print("\n您可以：")
    print("  1. 輸入 'approved' 或 '同意' 來批准此策略")
    print("  2. 提供修改建議（例如：'請改用藍綠色配色'）")
    print("  3. 輸入 'reject' 或 '重新設計' 來要求完全重做\n")

    user_feedback = input("你的決定：").strip()

    print("\n" + "="*60)
    print("[完成] 收到人工反饋，繼續執行")
    print("="*60 + "\n")

    return user_feedback


approval_coordinator = Agent(
    model=os.getenv("MODEL", "gemini-2.0-flash"),
    name='approval_coordinator',
    description='協調人工確認流程，暫停等待人類反饋',
    instruction=prompt.APPROVAL_COORDINATOR_PROMPT,
    tools=[FunctionTool(request_human_approval)],
)
