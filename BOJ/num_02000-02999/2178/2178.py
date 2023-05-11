import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
miro = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS(x, y) :
    q = deque()
    q.append((x, y))

    while q :
        x, y = q.popleft()

        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and miro[nx][ny] == 1 :
                q.append((nx, ny))
                miro[nx][ny] = miro[x][y] + 1
    return miro[N-1][M-1]

print(BFS(0, 0))