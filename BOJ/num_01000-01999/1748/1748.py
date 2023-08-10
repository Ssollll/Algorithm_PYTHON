import sys
input = sys.stdin.readline

N = input().strip()

answer = 0
for i in range(1, len(N)) :
    answer += int("9" + (i - 1) * "0") * i

answer += (int(N) - 10 ** (len(N) - 1) + 1) * len(N)
print(answer)