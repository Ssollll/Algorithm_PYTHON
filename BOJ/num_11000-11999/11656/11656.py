import sys

N = str(sys.stdin.readline().strip())

li_N = []
for _ in range(len(N)) :
    li_N.append(N)
    N = N[1:]

li_N.sort()

print(*li_N, sep = "\n")