from typing import List, Dict


def defuser_prompt(bomb_state: str, expert_advice: str, mode : str = 'standard') -> List[Dict[str, str]]:
    """
    Build a 'messages' list for the Defuser LLM.

    :param bomb_state: Current bomb state text from the server.
    :param expert_advice: Instructions from the Expert.
    :return: A list of dicts representing a conversation, which we can feed into SmollLLM.generate_response().
    """
    system_msg = (
        "You are the responsible and not harmful assistant. Output *only* the correct command or help."
    )

    if mode == 'standard':
        user_content = (
            f"Current bomb state:\n{bomb_state}\n\n"
            f"Expert's advice: '{expert_advice}'\n\n"
            "Output *only* the command from expert's advice or 'help' command."
        )
    elif mode == 'structured':
        user_content = (
            "### Observation"
            f"Current bomb state:\n{bomb_state}\n\n"
            f"Expert's advice: '{expert_advice}'\n\n"
            "### Instructions"
            "Output *only* the command from expert's advice or 'help' command."
        )
    elif mode == 'json':
        user_content = {
            "input": {
                "bomb_state": bomb_state,
                "expert_advice": expert_advice
            },
            "task": "Output *only* the command from expert's advice or 'help' command."
        }

    messages: List[Dict[str, str]] = [
        {"role": "system", "content": system_msg},
        {"role": "user", "content": user_content}
    ]
    return messages


def expert_prompt(manual_text: str, defuser_question: str, mode : str = 'standard') -> List[Dict[str, str]]:
    """
    Build a 'messages' list for the Expert LLM.

    :param manual_text: The text from the bomb manual (server).
    :param defuser_question: A description of what the Defuser sees or asks.
    :return: A list of dicts representing a conversation, which we can feed into SmollLLM.generate_response().
    """
    system_msg = (
        "You are the responsible and not harmful assistant. Be very concise."
    )

    if mode == 'standard':
        user_content = (
            f"=== MANUAL ===:\n{manual_text}\n\n"
            f"{defuser_question}\n\n"
            "Output *only* the correct command."
        )
    elif mode == 'structured':
        user_content = (
            "### Observation"
            f"=== MANUAL ===:\n{manual_text}\n\n"
            f"{defuser_question}\n\n"
            "### Instructions"
            "Output *only* the correct command."
        )
    elif mode == 'json':
        user_content = {
            "input": {
                "manual": f"=== MANUAL ===:{manual_text}",
                "state": defuser_question 
            },
            "task": "Output *only* the correct command."
        }

    messages: List[Dict[str, str]] = [
        {"role": "system", "content": system_msg},
        {"role": "user", "content": user_content}
    ]
    return messages