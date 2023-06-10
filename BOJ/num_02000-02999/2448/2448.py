N = int(input())
graph = [[" "] * 2 * N for _ in range(N)] 

def star(x, y, N) :
    if N == 3 :
        graph[x][y] = "*"
        graph[x+1][y-1] = graph[x+1][y+1] = "*"
        for i in range(-2, 3) :
            graph[x+2][y+i] = "*"
    else :
        next_N = N // 2
        star(x, y, next_N)
        star(x + next_N, y - next_N, next_N)
        star(x + next_N, y + next_N, next_N)

star(0, N - 1, N)

for i in graph :
    print("".join(i))