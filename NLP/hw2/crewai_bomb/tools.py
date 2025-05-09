from crewai.tools import BaseTool


# Feel free to import any libraries you need - if needed change requirements.txt
# In this file it also applies to classes and functions :)


class DefuserTool(BaseTool):
    # YOUR CODE STARTS HERE
    pass

    def __init__(self, server_url: str):
        super().__init__()
        self.client = Defuser()
        self.loop = asyncio.new_event_loop()
        self.loop.run_until_complete(self.client.connect_to_server(server_url))

    def _run(self) -> str:
        return self.loop.run_until_complete(self.client.run())


    # YOUR CODE ENDS HERE


class ExpertTool(BaseTool):
    # YOUR CODE STARTS HERE

    def __init__(self, server_url: str):
        super().__init__()
        self.client = Expert()
        self.loop = asyncio.new_event_loop()
        self.loop.run_until_complete(self.client.connect_to_server(server_url))

    def _run(self) -> str:
        return self.loop.run_until_complete(self.client.run())

    # YOUR CODE ENDS HERE
