import sys

N = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().split()))
num.sort()

v = int(sys.stdin.readline())

cnt = 0
for i in num :
    if i > v :
        break
    if i == v :
        cnt += 1

print(cnt)