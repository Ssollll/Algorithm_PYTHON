import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    cnt = 0
    N, M = map(int, input().split())
    impor = list(map(int, input().split()))

    dq = deque()
    for i in range(N) :
        dq.append(i)

    while True :
        x = dq.popleft()
        if impor[x] != max(impor) :
            dq.append(x)
        else :
            if x == M :
                cnt += 1
                print(cnt)
                break
            else :
                cnt += 1
                impor[x] = 0
