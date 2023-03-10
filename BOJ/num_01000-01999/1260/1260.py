import sys
from collections import deque
sys.setrecursionlimit(10**6)

N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for _ in range(M) :
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()

visited_dfs = [0] * (N+1)
visited_bfs = [0] * (N+1)

def BFS(v) :
    dq = deque()
    dq.append(v)
    visited_bfs[v] = 1

    while dq :
        a = dq.popleft()
        print(a, end = " ")
        for i in graph[a] :
            if visited_bfs[i] == 0 :
                dq.append(i)
                visited_bfs[i] = 1

def DFS(v) :
    visited_dfs[v] = 1
    print(v, end = " ")
    for i in graph[v] :
        if visited_dfs[i] == 0 :
            DFS(i)

DFS(V)
print()
BFS(V)