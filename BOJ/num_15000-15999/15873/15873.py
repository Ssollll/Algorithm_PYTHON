import sys
input = sys.stdin.readline

num = str(input().strip())

if len(num) == 2 :
    print(int(num[0]) + int(num[1]))
elif len(num) == 4 :
    print(int(num[:2]) + int(num[2:]))
else :
    if num[-1] == "0" :
        print(int(num[0]) + int(num[1:]))
    else :
        print(int(num[:2]) + int(num[2]))