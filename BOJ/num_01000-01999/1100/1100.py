import sys
input = sys.stdin.readline

chess = [input().strip() for _ in range(8)]
check = [[0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0, 1, 0]]

ans = 0
for ch in range(8) :
    if ch in [0, 2, 4, 6] :
        for c in range(8) :
            if chess[ch][c] == "F" and check[0][c] == 0 :
                ans += 1
    if ch in [1, 3, 5, 7] :
        for c in range(8) :
            if chess[ch][c] == "F" and check[1][c] == 0 :
                ans += 1
        
print(ans)