import sys

while(True) :
    result = 'yes'
    S = sys.stdin.readline().strip()
    if S == '0' :
        break
    for i in range((len(S) // 2)) :
        if S[i] != S[len(S) - 1 - i] :
            result = 'no'
            break
    print(result)