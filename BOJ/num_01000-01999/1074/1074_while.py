import sys

N, r, c = map(int, sys.stdin.readline().split())
cnt = 0

while N != 0 :
    size = 2 ** (N - 1)
    if r < size and c >= size :
        cnt += size * size
        c -= size
    elif r < size and c < size :
        pass
    elif r >= size and c < size :
        cnt += size * size * 2
        r -= size
    else :
        cnt += size * size * 3
        r -= size
        c -= size

    N -= 1

print(cnt)