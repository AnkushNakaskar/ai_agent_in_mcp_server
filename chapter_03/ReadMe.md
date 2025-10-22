### Model context protocol implementation : Chapter 3
* This folder explain the model context protocol chapter 3. 
* MCP explain the interface between Host application and LLM as explain in [MainReadMe.md](../ReadMe.md)
* There are two ways to connect to MCP server : local client and remote server
  * LocalClient example : [stdio](stdio)
  * Http client example : [http](http)
* Host application : [plain_mcp_agent.py](agents/plain_mcp_agent.py) 
  * It is simple application with just completion of messages
  * You can see, we are initiating the mcp client before we start with prompt and end the connection
  * Check the output pasted below :
```
/opt/homebrew/bin/python3 /Users/ankush.nakaskar/Office/newCode/personal_projects/ai_agent_in_mcp_server/chapter_03/agents/plain_mcp_agent.py 
Current directory (using os): /Users/ankush.nakaskar/Office/newCode/personal_projects/ai_agent_in_mcp_server
/Users/ankush.nakaskar/Office/newCode/personal_projects/ai_agent_in_mcp_server/api_key.txt
<token>
API key is : 
<token>
Env server_args ...
['--directory', '/Users/ankush.nakaskar/Office/newCode/personal_projects/ai_agent_in_mcp_server/chapter_03', 'run', 'calculator_server.py']
Welcome to your AI Assistant. Type 'goodbye' to quit.
You: Hi , How are you ?
Assistant: Hello! I'm just a program, so I don't have feelings, but I'm here and ready to help you. How can I assist you today?
You: goodbye
AI Assistant: Goodbye!
You: goodbye
AI Assistant: Goodbye!

Process finished with exit code 0  
```

* Host application with capability of list of available tools : [list_available_tool_mcp_agent.py](agents/list_available_tool_mcp_agent.py) 
  * It is simple application with just completion of messages
  * It will list down the list of available tools
  * You can see, we are initiating the mcp client before we start with prompt and end the connection
  * Check the output pasted below :
```
/opt/homebrew/bin/python3 /Users/ankush.nakaskar/Office/newCode/personal_projects/ai_agent_in_mcp_server/chapter_03/agents/list_available_tool_mcp_agent.py 
Current directory (using os): /Users/ankush.nakaskar/Office/newCode/personal_projects/ai_agent_in_mcp_server
/Users/ankush.nakaskar/Office/newCode/personal_projects/ai_agent_in_mcp_server/api_key.txt
<token>
API key is : 
<token>
Env server_args ...
['--directory', '/Users/ankush.nakaskar/Office/newCode/personal_projects/ai_agent_in_mcp_server/chapter_03', 'run', 'calculator_server.py']
Welcome to your AI Assistant. Type 'goodbye' to quit.
You: Hi , How are you
Assistant: Hello! I'm just a program, so I don't have feelings, but I'm here and ready to help you. How can I assist you today?
You: goodbye
AI Assistant: Goodbye!
[10/22/25 16:38:47] INFO     Processing request of type            server.py:672
                             ListToolsRequest                                   
Available tools: add, subtract, multiply, divide, power, square_root, count_rs, explain_math, signup_math_facts, count_files
You: goodbye
AI Assistant: Goodbye!

Process finished with exit code 0
```

* Host application with capability of list of available tools and tool call : [call_tool_mcp_agent.py](agents/call_tool_mcp_agent.py)) 
  * It is simple application with just completion of messages
  * It will list down the list of available tools
  * You can see, we are initiating the mcp client before we start with prompt and end the connection
  * Check the output pasted below :
```
/opt/homebrew/bin/python3 /Users/ankush.nakaskar/Office/newCode/personal_projects/ai_agent_in_mcp_server/chapter_03/agents/call_tool_mcp_agent.py 
Current directory (using os): /Users/ankush.nakaskar/Office/newCode/personal_projects/ai_agent_in_mcp_server
/Users/ankush.nakaskar/Office/newCode/personal_projects/ai_agent_in_mcp_server/api_key.txt
<token>
API key is : 
<token>
Env server_args ...
['--directory', '/Users/ankush.nakaskar/Office/newCode/personal_projects/ai_agent_in_mcp_server/chapter_03', 'run', 'calculator_server.py']
Welcome to your AI Assistant. Type 'goodbye' to quit.
[10/22/25 17:16:43] INFO     Processing request of type            server.py:672
                             ListToolsRequest                                   
Available tools: Adding
[{'name': 'Adding', 'description': 'Add two numbers together.\n\nArgs:\n    a: First number\n    b: Second number\n', 'input_schema': {'properties': {'a': {'title': 'A', 'type': 'number'}, 'b': {'title': 'B', 'type': 'number'}}, 'required': ['a', 'b'], 'title': 'addArguments', 'type': 'object'}}]
You: Hi Can you please add two values 4 and 5
ChatCompletion(id='chatcmpl-CTRanl8losOAecHEHaCS2DABH5Ti7', choices=[Choice(finish_reason='tool_calls', index=0, logprobs=None, message=ChatCompletionMessage(content=None, refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=[ChatCompletionMessageFunctionToolCall(id='call_SeUoVpC0bx4iouSBGiFJifGr', function=Function(arguments='{"a":4,"b":5}', name='Adding'), type='function')]))], created=1761133613, model='gpt-4o-mini-2024-07-18', object='chat.completion', service_tier=None, system_fingerprint='fp_efad92c60b', usage=CompletionUsage(completion_tokens=19, prompt_tokens=67, total_tokens=86, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=0, audio_tokens=0, reasoning_tokens=0, rejected_prediction_tokens=0), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cached_tokens=0)))
Assistant: [Function(arguments='{"a":4,"b":5}', name='Adding')]
You: goodbye
AI Assistant: Goodbye!

Process finished with exit code 0

```