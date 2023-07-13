import sys
input = sys.stdin.readline

A, B = map(str, input().strip().split())
max_A = ""
min_A = ""
max_B = ""
min_B = ""

for i in A :
    if i == "5" or i == "6":
        max_A += "6"
        min_A += "5"
    else :
        max_A += i
        min_A += i

for i in B :
    if i == "5" or i == "6":
        max_B += "6"
        min_B += "5"
    else :
        max_B += i
        min_B += i

print(int(min_A) + int(min_B), int(max_A) + int(max_B))