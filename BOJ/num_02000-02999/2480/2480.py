import sys

num = list(map(int, sys.stdin.readline().split()))
num.sort()

if num[0] == num[1] == num[2] :
    print(10000 + (1000 * num[0]))
elif num[0] == num[1] :
    print(1000 + (100 * num[0]))
elif num[0] == num[2] :
    print(1000 + (100 * num[0]))
elif num[1] == num[2] :
    print(1000 + (100 * num[1]))
else :
    print(100 * num[2])