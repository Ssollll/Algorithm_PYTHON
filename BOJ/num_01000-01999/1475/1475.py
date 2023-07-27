import sys
input = sys.stdin.readline

N = str(input().strip())
cnt = [0 for _ in range(10)]

for i in N :
    if int(i) == 9 or int(i) == 6 :
        if cnt[6] <= cnt[9] :
            cnt[6] += 1
        else :
            cnt[9] += 1
    else :
        cnt[int(i)] += 1

print(max(cnt))