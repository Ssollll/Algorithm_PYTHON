import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

N = int(input())
X, Y = map(int, input().split())
M = int(input())
fam = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
result = []

for _ in range(M) :
    a, b = map(int, input().split())
    fam[a].append(b)
    fam[b].append(a)

def DFS(v, cnt) :
    cnt += 1
    visited[v] = 1
    if v == Y :
        result.append(cnt)
    for i in fam[v] :
        if visited[i] == 0 :
            DFS(i, cnt)

DFS(X, 0)

if len(result) == 0 :
    print(-1)
else :
    print(result[0] - 1)