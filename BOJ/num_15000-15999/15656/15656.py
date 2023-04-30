import sys
from itertools import product

N, M = map(int, sys.stdin.readline().split())
num = sorted(list(map(int, sys.stdin.readline().split())))

pr = product(num, repeat = M)
for p in pr :
    print(*p, sep = " ")