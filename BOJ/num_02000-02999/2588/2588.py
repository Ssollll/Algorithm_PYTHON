import sys

N = sys.stdin.readline().strip()
M = sys.stdin.readline().strip()

num_3 = int(N) * int(M[2])
num_4 = int(N) * int(M[1])
num_5 = int(N) * int(M[0])
num_6 = num_5*100 + num_4*10 + num_3

print(num_3)
print(num_4)
print(num_5)
print(num_6)