import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    num = list(map(int, input().split()))
    num.sort()

    print(num[-3])