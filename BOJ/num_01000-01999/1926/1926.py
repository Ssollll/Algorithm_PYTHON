import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
paint = [list(map(int, input().split())) for _ in range(N)]

def BFS(x, y) :
    paint[x][y] = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    w = 1
    dq = deque()
    dq.append((x, y))
    while dq :
        x, y = dq.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and paint[nx][ny] == 1 :
                dq.append((nx, ny))
                paint[nx][ny] = 0
                w += 1
    return w

cnt = 0
ans = 0

for i in range(N) :
    for j in range(M) :
        if paint[i][j] == 1 :
            cnt += 1
            ans = max(BFS(i, j), ans)

print(cnt)
print(ans)