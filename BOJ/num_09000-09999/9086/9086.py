import sys

N = int(sys.stdin.readline())

for _ in range(N) :
    A = sys.stdin.readline().strip()
    print(A[0], A[-1], sep = '')