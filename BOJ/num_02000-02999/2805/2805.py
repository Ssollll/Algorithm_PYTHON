import sys

N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

left, right = 0, max(tree)

while left <= right :
    mid = (left + right) // 2
    go = 0

    for t in tree :
        if t >= mid :
            go += (t - mid)

    if go >= M :
        left = mid + 1
    else :
        right = mid - 1

print(right)