import sys

N = int(sys.stdin.readline())
coin = [500, 100, 50, 10, 5, 1]

change = 1000 - N

cnt = 0
for c in coin :
    cnt += change // c
    change = change % c

print(cnt)