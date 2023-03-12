import sys
from collections import deque

M, N, K = map(int, sys.stdin.readline().split())
square = [[0] * N for _ in range(M)]

for _ in range(K) :
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(y1, y2) :
        for j in range(x1, x2) :
            square[i][j] = 1

dq = deque()
area = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(M) :
    for j in range(N) :
        if square[i][j] == 0 :
            square[i][j] = 1
            dq.append((i, j))
            area.append(1)

            while dq :
                x, y = dq.popleft()
                for k in range(4) :
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < M and 0 <= ny < N and square[nx][ny] == 0 :
                        dq.append((nx, ny))
                        square[nx][ny] = 1
                        area[-1] += 1

print(len(area))
area.sort()
print(*area, sep = " ")