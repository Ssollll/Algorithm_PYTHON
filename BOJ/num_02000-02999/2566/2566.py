import sys
input = sys.stdin.readline

num = [list(map(int, input().split())) for _ in range(9)]

r, c = 0, 0
m = 0
for i in range(9) :
    for j in range(9) :
        if num[i][j] > m :
            m = num[i][j]
            r, c = i, j

print(m)
print(r+1, c+1)