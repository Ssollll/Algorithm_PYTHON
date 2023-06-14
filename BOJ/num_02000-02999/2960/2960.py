import sys

N, K = map(int, sys.stdin.readline().split())
cnt = 0
num = [0 for _ in range(N+1)]

for i in range(2, len(num) + 1) :
    for j in range(i, N+1, i) :
        if num[j] == 0 :
            num[j] = 1
            cnt += 1
            if cnt == K :
                print(j)
                break