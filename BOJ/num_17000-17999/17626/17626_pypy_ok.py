import sys

N = int(sys.stdin.readline())

dp = [0, 1]

for i in range(2, N+1) :
    m = 1e9
    for j in range(1, int(i ** 0.5) + 1) :
        m = min(m, dp[i - (j**2)])
    dp.append(m + 1)

print(dp[N])