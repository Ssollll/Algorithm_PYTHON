import sys

N = int(sys.stdin.readline())

for _ in range(N) :
    stu = list(map(int, sys.stdin.readline().split()))
    stu_m = sum(stu[1:]) / stu[0]

    cnt = 0
    for s in stu[1:] :
        if s > stu_m :
            cnt += 1

    stu_num = cnt/stu[0] * 100
    print(f"{stu_num:.3f}%")