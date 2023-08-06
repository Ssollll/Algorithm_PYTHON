import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N) :
    name = str(input().strip())
    print(name.lower())