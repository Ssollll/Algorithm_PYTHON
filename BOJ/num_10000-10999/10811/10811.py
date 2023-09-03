import sys
input = sys.stdin.readline

N, M = map(int, input().split())
bas = [i+1 for i in range(N)]

for i in range(M) :
    i, j = map(int, input().split())
    tmp = bas[i-1:j]
    tmp.reverse()
    bas[i-1:j] = tmp

print(*bas)