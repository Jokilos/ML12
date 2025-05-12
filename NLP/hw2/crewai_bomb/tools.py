import asyncio
import os
import time
import sys
import openai
from crewai.tools import BaseTool
from pydantic import Field, ConfigDict
from game_mcp.game_client import Defuser, Expert
from agents.two_agents import search_for_actions

# Feel free to import any libraries you need - if needed change requirements.txt
# In this file it also applies to classes and functions :)

async def call_client(client, server_url, input = None):
        await client.connect_to_server(server_url)
        if input is None: 
            result = await client.run()
        else:
            result = await client.run(input)

        await client.cleanup()

        return result 

class BombStateTool(BaseTool):
    name: str = "bomb_state_tool"
    description: str = "Recovers bomb state"
    model_config = ConfigDict(extra='allow')
    server_url: str = Field(default="http://localhost:8091")

    def __init__(self, client: Defuser, server_url: str = "http://localhost:8091"):
        super().__init__()
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.server_url = server_url
        self.client = client
        self.verbose = True
    
    def _run(self) -> str:
        bomb_state = asyncio.run(call_client(self.client, self.server_url, "state"))
        return bomb_state
        
class DefuserTool(BaseTool):
    name: str = "defuser_tool"
    description: str = "Handles defusal logic and returns the result"
    model_config = ConfigDict(extra='allow')
    server_url: str = Field(default="http://localhost:8091")

    def __init__(self, client: Defuser, server_url: str = "http://localhost:8091"):
        super().__init__()
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.client = client
        self.server_url = server_url

    def _run(self, command: str) -> str:
        action = "help"
        for line in command.splitlines():
            line = line.strip().lower()
            (is_action, found_action) = search_for_actions(line)
            if is_action:
                action = found_action 
                break
        
        result = asyncio.run(call_client(self.client, self.server_url, action))

        if 'BOOM!' in result:
            print(result)
            sys.exit(0)
        elif 'The module state has changed' in result:
            return 'Module defused successfully!'

        return result 

class ExpertTool(BaseTool):
    name: str = "expert_tool"
    description: str = "Receivers the manual info and returns the result"
    model_config = ConfigDict(extra='allow')
    server_url: str = Field(default="http://localhost:8091")

    def __init__(self, server_url: str = "http://localhost:8091"):
        super().__init__()
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.server_url = server_url
        self.client = Expert()

    def _fix_manual(self, manual: str):
        for i in range(5):
            manual = manual.replace(f'Round {i+1}', f'{i+1}.Input')

        return manual

    def _run(self) -> str:
        manual_text = asyncio.run(call_client(self.client, self.server_url))
        return self._fix_manual(manual_text)

if __name__ == '__main__':
    openai.api_key = os.getenv("OPENAI_API_KEY")

