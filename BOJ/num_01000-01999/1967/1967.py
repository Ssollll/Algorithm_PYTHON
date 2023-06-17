import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]

def DFS(x, w) :
    for i in graph[x] :
        a, b = i
        if distance[a] == -1 :
            distance[a] = w + b
            DFS(a, w + b)

for _ in range(N - 1) :
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

distance = [-1] * (N + 1)
distance[1] = 0
DFS(1, 0)

start = distance.index(max(distance))
distance = [-1] * (N + 1)
distance[start] = 0
DFS(start, 0)

print(max(distance))