import sys
input = sys.stdin.readline

S = [input().strip() for _ in range(5)]
S_len = [len(i) for i in S]

answer = ""
for i in range(max(S_len)) :
    for j in range(5) :
        if i < len(S[j]) :
            answer += S[j][i]

print(answer)