import sys

N = int(sys.stdin.readline())

RGB = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for i in range(1, N) :
    # R
    RGB[i][0] = min(RGB[i-1][1], RGB[i-1][2]) + RGB[i][0]
    # G
    RGB[i][1] = min(RGB[i - 1][0], RGB[i - 1][2]) + RGB[i][1]
    # B
    RGB[i][2] = min(RGB[i - 1][0], RGB[i - 1][1]) + RGB[i][2]

print(min(RGB[-1]))