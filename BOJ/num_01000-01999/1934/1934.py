from math import lcm
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    A, B = map(int, input().split())
    L = lcm(A, B)
    print(L)

