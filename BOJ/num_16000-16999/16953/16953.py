import sys

A, B = map(int, sys.stdin.readline().split())
cnt = 1

while A != B :
    cnt += 1
    F = B

    if B % 10 == 1 :
        B = B // 10 # 오른쪽의 1을 떼는 연산
    elif B % 2 == 0 :
        B = B // 2
    
    if F == B :
        print(-1)
        break

else :
    print(cnt)