### Model context protocol implementation : Chapter 3
* This folder explain the model context protocol chapter 3. 
* MCP explain the interface between Host application and LLM as explain in [MainReadMe.md](/Users/ankush.nakaskar/Office/newCode/personal_projects/ai_agent_in_mcp_server/ReadMe.md)
* There are two ways to connect to MCP server : local client and remote server
  * LocalClient example : [stdio](stdio)
  * Http client example : [http](http)
* Host application : [mcp_agent.py](mcp_agent.py) 
  * It is simple application with just completion of messages
  * You can see, we are initiating the mcp client before we start with prompt and end the connection
  * Check the output pasted below : 
  ```
  /opt/homebrew/bin/python3 /Users/ankush.nakaskar/Office/newCode/personal_projects/ai_agent_in_mcp_server/chapter_03/mcp_agent.py
  Current directory (using os): /Users/ankush.nakaskar/Office/newCode/personal_projects/ai_agent_in_mcp_server
  /Users/ankush.nakaskar/Office/newCode/personal_projects/ai_agent_in_mcp_server/api_key.txt
  <token>
  API key is : 
  <token>
  Env server_args ...
  ['--directory', '/Users/ankush.nakaskar/Office/newCode/personal_projects/ai_agent_in_mcp_server', 'run', 'chapter_03/calculator_server.py']
  Welcome to your AI Assistant. Type 'goodbye' to quit.
  You: Hi, How are you
  Assistant: I'm just a computer program, so I don't have feelings, but I'm here and ready to help you! How can I assist you today?
  You: goodbye
  AI Assistant: Goodbye!
  You: Thank you for your help MCP agent
  Assistant: You're welcome! If you have any questions or need assistance, feel free to ask. I'm here to help!
  You: goodbye
  AI Assistant: Goodbye!
  Process finished with exit code 0
  ```