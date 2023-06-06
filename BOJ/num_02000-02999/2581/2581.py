import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

prime = []

for i in range(M, N + 1) :
    flag = 0
    if i > 1 :
        for j in range(2, i) :
            if i % j == 0 :
                flag += 1
                break
        if flag == 0 :
            prime.append(i)

if len(prime) != 0 :
    print(sum(prime))
    print(min(prime))
else :
    print(-1)