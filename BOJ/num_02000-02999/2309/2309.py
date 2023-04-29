import sys
from itertools import combinations

nan = [int(sys.stdin.readline()) for _ in range(9)]
for i in combinations(nan, 7) :
    if sum(i) == 100 :
        i = sorted(i)
        print(*i, sep = "\n")
        break