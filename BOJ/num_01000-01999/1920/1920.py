import sys

N = int(sys.stdin.readline())
# list로 받으면 시간초과, set으로 받으면 통과
A = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))

for i in X :
    if i in A :
        print(1)
    else :
        print(0)