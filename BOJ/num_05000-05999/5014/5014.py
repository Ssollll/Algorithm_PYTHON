import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().split())
# F : 총 층수
# S : 강호위치 / G : 목표지점
# U : 위로 U층 / D : 아래로 D층
visited = [0 for _ in range(F+1)]
count = [0 for _ in range(F+1)]

def BFS(v) :
    dq = deque()
    dq.append(v)
    visited[v] = 1

    while dq :
        c = dq.popleft()
        if c == G :
            return count[G]

        for i in (c+U, c-D) :
            if 0 < i <= F and visited[i] == 0 :
                visited[i] = 1
                count[i] = count[c] + 1
                dq.append(i)

    if count[G] == 0 :
        return "use the stairs"

print(BFS(S))

