import sys
input = sys.stdin.readline

N = int(input())
serial = [input().strip() for _ in range(N)]

def count(x) :
    result = 0
    for i in x :
        if i.isdigit() :
            result += int(i)
    return result

serial.sort(key = lambda x : (len(x), count(x), x))

print(*serial, sep = "\n")