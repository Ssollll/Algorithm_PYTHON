import sys
from collections import deque

N = int(sys.stdin.readline())
house = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

def BFS(graph, x, y, N) :

    # 북동남서(시계방향) 상우하좌
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    dq = deque()
    dq.append((x, y))
    graph[x][y] = 0 # 방문노드 0으로 바꿔서 다시 방문하지 않도록
    cnt = 1

    while dq :
        a, b = dq.popleft()
        graph[a][b] = 0
        for i in range(4) :
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N :
                continue

            if graph[nx][ny] == 1 :
                graph[nx][ny] = 0
                dq.append((nx, ny))
                cnt += 1

    return cnt

sd = []
for i in range(N) :
    for j in range(N) :
        if house[i][j] == 1 :
            count = BFS(house, i, j, N)
            sd.append(count)

sd.sort()
print(len(sd))
print(*sd, sep = "\n")
