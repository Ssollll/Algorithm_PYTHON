import sys

while(True) :
    S = sys.stdin.readline().strip()
    if S == "END" :
        break
    print(S[::-1])
