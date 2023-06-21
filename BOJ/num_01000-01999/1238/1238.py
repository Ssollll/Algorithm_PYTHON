import sys
import heapq
input = sys.stdin.readline
INF = int(10e9)

N, M, X = map(int, input().split())
city = [[] for _ in range(N+1)]
for _ in range(M) :
    a, b, c = map(int, input().split())
    city[a].append((b, c))

def dijkstra(X) :
    distance = [INF] * (N+1)
    distance[X] = 0
    q = []
    heapq.heappush(q, (0, X))
    while q :
        d, n = heapq.heappop(q)
        if distance[n] >= d :
            for v, val in city[n] :
                if d + val < distance[v] :
                    distance[v] = d + val
                    heapq.heappush(q, (distance[v], v))
    return distance

answer = dijkstra(X)
answer[0] = 0
for i in range(1, N+1) :
    if i != X :
        tmp = dijkstra(i)
        answer[i] += tmp[X]

print(max(answer))