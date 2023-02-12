import sys

score = 0
for _ in range(5) :
    i = int(sys.stdin.readline())
    if i <= 40 :
        i = 40
    score += i

print(score // 5)