import sys
input = sys.stdin.readline
INF = int(10e9)

N = int(input())
M = int(input())

bus = [[INF] * (N+1) for _ in range(N+1)]
for i in range(1, N+1) :
    bus[i][i] = 0

for _ in range(M) :
    a, b, c = map(int, input().split())
    bus[a][b] = min(bus[a][b], c)

for k in range(1, N+1) :
    for a in range(1, N+1) :
        for b in range(1, N+1) :
            bus[a][b] = min(bus[a][b], bus[a][k] + bus[k][b])

for i in range(1, N+1) :
    for j in range(1, N+1) :
        if bus[i][j] == INF :
            print(0, end = " ")
        else :
            print(bus[i][j], end = " ")
    print()