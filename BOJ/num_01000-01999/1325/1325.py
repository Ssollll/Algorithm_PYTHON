import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
com = [[] for _ in range(N+1)]

for _ in range(M) :
    A, B = map(int, input().split())
    com[B].append(A)


def BFS(start) :
    cnt = 1
    dq = deque([start])
    graph = [0 for _ in range(N+1)]
    graph[start] = 1

    while dq :
        now = dq.popleft()
        for x in com[now] :
            if not graph[x] :
                graph[x] = 1
                cnt += 1
                dq.append(x)

    return cnt

answer = []
mxcnt = 1

for i in range(1, N+1) :
    cnt = BFS(i)
    if cnt > mxcnt :
        mxcnt = cnt
        answer.clear()
        answer.append(i)
    elif cnt == mxcnt :
        answer.append(i)

print(*answer)