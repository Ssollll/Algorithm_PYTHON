import sys
input = sys.stdin.readline

dp = [0, 1, 2, 4]
T = int(input())

for i in range(4, 1000001) :
    dp.append((dp[i-3] + dp[i-2] + dp[i-1]) % 1000000009)

for i in range(T) :
    N = int(input())
    print(dp[N])