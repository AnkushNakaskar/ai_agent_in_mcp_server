from openai import OpenAI
import httpx

from readkey import get_token
import httpx
from openai import OpenAI

from readkey import get_token

api_key= str(get_token())
print("API key is : ")
print(api_key)
http_client = httpx.Client(verify=False)
client = OpenAI(base_url="https://godric.nixy.stg-drove.phonepe.nb6/v1", api_key=api_key, http_client=http_client)

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



print("Welcome to your AI Assistant. Type 'goodbye' to quit.")

while True:
    prompt = input("You: ")
    if prompt.lower() == "goodbye":
        print("AI Assistant: Goodbye!")
        break

    message =call_open_ai_llm(prompt)
    # message = anthropic_client.messages.create(
    #     max_tokens=1024,
    #     system="You are a helpful assistant.",
    #     messages=[
    #         {
    #             "role": "user",
    #             "content": prompt,
    #         }
    #     ],
    #     model="claude-sonnet-4-0",
    # )
    # print(message)
    if message and message.content :
        print(f"Assistant: {message.content}")