import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    p = input().strip()
    n = int(input())
    flag = 0
    num = input().strip()[1:-1].split(",")
    q = deque(num)
    if n == 0 :
        q = []

    for i in p :
        if i == "R" :
            flag += 1
        elif i == "D" :
            if len(q) == 0 :
                print("error")
                break
            else :
                if flag % 2 == 0 :
                    q.popleft()
                else :
                    q.pop()
    else :
        if flag % 2 == 0 :
            print("[" + ",".join(q) + "]")
        else :
            q.reverse()
            print("[" + ",".join(q) + "]")