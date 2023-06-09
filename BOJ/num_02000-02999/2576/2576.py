import sys
input = sys.stdin.readline

min_num = int(1e9)
answer = 0
for _ in range(7) :
    n = int(input())
    if n % 2 != 0 :
        answer += n
        if min_num > n :
            min_num = n

if answer != 0 :
    print(answer)
    print(min_num)
else :
    print(-1)