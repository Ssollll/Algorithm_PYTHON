import sys
input = sys.stdin.readline

num = list(map(int, input().split()))
num.sort()

print(abs((num[0] + num[3]) - (num[1] + num[2])))