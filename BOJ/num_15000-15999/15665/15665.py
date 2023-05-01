import sys
from itertools import product

N, M = map(int, sys.stdin.readline().split())
num = sorted(list(map(int, sys.stdin.readline().split())))

pe = sorted(list(set(product(num, repeat = M))))

for p in pe :
    print(*p, sep = " ")