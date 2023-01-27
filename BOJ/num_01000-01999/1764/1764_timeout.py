import sys

N, M = map(int, sys.stdin.readline().split())

hear = [sys.stdin.readline() for _ in range(N)]
see = [sys.stdin.readline() for _ in range(M)]

answer = []
for i in hear :
    for j in see :
        if i == j :
            answer.append(i)
            break

print(len(answer))
for i in answer :
    print(i, end = "")

