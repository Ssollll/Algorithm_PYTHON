import sys

N = int(sys.stdin.readline())
num = sorted(list(map(int, sys.stdin.readline().split())))
X = int(sys.stdin.readline())

cnt = 0
left = 0
right = len(num) - 1

while left < right :
    temp = num[left] + num[right]
    if temp == X :
        cnt += 1
        left += 1
        right -= 1
    elif temp < X :
        left += 1
    else :
        right -= 1

print(cnt)