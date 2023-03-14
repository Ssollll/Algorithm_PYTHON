import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().split())
# F : 총 층수
# S : 강호위치 / G : 목표지점
# U : 위로 U층 / D : 아래로 D층
visited = [0 for _ in range(F+1)] # 방문처리
count = [0 for _ in range(F+1)] # 엘리베이터 탄 횟수 계산

def BFS(v) :
    dq = deque()
    dq.append(v)
    visited[v] = 1

    while dq :
        c = dq.popleft()
        if c == G : # 현재 위치가 목표 지점과 같다면
            return count[G]

        for i in (c+U, c-D) : # 기본적으로 BFS는 북동남서 연결된 부분 계산해주지만, 요기서는 U만큼 위, D만큼 아래 계산해주면 됨
            if 0 < i <= F and visited[i] == 0 :
                visited[i] = 1
                count[i] = count[c] + 1
                dq.append(i)

    if count[G] == 0 :
        return "use the stairs"

print(BFS(S))

