import sys

N = sys.stdin.readline().strip()
num = [int(i) for i in N]
num.sort(reverse = True)
print(*num, sep = "")