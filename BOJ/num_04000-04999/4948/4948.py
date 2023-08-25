import sys
input = sys.stdin.readline

N = 123456 * 2 + 1
num = [True] * N

for i in range(2, int(N ** 0.5) + 1) :
    if num[i] :
        for j in range(2 * i, N, i) :
            num[j] = False

def countPrime(x) :
    cnt = 0
    for k in range(x + 1, x * 2 + 1) :
        if num[k] :
            cnt += 1
    print(cnt)

while True :
    k = int(input())

    if not k :
        break
    countPrime(k)
