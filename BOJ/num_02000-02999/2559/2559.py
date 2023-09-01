import sys
input = sys.stdin.readline

N, K = map(int, input().split())
tem = list(map(int, input().split()))

ans = []
ans.append(sum(tem[:K]))

for i in range(N - K) :
    ans.append(ans[i] - tem[i] + tem[i + K])

print(max(ans))