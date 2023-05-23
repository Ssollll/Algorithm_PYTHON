import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
dq = deque([i for i in range(1, N+1)])

answer = []

while dq :
    for _ in range(K-1) :
        dq.append(dq.popleft())
    
    for _ in range(1) :
        answer.append(dq.popleft())
        
print("<", end = "")
print(*answer, sep = ", ", end = "")
print(">")