import sys

T = int(sys.stdin.readline())

P = [0] * 101
P[1], P[2], P[3] = 1, 1, 1

for i in range(4, 101) :
    P[i] = P[i-3] + P[i-2]

for _ in range(T) :
    tri = int(sys.stdin.readline())
    print(P[tri])
