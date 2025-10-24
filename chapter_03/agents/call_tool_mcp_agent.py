import asyncio
from pathlib import Path
import json
import httpx
from openai import OpenAI

from chapter_03.stdio import stdio_mcp_client
from readkey import get_token

api_key = str(get_token())
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


def call_open_ai_llm(prompts, available_tools):
    completion = client.chat.completions.create(
        model="global:LLM_GLOBAL_GPT_4O_MINI_STG",
        store=True,
        tools=available_tools,
        messages=prompts
    )
    print(completion)
    functions = []
    for choice in completion.choices:
        for completion_message in choice.message.tool_calls:
            functions.append(completion_message);
    return functions;
# You need to modify the values in function call, you can refer the available tool print and actual function calls

async def main():
    """Main async function to run the assistant."""
    await mcp_client.connect()
    available_tools = await mcp_client.get_available_tools()

    print(f"Available tools: {", ".join([tool['name'] for tool in available_tools])}")
    print(available_tools)
    openai_functions = []
    for available_tool in available_tools:
        available_tool['parameters'] = available_tool['input_schema']

        openai_functions.append({
            "type":"function",
            "function":available_tool
        })

    while True:
        prompt = input("You: ")
        if prompt.lower() == "goodbye":
            print("AI Assistant: Goodbye!")
            break
        conversation_messages = [{"role": "user", "content": prompt}]
        while True:
            print("Conversation messages :::")
            print(conversation_messages)
            print(openai_functions)
            llm_functions = call_open_ai_llm(conversation_messages, available_tools=openai_functions)
            print(f"Assistant: {llm_functions}")
            tool_results = []
            for llm_function in llm_functions:
                print(f"Assistant executing function: {llm_function}")
                tool_result = await mcp_client.use_tool(
                    tool_name=llm_function.function.name, arguments=json.loads(llm_function.function.arguments)
                )
                print("Printing result1 ::: ")
                print(tool_result)
                tool_results.append(
                    {
                        "type": "text",
                        "text": "\n".join(tool_result),
                    }
                )
                print("Printing result ::: ")
                print(tool_results)
                break;
            conversation_messages.append(
                {"role": "user", "content": tool_results}
            )
            break;


    await mcp_client.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
