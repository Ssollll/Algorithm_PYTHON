import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] * (N+1) for _ in range(N+1)]

for i in range(M) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def BFS(start) :
    num = [0] * (N+1)
    visited[start] = 1
    dq = deque()
    dq.append(start)

    while dq :
        x = dq.popleft()
        for i in graph[x] :
            if visited[i] == 0 :
                num[i] = num[x] + 1
                visited[i] = 1
                dq.append(i)
    return sum(num)

result = []
for i in range(1, N+1) :
    visited = [0 for _ in range(N+1)]
    result.append(BFS(i))

print(result.index(min(result)) + 1)