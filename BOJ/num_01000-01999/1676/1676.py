import sys

N = int(sys.stdin.readline())

F = 1
for i in range(1, N+1) :
    F *= i

cnt = 0

while True :
    if F % 10 == 0 :
        cnt += 1
        F = F // 10
    else :
        print(cnt)
        break