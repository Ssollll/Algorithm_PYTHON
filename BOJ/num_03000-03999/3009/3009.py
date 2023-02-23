import sys

x = []
y = []
for _ in range(3) :
    i, j = map(int, sys.stdin.readline().split())
    x.append(i)
    y.append(j)

answer = [0, 0]
for i in range(3) :
    if x.count(x[i]) == 1 :
        answer[0] = x[i]

    if y.count(y[i]) == 1 :
        answer[1] = y[i]

print(*answer)