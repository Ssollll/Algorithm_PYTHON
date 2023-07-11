import sys

N = int(sys.stdin.readline())

# dp = [0] * (N + 1)
# dp[1] = 4
# dp[2] = 8

# for i in range(3, N+1) :
#     dp[i] = dp[i-2] + dp[i-1]

# print(dp[-1])

print(4 * N)