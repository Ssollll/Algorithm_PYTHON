import sys
from collections import Counter

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
num_li = list(map(int, sys.stdin.readline().split()))

cnt = Counter(num)

for i in num_li :
    if i in cnt :
        print(cnt[i], end = " ")
    else :
        print(0, end = " ")

# for i in num :
#     if i in cnt_dict :
#         cnt_dict[i] += 1
#     else :
#         cnt_dict[i] = 1