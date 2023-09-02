import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    N = int(input()) 
    co = [list(map(int, input().split())) for _ in range(N)]
    co.sort()

    cnt = 1
    max_co = co[0][1]
    for i in range(1, N) :
        if max_co > co[i][1] :
            cnt += 1
            max_co = co[i][1]

    print(cnt)