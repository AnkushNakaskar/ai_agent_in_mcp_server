import asyncio
from pathlib import Path

import httpx
from openai import OpenAI

from chapter_03.stdio import stdio_mcp_client
from readkey import get_token

api_key= str(get_token())
print("API key is : ")
print(api_key)
http_client = httpx.Client(verify=False)
client = OpenAI(base_url="https://godric.nixy.stg-drove.phonepe.nb6/v1", api_key=api_key, http_client=http_client)


mcp_client = stdio_mcp_client.MCPClient(
    name="calculator_server_connection",
    command="uv",
    server_args=[
        "--directory",
        str(Path(__file__).parent.parent.resolve()),
        "run",
        "calculator_server.py",
    ],
)

print("Welcome to your AI Assistant. Type 'goodbye' to quit.")


def call_open_ai_llm(prompts):
    completion = client.chat.completions.create(
        model="global:LLM_GLOBAL_GPT_4O_MINI_STG",
        store=True,
        messages=[
    {
        "role": "user",
        "content": prompts
    }
]
    )
    return completion.choices[0].message;


async def main():
    """Main async function to run the assistant."""
    await mcp_client.connect()
    while True:
        prompt = input("You: ")
        if prompt.lower() == "goodbye":
            print("AI Assistant: Goodbye!")
            break
        message =call_open_ai_llm(prompt)
        if message and message.content:
            print(f"Assistant: {message.content}")
    await mcp_client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())