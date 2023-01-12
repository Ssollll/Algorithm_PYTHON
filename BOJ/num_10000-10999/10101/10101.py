import sys

ang = [int(sys.stdin.readline()) for _ in range(3)]

if sum(ang) == 180 :
    if ang[0] == ang[1] == ang[2] :
        print("Equilateral")
    elif ang[0] == ang[1] or ang[0] == ang[2] or ang[1] == ang[2] :
        print("Isosceles")
    else :
        print("Scalene")
elif sum(ang) != 180 :
    print("Error")