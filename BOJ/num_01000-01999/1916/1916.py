import sys
import heapq
INF = int(1e9)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

bus = [[] for _ in range(N+1)]
for _ in range(M) :
    a, b, cost = map(int, sys.stdin.readline().split())
    bus[a].append((cost, b))

s, e = map(int, sys.stdin.readline().split())

distant = [INF] * (N+1) # 최소 비용 저장 리스트

def dijkstra(start) :
    q = []
    heapq.heappush(q, (0, start))
    distant[start] = 0

    while q :
        d, x = heapq.heappop(q)

        if distant[x] < d :
            continue
            
        for nw, nx in bus[x] :
            nd = d + nw

            if distant[nx] > nd :
                heapq.heappush(q, (nd, nx))
                distant[nx] = nd

dijkstra(s)
print(distant[e])