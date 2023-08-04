import sys
input = sys.stdin.readline

A, B = map(int, input().split())
num_A = set(map(int, input().split()))
num_B = set(map(int, input().split()))

print(len(num_A - num_B) + len(num_B - num_A))