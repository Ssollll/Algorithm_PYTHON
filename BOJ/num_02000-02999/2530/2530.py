import sys

H, M, S = map(int, sys.stdin.readline().split())
cook = int(sys.stdin.readline())

S += cook
M += S // 60
H += M // 60

print(H%24, M%60, S%60)