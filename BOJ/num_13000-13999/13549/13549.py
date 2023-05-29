import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

def BFS() :
    graph = [-1] * 100001
    graph[N] = 0
    dq = deque([N])

    while dq :
        t = dq.popleft()
        if t == K :
            return graph[t]
        
        for i in (t + 1, t - 1, t * 2) :
            if 0 <= i <= 100000 and graph[i] == -1 :
                if i == t * 2 :
                    graph[i] = graph[t]
                    dq.appendleft(i)
                else :
                    graph[i] = graph[t] + 1
                    dq.append(i)

print(BFS())