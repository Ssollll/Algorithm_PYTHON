import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

def BFS(N, K) :
    graph = [int(10e9)] * 100001
    graph[N] = 0
    dq = deque([])
    dq.append((0, N))

    while dq :
        v, t = dq.popleft()
        for x in [(1, t + 1), (1, t - 1), (0, t * 2)] :
            if 0 <= x[1] < 100001 :
                if graph[x[1]] > v + x[0] :
                    graph[x[1]] = v + x[0]
                    dq.append([graph[x[1]], x[1]])
    return graph[K]

print(BFS(N, K))