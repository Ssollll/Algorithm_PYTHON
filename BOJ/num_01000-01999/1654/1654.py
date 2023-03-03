import sys

K, N = map(int, sys.stdin.readline().split())
lan = [int(sys.stdin.readline()) for _ in range(K)]

left, right = 1, max(lan)

while left <= right :
    mid = (left + right) // 2
    cnt = 0

    for l in lan :
        cnt += (l // mid)

    if cnt < N :
        right = mid - 1
    else :
        left = mid + 1

print(right)
