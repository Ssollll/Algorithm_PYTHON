import sys
input = sys.stdin.readline

A = int(input())
di = list(map(int, input().split()))

di.sort()

if A > 1 :
    N = di[0] * di[-1]
else :
    N = di[0] * di[0]

print(N)