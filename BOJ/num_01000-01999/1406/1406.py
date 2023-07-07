import sys
input = sys.stdin.readline

s1 = list(input().strip())
s2 = []

for _ in range(int(input())) :
    c = list(input().split())
    if c[0] == "L" :
        if s1 :
            s2.append(s1.pop())
    elif c[0] == "D" :
        if s2 :
            s1.append(s2.pop())
    elif c[0] == "B" :
        if s1 :
            s1.pop()
    else :
        s1.append(c[1])

s1.extend(reversed(s2))
print("".join(s1))