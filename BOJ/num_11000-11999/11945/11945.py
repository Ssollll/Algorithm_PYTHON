import sys

N, M = map(int, sys.stdin.readline().split())

bup = [list(map(str, sys.stdin.readline().strip())) for _ in range(N)]

for i in range(N) :
    print(*bup[i][::-1], sep = "", end = "\n")