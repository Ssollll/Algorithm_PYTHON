import sys
from itertools import combinations
input = sys.stdin.readline

N, S = map(int, input().split())
num = list(map(int, input().split()))
cnt = 0

for i in range(1, N+1) :
    com = combinations(num, i)

    for c in com :
        if sum(c) == S :
            cnt += 1

print(cnt)