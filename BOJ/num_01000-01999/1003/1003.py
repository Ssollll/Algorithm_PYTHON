import sys
input = sys.stdin.readline

T = int(input())

zero = [1, 0, 1]
one = [0, 1, 1]

def fib(N) :
    l = len(zero)
    if N >= l :
        for i in range(l, N+1) :
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    
    print(f"{zero[N]} {one[N]}")

for _ in range(T) :
    N = int(input())
    fib(N)
