import sys

N = int(sys.stdin.readline())

for _ in range(N) :
    i, j = map(int, sys.stdin.readline().split())
    print(i + j)