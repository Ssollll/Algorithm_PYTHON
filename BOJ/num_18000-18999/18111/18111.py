import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
answer = int(1e9)
index = 0

for t in range(257) :
    max_t, min_t = 0, 0

    for i in range(N) :
        for j in range(M) :
            if map[i][j] < t :
                min_t += (t - map[i][j])
            else :
                max_t += (map[i][j] - t)

    inven = max_t + B

    if inven < min_t :
        continue

    time = 2 * max_t + min_t

    if time <= answer :
        answer = time
        index = t

print(answer, index)