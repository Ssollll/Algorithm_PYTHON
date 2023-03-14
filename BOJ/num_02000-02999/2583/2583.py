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
        if square[i][j] == 0 : # 만약 칠해져있지 않은 부분이면
            square[i][j] = 1 # 칠해졌다고 표시, 나름의 방문처리
            dq.append((i, j)) # dq에 append 해주고
            area.append(1) # 영역 구하는 배열에 일단 1 append

            while dq : # dq가 빌때까지
                x, y = dq.popleft() # dq에서 제일 먼저 들어간 값 빼기
                for k in range(4) : # 4만큼 (북동남서) 연결된 부분 탐색
                    nx = x + dx[k] # 새로운 x
                    ny = y + dy[k] # 새로운 y
                    if 0 <= nx < M and 0 <= ny < N and square[nx][ny] == 0 :
                    # 새로운 x와 y의 범위가 각각 0이상이고, M, N 미만 일경우, 그리고 아직 방문하지 않았으면
                        dq.append((nx, ny)) # dq에 append 해주고
                        square[nx][ny] = 1 # 방문처리 해줌
                        area[-1] += 1 # 마지막으로 append된 area에 +1 해주기

print(len(area))
area.sort()
print(*area, sep = " ")