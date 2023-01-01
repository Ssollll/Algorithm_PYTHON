import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

result = 0

for i in range(N) :
    for j in range(i+1, N) :
        for k in range(i+2, N) :
            if num[i] + num[j] + num[k] > M :
                continue
            else :
                result = max(result, num[i] + num[j] + num[k])

print(result)