import sys
from collections import deque

dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [0, 1, 0, -1, -1, 1, -1, 1]

def BFS(x, y) :
    graph[x][y] = 0
    q = deque()
    q.append([x, y])

    while q :
        x, y = q.popleft()
        for i in range(8) :
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1 :
                graph[nx][ny] = 0
                q.append([nx, ny])

while True :
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0 :
        break
    
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    cnt = 0
    for i in range(h) :
        for j in range(w) :
            if graph[i][j] == 1 :
                BFS(i, j)
                cnt += 1
    
    print(cnt)