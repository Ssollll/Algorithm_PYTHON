import sys

N, r, c = map(int, sys.stdin.readline().split())
cnt = 0

def z(n, x, y) :
    global cnt
    if x == r and y == c :
        print(int(cnt))
        return

    if n == 1 :
        cnt += 1
        return

    if not (x <= r < x + n and y <= c < y + n) :
        cnt += n * n
        return

    z(n / 2, x, y)
    z(n / 2, x, y + (n / 2))
    z(n / 2, x + (n / 2), y)
    z(n / 2, x + (n / 2), y + (n / 2))

z(2 ** N, 0, 0)