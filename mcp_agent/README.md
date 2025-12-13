# MCP Agent

這是一個展示如何使用 Google ADK 連接 MCP (Model Context Protocol) Server 的範例 Agent。

## 系統需求

- Python 3.10+
- Google ADK (`pip install google-adk`)
- 一個運行中的 MCP Server

## 使用 ADK Web UI

1. **設置環境變數**

```
# .env
GOOGLE_GENAI_USE_VERTEXAI=FALSE
MODEL=gemini-flash-latest
GOOGLE_API_KEY=
MCP_SERVER_URL=http://localhost:8080/sse
```

2. **啟動 ADK Web UI**

```bash
adk web
```

3. **選擇 mcp_agent 並開始對話**

## 💬 範例對話

```
👤 用戶: 
- 請問什麼是 ADK?
- Gemini 是什麼?
- MCP
- MVP

```

### 關鍵代碼

```python
# 自動連接並獲取工具
tools, exit_stack = await MCPToolset.from_server(
    connection_params=SseServerParams(url=mcp_server_url)
)

# 創建整合 MCP 工具的 Agent
agent = Agent(
    model="gemini-2.0-flash-exp",
    name='mcp_simple_agent',
    instruction=prompt.MCP_AGENT_PROMPT,
    tools=tools,  # MCP 工具
)
```

## 故障排除

### 無法連接到 MCP Server

**症狀**：出現連接錯誤或超時

**解決方案**：
1. 確認 MCP Server 正在運行：`curl http://localhost:8080/sse`
2. 檢查 `MCP_SERVER_URL` 是否正確
3. 確認防火牆設定允許連接

### API Key 錯誤

**症狀**：認證失敗或權限錯誤

**解決方案**：
1. 確認已設置 `GOOGLE_API_KEY`
2. 檢查 API Key 是否有效
3. 確認有權限使用指定的 Gemini 模型

### Agent 不使用 MCP 工具

**症狀**：Agent 不調用 MCP 工具，直接回答問題

**可能原因**：
1. 問題不需要使用工具（Agent 已知答案）
2. 工具描述不夠清楚，Agent 不知道何時使用
3. Instruction 需要更明確地指示使用工具

**解決方案**：
- 優化工具的描述，讓 Agent 更容易理解其用途
- 在 prompt.py 中調整 instruction，強調使用工具的重要性

## 📝 延伸應用

這個 Agent 可以連接到各種 MCP Server，例如：

- **資料庫查詢**：連接到資料庫 MCP Server 進行資料查詢
- **檔案操作**：連接到檔案系統 MCP Server 進行檔案管理
- **API 整合**：連接到 API Gateway MCP Server 調用外部服務
- **開發工具**：連接到 IDE MCP Server 輔助程式開發

只需更換 `MCP_SERVER_URL`，Agent 就能立即使用新的工具！
