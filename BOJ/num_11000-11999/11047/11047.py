import sys

N, K = map(int, sys.stdin.readline().split())
coin = [int(sys.stdin.readline()) for _ in range(N)]
coin.sort(reverse = True)

count = 0
for c in coin :
    count += (K // c)
    K = K % c

print(count)