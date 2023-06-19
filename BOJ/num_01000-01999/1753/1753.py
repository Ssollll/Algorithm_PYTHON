import sys
import heapq
input = sys.stdin.readline
INF = int(10e9)

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(E) :
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

distance = [INF] * (V + 1)

q = []
def dijkstra(start) :
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q :
        d, now = heapq.heappop(q)
        for n, w in graph[now] :
            c = d + w
            if c < distance[n] :
                distance[n] = c
                heapq.heappush(q, (c, n))

dijkstra(K)

for i in distance[1:] :
    if i != INF :
        print(i)
    else :
        print("INF")