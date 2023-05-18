import sys

x, y = map(int, sys.stdin.readline().split())
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

day = 0
for i in range(x - 1) :
    day += month[i]

day += y
day = day % 7

print(week[day])