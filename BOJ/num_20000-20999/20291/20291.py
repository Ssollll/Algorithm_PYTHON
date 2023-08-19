import sys
input = sys.stdin.readline

N = int(input())
dic = {}

for _ in range(N) :
    A, B = map(str, input().strip().split("."))
    if B in dic :
        dic[B] += 1
    else :
        dic[B] = 1

dic = sorted(dic.items(), key = lambda x : x[0])

for i in range(len(dic)) :
    print(*dic[i], sep = " ")