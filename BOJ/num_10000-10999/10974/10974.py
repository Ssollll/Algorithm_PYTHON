import sys
from itertools import permutations

N = int(sys.stdin.readline())
num = [i for i in range(1, N+1)]

pe = permutations(num, N)

for p in pe :
    print(*p, sep = " ")
    