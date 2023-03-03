import sys

N = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for _ in range(N)]

stack = []
answer = []
for i in range(1, N+1) :
    answer.append("+")
    stack.append(i)
    if i == num[0] :
        answer.append("-")
        stack.pop()
        num = num[1:]
        for k in num :
            if len(stack) >= 1 and k == stack[-1] :
                answer.append("-")
                num = num[1:]
                stack.pop()
            else :
                break
# print(stack)
# print(num)
# if stack == num[::-1] :
#     for _ in num :
#         answer.append("-")
#     print(*answer, sep = "\n")
# else :
#     print("NO")

if len(stack) == 0 :
    print(*answer, sep = "\n")
else :
    print("NO")
