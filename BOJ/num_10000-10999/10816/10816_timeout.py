# pypy3로 해도, python3으로 해도 시간초과나는 코드
import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
num_li = list(map(int, sys.stdin.readline().split()))
cnt_li = [0] * M

for i in num :
    if i in num_li :
        cnt_li[num_li.index(i)] += 1

print(*cnt_li)