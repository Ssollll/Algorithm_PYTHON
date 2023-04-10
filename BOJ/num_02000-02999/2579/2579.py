import sys

N = int(sys.stdin.readline())

stairs = [int(sys.stdin.readline()) for _ in range(N)]
dp = [0 for _ in range(N)]

if N <= 2 :
    print(sum(stairs))
else :
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]

    for i in range(2, N) :
        dp[i] = max(stairs[i]+stairs[i-1]+dp[i-3], dp[i-2] + stairs[i])

    print(dp[-1])