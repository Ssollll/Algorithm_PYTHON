import sys

N = int(sys.stdin.readline())
tmp = list(map(int, sys.stdin.readline().split()))

max_dp = tmp
min_dp = tmp

for _ in range(N - 1) :
    tmp = list(map(int, sys.stdin.readline().split()))

    max_dp = [tmp[0] + max(max_dp[0], max_dp[1]), tmp[1] + max(max_dp), tmp[2] + max(max_dp[1], max_dp[2])]
    min_dp = [tmp[0] + min(min_dp[0], min_dp[1]), tmp[1] + min(min_dp), tmp[2] + min(min_dp[1], min_dp[2])]

print(max(max_dp), min(min_dp))