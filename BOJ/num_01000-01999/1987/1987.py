import sys

R, C = map(int, sys.stdin.readline().split())
alph = [list(map(str, sys.stdin.readline().strip())) for _ in range(R)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
tmp = 1
answer = 1

def BFS(start, end) :
    global answer
    q = set([(start, end, alph[start][end])])

    while q :
        x, y, z = q.pop()
        for i in range(4) :
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and alph[nx][ny] not in z :
                q.add((nx, ny, z + alph[nx][ny]))
                answer = max(answer, len(z) + 1)

BFS(0, 0)
print(answer)