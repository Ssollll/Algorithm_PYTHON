import sys
import math
input = sys.stdin.readline

G = "Goldbach's conjecture is wrong."
arr = [True for _ in range(1000001)]

def prime(x) :
    for i in range(2, int(math.sqrt(1000000)) + 1) :
        if arr[i] == True :
            for j in range(i+i, 1000001, i) :
                arr[j] = False
    return [i for i in range(2, 1000001) if arr[i] == True]

prime_list = prime(1000000)

while True :
    N = int(input())
    if N == 0 :
        break
    for i in prime_list :
        if arr[N - i] :
            print(f'{N} = {i} + {N-i}')
            break

