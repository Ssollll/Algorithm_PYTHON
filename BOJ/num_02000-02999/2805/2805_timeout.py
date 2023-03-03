import sys

N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

for i in range(max(tree), 0, -1) :
    c = [tree[j] - i for j in range(len(tree))]
    for k in range(len(c)) :
        if c[k] < 0 :
            c[k] = 0
    if sum(c) >= M :
        print(i)
        break