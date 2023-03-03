import sys

N = int(sys.stdin.readline())

if int(N ** 0.5) ** 2 == N :
    print(1)
    exit()

for i in range(1, int(N ** 0.5) + 1) :
    if int((N - (i ** 2)) ** 0.5) == ((N - (i ** 2)) ** 0.5) :
        print(2)
        exit()

for i in range(1, int(N ** 0.5) + 1) :
    for j in range(1, int((N - (i ** 2)) ** 0.5) + 1) :
        if int((N - (i ** 2) - (j ** 2)) ** 0.5) == ((N - (i ** 2) - (j ** 2)) ** 0.5) :
            print(3)
            exit()

print(4)