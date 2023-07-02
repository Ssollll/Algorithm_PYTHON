import sys
input = sys.stdin.readline

answer = 0
now = 0

for _ in range(4) :
    o, i = map(int, input().split())
    now -= o
    if now > answer :
        answer = now
    now += i
    if now > answer :
        answer = now

print(answer)