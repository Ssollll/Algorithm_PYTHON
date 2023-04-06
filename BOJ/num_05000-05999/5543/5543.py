import sys

burger = [int(sys.stdin.readline()) for _ in range(3)]
drink = [int(sys.stdin.readline()) for _ in range(2)]

setmenu = min(burger) + min(drink)

print(setmenu - 50)