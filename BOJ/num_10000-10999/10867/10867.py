import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

num = list(set(num))
num.sort()

print(*num, sep = " ")