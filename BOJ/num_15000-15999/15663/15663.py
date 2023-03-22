import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
num.sort()
visited = [0 for _ in range(N)]
an = []

def DFS() :
    if len(an) == M :
        print(*an)
        return

    now = 0

    for i in range(N) :
        if visited[i] == 0 and now != num[i] :
            visited[i] = 1
            an.append(num[i])
            now = num[i]
            DFS()
            visited[i] = 0
            an.pop()

DFS()