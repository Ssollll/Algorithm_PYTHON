import sys
input = sys.stdin.readline

color = {
    "black" : 0,
    "brown" : 1,
    "red" : 2,
    "orange" : 3,
    "yellow" : 4,
    "green" : 5,
    "blue" : 6, 
    "violet" : 7,
    "grey" : 8,
    "white" : 9,
}

c1 = input().strip()
c2 = input().strip()
c3 = input().strip()

answer = (color[c1] * 10 + color[c2]) * (10 ** (color[c3]))
print(answer)