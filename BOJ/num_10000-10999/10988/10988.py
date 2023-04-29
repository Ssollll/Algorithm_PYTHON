import sys

s = str(sys.stdin.readline().strip())

l = len(s)

for i in range(l//2) :
    if s[i] == s[l-i-1] :
        continue
    else :
        print(0)
        exit()

print(1)