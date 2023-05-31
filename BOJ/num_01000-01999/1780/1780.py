import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
cnt_minus, cnt_zero, cnt_plus = 0, 0, 0

def check(row, col, N) :
    global cnt_minus, cnt_zero, cnt_plus
    curr = paper[row][col]

    for i in range(row, row + N) :
        for j in range(col, col + N) :
            if paper[i][j] != curr :
                next_n =  N// 3
                check(row, col, next_n)
                check(row, col + next_n, next_n)
                check(row, col + (next_n * 2), next_n)
                check(row + next_n, col, next_n)
                check(row + next_n, col + next_n, next_n)
                check(row + next_n, col + (next_n * 2), next_n)
                check(row + (next_n * 2), col, next_n)
                check(row + (next_n * 2), col + next_n, next_n)
                check(row + (next_n * 2), col + (next_n * 2), next_n)
                return
            
    if curr == -1 :
        cnt_minus += 1
    elif curr == 0 :
        cnt_zero += 1
    else :
        cnt_plus += 1
    return

check(0, 0, N)

print(cnt_minus)
print(cnt_zero)
print(cnt_plus)