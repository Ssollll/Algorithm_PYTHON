import sys

N = int(sys.stdin.readline())
rope = [int(sys.stdin.readline()) for _ in range(N)]
rope.sort(reverse = True)

result = 0

for r in range(N) :
    result = max(result, rope[r]*(r+1))

print(result)