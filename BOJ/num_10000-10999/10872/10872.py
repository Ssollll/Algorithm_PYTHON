import sys

N = int(sys.stdin.readline())

answer = 1

for i in range(N) :
    answer *= (i + 1)

print(answer)