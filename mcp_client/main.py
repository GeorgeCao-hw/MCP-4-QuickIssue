from dotenv import load_dotenv
from mcp_client import MCPClient
from agent import Agent
#from llm import fake_llm
from llm import DeepSeekLLM


def main():
    mcp = MCPClient("http://0.0.0.0:8000")
    #agent = Agent(mcp, fake_llm)
    load_dotenv()
    llm = DeepSeekLLM()
    agent = Agent(mcp, llm)

    print("MCP Agent (DeepSeek)")
    print("Type 'exit' to quit.\n")    

    while True:
        user_input = input(">>> ").strip()
        if user_input.lower() in ("exit", "quit"):
            break

        try:
            result = agent.run(user_input)
            print("\nResult:")
            print(result)
            print()
        except Exception as e:
            print("\n❌ Error:")
            print(e)
            print()


if __name__ == "__main__":
    main()

