import sys
input = sys.stdin.readline

T = int(input())

for i in range(T) :
    S = list(map(str, input().strip().split()))
    ans = []
    for s in S :
        ans.append(s[::-1])
    print(*ans)