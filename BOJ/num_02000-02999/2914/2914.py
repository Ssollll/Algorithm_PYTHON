import sys

A, I = map(int, sys.stdin.readline().split())

print(A * (I - 1) + 1) # 평균값 -> 무조건 올림, 그래서 전 숫자의 최댓값에서 1 더한값이 내 출력값