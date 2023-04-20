import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())
arr = list(permutations([i for i in range(1, N+1)], M))

for a in arr :
    print(*a)