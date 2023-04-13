import sys

N = int(sys.stdin.readline())
poly = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
poly.append(poly[0])

xtoy = 0
ytox = 0
for i in range(N) :
    xtoy += poly[i][0] * poly[i+1][1]
    ytox += poly[i][1] * poly[i+1][0]

print(round(abs((xtoy - ytox)/2), 1))