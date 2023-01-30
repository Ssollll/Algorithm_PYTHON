import sys

while True :
    s = sys.stdin.readline().rstrip()
    if s == "." :
        break

    stack = []
    cnt = 0
    for i in s :
        if i == "(" or i == "[" :
            stack.append(i)
        elif i == ")" :
            if not stack or stack[-1] == "[" :
                cnt = 1
                break
            else :
                stack.pop()
        elif i == "]" :
            if not stack or stack[-1] == "(" :
                cnt = 1
                break
            else :
                stack.pop()

    if not stack and not cnt :
        print("yes")
    else :
        print("no")
