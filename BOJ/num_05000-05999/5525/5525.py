import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().strip()
ans, i, cnt = 0, 0, 0

while i < (M - 1) :
    if S[i:i+3] == "IOI" :
        i += 2
        cnt += 1
        if cnt == N :
            ans += 1
            cnt -= 1
    else :
        i += 1
        cnt = 0

print(ans)


# P = "I" + "OI" * N

# cnt = 0
# for i in range(M - (2 * N)) :
#     if S[i] == "I" :
#         if S[i:i+len(P)] == P :
#             cnt += 1

# print(cnt)