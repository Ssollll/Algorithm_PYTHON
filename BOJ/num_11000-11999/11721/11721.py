import sys

S = sys.stdin.readline().strip()

while(True) :
    if len(S) < 10 :
        print(S)
        break
    print(S[:10])
    S = S[10:]