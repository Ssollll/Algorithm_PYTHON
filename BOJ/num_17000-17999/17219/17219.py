import sys

N, M = map(int, sys.stdin.readline().split())

si = {}
for _ in range(N) :
    A, B = map(str, sys.stdin.readline().strip().split())
    si[A] = B

for i in range(M) :
    site = str(sys.stdin.readline().strip())
    print(si[site])