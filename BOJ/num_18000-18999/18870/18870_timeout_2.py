import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
num_set = sorted(list(set(num)))

for i in num :
    print(num_set.index(i), end = " ")

