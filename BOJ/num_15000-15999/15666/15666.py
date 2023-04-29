import sys
from itertools import combinations_with_replacement

N, M = map(int, sys.stdin.readline().split())
num = set(map(int, sys.stdin.readline().split()))

an = combinations_with_replacement(sorted(num), M)

for i in an :
    for j in i :
        print(j, end = " ")
    print()