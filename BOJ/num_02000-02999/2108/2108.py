import sys
from collections import Counter

N = int(sys.stdin.readline())

num = [int(sys.stdin.readline()) for _ in range(N)]
num.sort()
cnt = Counter(num).most_common(2)

print(round(sum(num) / N))    # 산술평균
print(num[N // 2])        # 중앙값
if len(num) > 1 :
    if cnt[0][1] == cnt[1][1] : # 최빈값
        print(cnt[1][0])
    else :
        print(cnt[0][0])
else :
    print(num[0])
print(num[N-1] - num[0])  # 범위