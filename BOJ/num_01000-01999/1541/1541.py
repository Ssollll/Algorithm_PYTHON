import sys

eq = list(map(str, sys.stdin.readline().split("-")))

answer = []
for e in eq :
    sum = 0
    so = e.split("+")
    for s in so :
        sum += int(s)
    answer.append(sum)

n = answer[0]
for i in range(1, len(answer)) :
    n -= answer[i]

print(n)
