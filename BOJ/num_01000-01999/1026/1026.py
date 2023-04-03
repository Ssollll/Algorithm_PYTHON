import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort()
B.sort(reverse = True)

an = 0
for i in range(N) :
    an += (A[i] * B[i])

print(an)