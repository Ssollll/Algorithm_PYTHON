import sys
input = sys.stdin.readline

first = [int(input()) for _ in range(4)]
second = [int(input()) for _ in range(2)]

first.sort(reverse = True)
second.sort(reverse = True)
print(sum(first[:3]) + second[0])