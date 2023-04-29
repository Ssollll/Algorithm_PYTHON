import sys
from collections import deque

N = int(sys.stdin.readline())
dq = deque()

for _ in range(N) :
    m = str(sys.stdin.readline().strip())
    if m[:4] == "push" :
        dq.append(int(m[5:]))
    elif m == "pop" :
        if dq :
            print(dq.popleft())
        else :
            print(-1)
    elif m == "size" :
        print(len(dq))
    elif m == "empty" :
        if dq :
            print(0)
        else :
            print(1)
    elif m == "front" :
        if dq :
            print(dq[0])
        else :
            print(-1)
    elif m == "back" :
        if dq :
            print(dq[-1])
        else :
            print(-1)