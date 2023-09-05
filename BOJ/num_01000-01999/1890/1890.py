import sys
input = sys.stdin.readline

N = int(input())
game = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N) :
    for j in range(N) :
        if i == j == N - 1 :
            print(dp[i][j])
            exit(0)

        dist = game[i][j] 
        if i + dist < N :
            dp[i + dist][j] += dp[i][j]
        if j + dist < N :
            dp[i][dist + j] += dp[i][j]

 