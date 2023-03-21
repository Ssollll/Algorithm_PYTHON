import sys

N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
num.sort()
an = []

def DFS(n) :
    if len(an) == M :
        print(" ".join(map(str, an)))
        return

    for i in range(n, N) :
        an.append(num[i])
        DFS(i)
        an.pop()

DFS(0)