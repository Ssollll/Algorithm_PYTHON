import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
answer = [[-1] * M for _ in range(N)]

for i in range(N) :
    for j in range(M) :
        if graph[i][j] == 2 :
            a, b = i, j
            visited[i][j] = 1
            answer[i][j] = 0

        if graph[i][j] == 0 :
            answer[i][j] = 0
            visited[i][j] = 1

def BFS(a, b) :
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dq = deque()
    dq.append([a, b])

    while dq :
        x, y = dq.popleft()

        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and graph[nx][ny] == 1 :
                dq.append([nx, ny])
                visited[nx][ny] = 1
                answer[nx][ny] = answer[x][y] + 1

BFS(a, b)

for i in answer :
    print(*i, sep = " ")
            