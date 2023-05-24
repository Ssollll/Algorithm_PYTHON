import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

def BFS(now, move) :
    q = deque()

    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]

    q.append(now)

    while q :
        x, y = q.popleft()

        if x == move[0] and y == move[1] :
            return matrix[x][y] - 1
    
        for i in range(8) :
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < L and 0 <= ny < L and matrix[nx][ny] == 0 :
                matrix[nx][ny] = matrix[x][y] + 1
                q.append([nx, ny])

for _ in range(T) :
    L = int(input())
    now = list(map(int, input().split()))
    move = list(map(int, input().split()))

    matrix = [[0] * L for _ in range(L)]
    matrix[now[0]][now[1]] = 1

    print(BFS(now, move))
    

    