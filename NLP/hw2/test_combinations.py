import subprocess
import time
import os
import pandas as pd

default_args = {
    "topk": 50,
    "topp": 0.9,
    "temp": 0.7,
    "prompt": "standard"
}

# Define your test values
# topk_values = [10, 200, 400]
# topp_values = [0.8, 0.9, 0.95]
# temp_values = [0.3, 0.6, 1.0]
topk_values = []
topp_values = []
temp_values = []
prompt_values = ['standard', 'structured', 'json']

tests = []
tests += [{"topk": v} for v in topk_values]
tests += [{"topp": v} for v in topp_values]
tests += [{"temp": v} for v in temp_values]
tests += [{"prompt": v} for v in prompt_values]

print(tests)

results = []

for test in tests:
    args = default_args.copy()
    args.update(test)

    # Start server
    p_server = subprocess.Popen(
        ["python", "-m", "game_mcp.game_server", "--port", "8091"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    time.sleep(0.2) 

    client_args = [
        "--topk", str(args["topk"]),
        "--topp", str(args["topp"]),
        "--temp", str(args["temp"]),
        "--prompt", args["prompt"],
        "--verbose", "0"
    ]

    status = 'done'
    try:
        print('\nTEST: ', client_args)
        p_client = subprocess.Popen(
            ["python", "-m", "agents.two_agents"] + client_args,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        p_client.wait(timeout=900)
        client_output = p_client.stdout
        
    except subprocess.TimeoutExpired:
        p_client.kill()
        status = 'timeout'

    # Kill server
    p_server.terminate()
    try:
        p_server.wait(timeout=5)
    except subprocess.TimeoutExpired:
        p_server.kill()

    if status == 'timeout':
        score, iters = 0, 0
    else:
        score, iters = map(int, client_output.split())

    test_type, test_value = test
    results.append({
        "test_type" : test_type,
        "value" : test_value,
        "status": status,
        "score" : score,
        "iters" : iters,
    })

    print(results)

# Save to DataFrame
df = pd.DataFrame(results)
df.to_csv("test_results.csv", index=False)
print("Results saved to 'test_results.csv'") 