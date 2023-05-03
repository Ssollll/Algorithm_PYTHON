import sys
from itertools import combinations

A = list(map(int, sys.stdin.readline().split()))

while A[0] != 0 :
    co = list(combinations(A[1:], 6))

    for c in co :
        print(*c, sep = " ")
    
    A = list(map(int, sys.stdin.readline().split()))
    print()