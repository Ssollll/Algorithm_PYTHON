import sys
input = sys.stdin.readline

S = list(map(str, input().strip().split("-")))
answer = ""

for i in S :
    answer += i[0]

print(answer)