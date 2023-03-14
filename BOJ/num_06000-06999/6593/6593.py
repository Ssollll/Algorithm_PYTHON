import sys
from collections import deque

# 북동남서상하
dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def BFS(x, y, z) :
    dq = deque()
    dq.append([x, y, z])
    visited[x][y][z] = 1
    while dq :
        x, y, z = dq.popleft()
        for i in range(6) :
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if 0 <= nx < L and 0 <= ny < R and 0 <= nz < C :
                if graph[nx][ny][nz] == "E" :
                    print(f"Escaped in {visited[x][y][z]} minute(s).")
                    return
                if graph[nx][ny][nz] == "." and visited[nx][ny][nz] == 0 :
                    visited[nx][ny][nz] = visited[x][y][z] + 1 #
                    dq.append([nx, ny, nz])
    print("Trapped!")

while True :
    L, R, C = map(int, sys.stdin.readline().split()) # L : 층수 / R : 행 / C : 열
    if L == 0 and R == 0 and C == 0 : # 0 0 0 입력시 while문 빠져나오게 -> 프로그램 종료!
        break

    graph = [[[] * C for _ in range(R)] for _ in range(L)]
    visited = [[[0] * C for _ in range(R)] for _ in range(L)]
    for i in range(L) :
        graph[i] = [list(map(str, sys.stdin.readline().strip())) for _ in range(R)]
        sys.stdin.readline() # 층 사이 공백 입력받음

    for i in range(L) :
        for j in range(R) :
            for k in range(C) :
                if graph[i][j][k] == "S" : # 시작지점 -> BFS 수행
                    BFS(i, j, k)

