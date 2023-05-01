import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
num = sorted(list(map(int, sys.stdin.readline().split())))

co = sorted(list(set(combinations(num, M))))

for c in co :
    print(*c, sep = " ")