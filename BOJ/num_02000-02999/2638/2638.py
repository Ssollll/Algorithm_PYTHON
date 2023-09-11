import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

cheese = [list(map(int, input().split())) for _ in range(N)]

def check(x, y) :
    dq = deque()
    dq.append([x, y])
    visited[x][y] = 1

    while dq :
        x, y = dq.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M :
                if visited[nx][ny] == 0 and cheese[nx][ny] == 0 :
                    dq.append([nx, ny])
                    visited[nx][ny] = 1
                elif cheese[nx][ny] == 1 :
                    visited[nx][ny] += 1

cnt = 0
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

while True :
    visited = [[0 for _ in range(M)] for _ in range(N)]

    check(0, 0)
    cnt += 1
    
    air_cnt = 0
    for i in range(N) :
        for j in range(M) :
            if visited[i][j] >= 2 :
                cheese[i][j] = 0
    
    for i in range(N) :
        for j in range(M) :
            if cheese[i][j] == 0 :
                air_cnt += 1
    
    if air_cnt == (N * M) :
        break

print(cnt)
            
    
