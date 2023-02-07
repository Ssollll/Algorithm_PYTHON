import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

s = [0] * (N+1)
for i in range(1, N+1) :
    s[i] = s[i-1] + num[i-1]
for _ in range(M) :
    i, j = map(int, sys.stdin.readline().split())
    print(s[j] - s[i-1])