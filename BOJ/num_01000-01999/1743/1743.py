import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
condo = [[0] * M for _ in range(N)]

for _ in range(K) :
    i, j = map(int, input().split())
    condo[i-1][j-1] = 1

def BFS(x, y) :
    dq = deque()
    dq.append((x, y))
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    cnt = 0
    while dq :
        x, y = dq.popleft()
        # print("x, y are", x, y)
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and condo[nx][ny] == 1 :
                # print("nx, ny are", nx, ny)
                condo[nx][ny] = 0
                cnt += 1
                # print("cnt is", cnt)
                dq.append((nx, ny))
    return cnt

answer = []
for i in range(N) :
    for j in range(M) :
        if condo[i][j] == 1 :
            answer.append(BFS(i, j))

print(max(answer))

