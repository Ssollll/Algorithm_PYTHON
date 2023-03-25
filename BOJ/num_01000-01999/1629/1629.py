import sys

A, B, C = map(int, sys.stdin.readline().split())

def answer(A, B, C) :
    if B == 1 :
        return A % C
    elif B % 2 == 0 :
        return (answer(A, B//2, C) ** 2) % C
    else :
        return ((answer(A, B//2, C) ** 2) * A) % C

print(answer(A, B, C))