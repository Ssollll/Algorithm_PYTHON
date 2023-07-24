import sys
input = sys.stdin.readline

while True :
    S = input().rstrip("\n")
    if not S :
        break
    l, u, n, s = 0, 0, 0, 0
    for st in S :
        if st.islower() :
            l += 1
        elif st.isupper() :
            u += 1
        elif st.isspace() :
            s += 1
        else :
            n += 1

    print(l, u, n, s)