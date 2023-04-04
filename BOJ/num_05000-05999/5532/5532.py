import sys

L = int(sys.stdin.readline())

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())

if A % C == 0 :
    k = A // C
else :
    k = A // C + 1

if B % D == 0 :
    m = B // D
else :
    m = B // D + 1

st = max(k, m)
print(L - st)