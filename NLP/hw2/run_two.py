import subprocess
import time

# This command's output is suppressed
p1 = subprocess.Popen(["python", "-m", "game_mcp.game_server"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

time.sleep(0.1)

# This command's output is shown
p2 = subprocess.Popen(["python", "-m", "agents.two_agents"])

p1.wait()
p2.wait()