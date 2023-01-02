import sys

while(True) :
    S = sys.stdin.readline().strip()
    if S == '0' :
        break

    if S == S[::-1] :
        print('yes')
    else :
        print('no')

    # print("yes" if S == S[::-1] else "no")
    # 파이썬.. 기본도 하나도 모르네 나..