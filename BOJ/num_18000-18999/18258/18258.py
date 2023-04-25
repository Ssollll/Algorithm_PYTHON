import sys
from collections import deque

N = int(sys.stdin.readline())
dq = deque()

for _ in range(N) :
    m = str(sys.stdin.readline().strip())
    if m[:4] == "push" :
        dq.push(int(m[5:]))
    elif m == "pop" :
        if m :
            print(dq.popleft())
        else :
            print(-1)
    elif m == "size" :
        print(dq.size())
    elif m == "empty" :
        if m :
            print(0)
        else :
            print(1)
    elif m == "front" :
        if m :
            print(dq[0])
        else :
            print(-1)
    elif m == "back" :
        if m :
            print(dq[-1])
        else :
            print(-1)