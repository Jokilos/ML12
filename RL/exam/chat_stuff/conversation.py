import os
from dotenv import load_dotenv
from openai import OpenAI
import tqdm

# Load API key from .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

previous_response_id = None
instructions = "You are a helpful AI assistant. Explain following Reinforcement Learning topics. Answer only in Markdown format."

with open('questions.md', 'r', encoding='utf-8') as f:
    questions = f.read()

# paragraphs = []
# paragraph = []
# for line in questions.splitlines():
#     if line == '':
#         paragraphs += [paragraph]
#         paragraph = []
#     else:
#         paragraph += [line]

for line in tqdm.tqdm(questions.splitlines()):
    topic_line = line.strip()[:2] == '##'

    if line == '':
        continue
    elif topic_line:
        user_input = 'Describe following topics regarding ' + line.replace('##', '')
    else:
        user_input = line
    
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=user_input,
        instructions=instructions,
        previous_response_id=previous_response_id, 
        temperature=0.7,
    )

    print("Response:", end=" ", flush=True)
    print(response.output_text)

    previous_response_id = response.id

    with open("chat_log.md", "a", encoding="utf-8") as f:
        if topic_line:
            f.write(f'{line[1:]}\n\n')
        if not topic_line: 
            f.write(f"\n{response.output_text}\n")
