import requests


class MCPClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def list_tools(self):
        resp = requests.post(f"{self.base_url}/tools/list")
        resp.raise_for_status()
        return resp.json()["tools"]

    def call_tool(self, name: str, arguments: dict):
        resp = requests.post(
            f"{self.base_url}/tools/call",
            json={
                "name": name,
                "arguments": arguments
            }
        )
        resp.raise_for_status()
        return resp.json()

