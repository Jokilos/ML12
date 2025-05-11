import asyncio

from agents.prompts import expert_prompt, defuser_prompt
from game_mcp.game_client import Defuser, Expert
from agents.models import HFModel, SmollLLM

def print_prompt(prompt, who, verbose):
    if verbose: 
        print("-" * 30)
        print(f" {who} ")
        print("-" * 30)
        print("\n" * 1)

        if who == 'CONVO':
            print(prompt)
        else:
            print(prompt[1]['content'])

def cut_to_last_dot(text):
    return text[:text.rfind('.') + 1]

def search_for_actions(text):
    actions = [f"press position {i}" for i in range(1, 5)]
    actions += [f"press {color}" for color in ["red", "blue", "green", "yellow"]]
    actions += [f"cut wire {i+1}" for i in range(6)]
    actions += ["release on 1", "release on 4", "release on 5"]
    actions += ["press", "hold", "state", "help"]

    for action in actions:
        if action in text:
            return (True, action)
        
    return (False, None)

async def run_two_agents(
        defuser_model: HFModel,
        expert_model: HFModel,
        server_url: str = "http://0.0.0.0:8080",
        max_new_tokens: int = 50,
        top_k = 50,
        top_p = 0.9,
        temperature = 0.7,
        prompt_type = 'standard',
        verbose = True,
) -> None:
    """
    Main coroutine that orchestrates two LLM agents (Defuser and Expert)
    interacting with the bomb-defusal server.

    :param defuser_model: The HFModel for the Defuser's role.
    :param expert_model: The HFModel for the Expert's role.
    :param server_url: The URL where the bomb-defusal server is running.
    :param max_new_tokens: Max tokens to generate for each LLM response.
    """
    defuser_client = Defuser()
    expert_client = Expert()
    max_new_tokens_expert = max_new_tokens + 420
    try:
        # 1) Connect both clients to the same server
        await defuser_client.connect_to_server(server_url)
        await expert_client.connect_to_server(server_url)
        
        score = 0
        iters = 0

        while True:
            iters += 1

            # 2) Defuser checks the bomb's current state
            bomb_state = await defuser_client.run("state")

            if "Bomb disarmed!" in bomb_state or "Bomb exploded!" in bomb_state:
                break

            # 3) Expert retrieves the relevant manual text
            manual_text = await expert_client.run()
            manual_text = '\n'.join(manual_text.strip().splitlines()[1:])

            # 4) Expert LLM uses the manual text + defuser’s question (bomb_state)
            #    to generate instructions
            exp_messages = expert_prompt(manual_text, bomb_state, prompt_type)
            print_prompt(exp_messages, 'EXPERT', verbose)
            expert_advice = expert_model.generate_response(
                exp_messages,
                max_new_tokens=max_new_tokens_expert,
                temperature=temperature,
                top_p=top_p,
                top_k=top_k,
                do_sample=True,
                keep_prompt=False,
            )
            expert_advice = expert_advice.replace("</think>", "").replace("\n", "")

            # 5) Defuser LLM uses the bomb state + expert advice to pick a single action
            def_messages = defuser_prompt(bomb_state, expert_advice, prompt_type)
            print_prompt(def_messages, 'DEFUSER', verbose)
            def_action_raw = defuser_model.generate_response(
                def_messages,
                max_new_tokens=max_new_tokens,
                temperature=temperature,
                top_p=top_p,
                top_k=top_k,
                do_sample=True,
                keep_prompt=False,
            )

            # 6) Attempt to extract a known command from def_action_raw
            #    If no recognized command is found, default to "help"
            action = "help"
            for line in def_action_raw.splitlines():
                line = line.strip().lower()
                (is_action, found_action) = search_for_actions(line)
                if is_action:
                    action = found_action 
                    break
            
            if verbose:
                print("\n[DEFUSER ACTION DECIDED]:", action)

            # 7) Send that action to the server
            result = await defuser_client.run(action)

            if verbose:
                if action != 'help': 
                    print("[SERVER RESPONSE]:")
                    print(result)
                print("-" * 60)
            
            if "BOMB HAS EXPLODED" in result:
                break
            elif action not in ['help', 'state']:
                score += 1
            elif "BOMB SUCCESSFULLY DISARMED" in result:
                score += 100
                break

            if iters > 15:
                break

    finally:
        await expert_client.cleanup()
        await defuser_client.cleanup()

    print(score, iters)

if __name__ == "__main__":
    import argparse
    import torch
    parser = argparse.ArgumentParser(description='Run MCP SSE-based ')
    parser.add_argument('--url', default = "http://localhost:8091/", help = 'URL to connect to')
    parser.add_argument('--prompt', default = 'standard', help = 'propmt type')
    parser.add_argument('--temp', type = float, default = 0.7,  help = 'temperature')
    parser.add_argument('--topk', type = int, default = 50,  help = 'topk')
    parser.add_argument('--topp', type = float, default = 0.9,  help = 'topp')
    parser.add_argument('--verbose', type = int, default = 0,  help = 'verbosity')
    args = parser.parse_args()

    defuser_checkpoint: str = "Qwen/Qwen3-0.6B"
    expert_checkpoint: str = defuser_checkpoint

    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    defuser_model = SmollLLM(defuser_checkpoint, device=device)
    expert_model = SmollLLM(expert_checkpoint, device=device)

    asyncio.run(
        run_two_agents(
            defuser_model=defuser_model,
            expert_model=expert_model,
            server_url=args.url,
            max_new_tokens=80,
            top_k=args.topk,
            top_p=args.topp,
            temperature=args.temp,
            prompt_type=args.prompt,
            verbose=bool(args.verbose),
        )
    )