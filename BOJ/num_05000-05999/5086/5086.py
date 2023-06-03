import sys

A, B = map(int, sys.stdin.readline().split())

while A != 0 and B != 0 :
    if A > B :
        if A % B == 0 :
            print("multiple")
        else :
            print("neither")
    elif A < B :
        if B % A == 0 :
            print("factor")
        else :
            print("neither")
    A, B = map(int, sys.stdin.readline().split())