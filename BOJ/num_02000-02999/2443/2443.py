import sys

N = int(sys.stdin.readline())

for i in range(N) :
    print(" " * i + "*" * (2*(N-i) - 1))