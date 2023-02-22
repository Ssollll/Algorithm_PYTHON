import sys

S1 = sys.stdin.readline().strip()
S2 = sys.stdin.readline().strip()
answer = []

for i in S1 :
    for j in range(len(S2)) :
        if i == S2[j] :
            answer.append(i)
            S2 = S2[j+1:]
            print(i, S2)
            break

print(len(answer))