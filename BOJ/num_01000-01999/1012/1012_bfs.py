import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)

T = int(sys.stdin.readline())

def bfs(arr, a, b) :
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    dq = deque()
    dq.append((a, b))
    graph[b][a] = 0

    while dq :
        x, y = dq.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < M) and (0 <= ny < N) :
                if graph[ny][nx] == 1 :
                    graph[ny][nx] = 0
                    dq.append((nx, ny))

for _ in range(T) :
    cnt = 0
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0] * M for _ in range(N)]

    for _ in range(K) :
        i, j = map(int, sys.stdin.readline().split())
        graph[j][i] = 1

    for a in range(M) :
        for b in range(N) :
            if graph[b][a] == 1 :
                bfs(graph, a, b)
                cnt += 1

    print(cnt)