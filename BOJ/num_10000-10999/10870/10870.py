import sys

N = int(sys.stdin.readline())
fib = [0, 1]

if N <= 1 :
    print(fib[N])

else :
    for i in range(2, N+1) :
        fib.append(fib[i-1] + fib[i-2])

    print(fib[N])