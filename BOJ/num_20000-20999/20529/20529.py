import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    cnt = 999999
    N = int(input())
    mbti = list(map(str, input().strip().split()))
    if N > 32 :
        print(0)
    else :
        for i in range(N) :
            for j in range(N) :
                for k in range(N) :
                    tmp = 0
                    if i == j or j == k or i == k :
                        continue
                    for x in range(4) :
                        if mbti[i][x] != mbti[j][x] :
                            tmp += 1
                        if mbti[j][x] != mbti[k][x] :
                            tmp += 1
                        if mbti[i][x] != mbti[k][x] :
                            tmp += 1
                    cnt = min(tmp, cnt)

        print(cnt)