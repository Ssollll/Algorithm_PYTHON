import sys

N = int(sys.stdin.readline())

graph = [list(map(str, sys.stdin.readline().strip())) for _ in range(N)]

def solve(x, y, n) :
    sq = graph[x][y]
    for i in range(x, x+n) :
        for j in range(y, y+n) :
            if sq != graph[i][j] :
                sq = -1
                break

    if sq == -1 :
        print("(", end = "")
        n = n // 2
        solve(x, y, n)
        solve(x, y + n, n)
        solve(x + n, y, n)
        solve(x + n, y + n, n)
        print(")", end = "")
    elif sq == "1" :
        print(1, end = "")
    elif sq == "0" :
        print(0, end = "")

solve(0, 0, N)