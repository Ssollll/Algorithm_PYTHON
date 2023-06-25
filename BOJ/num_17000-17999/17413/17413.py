import sys

S = sys.stdin.readline().strip()
stack = []
tag = False
ans = ''

for s in S :
    if s == " " :
        while stack :
            ans += stack.pop()
        ans += s

    elif s == "<" :
        while stack :
            ans += stack.pop()
        tag = True
        ans += s
    
    elif s == ">" :
        tag = False
        ans += s

    elif tag :
        ans += s
    
    else :
        stack.append(s)

while stack :
    ans += stack.pop()

print(ans)