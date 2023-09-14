import sys
input = sys.stdin.readline

V, E = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(E)]
graph.sort(key = lambda x : x[2])

root = {}
for i in range(1, V+1) :
    root[i] = i

def find(x) :
    if root[x] == x :
        return x
    else :
        root[x] = find(root[x])
        return root[x]

def union(x, y) :
    x = find(x)
    y = find(y)

    root[y] = x

ans = 0

for e in graph :
    if find(e[0]) == find(e[1]) :
        continue
    else :
        ans += e[2]
        union(e[0], e[1])
print(ans)