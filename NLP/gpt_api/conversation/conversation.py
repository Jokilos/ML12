import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

previous_response_id = None
instructions = "You are a helpful, concise AI assistant. Answer only in Markdown format."

user_input = ''

while True:
    clear = False
    skip = False
    try:
        if user_input.strip().lower() == "skip":
            skip = True

        user_input = input("Query: ")

        if user_input.strip().lower() in {"exit", "quit", "clear"}:
            clear = user_input.strip().lower() == "clear"
            raise KeyboardInterrupt

        response = client.responses.create(
            model="gpt-4.1",
            input=user_input,
            instructions=instructions,
            previous_response_id=previous_response_id, 
            temperature=0.7,
        )

        print("Response:", end=" ", flush=True)
        print(response.output_text)

        previous_response_id = response.id

        if not skip:
            with open("chat_log.md", "a", encoding="utf-8") as f:
                f.write(f"### You:\n{user_input}\n\n")
                f.write(f"### Response:\n{response.output_text}\n")

    except KeyboardInterrupt:
        if clear:
            with open("chat_log.md", "w", encoding="utf-8") as f:
                    f.write("")
        print("\nExiting.")
        break
