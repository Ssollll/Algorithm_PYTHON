import sys

N, M = map(int, sys.stdin.readline().split())

S = [str(sys.stdin.readline().strip()) for _ in range(N)]
te = [str(sys.stdin.readline().strip()) for _ in range(M)]

cnt = 0
for t in te :
    if t in S :
        cnt += 1

print(cnt)