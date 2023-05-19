import sys

N = int(sys.stdin.readline())
student = []

for _ in range(N) :
    name, a, b, c = map(str, sys.stdin.readline().split())
    student.append([name, int(a), int(b), int(c)])

student.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

for i in range(N) :
    print(student[i][0])