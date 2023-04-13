import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

dp = [[0] * N for _ in range(N)]
for i in range(N) :
    dp[i][i] = 1
for i in range(N-1) : 
    if num[i] == num[i+1] :
        dp[i][i+1] = 1
    else :
        dp[i][i+1] = 0
for i in range(3, N+1) :
    for start in range(N - i + 1) :
        end = start + i - 1
        if num[start] == num[end] and dp[start+1][end-1] == 1 :
            dp[start][end] = 1

M = int(sys.stdin.readline())

for _ in range(M) :
    A, B = map(int, sys.stdin.readline().split())
    print(dp[A-1][B-1])