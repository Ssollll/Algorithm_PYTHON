import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0] * M for _ in range(N)] for _ in range(H)]

dq = deque()

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

ans = 0

def BFS() :
    while dq :
        x, y, z = dq.popleft()
        for i in range(6) :
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M :
                if tomato[nx][ny][nz] == 0 :
                    dq.append((nx, ny, nz))
                    tomato[nx][ny][nz] = tomato[x][y][z] + 1
                    visited[nx][ny][nz] = 1

for i in range(H) :
    for j in range(N) :
        for k in range(M) :
            if tomato[i][j][k] == 1 and visited[i][j][k] == 0 : 
                dq.append((i, j, k))
                visited[i][j][k] = 1

BFS()

for a in tomato :
    for b in a :
        for c in b :
            if c == 0 :
                print(-1) 
                exit(0)
        ans = max(ans, max(b))

print(ans - 1)