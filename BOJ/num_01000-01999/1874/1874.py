import sys

N = int(sys.stdin.readline())
stack = []
answer = []
flag = 1
cnt = 1

for _ in range(N) :
    num = int(sys.stdin.readline())
    while cnt <= num :
        stack.append(cnt)
        answer.append("+")
        cnt += 1
    if stack[-1] == num :
        stack.pop()
        answer.append("-")
    else :
        flag = 0

if flag == 0 :
    print("NO")
else :
    print(*answer, sep = "\n")
