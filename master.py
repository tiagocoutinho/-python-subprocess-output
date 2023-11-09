import os
import select
import subprocess

env = {
  "PYTHONUNBUFFERED": "1"
}
proc = subprocess.Popen(["python", "run.py", "10", "1"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=0, env=env)

os.set_blocking(proc.stdout.fileno(), False)

reads = (proc.stdout,)
while proc.poll() is None:
    r, _, _ = select.select(reads, (), ())
    if not r:
        print("STOPPING!")
        break
    data = proc.stdout.read().decode()
    print(data, end="", flush=True)

proc.wait()
