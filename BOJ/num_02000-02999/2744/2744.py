import sys

S = sys.stdin.readline()
answer = ""

for i in S :
    if not i.isupper() :
        answer += (i.upper())
    else :
        answer += (i.lower())

print(answer)