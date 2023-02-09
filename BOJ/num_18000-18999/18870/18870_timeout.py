import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
num_set = set(num)

for i in num :
    cnt = 0
    for j in num_set :
        if i > j :
            cnt += 1
    print(cnt, end = " ")