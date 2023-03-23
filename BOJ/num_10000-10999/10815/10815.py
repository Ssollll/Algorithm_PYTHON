import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
num.sort()

M = int(sys.stdin.readline())
mum = list(map(int, sys.stdin.readline().split()))

for i in mum :
    left, right = 0, N-1
    check = 0
    while left <= right :
        mid = (left + right) // 2
        if num[mid] > i :
            right = mid - 1
        elif num[mid] < i :
            left = mid + 1
        else :
            check = 1
            break
    if check :
        print(1, end = " ")
    else :
        print(0, end = " ")