import time
import sys

n, nap = sys.argv[1:]

n = int(n)
nap = float(nap)


def sleep(nap):
    x = int(nap * 10)
    for i in range(x):
        time.sleep(0.1)
        print(".", end="", file=sys.stderr)
    print()


print("start!")
for i in range(n):
    print(f"running {i+1:4}/{n} - sleep {nap} ", end="")
    sleep(nap)

print("done!")
