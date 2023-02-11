import sys

N = int(sys.stdin.readline())
color = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
an = [0, 0]

def cut(x, y, N) :
    c = color[x][y]
    for i in range(x, x + N) :
        for j in range(y, y + N) :
            if c != color[i][j] :
                cut(x, y, N // 2)
                cut(x, y + (N // 2), N // 2)
                cut(x + (N // 2), y, N // 2)
                cut(x + (N // 2), y + (N // 2), N // 2)
                return # 완전 함수 종료, break는 반복문의 종료를 뜻하므로 사용하면 요기서는 사용하면 안됨
    # 함수가 종료 안되고 넘어왔을 때 색종이의 수를 계산
    if c == 0 :
        an[0] += 1
    else :
        an[1] += 1

cut(0, 0, N)
print(*an, sep = "\n")