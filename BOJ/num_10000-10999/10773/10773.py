import sys
from collections import deque

K = int(sys.stdin.readline())

dq = deque()
for _ in range(K) :
    i = int(sys.stdin.readline())
    if i == 0 :
        dq.pop()
    else :
        dq.append(i)

print(sum(dq))

