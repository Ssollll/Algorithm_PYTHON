import sys
input = sys.stdin.readline

N, K = map(int, input().split())
bag = [[0, 0]]
for _ in range(N) :
    bag.append(list(map(int, input().split())))

dp = [[0] * (K+1) for _ in range(N+1)]

for y in range(1, N+1) :
    for x in range(1, K+1) :
        W, V = bag[y][0], bag[y][1]
        if x < W :
            dp[y][x] = dp[y-1][x]
        else :
            dp[y][x] = max(dp[y-1][x], dp[y-1][x-W] + V)

print(dp[N][K])