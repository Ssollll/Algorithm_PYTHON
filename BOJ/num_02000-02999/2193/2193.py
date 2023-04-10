import sys

N = int(sys.stdin.readline())
dp = [0 for _ in range(N)]

if N == 1 :
    print(1)
else :
    dp[0] = 1
    dp[1] = 1
    for i in range(2, N) :
        dp[i] = dp[i-2] + dp[i-1]
    print(dp[-1])