
import subprocess

env = {
  "PYTHONUNBUFFERED": "1"
}
proc = subprocess.Popen(["python", "run.py", "10", "1"], stdout=subprocess.PIPE, env=env)

for line in proc.stdout:
    line = line.decode()
    print(line, end='', flush=True)

proc.wait()
