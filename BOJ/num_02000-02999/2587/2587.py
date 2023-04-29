import sys

num = [int(sys.stdin.readline()) for _ in range(5)]

num.sort()

print(sum(num) // 5)
print(num[2])