import sys

N, M = map(int, sys.stdin.readline().split())

truth = list(map(int, sys.stdin.readline().split()))[1:]

know_truth = 0

parent = [i for i in range(N + 1)]
for t in truth :
    parent[t] = know_truth

def find(x) :
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b) :
    a = find(a)
    b = find(b)

    if a < b :
        parent[b] = a
    else :
        parent[a] = b

party = []
for _ in range(M) :
    p = list(map(int, sys.stdin.readline().split()))[1:]
    for i in range(len(p) - 1) :
        union(p[i], p[i+1])
    party.append(p)

answer = 0

for p in party :
    know = False
    for i in range(len(p)) :
        if find(p[i]) == know_truth :
            know = True
            break
    if not know :
        answer += 1

print(answer)