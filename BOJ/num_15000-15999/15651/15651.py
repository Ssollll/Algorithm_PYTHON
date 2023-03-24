import sys

N, M = map(int, sys.stdin.readline().split())

arr = []
def DFS(cnt) :
    if cnt - 1 == M :
        print(" ".join(map(str, arr)))
        return

    for i in range(1, N+1) :
        arr.append(i)
        DFS(cnt + 1)
        arr.pop()

DFS(1)