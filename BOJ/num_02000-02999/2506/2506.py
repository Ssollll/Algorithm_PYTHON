import sys
input = sys.stdin.readline

N = int(input())
score = list(map(int, input().split()))

flag = 1
answer = 0
for s in score :
    if s == 1 :
        answer += flag
        flag += 1

    if s == 0 :
        flag = 1

print(answer)