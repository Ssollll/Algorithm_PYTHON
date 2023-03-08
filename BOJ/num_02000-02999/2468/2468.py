import sys
from collections import deque

N = int(sys.stdin.readline())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 0
max_n =  max(map(max, graph))


def BFS(i, j, k) :

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    dq = deque()
    dq.append((i, j))
    visited[i][j] = 1

    while dq :
        x, y = dq.popleft()

        for r in range(4) :
            nx, ny = x + dx[r], y + dy[r]
            if 0 > nx or nx >= N or 0 > ny or ny >= N :
                continue
            if graph[nx][ny] > k and visited[nx][ny] == 0 :
                dq.append((nx, ny))
                visited[nx][ny] = 1

for i in range(max_n) :
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    for j in range(N) :
        for k in range(N) :
            if graph[j][k] > i and visited[j][k] == 0 :
                BFS(j, k, i)
                cnt += 1
    if answer < cnt :
        answer = cnt

print(answer)
