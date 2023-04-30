import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
dq = deque([i for i in range(1, N+1)])
posi = list(map(int, sys.stdin.readline().split()))

cnt = 0
for i in posi :
    while True :
        if dq[0] == i :
            dq.popleft()
            break
        else :
            if dq.index(i) < len(dq) / 2 : # dq 앞쪽이라면
                while dq[0] != i :
                    dq.append(dq.popleft()) # 2번연산 수행
                    cnt += 1
            else :
                while dq[0] != i :
                    dq.appendleft(dq.pop())
                    cnt += 1

print(cnt)