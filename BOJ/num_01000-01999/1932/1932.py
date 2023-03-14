import sys

N = int(sys.stdin.readline())

tri = [[] for _ in range(N)]
for i in range(N) :
    tri[i] = list(map(int, sys.stdin.readline().split()))

for i in range(1, N) :
    for j in range(i+1) :
        if j == 0 :
            tri[i][j] = tri[i-1][j] + tri[i][j]
        elif i == j :
            tri[i][j] = tri[i-1][j-1] + tri[i][j]
        else :
            tri[i][j] = max(tri[i-1][j-1], tri[i-1][j]) + tri[i][j]

print(max(tri[-1]))
