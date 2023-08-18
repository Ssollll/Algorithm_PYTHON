import sys
input = sys.stdin.readline

N = int(input())
dic = {}

for _ in range(N) :
    A = int(input())
    if A in dic :
        dic[A] += 1
    else :
        dic[A] = 1

dic = sorted(dic.items(), key = lambda x : (-x[1], x[0]))
print(dic[0][0])