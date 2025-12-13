"""MCP Agent - 連接到 SSE MCP Server 的 Agent

這個 Agent 使用 Google ADK 的 MCPToolset 連接到 SSE MCP Server，並自動發現和使用 Server 提供的工具。

使用方式：
1. 確保 MCP Server 正在運行（預設：http://localhost:8080/sse）
2. 設置環境變數
3. 啟動 ADK Web UI：adk web
4. 選擇 mcp_agent 開始對話
"""

import os

from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import SseServerParams

from .prompt import MCP_AGENT_PROMPT

# 從環境變數讀取設定
MCP_SERVER_URL = os.environ.get('MCP_SERVER_URL', 'http://localhost:8080/sse')
MODEL = os.environ.get('MODEL', 'gemini-flash-latest')


# 創建 MCP Agent
# 使用 MCPToolset 連接到 SSE MCP Server
root_agent = LlmAgent(
    model=MODEL,
    name='mcp_agent',
    description='一個可以連接 MCP Server 並使用其工具的 AI 助手',
    instruction=MCP_AGENT_PROMPT,
    tools=[
        MCPToolset(
            connection_params=SseServerParams(
                url=MCP_SERVER_URL,
                headers={'Accept': 'text/event-stream'}
            )
        )
    ],
)
