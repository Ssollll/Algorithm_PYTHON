import sys

N = int(sys.stdin.readline())

answer = 0

for i in range(1, N+1) :
    num = list(map(int, str(i)))
    if i < 100 :
        answer += 1
    elif num[0] - num[1] == num[1] - num[2] :
        answer += 1
print(answer)