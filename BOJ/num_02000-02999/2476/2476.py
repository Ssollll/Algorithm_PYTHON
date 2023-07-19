import sys
input = sys.stdin.readline

N = int(input())
price = [0 for _ in range(N)]

for i in range(N) :
    A, B, C = map(int, input().split())
    if A == B and B == C :
        price[i] = 10000 + 1000 * A
    elif A == B and B != C :
        price[i] = 1000 + 100 * A
    elif A != B and B == C :
        price[i] = 1000 + 100 * B
    elif A == C and B != C :
        price[i] = 1000 + 100 * C
    else :
        price[i] = 100 * (max(max(A, B), C))

print(max(price))