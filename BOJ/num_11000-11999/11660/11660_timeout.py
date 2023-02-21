import sys

N, M = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(M) :
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    s = 0

    for a in range(x1-1, x2) :
        for b in range(y1-1, y2) :
           s += graph[a][b]

    print(s)