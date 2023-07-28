import sys
input = sys.stdin.readline

N = int(input())
an = list(map(int, input().split()))

for i in range(N-1, 0, -1) :
    if an[i] < an[i-1] :
        x, y = i-1, i
        for j in range(N-1, 0, -1) :
            if an[j] < an[x] :
                an[j], an[x] = an[x], an[j]
                an = an[:i] + sorted(an[i:], reverse = True)
                print(*an)
                exit(0)

print(-1)