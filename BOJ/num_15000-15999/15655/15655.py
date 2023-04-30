import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
num = sorted(list(map(int, sys.stdin.readline().split())))

an = combinations(num, M)
for i in an :
    print(*i, sep = " ")