import sys
input = sys.stdin.readline

A = int(input())
num = list(map(int, input().split()))

dp = [0 for _ in range(A)]
dp[0] = num[0]

for i in range(1, A) :
    for j in range(i) :
        if num[i] > num[j] :
            dp[i] = max(dp[i], dp[j] + num[i])
        else :
            dp[i] = max(dp[i], num[i])

print(max(dp))