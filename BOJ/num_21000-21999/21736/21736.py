import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

school = [list(map(str, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

def BFS(x, y) :
    dq = deque()
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    dq.append([x, y])

    visited[x][y] = 1

    cnt = 0
    
    while dq :
        x, y = dq.popleft()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 :
                if school[nx][ny] != "X" :
                    dq.append([nx, ny])
                    visited[nx][ny] = 1
                    if school[nx][ny] == "P" :
                        cnt += 1
            
    if cnt == 0 :
        print("TT")
    else :
        print(cnt)

for i in range(N) :
    for j in range(M) :
        if school[i][j] == "I" :
            BFS(i, j)
