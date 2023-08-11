import sys
input = sys.stdin.readline

N = input().strip()
N = sorted(N, reverse = True)

if "0" not in N :
    print(-1)
else :
    s = 0
    for i in N :
        s += int(i)
    if s % 3 != 0 :
        print(-1)
    else :
        print("".join(N))