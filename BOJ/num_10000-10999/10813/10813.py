import sys

N, M = map(int, sys.stdin.readline().split())

ball = [i for i in range(1, N+1)]

for i in range(M) :
    A, B = map(int, sys.stdin.readline().split())
    ball[A-1], ball[B-1] = ball[B-1], ball[A-1]

print(*ball, sep = " ")