import sys
input = sys.stdin.readline

N, M = map(int, input().split())
basket = [0 for _ in range(N+1)]

for _ in range(M) :
    i, j, k = map(int, input().split())
    for a in range(i, j+1) :
        if basket[a] == 0 :
            basket[a] = k
        else :
            basket[a] = k

print(*basket[1:])