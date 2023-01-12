import sys

while (True):
    cnt = 0
    S = sys.stdin.readline().strip()
    if S == "#":
        break
    for i in S:
        if i.lower() in ['a', 'e', 'i', 'o', 'u']:
            cnt += 1
    print(cnt)
