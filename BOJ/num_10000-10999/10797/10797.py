import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

cnt = 0
for i in num :
    if N == i :
        cnt += 1

print(cnt)