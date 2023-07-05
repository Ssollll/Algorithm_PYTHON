import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())

def DFS(v) :
    visited[v] = 1
    ne = case[v]
    if visited[ne] == 0 :
        DFS(ne)

for _ in range(T) :
    N = int(input())
    case = [0] + list(map(int, input().split()))
    visited = [0 for _ in range(N+1)] 
    p = 0

    for i in range(1, N+1) :
        if visited[i] == 0 :
            DFS(i)
            p += 1
    print(p)