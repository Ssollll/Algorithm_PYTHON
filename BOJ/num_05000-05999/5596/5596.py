import sys

Min = list(map(int, sys.stdin.readline().split()))
Man = list(map(int, sys.stdin.readline().split()))

Min_to = sum(Min)
Man_to = sum(Man)

print(max(Min_to, Man_to))