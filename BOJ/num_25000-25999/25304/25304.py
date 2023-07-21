import sys
input = sys.stdin.readline

X = int(input())
N = int(input())
answer = 0
for _ in range(N) :
    A, B = map(int, input().split())
    answer += (A * B)

if answer == X :
    print("Yes")
else :
    print("No")