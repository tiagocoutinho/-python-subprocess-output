import time
import sys

n, nap = sys.argv[1:]

n = int(n)
nap = float(nap)


print("start!")
for i in range(n):
    print(f"running {i+1:4}/{n} - sleep {nap} ")
    time.sleep(nap)

print("done!")
