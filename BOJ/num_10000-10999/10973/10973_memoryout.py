import sys
from itertools import permutations

N = int(sys.stdin.readline())
an = list(map(int, sys.stdin.readline().split()))
num = [i for i in range(1, N+1)]

pe = list(permutations(num, N))
 
for p in range(len(pe)) :
    if list(pe[p]) == an : 
        if p == 0 :
            print(-1)
        else :
            print(*pe[p-1])