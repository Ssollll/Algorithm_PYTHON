import sys

N, M = map(int, sys.stdin.readline().split())

po = [sys.stdin.readline().strip() for _ in range(N)]
pro = [sys.stdin.readline().strip() for _ in range(M)]

for i in pro :
    if i.isdigit() == True :
        print(po[int(i)-1])
    else :
        print(po.index(i) + 1)