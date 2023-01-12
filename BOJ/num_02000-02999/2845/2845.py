import sys

L, P = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
peo = L * P

dis = [x - peo for x in num]

print(*dis)