import sys
input = sys.stdin.readline

S = input().strip()
bomb = input().strip()

stack = []
b_len = len(bomb)

for i in range(len(S)) :
    stack.append(S[i])
    if "".join(stack[-b_len:]) == bomb :
        for _ in range(b_len) :
            stack.pop()

if stack :
    print("".join(stack))
else :
    print("FRULA")