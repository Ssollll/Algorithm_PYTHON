import sys
from collections import deque

N = int(sys.stdin.readline())
paint = [list(sys.stdin.readline().strip()) for _ in range(N)]
visited_x= [[0] * N for _ in range(N)]
visited_o= [[0] * N for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS(start, end, visited) :
    dq = deque()
    dq.append([start, end])
    visited[start][end] = 1

    while dq :
        x, y = dq.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and paint[x][y] == paint[nx][ny] and visited[nx][ny] == 0 :
                visited[nx][ny] = 1
                dq.append([nx, ny])

cnt_x, cnt_o = 0, 0

for i in range(N) :
    for j in range(N) :
        if visited_x[i][j] == 0 :
            BFS(i, j, visited_x)
            cnt_x += 1

for i in range(N) :
    for j in range(N) :
        if paint[i][j] == 'G' :
            paint[i][j] = "R"

for i in range(N) :
    for j in range(N) :
        if visited_o[i][j] == 0 :
            BFS(i, j, visited_o)
            cnt_o += 1

print(cnt_x, cnt_o)