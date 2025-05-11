from crewai import Agent, Crew, Task, LLM
from crewai_bomb.tools import ExpertTool, DefuserTool, BombStateTool
from game_mcp.game_client import Defuser
import asyncio

# Feel free to import any libraries you need - if needed change requirements.txt
# In this file it also applies to classes and functions :)

# YOUR CODE STARTS HERE
llm = LLM(model="gpt-4.1")

defuser_client = Defuser()
bomb_state_tool = BombStateTool(defuser_client, server_url="http://localhost:8091")
defuser_tool = DefuserTool(defuser_client, server_url="http://localhost:8091")

expert_tool = ExpertTool(server_url="http://localhost:8091")

# Define agents
defuser_agent = Agent(
    role="Defuser",
    goal=(
        "Provide the bomb state to the expert and defuse the bomb using command from the expert."
        "Only use commands produced by the expert. Remember to provide the bomb state to the expert "
        "every time the module state changes."
    ),
    backstory="An advanced analysis AI.",
    tools=[bomb_state_tool, defuser_tool],
    cache=False,
    verbose=True
)

expert_agent = Agent(
    role="Expert",
    goal=(
        "Analyze the information from defuser. Get the bomb manual from the expert tool."
        "Send the correct commant to the defuser."
    ),
    backstory="An advanced analysis AI.",
    tools=[expert_tool],
    cache=False,
    verbose=True
)

# Define task logic
def run_bomb_loop():
    exploded = False
    max_cycles = 20
    step = 1

    while not exploded and step <= max_cycles:

        gather_info_task = Task(
            description="Collect information about the bomb and pass it to the expert",
            expected_output="Information about the bomb state",
            agent=defuser_agent,
        )

        module_description = gather_info_task.execute_sync()

        generate_advice = Task(
            description=(
                "Get the bomb manual from the expert tool and produce the correct command"
                f" based on {module_description}"
            ),
            expected_output="Correct defusal command",
            agent=expert_agent
        )
        instructions = generate_advice.execute_sync()

        defuse_task = Task(
            description=f"Pass the expert's command '{instructions}' to the defusal tool.",
            expected_output="'The module state has changed.' text",
            agent=defuser_agent
        )
        outcome = defuse_task.execute_sync()

        if "BOOM!" in f"{outcome}":
            exploded = True
        elif "disarmed" in f"{outcome}".lower():
            print(outcome)
            break

        print('=' * 60)

        step += 1

if __name__ == "__main__":
    run_bomb_loop()

