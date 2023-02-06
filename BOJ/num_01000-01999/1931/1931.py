import sys

N = int(sys.stdin.readline())
time = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

time.sort(key = lambda x : (x[1], x[0]))

cnt = 0
etime = 0
for i, j in time :
    if etime <= i :
        etime = j
        cnt += 1

print(cnt)