import sys
input = sys.stdin.readline

A, B = map(int, input().split())
num = [0]

for i in range(1, B + 1) :
    for j in range(i) :
        num.append(i)

answer = 0
for i in range(A, B+1) :
    answer += num[i]

print(answer)