import sys

n = int(sys.stdin.readline())

sq = [0] * 1001
sq[1], sq[2] = 1, 3

for i in range(3, n+1) :
    sq[i] = sq[i-1] + (sq[i-2] * 2)

print(sq[n] % 10007)