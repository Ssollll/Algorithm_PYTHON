import sys

N = int(sys.stdin.readline())
num = [0] * 2

for _ in range(N) :
    y = int(sys.stdin.readline())
    num[y] += 1

if num[0] > num[1] :
    print("Junhee is not cute!")
else :
    print("Junhee is cute!")