'''
def fake_llm(prompt: str, tools: list):
    """
    A fake LLM that always calls query_community_issues
    """
    return {
        "action": "call_tool",
        "name": "query_community_issues",
        "arguments": {
            "state": "open",
            "search": "kernel",
            "page_size": 5
        }
    }

'''
# =============================================================================
import json
import os
from openai import OpenAI


SYSTEM_PROMPT = """You are a coding agent using MCP tools.

Rules:
- You MUST respond with a single JSON object
- Do NOT add any extra text
- If you want to call a tool, respond in this format:

{
  "action": "call_tool",
  "name": "<tool_name>",
  "arguments": { ... }
}

- If no tool is needed, respond with:

{
  "action": "final",
  "content": "<answer>"
}
"""

class DeepSeekLLM:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url="https://api.deepseek.com"
        )

    def __call__(self, user_input: str, tools: list):
        tool_desc = "\n".join(
            f"- {t['name']}: {t.get('description', '')}"
            for t in tools
        )

        prompt = f"""
User request:
{user_input}

Available MCP tools:
{tool_desc}
"""

        resp = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            temperature=0,
        )

        content = resp.choices[0].message.content.strip()

        # 🔒 强制 JSON 解析，防止 LLM 自由发挥
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            raise RuntimeError(
                f"LLM did not return valid JSON:\n{content}"
            )