import sys

score = [sum(list(map(int, sys.stdin.readline().split()))) for _ in range(5)]
m = max(score)

print(score.index(m) + 1, m, sep = " ")
# 인덱스는 0부터 시작하고, 참가자의 번호는 1부터 시작하기에 +1을 해줌