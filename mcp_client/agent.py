class Agent:
    def __init__(self, mcp_client, llm):
        self.mcp = mcp_client
        self.llm = llm

    def run(self, user_query: str):
        tools = self.mcp.list_tools()

        print("Available tools:")
        for t in tools:
            print("-", t["name"])

        decision = self.llm(user_query, tools)

        if decision["action"] == "call_tool":
            result = self.mcp.call_tool(
                decision["name"],
                decision["arguments"]
            )
            return result

        return {"message": "no action"}

