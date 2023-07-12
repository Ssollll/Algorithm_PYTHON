import sys
input = sys.stdin.readline

answer = 0
result = []
for _ in range(10) :
    d, u = map(int, input().split())
    answer = answer - d + u
    result.append(answer)

print(max(result))