from typing import Optional
import asyncio
from contextlib import AsyncExitStack
from mcp.client.sse import sse_client 
from mcp.types import JSONRPCMessage
from mcp import types
from mcp import ClientSession, types
import argparse
import uuid

# Feel free to import any libraries you need - if needed change requirements.txt

class BombClient:
    def __init__(self):
        # YOUR CODE STARTS HERE

        self.server_url = None 
        self.exit_stack = AsyncExitStack()
        self.session : Optional[ClientSession] = None

        # YOUR CODE ENDS HERE

    async def connect_to_server(self, server_url: str):
        """Connect to an sse MCP server"""
        # YOUR CODE STARTS HERE

        self.server_url = server_url
        context = sse_client(self.server_url)
        read, write = await self.exit_stack.enter_async_context(context)

        client = ClientSession(read, write)
        self._session = await self.exit_stack.enter_async_context(client)

        await self._session.initialize()

        # YOUR CODE ENDS HERE

    async def process_query(self, tool_name: str, tool_args: dict[str, str]) -> str:
        """Process a query using the game_interaction tool"""
        # YOUR CODE STARTS HERE

        if not self._session:
            raise RuntimeError("Client not connected. Call connect() first.")

        # tools = await self._session.list_tools()

        result = await self._session.call_tool(tool_name, tool_args)
        
        text_response = result.content[0].text

        return text_response

        # YOUR CODE ENDS HERE

    async def cleanup(self):
        """Properly clean up the session and streams"""
        # YOUR CODE STARTS HERE

        await self.exit_stack.aclose()

        # YOUR CODE ENDS HERE

class Defuser(BombClient):
    async def run(self, action: str) -> str:
        """Run a defuser action"""
        # YOUR CODE STARTS HERE

        # await self.connect_to_server("http://localhost:8080/")

        response = await self.process_query("game_interaction", {"command" : action})

        # await self.cleanup()

        return response

        # YOUR CODE ENDS HERE


class Expert(BombClient):
    async def run(self) -> str:
        """Run an expert action"""
        # YOUR CODE STARTS HERE

        # await self.connect_to_server("http://localhost:8080/")

        response = await self.process_query("get_manual", {})

        # await self.cleanup()

        if 'exploded' in response:
            return response + "BOOM! BOMB HAS EXPLODED!"
        if 'disarmed' in response:
            return response + "BOMB SUCCESSFULLY DISARMED!"

        return response

        # YOUR CODE ENDS HERE


async def main():
    """ Main function to connect to the server and run the clients """
    # YOUR CODE STARTS HERE

    parser = argparse.ArgumentParser(description='Run MCP SSE-based ')
    parser.add_argument('--url', default = "http://localhost:8080/", help = 'URL to connect to')
    parser.add_argument('--role', default = 'Expert', help = 'Client role (Expert/Defuser)')
    args = parser.parse_args()

    if args.role not in ['Expert', 'Defuser']:
        raise RuntimeError('Invalid role provided!')

    client = Defuser() if args.role == 'Defuser' else Expert()

    await client.connect_to_server("http://localhost:8080/")

    await expert_test(client)

    await client.cleanup()

    # YOUR CODE ENDS HERE


async def expert_test(expert_client: Expert):
    """Test the Expert class"""
    result = await expert_client.run()

    possible_outputs = ["BOOM!", "BOMB SUCCESSFULLY DISARMED!", "Regular Wires Module", "The Button Module",
                        "Memory Module", "Simon Says Module"]

    assert any(result.find(output) != -1 for output in possible_outputs), f"Expert test failed"
    # assert any(output.find(result) != -1 for output in possible_outputs), f"Expert test failed"


async def defuser_test(defuser_client: Defuser):
    """Test the Defuser class"""
    result = await defuser_client.run("state")

    possible_outputs = ["BOMB STATE"]

    assert any(result.find(output) != -1 for output in possible_outputs), f"Defuser test failed"
    # assert any(output.find(result) != -1 for output in possible_outputs), f"Defuser test failed"

if __name__ == "__main__":
    asyncio.run(main())
