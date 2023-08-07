import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
dq = deque(enumerate(map(int, input().split())))

answer = []
while dq :
    idx, b = dq.popleft()
    answer.append(idx + 1)
    if b > 0 :
        dq.rotate(-(b - 1))
    elif b < 0 :
        dq.rotate(-b)

print(*answer)