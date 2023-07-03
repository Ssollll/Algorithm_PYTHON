import sys
input = sys.stdin.readline

N = int(input())

group = 0

for _ in range(N) :
    w = input().strip()
    flag = 0
    for i in range(len(w) - 1) :
        if w[i] != w[i + 1] :
            new_w = w[i + 1:]
            if new_w.count(w[i]) > 0 :
                flag += 1

    if flag == 0 :
        group += 1

print(group)