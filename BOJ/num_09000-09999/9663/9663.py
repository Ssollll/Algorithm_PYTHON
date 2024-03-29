import sys

N = int(sys.stdin.readline())

answer = 0
row = [0] * N

def check(x) :
    for i in range(x) :
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i) :
            return False
    
    return True

def n_queen(x) :
    global answer
    if x == N :
        answer += 1
    else :
        for i in range(N) :
            row[x] = i
            if check(x) :
                n_queen(x+1)

n_queen(0)
print(answer)