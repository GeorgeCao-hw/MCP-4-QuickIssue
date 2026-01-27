# app/main.py
from fastapi import FastAPI
from app.tools import list_tools, call_tool

app = FastAPI(title="MCP Server")


@app.post("/tools/list")
def tools_list():
    return list_tools()


@app.post("/tools/call")
def tools_call(payload: dict):
    """
    payload = {
        "name": "tool_name",
        "arguments": {...}
    }
    """
    return call_tool(payload["name"], payload.get("arguments", {}))

