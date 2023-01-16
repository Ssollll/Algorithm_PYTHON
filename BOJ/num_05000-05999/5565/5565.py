import sys

Total = int(sys.stdin.readline())

for _ in range(9) :
    b = int(sys.stdin.readline())
    Total -= b

print(Total)