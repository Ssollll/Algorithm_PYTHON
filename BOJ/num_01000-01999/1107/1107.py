import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

if M != 0 :
    button = list(input().split())
else :
    button = list()

ans = abs(100 - N)

for i in range(1000001) :
    for j in str(i) :
        if j in button :
            break
    
    else :
        ans = min(ans, len(str(i)) + abs(i - N))

print(ans)