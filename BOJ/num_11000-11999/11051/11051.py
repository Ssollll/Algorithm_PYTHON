import sys
input = sys.stdin.readline

N, K = map(int, input().split())

son = 1
for i in range(K) :
    son *= N
    N -= 1

mom = 1
for i in range(2, K+1) :
    mom *= i

print((son // mom) % 10007)
