import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
data = list(permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9'], 3))

for _ in range(N) :
    num, s, b = map(int, input().split())
    num = list(str(num))
    remove_cnt = 0

    for i in range(len(data)) :
        s_cnt = 0
        b_cnt = 0

        i -= remove_cnt

        for j in range(3) :
            if num[j] == data[i][j] :
                s_cnt += 1
            elif num[j] in data[i] :
                b_cnt += 1

        if s_cnt != s or b_cnt != b :
            data.remove(data[i])
            remove_cnt += 1

print(len(data))

