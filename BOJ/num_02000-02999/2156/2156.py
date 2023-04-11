import sys

N = int(sys.stdin.readline())
podo = [int(sys.stdin.readline()) for _ in range(N)]
dp = [0 for _ in range(N)]

dp[0] = podo[0]
if N > 1:
    dp[1] = podo[0]+podo[1]

if N > 2:
    dp[2] = max(podo[2]+podo[1], podo[2]+podo[0], dp[1])

for i in range(3, N):
    dp[i] = max(dp[i-1], dp[i-3]+podo[i-1]+podo[i], dp[i-2]+podo[i])

print(dp[-1])