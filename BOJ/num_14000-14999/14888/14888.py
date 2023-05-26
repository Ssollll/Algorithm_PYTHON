import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))

maxi = int(-1e9)
mini = int(1e9)

def DFS(depth, total, plus, minus, multiply, divide) :
    global maxi, mini

    if depth == N :
        maxi = max(total, maxi)
        mini = min(total, mini)
        return
    
    if plus :
        DFS(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus :
        DFS(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply :
        DFS(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide :
        DFS(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)

DFS(1, num[0], op[0], op[1], op[2], op[3])

print(maxi)
print(mini)