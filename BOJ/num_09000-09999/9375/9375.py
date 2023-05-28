import sys

T = int(sys.stdin.readline())

for _ in range(T) :
    N = int(sys.stdin.readline())
    wear_dict = {}
    for _ in range(N) :
        wear = list(sys.stdin.readline().split())
        if wear[1] in wear_dict :
            wear_dict[wear[1]].append(wear[0])
        else :
            wear_dict[wear[1]] = [wear[0]]

    cnt = 1

    for k in wear_dict :
        cnt *= (len(wear_dict[k]) + 1)
    
    print(cnt - 1)