import sys
input = sys.stdin.readline

X, Y = map(str, input().strip().split())

R_X = X[::-1]
R_Y = Y[::-1]

answer = int(R_X) + int(R_Y)
print(int(str(answer)[::-1]))