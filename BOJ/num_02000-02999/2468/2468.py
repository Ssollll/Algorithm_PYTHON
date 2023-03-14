import sys
from collections import deque

N = int(sys.stdin.readline())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 0
max_n =  max(map(max, graph)) # 모든 그래프에서 제일 큰 값 찾기, 2중리스트라서 그냥 max는 안됨


def BFS(i, j, k) : # BFS 정의

    # 북동남서 (시계방향)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    dq = deque()
    dq.append((i, j))
    visited[i][j] = 1

    while dq :
        x, y = dq.popleft()

        for r in range(4) : # 북동남서, 연결방향 찾는 것
            nx, ny = x + dx[r], y + dy[r]
            if 0 > nx or nx >= N or 0 > ny or ny >= N : # 만약 연결지점이 원래 영역에서 벗어난다면
                continue
            if graph[nx][ny] > k and visited[nx][ny] == 0 : # 연결 지점이 잠기지 않고, 방문하지 않은 노드라면
                dq.append((nx, ny))
                visited[nx][ny] = 1 # 방문처리

for i in range(max_n) : # 0부터, graph에서 제일 큰값까지 for문 반복
    cnt = 0
    visited = [[0] * N for _ in range(N)] # 방문 처리 위한 배열
    for j in range(N) : # 행
        for k in range(N) : # 열
            if graph[j][k] > i and visited[j][k] == 0 : # 그래프가 현재 높이 보다 높고, 방문이 안되어 있다면 (= 잠기지 않는다면)
                BFS(j, k, i) # BFS 실행 -> 내 노드부터 연결된 안전영역 찾기
                cnt += 1 # 안전영역 +1 해주기
    if answer < cnt :
        answer = cnt

print(answer)
