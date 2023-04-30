import sys
from itertools import combinations

N = int(sys.stdin.readline())
num = sorted(list(map(int, sys.stdin.readline().split())))
X = int(sys.stdin.readline())
co = combinations(num, 2)

cnt = 0
for c in co :
    if sum(c) == X :
        cnt += 1

print(cnt)