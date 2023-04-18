import sys

for i in range(3) :
    pl = list(map(int, sys.stdin.readline().split()))
    if sum(pl) == 0 :
        print("D")
    elif sum(pl) == 1 :
        print("C")
    elif sum(pl) == 2 :
        print("B")
    elif sum(pl) == 3 :
        print("A")
    elif sum(pl) == 4 :
        print("E")